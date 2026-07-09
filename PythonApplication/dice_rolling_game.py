import random as r

def rolling(i):
    result = []
    for rol in range(i):
         die = r.randint(1,6)
         result.append(die)
         rol += 1
    #die2 = r.randint(1,6)
    #result = (die1, die2)
    return result

def main():
    tries = 0
    while True:
       answer = input('Roll the dice(y/n):')
       answer = answer.lower()
       if answer == 'y':
            tries += 1
            dice_number = int(input('How many time do you want to roll the dice: '))
            print(rolling(dice_number))
       elif answer == 'n':
            print('Thanks for playing')
            print(f'You have played {tries} times.')
            break
       else:
            print('Invalid choice.')

main()




        

     