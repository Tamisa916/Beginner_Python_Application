# a loop
#user input
# invalid
#computer choice
#compare result

import random

def main():
    while True:
        choices = ('r','p','s')
        choice_emoji ={ 
        'r': '🪨',
        'p': '📃',
        's': '✂️' 
        }
        user_input = input("Rock, Paper, Scissor (r/p/s): ").lower()
        if user_input not in choices:
            print('Invalid choice. Try again!')
            continue

        computer_input = random.choice(choices)

        print(f'You chose {choice_emoji[user_input]}')
        print(f'Computer chose {choice_emoji[computer_input]}')

        if ( (user_input == 'r' and computer_input == 's') or 
             (user_input == 'p' and computer_input == 'r') or
             (user_input == 's' and computer_input == 'p') ) :
            print('You win!')

        elif user_input == computer_input:
            print('Tie!')

        else:
            print('You fail!')

        choice_to_continue = input('Do you want to continue(y/n): ').lower()
        if choice_to_continue == 'n':
            break


main()
