
while true:
  num=input("Enter a number")
if num=='done':
   break
try:
  n=int(num)
  if n>large:
    large=num
  elif n<small:
    small=num
    except:
     print("Invalid Input")

print("Largest:",large)
print("Smallest",small)
  
