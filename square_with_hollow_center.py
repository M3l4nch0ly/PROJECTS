number = int(input())
for i in range(number):
    for k in range(number):
        if i == 0 or i == number-1 or k == 0 or k == number-1:
            print('*', end='')
        else:
            print(' ', end='')
    print()