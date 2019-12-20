list=[]

a=int(input("Enter the Range "))
for i in range(0, a):
  b=int(input("Enter Numbers "))
  list.append(b)
  
for x in list:
 if x>1:
  for i in range(2, x):
    if (x % i == 0):
      print(x, "is not a prime Number")
      break
    else:
      print(x, "is a prime Number")
      break

