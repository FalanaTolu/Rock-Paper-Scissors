import random
print("Hi. Let's play rock, paper, scissors!")
while True:
    user_choice = input("Enter a choice ('R' for 'rock', 'P' for 'paper', 'S' for 'scissors'): ")  
    possible_actions = ["R", "P", "S"]
    computer_choice = random.choice(possible_actions)
    printed_choice = {"R": "Rock", "P": "Paper", "S": "Scissors"}
    try:
        print(f"\n Player ({printed_choice[user_choice]}) : CPU ({printed_choice[computer_choice]})\n")
    except:
        print("Error! The input is invalid. Please type 'R' 'P' or 'S'")
        continue
    
    if user_choice == computer_choice:
        print(f"Both players selected {printed_choice[user_choice]}. It's a tie!")
        pass
    elif user_choice == "R":
        if computer_choice == "S":
            print("Rock smashes scissors! You win! \N{grinning face}")
            break
        else:
            print("Paper covers rock! You lose. \N{crying face}")
            break
    elif user_choice == "P":
        if computer_choice == "R":
            print("Paper covers rock! You win! \N{grinning face}")
            break
        else:
            print("Scissors cuts paper! You lose. \N{crying face}")
            break
    elif user_choice == "S":
        if computer_choice == "P":
            print("Scissors cuts paper! You win! \N{grinning face}")
            break
        else:
            print("Rock smashes scissors! You lose. \N{crying face}")
            break
            