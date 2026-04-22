secret_number = 7
guess = int(input("Guess a number between 1 and 10: "))

if guess == secret_number:
    print("You got it! You think like a computer.")
else:
    print("Not quite. That's why we practice!")