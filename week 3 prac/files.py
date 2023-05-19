name = input("Enter your name:")

file = open("name.txt", "w")
file.write(name)
file.close()

file = open("name.txt", "r")
print(file.read())

file = open("numbers.txt", "r")
num_1 = int(file.readline())
num_2 = int(file.readline())
result = num_1 + num_2
print(result)

file = open("numbers.txt", "r")
total = 0

for line in file:
    num = int(line)
    total += num
    print(f"The total is :", total)
