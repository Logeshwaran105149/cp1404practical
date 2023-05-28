import wikipedia


def main():
    while True:
        choice = display_menu()
        if choice == "1":
            search_wikipedia()
        elif choice == "2":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please choose 1 or 2.")


def search_wikipedia():
    search = input("Enter a page title to search for: ")
    try:
        page = wikipedia.page(search)
        print("Title:", page.title)
        print("Summary:", page.summary)
        print()
    except wikipedia.DisambiguationError as e:
        print("Disambiguation page. Possible options:")
        for i, option in enumerate(e.options, start=1):
            print(f"{i}. {option}")
        print()
    except wikipedia.PageError:
        print("The Page you're trying to search does not exist.")
        print()


def display_menu():
    print("What would you like to do?")
    print("1. Search Wikipedia")
    print("2. Exit")
    choice = input("Enter choice: ")
    return choice


if __name__ == "__main__":
    main()
