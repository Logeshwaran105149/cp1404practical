MIN_SCORE = 0
PASS_SCORE = 50
HIGH_SCORE = 90
MAX_SCORE = 100

menu = """Menu:
G - Get a valid score (must be 0-100 inclusive)
P - Print result
S - Show stars
Q - Quit"""


def main():
    print(menu)
    choice = input(">>> ").upper()
    score = 0
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            result = get_result(score)
            print(result)
        elif choice == "S":
            show_stars(score)
        else:
            print("Invalid option")
        choice = input(">>> ").upper()
    print("Farewell.")


def get_result(score):
    if score is 0:
        return "No score entered yet"
    elif score < MIN_SCORE or score > MAX_SCORE:
        return "Invalid score"
    elif score >= HIGH_SCORE:
        return "Excellent"
    elif score >= PASS_SCORE:
        return "Passable"
    else:
        return "Bad"


def get_valid_score():
    score = float(input("Enter score: "))
    while score < MIN_SCORE or score > MAX_SCORE:
        print("Invalid score")
        score = float(input("Enter score: "))
    return score


def show_stars(score):
    if score is 0:
        print("No score entered yet")
    else:
        stars = "*" * int(score * 10)
        print(stars)


main()
