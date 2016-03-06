# vim:fileencoding=utf-8
"""
* cp932のファイルを開く
* notepad.exeを起動
"""

import sys
import os
import re
import subprocess

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILENAME = "output.txt"
OUTPUT_FILEPATH = os.path.join(CURRENT_DIR, OUTPUT_FILENAME)
EDITOR = 'notepad.exe'
ENCODING = "cp932"
RE_DENPYO = re.compile(r"^\*.*$", re.MULTILINE)

def usage():
    print u"python NyukinDataCheck.py 入金データ.txtへのパス 勘定奉行のエラー行番号"
    print u"勘定奉行のエラー行番号は半角スペース区切りで複数入力可能です。"

def main():
    argc = len(sys.argv)
    if argc < 3:
        print usage()
        sys.exit(1)

    filepath = sys.argv[1]
    match_line_numbers = map(int, sys.argv[2:])

    with open(filepath, "r") as f:
        lines = f.read().decode(ENCODING).splitlines()

    cnt = 0
    line_number=0
    output = []
    FMT = u"{target_num:>4} : {line_num:>4} : {line_string}"
    for line in lines:
        line_number += 1
        m = RE_DENPYO.match(line)
        if m:
            cnt += 1
        if not cnt in match_line_numbers:
            continue 
        output.append(FMT.format(
                target_num=cnt, 
                line_num=line_number, 
                line_string=line
                ))

    with open(OUTPUT_FILEPATH, "w") as f:
        f.write("\n".join(output).encode(ENCODING))

    proc = subprocess.Popen([EDITOR, OUTPUT_FILEPATH])

if __name__ == '__main__':
    main()

