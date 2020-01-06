# Write a program to input week number and print week day.

weekno=int(input("enter a weekno:"))
weekno=int(weekno)
if (weekno == 1):
  weekDay = "Saturday"
elif (weekno == 2):
  weekDay = "Sunday"
elif (weekno == 3):
  weekDay = "Monday"
elif (weekno == 4):
  weekDay = "Tuesday"
elif (weekno == 5):
  weekDay = "Wednesday"
elif (weekno == 6):
  weekDay = "Thursday"
elif (weekno == 7):
  weekday="Friday"
else:
 weekday="please give the weekday between 1 o 7"
print(weekDay)