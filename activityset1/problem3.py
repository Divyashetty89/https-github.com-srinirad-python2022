hours=input("Enter hours")
h=float(hours)
rate=input("Enter rate per hour")
r=float(rate)
if h<=40:
  pay=h*r
  print(pay)
else:
  eh=h-40
  p=40*r+eh*(1.5*r)
  print(p)


