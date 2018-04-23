# coding: utf-8
# cat ./Input/hightemp.txt | cut -f 1
# cat ./Input/hightemp.txt | cut -f 2

import sys

Input = open(sys.argv[1],			"r+", 	encoding='utf-8')
col1  = open('./Output/col1.txt', 	'w', 	encoding='utf-8')
col2  = open('./Output/col2.txt', 	'w', 	encoding='utf-8')

line = Input.readline()
while line:
	values = line.split("\t")
	col1.writelines(values[0]+"\n")
	col2.writelines(values[1]+"\n")
	line = Input.readline()

Input.close()
col1.close()
col2.close()
