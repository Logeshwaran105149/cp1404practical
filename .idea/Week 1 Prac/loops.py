for i in range(0, 101, 10):
    print(i, end=' ')
print()

for i in range(20, 0, -1):
    print(i, end=' ')
print()

n = int(input("number of stars:"))
for i in range(n):
    print('*', end='')
for i in range(n + 1):
    print('*' * i)
