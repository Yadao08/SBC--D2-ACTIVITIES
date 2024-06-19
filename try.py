import random

def check_lottery_result(bet, result):
    if bet == result:
        return "You win!"
    elif sorted(bet) == sorted(result):
        return "You partially win!"
    else:
        return "You lose!"

def main():
    bet = input("Enter your bet (3 numbers with spaces): ")
    bet = list(map(int, bet.split()))
    result = random.sample(range(3, 6), 3)
    print(f"Lottery result: {' '.join(map(str, result))}")

    outcome = check_lottery_result(bet, result)
    print(outcome)

if __name__ == "__main__":
    main()