import random


def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']

    return [random.choice(symbols) for _ in range(3)]

    
def print_row(row):
    print("****************")
    print("/".join(row))
    print("****************")

def get_payout():
    pass
def main():
    balance = 100

    print("Welcome To Python Slots")
    print("Sybomls: 🍒 🍉 🍋 🔔 ⭐")
    
    while balance > 0:
        print(f"Current Balance: ${balance}")

        bet = input("Place Your Amount: ")

        if not bet.isdigit():
            print("Please Enter a Valid Number: ")
            continue

        bet = int(bet)

        if bet > balance:
            print("insufficient funds")
            continue

        if bet <= 0:
            print("Bet Must be greater than 0")
            continue

        balance -= bet

        row = spin_row()
        print("Spinning....\n")
        print_row(row)

if __name__ == '__main__':
    main()