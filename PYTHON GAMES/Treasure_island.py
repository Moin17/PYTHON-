print("Welcome to treasure island:")
print("Your mission is to find the treasure:")
choice1 = input('You r at road where do u go "left" or "right" ?').lower()

if choice1 == "left":
  choice2 = input("You came to lake ,type 'wait' for boat or 'swim' to swim across.").lower()
  if choice2 == "wait":
    choice3 = input('you have reached island safely which door u wanna go "red" "blue" or "yellow."').lower()
    if choice3 =="red":
      print("Game Over:")
    elif choice3 == "blue":
      print("Game over:")
    elif choice3 == "yellow":
      print("You won:")
    else:
      print("you choose the door that doesnt exist:")
  else:
    print("Game over:")
else:
  print("Game over:")