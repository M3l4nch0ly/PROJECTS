group_size = int(input())
days = int(input())
coins = 0
for time in range(1, days + 1):
    if time % 10 == 0:
        group_size -= 2
    if time % 15 == 0:
        group_size += 5
    if time % 3 == 0:
        coins -= 3 * group_size
    if time % 5 == 0:
        coins += 20 * group_size
        if time % 3 == 0:
            coins -= 2 * group_size
    coins += 50
    coins -= 2 * group_size
loot = coins // group_size
print(f'{group_size} companions received {loot} coins each.')
