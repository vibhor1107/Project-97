from ast import Break
import random
print("NumberGuesing")
print("Guess a number (between 1 - 9 :)")
number= random.randint(1,9)
chances=0

while chances < 5:
    guess = int(input("Enter your guess"))


    if guess == number:
        print("Congratulation YOU WON!!!")
        break

    elif guess < number:
        print("Your guess was too low: Guess a number higher than ", guess)

    else:
        print("Your guess was too high : Guess a number lower than ", guess)    


    chances += 1
    if not chances <5:
        print("You LOSE!!! The number is", number)


 

