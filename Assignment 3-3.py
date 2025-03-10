import datetime
year = input("Enter the year: ")
month = input("Enter the month: ")
day = input("Enter the day: ")

year = int(year)
month = int(month)
day = int(day)

try:
    date = datetime.date(year, month, day)
    print(f"{month}/{day}/{year} is a valid date.")
except ValueError:
    print(f"{month}/{day}/{year} is an invalid date.")
    