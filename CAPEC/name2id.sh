#!/bin/bash
cat $1|egrep "[0-9]{1,}" -o  > tm-id