MENU = """(H)ello 
(G)oodbye 
(Q)uit"""
name = input("Enter name:")
print(MENU)
choice = input(">>> ")
while choice != "Q":
    if choice == "H":
        print("Hello", name)
    elif choice == "G":
        print("Goodbye", name)
    else:
        print("Invalid choice")
    print(MENU)
    choice = input(">>> ")
print("Finished.")
