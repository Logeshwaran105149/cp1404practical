# List of authorized usernames
usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn',
             'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob']

# Ask user for their username
user_input = input("Enter your username:")
# Check if the entered username is in the list of authorized usernames
if user_input in usernames:
    print("Access granted")

else:
    print("Access denied")

