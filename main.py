import random

playerScore = 0
computerScore = 0

choices = ["rock", "paper", "scissors"]

while playerScore != 10 and computerScore != 10:
  playerChoice = input("Enter rock, paper or scissors: ").lower()

  computerChoice = random.choice(choices)

  if playerChoice == computerChoice:
    print(f"Both of you chose {computerChoice}!")

  elif (playerChoice == "scissors" and computerChoice == "paper") or (playerChoice == "rock" and computerChoice == "scissors") or (playerChoice == "paper" and computerChoice == "rock"):
    print(f"You chose: {playerChoice}")
    print(f"And the computer chose: {computerChoice}")
    print("You win!")

    playerScore += 1

    print(f"Current computer score: {computerScore}")
    print(f"Your current score: {playerScore}")
    print()


  elif (playerChoice == "scissors" and computerChoice == "rock") or (playerChoice == "rock" and computerChoice == "paper") or (playerChoice == "paper" and computerChoice == "scissors"):
    print(f"You chose: {playerChoice}")
    print(f"And the computer chose: {computerChoice}")
    print("You loose!")

    computerScore += 1

    print(f"Current computer score: {computerScore}")
    print(f"Your current score: {playerScore}")
    print()


if playerChoice == 10:
  print("You were first to 10! You win!")
else:
  print("The computer beat you to 10. You loose!")
