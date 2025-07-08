import random

print("Welcome to Rock, Paper, Scissors!")
print("Winning rules of the game Rock, Paper, Scissors are:\n"
      +"Rock vs Scissors -> Rock wins\n"
      + "Rock vs Paper -> Paper wins\n"
      + "Scissors vs Paper -> Scissors wins\n")

while True:
    print("Enter your choice \n 1 - Rock \n 2 - Paper \n 3 - Scissors \n 4 - Exit")
    
    user_choice = int(input("Enter your choice: "))
    
    
    # Validate user input
    while user_choice < 1 or user_choice > 4:
        print("Invalid choice. Please try again.")
        user_choice = int(input("Enter your choice: "))
        
        
        
   
    if user_choice == 4:
        print("Exiting the game. Goodbye!")
        break
    elif user_choice == 1:
        user_choice_name = "Rock"
    elif user_choice == 2:
        user_choice_name = "Paper"
    else:
        user_choice_name = "Scissors"
        
    print(f"User choice is: {user_choice_name}")
    print("Now, let's see what the computer chooses...")
    
    comp_choice = random.randint(1, 3)
    if comp_choice == 1:
        comp_choice_name = "Rock"
    elif comp_choice == 2:
        comp_choice_name = "Paper"
    else:
        comp_choice_name = "Scissors"
        
        
    print(f"Computer choice is: {comp_choice_name}")
    print(user_choice_name + " vs " + comp_choice_name)
    
    if user_choice == comp_choice:
        result = "Draw"
    elif (user_choice ==1 and comp_choice ==2) or (user_choice == 2 and comp_choice ==1):
        result = "paper"
    elif (user_choice == 1 and comp_choice == 3) or (user_choice == 3 and comp_choice == 1):
        result = "Rock"
    elif (user_choice == 2 and comp_choice == 3) or (user_choice == 3 and comp_choice == 2):
        result = "Scissors"
        
        
    if result == "Draw":
        print("It's a draw!")
    elif result == user_choice_name:
        print("You win!")
    else:
        print("Computer wins!")
        
    print("DO you want to play again? (yes/no)")
    ans = input().lower()
    if ans == 'no':
        print("Thanks for playing! Goodbye!")
        break


print("Game Over!")
print("Thank you for playing Rock, Paper, Scissors!")
        
        
        

    