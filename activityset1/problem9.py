fname = input("Enter file name: ")
fh = open(fname)
lst = list()
for line in fh:
  ln=line.rstrip()
  words=ln.split()
for element in words:
  if element in lst :
    continue
else :
  lst.append(element)
  lst.sort()
  print(lst)
