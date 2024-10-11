import random
print("Rock paper Seasor game")
user =input("Enter your choise Rock/Paper/Seasor")
options = ["Rock", "Paper", "Seasor"]

computer_choice = random.choice(options)
print (computer_choice)

if user == computer_choice:
    print("match tie!")

elif user == "Rock":
    if computer_choice =="paper":
        print("Paper covers rock computer won")

    else:
        print("Rock smashes seasor you won")

elif user == "Paper":
    if computer_choice =="Rock":
        print("Paper covers rock computer won")

    else:
        print("Seasor cuts paper computer won")

elif user == "Seasor":
    if computer_choice =="Rock":
        print("Rock smashes paaper computer won")
    
    else:
        print("Seasor cuts paper You won")   

else:
    print("invalid option")