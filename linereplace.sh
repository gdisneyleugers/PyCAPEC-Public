#!/bin/bash
while read line
do
ider=$(./id-match.sh $1)
ide=$(./GenerateTree.sh $1)
name=$line
echo "Linking ID:"
echo $name
echo "// $1" > tm-$1
echo "digraph{" >> tm-$1
cat $1| grep "CAPEC" >> tm-$1
cat $1| grep "CWE" >> tm-$1
aa=$(cat $1|grep "CAPEC"|egrep "[0-9]{1,}" -o)
cat $1|sed -e "s/Name/$name/" >> tm-$1
#cat $1|grep "CWE"|egrep "[0-9]{1,}" -o
capecid=$(cat id)
cweid=$(cat tm1-id)
quote=$(echo '"')
space=$(echo '    ')
echo "}" >> tm-$1
done < tm-id
