# coding: utf-8
# cat ./Input/hightemp.txt | tr "\t" " "


import sys

f = open(sys.argv[1],"r+", encoding='utf-8')
line = f.readline()
 
while line:
	#print(line, end="")
	print(line.replace("\t", " "), end="")
	line = f.readline()
f.close()