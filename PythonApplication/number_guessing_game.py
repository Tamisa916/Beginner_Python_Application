#a fixed number
#user input
#compare the number 
#print appropriate comment

#from curses.ascii import isdigit
import random


def main():
   original_num = random.randint(1,100)
   i = 0
   while True:
    guess = input("Guess the number between 1 to 100: ")
    if (guess.isdigit) :
        guess = int(guess)
        i += 1
        if guess<original_num:
            print('TOO LOW!')
        elif guess>original_num:
            print('TOO HIGH!')
        elif guess==original_num:
            print("Congratulations! You guessed the number.")
            print(f'You have tried {i} times.')
            break
     
    else:
        print('Please enter a valid number.')

main()
