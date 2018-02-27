import sys

file = open(sys.argv[1], "r")

firstLine = file.readline()
infoList = firstLine.split('\n')
infoList = infoList[0].split(' ')

infos = {
	'row': int(infoList[0]),
	'column': int(infoList[1]),
	'min':int(infoList[2]),
	'max':int(infoList[3]),
	'nbT':0,
	'nbM':0
	}

pizza = [[0 for x in range(infos['column'])] for y in range(infos['row'])]

y = 0
for line in file:
	x = 0
	line = line.split('\n')
	for letter in line[0]:
		if letter == 'T':
			infos['nbT']+=1
			pizza[y][x] = 0
		else:
			infos['nbM']+=1
			pizza[y][x] = 1
		x+=1
	y+=1


