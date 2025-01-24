combat_lost = int(input())
helmet_price = float(input())
sword_price = float(input())
shield_price = float(input())
armour_price = float(input())
helmet = 0
sword = 0
shield = 0
armour = 0
for game in range(1, combat_lost + 1):
    if game % 2 == 0:
        helmet += 1
    if game % 3 == 0:
        sword += 1
        if game % 2 == 0:
            shield += 1
armour = shield // 2
expenses = (armour * armour_price) + (shield * shield_price) + (sword * sword_price) + (helmet * helmet_price)
print(f'Gladiator expenses: {expenses:.2f} aureus')
