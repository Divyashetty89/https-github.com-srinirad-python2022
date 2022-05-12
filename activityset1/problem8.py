fname = input("Enter file name: ")
fhand = open(fname)
count = 0
total = 0

for line in fhand:
  if line.startswith("X-DSPAM-Confidence:"):
    count = count + 1
    z = line.find(':')
    y = float(line[z+1:])
    total = float(total + y)

average = total / count
print("Average spam confidence:",average)
