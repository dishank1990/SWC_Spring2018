#!/bin/bash
cut -f1,3,4 gapminder.txt | grep 2002 | sort -n -k3 | tail -n 1 > country_max_life_exp_2002