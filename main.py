from random import choice

done = False
all_choices = ("R", "P", "S")
CPU_score = 0
user_score = 0

print("Winning rules of the rock paper scissors game as follow: \n" + "rock vs paper -> paper wins \n" +
      "rock vs scissors -> rock wins \n" + "paper vs scissors -> scissors wins \n")

# game loop
while not done:
    choice_made = None

    # generate random choice for computer
    CPU_choice = choice(all_choices)

    # ask for user's choice
    user_input = input("\nEnter \n R for Rock, \n P  for Paper or \n S  for Scissors, \n Enter X to quit: ")

    # validate user's input
    if user_input == "R":
        user_choice = "R"
        choice_made = "valid"
    elif user_input == "P":
        user_choice = "P"
        choice_made = "valid"
    elif user_input == "S":
        user_choice = "S"
        choice_made = "valid"
    elif user_input == "X":
       choice_made = "quit" 
    else:
        print("Invalid input.Please try again !!!")              

    # if user's input is valid, compare
    if choice_made == "valid":
      print(f"Machine selects \"{CPU_choice}\", user selects \"{user_choice}\" ")

      if user_choice == CPU_choice:
          print("It's a tie !!!")
      else:
          if user_choice == "R":
              if CPU_choice == "P":
                  print("Machine wins !!!")
                  CPU_score += 1
              else:
                  print("User wins !!!")
                  user_score += 1    
          if user_choice == "P":
              if CPU_choice == "S":
                  print("Machine wins !!!")
                  CPU_score += 1
              else:
                  print("User wins !!!")
                  user_score += 1
          if user_choice == "S":
              if CPU_choice == "R":
                  print("Machine wins !!!")
                  CPU_score += 1
              else:
                  print("User wins !!!")
                  user_score += 1                       
        
    print(f"Current score: Machine = {CPU_score}, User = {user_score}")

    # if user's input is to quit, end game
    if choice_made == "quit":
      print("Thank you for playing")
      print(f"Final score: Machine = {CPU_score}, User = {user_score}")
    Done = True





