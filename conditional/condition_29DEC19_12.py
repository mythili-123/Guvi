# Write a program to input month number and print number of days in that month.


print("jan,feb,march,apr,may,june,july,aug,sep,oct,nov,dec")
month=(input("enter the month:"))
if(month=="feb"):
 print("number of days 28/29")
elif(month=="apr","june","sep","nov"):
 print("number of the month 30")
elif(month=="jan","march","may","july","aug","oct","dec"):
 print("number of thr month 31")
else:
 print("wrong month")