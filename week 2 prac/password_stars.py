min_len = 10


def main():
    password = input("Enter a password:")
    print("*" * len(password))


def grid_line(password):
    while True:
        if len(password) < min_len:
            print(f"Password must be at least {min_len} characters long. Try again.")
        else:
            break


main()
