# coding: utf-8
# cat ./Input/hightemp.txt | cut -f 1
# cat ./Input/hightemp.txt | cut -f 2

import sys

with open('./Input/col1.txt', 'r+', encoding='utf-8') as col1, open('./Input/col2.txt', 'r+', encoding='utf-8') as col2
	file1, file2 = col1.readlines(), col2.readlines()

with open('./Output/merged.txt', 'w', encoding='utf-8') as merged
	for line1, line2 in zip(file1, file2):