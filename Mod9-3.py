# Angelo Smith
# 12/9/2022
# This code will continue to ask the user for a number until that said number is greater than or exactly 100.
List = []
sum = 0
while sum < 100:
    basket = int(input("Enter a number"))
    List.append(basket)
    sum = basket + sum
print(sum, List)
