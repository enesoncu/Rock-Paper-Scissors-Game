import random

def print_choice(choice):
    if choice == 0:
        print(rock)
    elif choice == 1:
        print(paper)
    elif choice == 2:
        print(scissors)

def determine_winner(user_choice, comp_choice):
    if user_choice == comp_choice:
        return "It's a tie!"
    elif (user_choice == 0 and comp_choice == 2) or \
         (user_choice == 1 and comp_choice == 0) or \
         (user_choice == 2 and comp_choice == 1):
        return "You won!"
    else:
        return "Computer won!"

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

def main():
    user_score = 0
    comp_score = 0

    while True:
        user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors: ")

        if user_choice not in ["0", "1", "2"]:
            print("You typed the wrong number. Please try again!")
            continue

        user_choice = int(user_choice)
        print("You chose:")
        print_choice(user_choice)

        comp_choice = random.randint(0, 2)
        print("Computer chose:")
        print_choice(comp_choice)

        result = determine_winner(user_choice, comp_choice)
        print(result)

        if "You won" in result:
            user_score += 1
        elif "Computer won" in result:
            comp_score += 1

        print("Score - You:", user_score, "Computer:", comp_score)

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            print("Final Score - You:", user_score, "Computer:", comp_score)
            print("Goodbye!")
            break

if __name__ == "__main__":
    main()
