#!/bin/bash
input=$1
cut -f1,3,4 $input | grep 2002 | sort -n -k3 | tail -n 1 > country_max_life_exp_2002