import csv
import urllib
import webbrowser

f = open('shuffledLinks.csv')
csv_f = csv.reader(f)

shuffleIDs = []
groupIDs = []
postIDs = []
links = []

for row in csv_f:
	shuffleIDs.append(row[0])
	groupIDs.append(row[1])
	postIDs.append(row[2])
	links.append(row[3])

postLink = str(links[3])
url = urllib.urlopen(postLink)
page = url.read()

webbrowser.open(postLink)