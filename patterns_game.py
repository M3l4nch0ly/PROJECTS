print("🌟 Welcome to the Python Pattern Drawing Program!")
print("Choose a pattern type:")
print("1. Right-angled Triangle")
print("2. Square with Hollow Center")
print("3. Diamond")
print("4. Left-angled Triangle")
print("5. Hollow Square")
print("6. Pyramid")
print("7. Reverse Pyramid")
print("8. Rectangle with Hollow Center")
command = int(input())
if command in [1, 3, 4, 6, 7]:  # Patterns that need the number of rows
    rows = int(input("Enter the number of rows: "))
elif command in [2, 5, 8]:  # Patterns that need size
    size = int(input("Enter the size of the square/rectangle: "))
if command == 1:
    for i in range(1, rows + 1):
     print('*' * i)
elif command == 2:
    for i in range(size):
        for k in range(size):
            if i == 0 or i == size - 1 or k == 0 or k == size - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()
elif command == 3:
    for i in range(rows):
        print(' ' * (rows - i - 1) + '*' * ((2 * i) + 1))
    for i in range(rows):
        print(' ' * (i + 1) + '*' * ((2 * ((rows - 1) - i)) - 1))
elif command == 4:
    for i in range(rows, -1, -1):
        print('*' * i)
elif command == 5:
    for i in range(size):
        for k in range(size):
            if i == 0 or i == size - 1 or k == 0 or k == size - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()
elif command == 6:
    if rows > 0:
        for i in range(rows):
            for k in range(rows - i):
                print(" ", end="")
            for j in range((i * 2) - 1):
                print('*', end="")
            print()
elif command == 7:
    if rows > 0:
        for i in range(rows, 1, -1):
            for space in range(0, rows - i):
                print(" ", end="")
            for j in range(i, 2 * i - 1):
                print('*', end="")
            for j in range(1, i - 1):
                print('*', end='')
            print()
elif command == 8:
    width = int(input("Enter the width of the rectangle: "))
    height = int(input("Enter the height of the rectangle: "))
    for i in range(1, width + 1):
        for j in range(1, height + 1):
            if i == 1 or i == width or j == 1 or j == height:
                print("*", end="")
            else:
                print(" ", end="")
        print()
else:
    print("❌ Invalid choice! Please restart the program.")
print('Please write RESTART to restart the game: ')
restart = input()
if restart == 'RESTART':
 print("🌟 Welcome to the Python Pattern Drawing Program!")
 print("Choose a pattern type:")
 print("1. Right-angled Triangle")
 print("2. Square with Hollow Center")
 print("3. Diamond")
 print("4. Left-angled Triangle")
 print("5. Hollow Square")
 print("6. Pyramid")
 print("7. Reverse Pyramid")
 print("8. Rectangle with Hollow Center")
command = int(input())
if command in [1, 3, 4, 6, 7]:  # Patterns that need the number of rows
        rows = int(input("Enter the number of rows: "))
elif command in [2, 5, 8]:  # Patterns that need size
        size = int(input("Enter the size of the square/rectangle: "))
if command == 1:
   for i in range(1, rows + 1):
            print('*' * i)
elif command == 2:
        for i in range(size):
            for k in range(size):
                if i == 0 or i == size - 1 or k == 0 or k == size - 1:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()
elif command == 3:
        for i in range(rows):
            print(' ' * (rows - i - 1) + '*' * ((2 * i) + 1))
        for i in range(rows):
            print(' ' * (i + 1) + '*' * ((2 * ((rows - 1) - i)) - 1))
elif command == 4:
        for i in range(rows, -1, -1):
            print('*' * i)
elif command == 5:
        for i in range(size):
            for k in range(size):
                if i == 0 or i == size - 1 or k == 0 or k == size - 1:
                    print('*', end='')
                else:
                    print(' ', end='')
            print()
elif command == 6:
        if rows > 0:
            for i in range(rows):
                for k in range(rows - i):
                    print(" ", end="")
                for j in range((i * 2) - 1):
                    print('*', end="")
                print()
elif command == 7:
        if rows > 0:
            for i in range(rows, 1, -1):
                for space in range(0, rows - i):
                    print(" ", end="")
                for j in range(i, 2 * i - 1):
                    print('*', end="")
                for j in range(1, i - 1):
                    print('*', end='')
                print()
elif command == 8:
        width = int(input("Enter the width of the rectangle: "))
        height = int(input("Enter the height of the rectangle: "))
        for i in range(1, width + 1):
            for j in range(1, height + 1):
                if i == 1 or i == width or j == 1 or j == height:
                    print("*", end="")
                else:
                    print(" ", end="")
            print()




