min_len = 10


def main():
    password = input("Enter a password:")
    check_password(password)
    print("*" * len(password))


def check_password(password):
    while len(password) < min_len:
        print(f"Password must be at least {min_len} characters long. Try again.")
        password = input("Enter a password:")


main()
