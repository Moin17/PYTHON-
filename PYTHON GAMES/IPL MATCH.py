import random
print("welcome to IPL MATCH")
team = ["KKR","RAJASTHAN ROYALS", "PUNJAB KINGS","SUNRISERS HYDERABAD","DELHI CAPITALS"]
team3 = ["CHENNAI SUPER KINGS", "ROYAL CHALLENGERS BANGLORE", "MUMBAI INDIANS","GUJARAT TITANS"]
wicket = 0
over = 0
team1 = random.choice(team)
team2 = random.choice(team3)
runs = [1,2,3,4,5,6]
ball_speed =0
balls = 0
print(f"The match is between {team1} vs {team2}")
team1_toss =input(f"{team1} choose heads or tails:-").lower()
team2_toss = input(f"{team2} choose heads or tails:-").lower()

print(f"{team1} choose {team1_toss} and {team2} choose {team2_toss}")
if team1_toss == "heads" and team2_toss== "heads" or team1== "tails" and team2 == "tails":
    print("Invalid choosen")
if team1_toss == "heads" and team2_toss == "tails":
    print(f"{team1} choose {team1_toss} and won the toss")
    a = input(f"{team1} choose batting or bowling:-").lower()
    if a == "batting":
        print(f"{team1} choose to bat")
    elif a == "bowling":
        print(f"{team1} choose to ball")

elif team1_toss == "tails" and team2_toss == "heads":
    print(f"{team2} won the toss")
    a = input(f"{team2} choose batting or bowling:-").lower()
    if a == "batting":
        print(f"{team2} choose to bat")
    elif a == "bowling":
        print(f"{team2} choose to ball")

print("We will now start the match:")
status = True
while wicket <2:
    ball_speed = int(input("Throw ball:"))
    if wicket == 0:
        if ball_speed < 100:
            run = random.choice(runs)
            
            balls += 1
            print(f"Overs are {over},balls are {balls},Runs are {run}, wickets are {wicket}")      

        elif ball_speed > 120:
            run = random.choice(runs)
            print("No Ball")
            print(f"Overs are {over},balls are {balls} ,Runs are {run}, wickets are {wicket}")

    elif wicket == 1:
            wicket += 1
            run = random.choice(runs)
            print(f"Overs are {over},balls are {balls},Runs are {run}, wickets are 1")

    elif wicket == 2:
            wicket += 1
            run = random.choice(runs)
            print(f"Overs are {over}, balls are {balls} ,Runs are {run}, wickets are 2 you are all out")



