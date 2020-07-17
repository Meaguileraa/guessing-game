"""A number-guessing game."""
import random 
#from random import randint

number = random.randint(1,100)

player_name = input("Hi, what's your name? ")
player_name = player_name.title()

print (f"Hi {player_name}, I'm thinking of a number between 1 and 100. \nTry to guess my number.")

count = 0
while True:
    try:
        guess = int( input ("Your guess?: "))
        if guess > 100 or guess < 1:
            print ("Silly child, that's not even between 1 and 100. Let's put in a real guess.")
        elif guess > number:
            print ("Your guess is too high, try again.")
            count += 1
        elif guess < number:
            print ("Your guess in too low, try again.")
            count += 1
        else:
            count += 1
            print (f"Well done, {player_name} ! You found my number in {count} tries ")
            break 
    except ValueError:
        print("Thats not a number...")