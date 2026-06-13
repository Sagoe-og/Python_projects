import random

def get_secret_word():
    return random.choice([    "leader", "python", "programming", "challenge", "hangman", "computer", "science" ])

def display_initial_board(word):
    return "_ " * len(word)

def generate_hint(secret_word, guess):
    hint = []
    secret_word_lower = secret_word.lower()
    guess_lower = guess.lower()
    for i in range(len(guess)):
        if guess_lower[i] == secret_word_lower[i]:
            hint.append(guess.upper()[i])
        elif guess_lower[i] in secret_word_lower:
            hint.append(guess.lower()[i])
        else:
            hint.append("_")
    return " ".join(hint)

def play_game():
    secret_word = get_secret_word()
    num_guesses = 0
    game_over = False

    print("Welcome to the Word Guessing Game!")
    print(f"The word has {len(secret_word)} letters: {display_initial_board(secret_word)}")

    while not game_over:
        num_guesses += 1
        guess = input(f"Guess #{num_guesses}: Enter your {len(secret_word)}-letter guess: ").strip()
        if len(guess) != len(secret_word):
            print(f"Your guess must be exactly {len(secret_word)} letters long. Please try again.")
            continue
        if guess.upper() == secret_word.upper():
            print(f"\nCongratulations! You guessed the word '{secret_word}' correctly!")
            game_over = True
        else:
            hint = generate_hint(secret_word, guess)
            print(f"Hint: {hint}")
    print(f"You made {num_guesses} guesses.")

if __name__ == "__main__":
    ans = "yes"
    while ans == "yes":
        play_game()
        while True:
            ans = input("Do you want to play the word guessing game? (yes/no): ").strip().lower()
            if ans in ["yes", "no"]:
                break
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")
    print("Thanks for playing!")