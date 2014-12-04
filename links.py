import csv
import urllib
import webbrowser

f = open('shuffledLinks.csv')
csv_f_read = csv.reader(f)

shuffleIDs = []
groupIDs = []
postIDs = []
links = []
visited = []

for row in csv_f_read:
	shuffleIDs.append(row[0])
	groupIDs.append(row[1])
	postIDs.append(row[2])
	links.append(row[3])

for i in links:
	if  visited[i] == 1: #if this row was visited already, move to the next row
		i += 1
	postURL = str(links[i]) #get the next link
	#url = urllib.urlopen(postLink)
	#page = url.read()
	visited.append(1) #update the visited value

webbrowser.open(postURL)