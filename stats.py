import os
import xml.etree.ElementTree as ET
from collections import Counter

DATADIR = "C:\\Users\\Aaron\\python\\nfl\\data"

# Define global variables and open files for writing
allEndScores = []
allEndScoresFile = open("allEndScores.txt","w")
allEndScoresFile.write("ALL FINAL SCORES SINCE 2000\n---------------------------\n")
scoreCount = Counter()
scoreCountFile = open("scoreCount.txt","w")
scoreCountFile.write("FINAL GAME SCORE COUNTS\n-----------------------\n")
percentages = {}
percentagesFile = open("percentages.txt","w")
percentagesFile.write("FINAL GAME SCORE PERCENTAGES\n----------------------------\n")

# Parse data
for filename in os.listdir(DATADIR):
	tree = ET.parse(DATADIR+"\\"+filename)
	root = tree.getroot()
	for game in root.iter("game"):
		score1 = game[0].find('score').text
		score2 = game[1].find('score').text
		allEndScoresFile.write(score1+","+score2+"\n")
		if score1[-1:] < score2[-1:]:
			allEndScores.append(score1[-1:]+","+score2[-1:])
		else:
			allEndScores.append(score2[-1:]+","+score1[-1:])

# Count Occurances
for score in allEndScores:
	scoreCount[score] += 1
print scoreCount

# Calculate Percentages
totalGames = sum(scoreCount.values())
for score in scoreCount.items():
	percent = 100*float(score[1])/float(totalGames)
	percentages[score[0]] = str(percent)[:-8]

# Print percentages in a nice sorted manner
for i in sorted(percentages,key=percentages.get, reverse=True):
	print "Score: "+i+" - "+percentages[i]+"%"
	percentagesFile.write("Score: "+i+" - "+percentages[i]+"%\n")
	scoreCountFile.write("Score: "+i+" - "+str(scoreCount[i])+"\n")