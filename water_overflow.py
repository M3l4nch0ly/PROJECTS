water_tank = 255
number = int(input())
for i in range(number):
    liters = int(input())
    if water_tank - liters < 0:
        print(f'Insufficient capacity!')
        continue
    water_tank -= liters
print(255 - water_tank)