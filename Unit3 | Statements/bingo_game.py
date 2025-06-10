"""Write a python code for a bingo game: Start off with setting a secret number
between 1 and 20. The player has 5 chances to guess what that secret
number is. So, at the prompt the player makes a guess. If the guess is lower
(higher) than the secret number, the program returns a hint: ‘higher’
(‘lower’) and lets the player make another guess. If the player makes a
correct guess at the prompt, the program returns ‘bingo!’ and exits. If the
player does not manage a correct guess within the allowed 5 chances, the
program returns ‘Oops, game over!’ and tells the player the secret number."""

import random

def get_integer () -> int:
    while True:
        try:
            input_number = int(input("Enter number:"))
            return input_number
        except ValueError:
            print("❌ Oops! That doesn't look like a whole number.")
            print("   • Please try again using only digits (0-9)")
            print("   • For negative numbers, include just one '-' at the front")
            print("   • Examples: 7, -3, 125\n")


secret_number = random.randint(1, 20)
print("Hi, dear player, let me to introduce our game rules:\n"
      "1. A secret number between 1 and 20 is randomly chosen.\n"
      "2. You have 5 chances to guess the secret number.\n"
      "3. After each guess, you’ll get a hint: Higher, Lower\n"
      "4. If you guess the number correctly, you win with a \"Bingo!\" message.\n"
      "5. If you don’t guess it within 5 tries, the game ends and reveals the secret number")


for i in range(1, 6):
    user_guessed_number = get_integer()
    if user_guessed_number == secret_number:
        print("Bingo!")
        break
    elif user_guessed_number < secret_number:
        print("Higher")
    else:
        print("Lower")

print(f"Oops, game over! Secret number was: {secret_number}")