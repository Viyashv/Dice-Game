import random

print("Welcome to the Dice Game")
print("Rules: ")
print("1. Each player will roll the dice alternatively.")
print("2. The player who reaches first to 20 points wins the game.")
print("3. If you want to exit the game, press 2.")
print("4. If you roll the dice, the number will be added to your score.")
print("Game Begins.")

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