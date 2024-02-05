import random

print("Welcome to Rock Paper And Scissor ")
user_input = input("Choose Rock, Paper, or Scissor: ")

if user_input in ['rock', 'paper', 'scissor', 'Rock', 'Paper','Scissor']:
    print("You Have Chosen:", user_input)
else:
    print("Invalid choice. Please choose Rock, Paper, or Scissor.")

comp_decision = ['rock', 'paper', 'scissor', 'Rock', 'Paper', 'Scissor']

# Choose a random sample
random_choice = random.choice(comp_decision)
print("Random Choice:", random_choice)

if user_input == comp_decision:
    print("It's a tie!")
elif (user_input == 'rock' and comp_decision == 'scissors') or \
        (user_input == 'paper' and comp_decision == 'rock') or \
        (user_input == 'scissors' and comp_decision == 'paper'):
    print("You win!")
else:
    print("Computer wins!")
