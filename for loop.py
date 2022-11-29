# for loop
# while loop
# for i in range(1,6):
#     num1 = int(input("Enter number " +str(i)+ ":"))

# #format func.
# num1 = 10
# num2 = 20

# print(f"{num1} + {num2} = {num1 + num2}")
# for i in range(1,6):
#     num1 = int(input(f"Enter number {i} :"))

# #accept 5 sub marks and count total marks:
# sum = 0
# for i in range(1,6):
#     marks = int(input("Enter marks"))
#     sum += marks
# print(sum)

# #Russian Roulette game
# for i in range(3, 37 ,3):
#     print(i , end=" ")
# print()
# for i in range(2,36, 3):
#     print(i, end =" ")

# #while loop
# i = 1
# while i<5:
#     print(i)
#     i += 1

# #while task 2
# status = True

# while status:
#     name = input("Enter your name")

#     choice = input("do you want to add more name: press "y" for yes
#     and press "n" for no: ")

#     if choice = 'n' or choice = 'no':
#         status = false

# #task3
# import random

# computer = random.randint(1, 100)

# status = True

# while status:
#     user = int(input("Enter number:"))

#     if user<computer:
#         print("Guess higher number")
#     elif user > computer:
#         print("Guess lower no:")
#     else:
#         print("You won")
#         status = false
#rock paper scissors
import random

l1 = ["ROCK", "PAPER","SCISSORS"]

status = True
while status:
    computer = random.choice(l1)
    user = input("Enter Rock/ Paper / Scissor").upper()
    print("user",user)
    print("computer",computer)

    if user == computer:
        print("Its a draw:")
    elif user =="ROCK" and computer == "PAPER":
        print("computer won")
    elif user =="ROCK" and computer == "SCISSOR":
        print("user won")
    
    elif user =="PAPER" and computer == "ROCK":
        print("USER won")
    elif user =="PAPER" and computer == "SCISSOR":
        print("COMPUTER won")

    elif user =="SCISSOR" and computer == "ROCK":
        print("COMPUTER won")
    elif user =="SCISSOR" and computer == "PAPER":
        print("USER won")

    choice = input("do u want to play again ?")
    if choice == "n" or choice =="no":
        status = False