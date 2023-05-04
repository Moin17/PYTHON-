print("Welcome to Dominos")
pizza = 0
pasta = 0
price_of1_pizza = 10.99
price_of1_pasta = 9.5

def menu():
    print("Pizza")
    print("Pasta")
    print("Offers :-")
    print("Buy 4 or more Pizza and Get 1.5 lt soft drink free ")
    print("Buy 4 or more pasta and get 2 choco browny ice cream free ")
    
status = True
while status:
    name = input("Enter your name:")
    print("Welcome",name)
    choice = int(input("Enter your choice :- 1 for Menu, 2 for Exit :-"))
    if choice == 1:
        print(menu())
        choice = int(input(print("What do you want to order 1 for 'pizza' 2 for 'pasta' :-")))
        if choice==1:
            pizza = int(input("How much pizza u want to order ?"))
            if pizza == 1:
                print("Price of 1 Large pizza is 10.99 AUD")
                pizza * 10.99
            elif pizza == 2:
                print("Price of 2 Large pizza is 21.98 AUD")
                pizza * 20.99
            elif pizza == 3:
                print("Price of 3 Large pizza is 32.97 AUD")
                pizza * 29.99
            elif pizza >= 4:
                pizza * 10.99
                print("Yay you got 1.5 lt of Soft drink free")
            choice= input("Do you want pasta too ? Press 'y' for continue or 'n' for bill :-")
            if choice == "y":
                continue
            elif choice == "n":
                break
        if choice == 2:
            pasta = int(input("How much pasta u want to order ?"))
            if pasta == 1:
                print("Price of 1 Large pasta is 9.5 AUD")
                pasta * 5.99
            elif pasta == 2:
                print("Price of 2 Large pasta is 19.00 AUD")
                pasta * 10.99
            elif pasta == 3:
                print("Price of 3 Large pasta is 28.50 AUD")
                pasta * 15.99
            elif pasta >= 4:
                print("You got 2 choco brownie ice cream free")
                pasta * 20.99

    elif choice == 2:
        status = False


total_pizza_amnt = price_of1_pizza * pizza
print(f"{name} Your Total pizza order amount is :",total_pizza_amnt)


total_pasta_amnt = price_of1_pasta * pasta
print(f"{name} Your Total pasta order amount is :",total_pasta_amnt)