======
awk
======

* 元はドットインストールの内容


sales.dat

.. literal-include:: sales.dat

::

    awk '{ print $0 }' sales.dat

    awk '{ print $3 }' sales.dat

    awk '{ print $NF }' sales.dat

    awk '{ print NR ":" }' sales.dat

    awk '{ print NR ":" $0 }' sales.dat

    awk 'NR < 5 { print "aa : " $1 }; NR>10{print "cc : " $1}; ' sales.dat

    awk 'BEGIN{ print "---";FS=" "} NR < 5 { print "aa : " $1 } NR>10{print "cc : " $1} END{ "---"} ' sales.dat

    awk 'BEGIN{ print "---";FS=":"} NR < 5 { print "aa" $1 } NR>10{print "cc" $1} END{ "---"} ' sales.dat


.. note:: FSはフィールドの区切り。レコードの区切りはRSで、デフォルトは改行


::

    awk '/koji/ { print $0 }' sales.dat

    awk '$2 ~ /item-[23]/ { print $0 }' sales.dat




