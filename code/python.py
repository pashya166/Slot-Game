import random


def spin_row():
    symbols = ['🍒', '🍉', '🍋', '🔔', '⭐']

    return [random.choice(symbols) for _ in range(3)]

    
def print_row(row):
    print("****************")
    print("/".join(row))
    print("****************")

def get_payout(row, bet):
    if row[0] == row[1] == row[2]:
        if row[0] == '🍒':
            return bet * 3
        elif row[0] == '🍉':
            return bet * 4
        elif row[0] == '🍋':
            return bet * 5
        elif row[0] == '🔔':
            return bet * 10
        elif row[0] == '⭐':
            return bet * 20
    return 0

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

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"You Won ${payout}!")
        else:
            print("Sorry You Lost!")

        balance += payout

        play_again = input("Do You Want to spin again? (y/n): ")

        if play_again != 'y':
            break

    print(f"Game Over! Your final balance is ${balance}")

if __name__ == '__main__':
    main()
