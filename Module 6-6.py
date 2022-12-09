#Angelo Smith
#11/10/2022
#This code lets users input a number for factorial answer.
import math
X = int(input("Please add a number"))
J = 1
for i in range(1,X+1):
   J = J * i
   print(J)
print(math.factorial(X))