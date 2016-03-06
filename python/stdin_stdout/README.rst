======
README
======

python3でのopen
================
python3からopenの仕様が変更となり、text modeの場合(mode=rやwだけで開いた場合）には、encoding付きでopenするようになっています。

返されるオブジェクトもfileオブジェクトではなく_io.TextIOWrapper, _io.BufferedReaderまたは_io.BufferedWriterとなっています。

例::

    >>> f = open('sample.csv', 'r')
    >>> f
    <_io.TextIOWrapper name='sample.csv' mode='r' encoding='UTF-8'>
    >>> f.close()

    >>> f = open('sample.csv', 'w')
    >>> f
    <_io.TextIOWrapper name='sample.csv' mode='w' encoding='UTF-8'>
    >>> f.close()

    >>> f = open('sample.csv', 'a')
    >>> f
    <_io.TextIOWrapper name='sample.csv' mode='a' encoding='UTF-8'>
    >>> f.close()
    
    >>> f = open('sample.csv', 'r+')
    >>> f
    <_io.TextIOWrapper name='sample.csv' mode='r+' encoding='UTF-8'>
    >>> f.close()
    
    >>> f = open('sample.csv', 'w+')
    >>> f
    <_io.TextIOWrapper name='sample.csv' mode='w+' encoding='UTF-8'>
    >>> f.close()
    
    >>> f = open('sample.csv', 'rb')
    >>> f
    <_io.BufferedReader name='sample.csv'>
    >>> f.close()

    >>> f = open('sample.csv', 'wb')
    >>> f
    <_io.BufferedWriter name='sample.csv'>
    >>> f.close()


python3の標準入出力のencodingを切り替える
=================================================
上述のとおりstdin, stdoutにencodingが付いているわけですが、これのデフォルトのencodingは環境に依存しています。

私の環境ではUTF-8がデフォルトのencodingとして設定しているので、何も指定しない状態ではUTF-8でstdinを読もうとします。


例えば、SJISのファイルをcatしてstdinから読み込むとどうなるかというと、

sample1.py::

    from __future__ import print_function
    import sys
    print(sys.stdin.read())

実行::

    cat sample.csv | python3 sample1.py

    Traceback (most recent call last):
    File "sample1.py", line 2, in <module>
        print(sys.stdin.read())
    File "/usr/local/Cellar/python3/3.4.0_1/Frameworks/Python.framework/Versions/3.4/lib/python3.4/codecs.py", line 313, in decode
        (result, consumed) = self._buffer_decode(data, self.errors, final)
    UnicodeDecodeError: 'utf-8' codec can't decode byte 0x82 in position 3: invalid start byte


SJISの文字列を渡した場合、Decodeできなかったと怒られます。

ちなみにpython2で同じことをすると文字化けしました。::

    1, �ق��ق�
    2, �ӂ��ӂ�


python2の場合、この問題を解決するために次のようにしていました。

sample2.py::

    from __future__ import print_function
    import sys
    import codecs

    _stdin = codecs.getreader('sjis')(sys.stdin)
    print(_stdin.read())

これを実行すると::

    cat sample.csv | python sample2.py
    1, ほげほげ
    2, ふがふが

となります。
SJISをデコードして読み取ることができています。

これをpython3で実行すると::

    cat sample.csv | python3 sample2.py
    Traceback (most recent call last):
    File "sample2.py", line 6, in <module>
        print(_stdin.read())
    File "/usr/local/Cellar/python3/3.4.0_1/Frameworks/Python.framework/Versions/3.4/lib/python3.4/codecs.py", line 313, in decode
        (result, consumed) = self._buffer_decode(data, self.errors, final)
    UnicodeDecodeError: 'utf-8' codec can't decode byte 0x82 in position 3: invalid start byte

残念ながら使えません・・・。

そこで、思い出すのが、冒頭に書いていたfileが_io.TextIOWrapperに変わったということです。
text modeで開いた時はすでにTextIOWrapperオブジェクトになっているので、.bufferにアクセスして、それをcodecs.getreaderします。

sample3.py::

    import sys
    import codecs

    _stdin = codecs.getreader('sjis')(sys.stdin.buffer)
    print(_stdin.read())


しかし、調べて見ると他のやり方がもあるようです。

sample4.py::

    import sys
    import io

    _stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='sjis')
    print(_stdin.read())
    

sample5.py::

    import sys
    _stdin = open(sys.stdin.fileno(), 'r', encoding='sjis')
    print(_stdin.read())


どれも上記のスクリプトでは正常に動作しています。
結局どれを使えばいいの？となりますが、getreaderやらTextIOWrapperという単語を見るよりも、openでstdinをsjisで開き直す、という方がさっぱりしていて良いな、と私はお思っています。


・・・ということで寝られるかと思ったら、何やら怪しい挙動が・・・


sample6.py::

    import sys
    import codecs

    _stdin = codecs.getreader('sjis')(sys.stdin.buffer)
    _stdout = codecs.getwriter('utf-8')(sys.stdout.buffer)

    for line in _stdin:
        print('!!!', file=sys.__stdout__)
        print('???', file=sys.__stderr__)
        _stdout.write(line)

実行すると::

    !!!
    ???
    1, ほげほげ
    !!!
    ???
    2, ふがふが


sample7.py::    

    import sys
    import io

    _stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='sjis')
    _stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    for line in _stdin:
        print('!!!', file=sys.__stdout__)
        print('???', file=sys.__stderr__)
        _stdout.write(line)

実行すると::

    !!!
    ???
    !!!
    ???
    1, ほげほげ
    2, ふがふが

あれ？？？


sample8.py::

    import sys
    _stdin = open(sys.stdin.fileno(), 'r', encoding='sjis')
    _stdout = open(sys.stdout.fileno(), 'w', encoding='utf-8')

    for line in _stdin:
        print('!!!', file=sys.__stdout__)
        print('???', file=sys.__stderr__)
        _stdout.write(line)

実行すると::

    !!!
    ???
    1, ほげほげ
    !!!
    ???
    2, ふがふが


なぜかTextIOWrapperのとき、出力順序が違っています。
なんとなくですが、TextIOWrapperを作りなおしている時に、バッファも別になってる気がします。

sample7a.py::

    import sys
    import io

    _stdin = io.TextIOWrapper(sys.stdin.buffer, encoding='sjis')
    _stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

    for line in _stdin:
        print('!!!', file=sys.__stdout__)
        print('???', file=sys.__stderr__)
        _stdout.write(line)
        _stdout.flush()

実行すると::

    !!!
    ???
    1, ほげほげ
    !!!
    ???
    2, ふがふが


よし。きっと正解です。よし寝よう。


まとめ
=======
どうしてもpython側でstd(in|out|err)の文字コードを吸収(変換)したいなら、今回書いた方法のどれかで変換すればよさそうです。

ただ、pythonでの文字コード変換が必須ではなく、コマンドラインで処理するスクリプトの場合には、iconvやnkfを使った方がpythonのコードもシンプルになります。

sample_simple.py::

    import sys
    print(sys.stdin.read())

これをこう::

    cat sample.csv | iconv -f SJIS -t UTF-8 | python3 sample_simple.py



頑張った割に、最終的にはpythonで文字コード変換しない方が良い気がするという結論でした。



* sys.stdout のエンコードを変更する in Python3.0 - @kei10in の日記 http://kei10in.hatenablog.jp/entry/20090331/1238520386
* 404 Blog Not Found:備忘録 - #python3 で sys.std(in|out|err) の encoding を強制する http://blog.livedoor.jp/dankogai/archives/51816624.html
* kPython 3 の標準入出力のエンコーディング - methaneのブログ http://methane.hatenablog.jp/entry/20120806/1344269400
* 元に戻すには、sys.__stdout__に本来のsys.stdoutが保存されているので、これを再代入します。 http://doloopwhile.hatenablog.com/entry/20111225/1324822224
* <a href="http://gihyo.jp/dev/serial/01/pythonhacks/0004">第4回　「俺様プチencoding」を実装して理解するPython3.0のioとcodec，encodingの機構：Python 3.0 Hacks｜gihyo.jp … 技術評論社</a>
