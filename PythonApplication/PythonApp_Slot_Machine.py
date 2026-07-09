import random

MAX_LINE = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLS = 3

Symbol_count = {
    'A':2,
    'B':4,
    'C':6,
    'D':8
    }
symbol_values = {
    'A' : 8,
    'B' : 6,
    'C' : 4,
    'D' : 2}


def check_winnings(columns,lines, bet, values):
    winnings = 0
    winning_line = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol_to_check != symbol:
                break
        else:
            winnings += values[symbol] * bet
            winning_line.append(line + 1)

    return winnings, winning_line
    
def get_slot_machine_spin(rows,cols,symbols):
    all_symbol = []
    for symbol,symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbol.append(symbol)

    columns = []
    for col in range(cols):
        column = []
        current_symbol = all_symbol[:]
        for ros in range(rows):
            value = random.choice(current_symbol)
            current_symbol.remove(value)
            column.append(value)

        columns.append(column)

    return columns




def deposit():
    while True:
        amount = input("Type your deposit: ")
        if amount.isdigit():
            amount = int(amount)
            if amount>0:
                break
            else:
                print('Enter amount greater than 0.')   
        else:
            print('Enter valid number.')
    return amount

def print_slot_machine(columns):
    for rows in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[rows], end = ' | ')
            else:
                print(column[rows], end = ' ')
        print()


def get_lines():
    while True:
        lines = input('Type your desired line(1 - ' + str(MAX_LINE) + "): ")
        if lines.isdigit():
            lines = int(lines)
            if 1<=lines<=MAX_LINE:
                break
            else:
                print('Enter line number within bound.')   
        else:
            print('Enter valid number.')
    return lines

def get_bet():
    while True:
        bet= input("What would you like to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET<=bet<=MAX_BET:
                break
            else:
                print(f'Amount must be within ${MIN_BET} - {MAX_BET}')   
        else:
            print('Enter valid number.')
    return bet

def spin(balance):
    lines = get_lines()
    while True:
     bet = get_bet()
     total_bet = lines * bet
     if total_bet > balance:
         print(f"You donot have enough money to be this amount. Your balance is: ${balance}")
     else:
         break
    print(f"You are betting ${bet} on line {lines}. Total bet is equal to: ${total_bet}")
    slots = get_slot_machine_spin(ROWS,COLS,Symbol_count)
    print_slot_machine(slots)
    winnings, winning_line = check_winnings(slots,lines, bet, symbol_values)
    print(f"You won {winnings}")
    print(f"You won on lines: ", *winning_line)
    return winnings - total_bet

def main():
    balance = deposit()
    while True:
       current_balance = print('Your current balance:', balance)
       sp = input("Press enter to play(q to quit)")
       if sp == 'q':
           break
          
       else:
           balance += spin(balance)

    print(f'You are left with {balance}')

   

main()

   

   





