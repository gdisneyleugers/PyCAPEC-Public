#!/bin/bash
./name2id.sh $1
while read line
do
echo $line
id=$(cat $1|grep "Name"|sed -e "s/Name/$line/")
echo $id
done < id