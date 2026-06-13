#using the random libraries to generate random numbers for the game
import random
ans = "yes"
#using the while loop in order to enable the user to continue playing even if the game ends so far as the user inputs yes
while ans == "yes":
    # Secret Number Game
    secret_number = random.randint(1, 100)
    guess = 0
    total_guesses = 0
    print("Welcome to the Secret Number Game!")            

    while guess != secret_number:
        guess = int(input("What is your guess? "))
        total_guesses = total_guesses + 1


        if guess < secret_number:
            print("Higher")
        elif guess > secret_number:
            print("Lower")
        else:  
            print("You got it!")
        # The user guessed the secret number correctly

#using an if function in order to enable the output to display the proper tense ie.guess/guesses
    if total_guesses == 1:
        print(f"It took you {total_guesses} guess")
    else:
        print(f"It took you {total_guesses} guesses")

#asking the user if he/she wants to play again in order to rerun the code from the while loop above
    print("Will you like to play again? (yes/no)")
    ans = input().lower()
    if ans == "no":
        print("Thanks for playing")


