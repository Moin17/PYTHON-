# using without any temp variable :
"""
a = 5
b = 10

# Before swapping numbers 

print("Before swapping : ")
print("Value of a : ", a, " and b : ", b)

a ,b = b , a

# After swapping numbers 

print("After swapping : ")
print("Value of a : ", a, " and b : ", b)

"""

# using with temporary variable :

x = int(input("Enter the number : "))
y = int(input("Enter the number : "))

temp = x
x = y
y = temp

print("Value of x : ",x)
print("Value of y : ",y)