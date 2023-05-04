n = int(input("How many terms ? : "))

a, b = 0, 1
count = 0
result = 0

if n <= 0:
    print("Please enter a positive integer")


elif n == 1:
    print("Fibonacci sequence upto",n,":")
    print(a)

else:
    print("Fibonacci sequence : ")
    while count < n:
        print(a)
        result = a + b
        a = b
        b = result
        count += 1