import random
computer_choice_list=["stone","paper","scissors"]
computer_choice=random.choice(computer_choice_list)
print("\n\t\t\twelcome To 'Stone Paper Scissors Game !'")
i=5
user_points=0
computer_points=0
while (i>=1):
    print("You have ",i,"chance ")
    print("options : stone  paper  scissors")
    user=input("Enter The Keyword from above Options : ")
    if user==computer_choice:
        print("User choise is",user)
        print("computer_choice is",computer_choice)
        print("Both Choice is same ")
    elif user=="stone" and computer_choice=="scissors":
        print("User choise is",user)
        print("computer_choice is",computer_choice)
        print("User Wins")
        user_points=user_points+1
        print(f"user Total : {user_points} points")
        print(f"computer Total : {computer_points} points")
    elif user=="stone" and computer_choice=="paper":
        print("User choise is",user)
        print("computer_choice is",computer_choice)
        print("computer wins")
        computer_points=computer_points+1
        print(f"user Total : {user_points} points")
        print(f"computer Total : {computer_points} points")
    elif user=="paper" and computer_choice=="scissors":
        print("User choise is",user)
        print("computer_choice is",computer_choice)
        print("computer wins")
        computer_points=computer_points+1
        print(f"user Total : {user_points} points")
        print(f"computer Total : {computer_points} points")
    elif user=="paper" and computer_choice=="stone":
        print("User choise is",user)
        print("computer_choice is",computer_choice)
        print("user wins !")
        user_points=user_points+1
        print(f"user Total : {user_points} points")
        print(f"computer Total : {computer_points} points")
    elif user=="scissors" and computer_choice=="stone":
        print("User choise is",user)
        print("computer_choice is",computer_choice)
        print("computer wins")
        computer_points=computer_points+1
        print(f"user Total : {user_points} points")
        print(f"computer Total : {computer_points} points")
    elif user=="scissors" and computer_choice=="paper":
        print("User choise is",user)
        print("computer_choice is",computer_choice)
        print("user wins !")
        user_points=user_points+1
        print(f"user Total : {user_points} points")
        print(f"computer Total : {computer_points} points")
    else:
        print("You didn't pressed Right key !")
    i=i-1



