import random
while True:
    Answer = random.randint(1, 15)

    print("GUESSING GAME😒")
    print("Guess a number between 1 and 15")

    while True:

        guess = int(input("Enter the number:"))

        if guess == Answer:
            print("Correct 🎉🎉🎉🎉 ")
            break
        elif guess > 15:
            print("Not within the range")
        elif guess > Answer:
            print("🥱too high")
        elif guess < Answer:
            print("😤too low")

    try_again = input("Would you like to play again? (y/n):")
    if try_again != "y":
        print("Thanks for playing")
        break
