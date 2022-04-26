hours=input("Enter hours")
h=float(hrs)
rate=input("Enter rate")
r=float(rate)
if h<=40:
  pay=float(hours)*float(rate)
print(pay)
else:
  eh=h-40
  pay=eh(1.5*r)+40*r
print(pay)
  