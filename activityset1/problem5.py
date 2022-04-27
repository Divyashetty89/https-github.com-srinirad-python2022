def computepay(hrs,rat):
  if hrs>40:
    p=40*rat+(hrs-40)*(1.5*r)  
    return p
  else:
    p=hrs*rat;
  return p
hours=input("Enter hours")
hr=float(hours)
rate=input("Enter rate per hour")
r=float(rate)
p=computepay(hr,r)
print("Pay",p)