# Angelo Smith
# 12/3/2022
# This code finds if 10 is greater or less than the number the user inputs and if it's 10 its equal
def ten_equal():
    Number = int(input("Give me a number"))
    Number3 = int(input("Give me a number"))

    Number = Number3 + Number
    if Number > 10:
        print("It's greater than 10")
    elif Number < 10:
        print("It's less than 10")
    else:
        print("It's equal to 10")


ten_equal()
