import sys
import algo

fileName = sys.argv[1]

def readFile(filename):
	file = open(filename, 'r')

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
	return infos, pizza

		
# {'size':3, 'slice':[(1, 2, 3, 4), (5, 6, 7, 8), (9, 10, 11, 12)]}
		
def writeOutput(result, filename):
	file = open(filename, 'w')
	
	file.write(str(result['size']))
	
	for slice in result['slices']:
		file.write('\n')
		strTmp = str(slice)
		strTmp = strTmp.replace('(', '')
		strTmp = strTmp.replace(')', '')
		strTmp = strTmp.replace(',', '')
		file.write(strTmp)
		
infos, pizza = readFile(fileName)
result = algo.run(infos, pizza)
fileName = (fileName.split('.'))[0] + '.out'
writeOutput(result, fileName)
