import random
print('Welcome to Snake and ladders Game')
status = True
num=[1,2,3,4,5,6]
obstacle = [10,25,36,50,60,80,93,95]
game_start = False
i = 0
while i<101:
    num=int(input("enter any number from 1 to 6:"))

    if num == 6:
        if game_start == False:
            print("Your game will now start")
        
        game_start = True
    elif game_start==False:
        print("Roll 6 to start the match:-")
    if game_start:
        if i<101:
            i +=num
            print(i)
            if i in obstacle:
                print("Game Over You have been bitted by snake ")
                choice =input("do you want to play again:-")
                if choice == "n" or "no":
                    status = False
                    i=200
            elif i == 100:
                print("You won the game:")
                game_start= False

        
        
        
    
    