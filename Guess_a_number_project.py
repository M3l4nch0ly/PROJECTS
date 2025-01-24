import random
pc_number = random.randint(1,100)
while True:
    player_input = input("Guess the number (1-100): ")
    if not player_input.isdigit():
        print('Invalid input. Try again ... ')
        continue
    player_input = int(player_input)
    if player_input == pc_number:
        print('You guess it!')
        break
    elif player_input > pc_number:
        print('Too High!')
    else:
        print('Too Low!')

