import random


Player_One = input("Player 1 Enter your name: ")
Player_Two = input("Player 2 Enter your name: ")

Player_One_Score = 0
Player_Two_Score = 0

while Player_One_Score < 20 or Player_Two_Score < 20:
    print(f"\n{Player_One}'s turn: ")
    print("\nChoose an option: ")
    print("1. Roll")
    print("2. Exit")
    Player_One_Choice = input("Enter your choice: ")
    if Player_One_Choice == "1":
        Player_One_Score += random.randint(1, 6)
        print(f"\n{Player_One}'s score: {Player_One_Score}")
    elif Player_One_Choice == "2":
        break
    else:
        print("Due to Invalid choice.Your Turn is Over")
    
    print(f"\n{Player_Two}'s turn: ")
    print("\nChoose an option:")
    print("1. Roll")
    print("2. Exit")
    Player_Two_Choice = input("Enter your choice (1-2): ")

    if Player_Two_Choice == "1":
        Player_Two_Score += random.randint(1, 6)
        print(f"\n{Player_Two}'s score: {Player_Two_Score}")
    elif Player_Two_Choice == "2":
        break
    else:
        print("Due to Invalid choice.Your Turn is Over.")


print(f"\n{Player_One}'s score: {Player_One_Score}")