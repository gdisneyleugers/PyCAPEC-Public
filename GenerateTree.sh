#!/bin/bash
quote=$(echo '"')
break=$(echo "\n")
echo > map
echo > id-tree
while read line
do
echo $quote'CAPEC-'$line$quote >> id-tree
done < capecid
while read line
do
echo $quote'CWE-'$line$quote >> id-tree
done < cweid

rr=$(cat id-tree|sed -e 's/-/->/')
for i in $rr
do
echo $i >> map
done