#Load file
FILENAME = "eventLocations.csv"
with open(FILENAME) as f:
  lines = f.readlines()

def isPreTrail(date): #LemmingTrail happened August 2013
  if date[:4] == '2014':
    return False
  elif date[:4] == '2013' and int(date[5:7]) > 8:
    return False
  else:
    return True
  
dates = [l.split()[-1][:10] for l in lines[1:]]
bostondates = dates[245:]
wmassdates = dates[:245]

predates = (len([d for d in bostondates if isPreTrail(d)]), len([d for d in wmassdates if isPreTrail(d)]))

print "Boston events with date field before Lemming Trail:", predates[0]
print "Boston events with date field after Lemming Trail:", len(bostondates) - predates[0]

print "Western Mass events with date field before Lemming Trail:", predates[1]
print "Western Mass events with date field after Lemming Trail:", len(wmassdates)-predates[1]
