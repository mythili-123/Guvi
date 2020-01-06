# Write a program to check whether a year is leap year or not.



year=int(input("enter the year:"))
if(year%4==0)and(year%100==0):
 print("is leap year")
else:
 print("is not leap year")
