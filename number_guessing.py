import random

number = random.randint(1, 100) # generate a random number between 1 and 100

max_guesses = 6 # set the number of guesses allowed
num_guesses = 0 # set the variable of guesses made to zero

while num_guesses < max_guesses: # loop until player runs out of guesses
    print(f"You have {max_guesses - num_guesses} guesses left")
    guess = int(input("Guess a number between 1 and 100: "))

    if guess == number: # if players guesses the number right than the loop ends
        print("Great job, you guessed the number!")
        break
    else:
        if guess > number: # the program will tell player if the guess is too high or low
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")

        num_guesses += 1 # adds one to guesses

print("Sorry, you ran out of guesses. The number was", number) # if player loses