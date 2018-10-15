import random

def magicNum():
    num = random.randint(0, 101)

    print("The computer has chosen the magic number! It's between 0 - 100. \n")
    guess = -1

    while guess != num:
        guess = int(input("Enter a number and we'll see if it's right. "))

        if guess > 100 or guess < 0:
            guess = int(input("You've entered an invalid number, please enter another number. "))

        elif guess < num:
            print("Your guess is less than the magic number. \n")

        elif guess > num:
            print("Your guess is greater than the magic number. \n")

        else:
            print("Good job! You guessed the magic number! \n")
            exit()

magicNum()
