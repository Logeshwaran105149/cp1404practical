MIN_SCORE = 0
PASS_SCORE = 50
HIGH_SCORE = 90
MAX_SCORE = 100

import random


def main():
    score = float(input("Enter score: "))
    random_score = random.randint(0, 100)
    result = get_result(score)
    print(result)
    result = get_result(random_score)
    print(f"Random score {random_score}: {result}")


def get_result(score):
    if score < MIN_SCORE or score > MAX_SCORE:
        return "Invalid score"
    elif score >= HIGH_SCORE:
        return "Excellent"
    elif score >= PASS_SCORE:
        return "Passable"
    else:
        return "Bad"


main()
