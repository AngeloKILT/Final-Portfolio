# Angelo Smith
# 12/3/2022
# This program meant to tell the user which year is a leap year from the users input
def isLeapYear(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False

        else:
            return True
    else:
        return False


print(isLeapYear(2000))
