# Python program to calculate Day of the week from a date input by the user
date = eval(input("Please enter the date: ex - 22, 01, 19 etc\n"))
month = eval(input("Please enter the month number: 1 for January, 2 for February, 3 for March and so on...\n"))
year = eval(input("Please enter the year: ex - 2019, 2001 etc\n"))

dateString = str(date) + "/" + str(month) + "/" + str(year)
print("The date you have entered is", dateString)

m = month
if month == 1:
    m = 13
    year -= 1
elif month == 2:
    m = 14
    year -= 1
# D is the first two digits of the

q = date

k = year % 100
j = year // 100
h = q + 13 * (m + 1) // 5 + k + k // 4 + j // 4 + 5 * j
res = h % 7

dayString = ""
if res == 0:
    dayString = "Saturday"
elif res == 1:
    dayString = "Sunday"
elif res == 2:
    dayString = "Monday"
elif res == 3:
    dayString = "Tuesday"
elif res == 4:
    dayString = "Wednesday"
elif res == 5:
    dayString = "Thursday"
elif res == 6:
    dayString = "Friday"

print(dateString, "was a", dayString)