import random

MAX_LINES = 1
MAX_BET = 1000
MIN_BET = 1

symbols_count = {
    "A": 2,
    "B": 3,
    "C": 4,
    "D": 5,
}

symbols_value = {
    "A": 1.5,
    "B": 1,
    "C": 0.6,
    "D": 0.4,
}

def check_win(result,bet,values):
    win = 0
    for i in range(len(result)):
        if result[i][0] == result[i][1] == result[i][2]:
            win += bet * values[result[i][0]] * 3
        elif result[i][0] == result[i][1]:
            win += bet * values[result[i][0]] * 2
        elif result[i][0] == result[i][2]:
            win += bet * values[result[i][0]] * 2
        elif result[i][1] == result[i][2]:
            win += bet * values[result[i][1]] * 2
    return win

def get_random_symbols():
    symbols = list(symbols_count.keys())
    result = []
    for i in range(MAX_LINES):
        result.append(random.choices(symbols, weights=symbols_count.values(), k=3))
    return result

def print_result(result):
    for i, line in enumerate(result):
        if i != len(result) - 1: 
            print(" | ".join(line), end=" ")
        else: 
            print(" | ".join(line))

def deposite():
    while True: 
        amount = input("Enter the amount you want to deposite:$")
        if amount.isdigit():
            amount = int(amount)
            if(amount > 0):
                break
            else:
                print("Please enter a valid amount greater than 0.")
        else:
            print("Please enter a number.")
    return amount

def get_bet():
    while True: 
        amount = input("Would you like to bet?: $")
        if amount.isdigit():
            amount = int(amount)
            if(MIN_BET <= amount <= MAX_BET):
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET}.")
        else:
            print("Please enter a number.")
    return amount

def game(balance):
    line = MAX_LINES
    bet = get_bet()
    total_bet = bet * line
    while total_bet > balance:
        print("Insufficient funds. Please try again.")
        bet = get_bet()
        total_bet = bet * line
    print(f"You are betting: ${bet} on {line} line. Total bet is equal to ${total_bet}")
    random = get_random_symbols()
    result = print_result(random)
    win = check_win(random,bet,symbols_value)
    print(f"Your win is: ${win}")
    return win - total_bet

def main():
    balance = deposite()
    while True:
        print(f"Your balance is: ${balance}")
        spin = input("press 's' to spin or 'q' to quit: ")
        if spin.lower() == "q":
            break
        elif spin.lower() == "s":
            balance += game(balance)
        else:
            print("Invalid input. Please try again.")
    print(f"You left with ${balance}.Thank you for playing. Goodbye!")

main()