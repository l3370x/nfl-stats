import os
import xml.etree.ElementTree as ET
from collections import Counter

DATADIR = "C:\\Users\\Aaron\\python\\nfl\\data"

allEndScores = []
scoreCount = Counter()

def parseFile(filename):
	tree = ET.parse(DATADIR+"\\"+filename)
	root = tree.getroot()
	for game in root.iter("game"):
		score1 = game[0].find('score').text[-1:]
		score2 = game[1].find('score').text[-1:]
		if score1 < score2:
			allEndScores.append(score1+","+score2)
		else:
			allEndScores.append(score2+","+score1)

for filename in os.listdir(DATADIR):
		parseFile(filename)
for score in allEndScores:
		scoreCount[score] += 1
print scoreCount
totalGames = sum(scoreCount.values())

percentages = {}

for score in scoreCount.items():
	percent = 100*float(score[1])/float(totalGames)
	percentages[score[0]] = str(percent)[:-8]


for i in sorted(percentages,key=percentages.get, reverse=True):
	print "Score: "+i+" - "+percentages[i]+"%"
