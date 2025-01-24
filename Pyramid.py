number = int(input())
if number > 0:
    for i in range(number):
        for k in range(number - i):
            print(" ", end="")
        for j in range((i * 2) - 1):
            print('*', end="")
        print()
