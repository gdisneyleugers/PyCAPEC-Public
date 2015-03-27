#!/bin/bash
echo > tm-$1
./GenerateTree.sh
cat $1|grep "CAPEC"|egrep "[0-9]{1,}" -o  > capecid
cat $1|grep "CWE"|egrep "[0-9]{1,}" -o > cweid
cat capecid > id
cat cweid >> id
quote=$(echo '"')
space=$(echo '    ')
ids=$(cat term)
echo "// $ids" > tm-$1
#cat $1|grep "digraph{" >> tm-$1
#echo "digraph{" >> tm-$1
while read line
do
cat $1|grep -C 1 "$line"|sed -e "s/Name/$line/"|sed -e 's/--/ /'|tail -n +1 >> tm-$1
done < id
echo "}" >> tm-$1