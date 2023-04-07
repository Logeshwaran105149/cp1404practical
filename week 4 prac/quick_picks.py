
import random


MIN_NUM = 1
MAX_NUM = 45
NUMS_PER_QUICK_PICKS = 6


# define the main function that asks the user how many quick picks they want and generates the quick picks
def main():
    num_quick_picks = int(input("How many quick picks:"))

    # generate the specified number of quick picks
    for i in range(num_quick_picks):
        # generate a quick pick of random numbers without repeats
        quick_pick = generate_quick_pick()
        # print the quick pick as a string with each number separated by a space and aligned to two columns
        print(" ".join("{:2d}".format(num) for num in quick_pick))


# define a function that generates a quick pick of random numbers without repeats
def generate_quick_pick():
    # use the random.sample function to generate NUMS_PER_QUICK_PICKS unique random numbers between MIN_NUM and MAX_NUM
    # and then sort the numbers in ascending order
    return sorted(random.sample(range(MIN_NUM, MAX_NUM + 1), NUMS_PER_QUICK_PICKS))


main()
