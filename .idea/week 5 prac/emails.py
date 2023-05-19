SENTINEL = ""
user_dict = {}

email = input("Enter your email address (blank to stop): ")
while email != SENTINEL:
    username, domain = email.split("@")
    name_parts = username.split(".")
    if len(name_parts) == 1:
        first_name = name_parts[0]
        last_name = ""
    else:
        first_name, last_name = name_parts
    name = ''.join([first_name.title(), last_name.title()])
    choice = input(f"Is your name {name}? [Y/n] ").lower()
    if choice == "n":
        name = input("Enter your name: ").title()
    user_dict[email] = name
    email = input("Enter your email address (blank to stop): ")

print("user list:")
for email, name in user_dict.items():
    print(f"{email}:{name}")
