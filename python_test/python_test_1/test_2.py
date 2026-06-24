day = int(input("Enter a day (1-31): "))
if day < 1 or day > 31:
    print("Error. Day must be between 1 and 31.")

month = int(input("Enter a month (1-12): "))
if month < 1 or month > 12:
    print("Error. Month must be between 1 and 12.")

elif month == 2:
    if day <= 10:
        print("OK. This day is within the first 10 days of February.")
    else:
        print("Error. February is only available until the 10th.")

# Validate day-month combination (months with only 30 days: April=4, June=6, September=9, November=11)
elif (month == 4 or month == 6 or month == 9 or month == 11) and day == 31:
    print("Error. Day must be within the month.")
else:
    print("Valid date")
    # I need criptograf it and insert a keyword and sen to email, how can stract virus of image