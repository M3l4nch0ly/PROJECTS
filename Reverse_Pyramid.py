number = int(input())
if number > 0:
    for i in range(number, 1, -1):
        for space in range(0,number - i):
            print(" ", end="")
        for j in range(i, 2*i-1):
            print('*', end="")
        for j in range(1,i-1):
            print('*', end='')
        print()