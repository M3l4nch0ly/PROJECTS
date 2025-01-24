key = int(input())
n_lines = int(input())
message = []
for line in range(n_lines):
    character = input()
    check = ord(character) + key
    message.append(chr(check))
for character in message:
    print(character, end="")