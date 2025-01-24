number = int(input())
dex = 0
for x in range(number):
    data = input()
    dex += ord(data)

print(f'The sum equals: {dex}')

