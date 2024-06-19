import random
print("WELCOME!,BET AT YOUR OWN RISK!")
def check_lotres(bet, result):
    if bet == result:
        return "You Win!", 1, 0, 0
    elif sorted(bet) == sorted(result):
        return "You Partially win!", 0, 1, 0
    else:
        return "You Lose!", 0, 0, 1

def main():
    t_wins, tp_wins, t_los = 0, 0, 0

    for round_number in range(1, 4):
        print(f" FOR R O U N D {round_number}")

        bet = input("Enter your bet (3 digits): ")
        bet = [int(digit) for digit in bet]

        result = random.sample(range(5, 8), 3)

        print(f"Lottery result: {''.join(map(str, result))}")

        round_res, win, partial_win, lose = check_lotres(bet, result)
        t_wins += win
        tp_wins += partial_win
        t_los += lose

        print(round_res)
        print()

    print(f"Your Total Wins: {t_wins}")
    print("-------------------")

    print(f"Your Total Partial Wins: {tp_wins}")
    print("-------------------")

    print(f"Your Total Losses: {t_los}")

    print("-------------------")

    print("Thank You for Playing!")

if __name__ == "__main__":
    main()
