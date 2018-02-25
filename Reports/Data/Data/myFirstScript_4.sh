#!/bin/bash
input=$1
column=$2
year=$3
out=$4
cut -f1,3,$column $input | grep $year | sort -n -k3 | tail -n 1 > $out