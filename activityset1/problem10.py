fhand = open("activityset1/mbox-short.txt")
count = 0
for line in fhand:
    line = line.rstrip()
    if line == "": 
      continue
    words = line.split()
    if words[0] !="From": 
      continue
        
    print(words[1])
    count = count+1

print ( count, "lines in the file with From as first word ")