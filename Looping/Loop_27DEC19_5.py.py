# Write a program to print all odd number between 1 to 100.

start=int(input("enter the start of range"))
end=int(input("enter the end of range"))
for num in range(start,end+1):
  if (num%2!=0):
   print(num,end="")