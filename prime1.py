list=[]
print("enter max digits in list")
a=int(inpput())
for i in range(0,a):
 b=int(input())
list.append(b)
if (b>1):
  for i in range(2,b):
 if(b%1)==0:
  print(b,"is not prime")
   break
else:
 print(b,"is prime")
else:
 print(b,"is not prime")
 print list