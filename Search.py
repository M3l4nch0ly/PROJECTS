number = int(input())
word = input()
strings = []
filtered_strings = []
for _ in range(number):
    current_string = input()
    strings.append(current_string)

    if word in current_string:
        filtered_strings.append(current_string)


print(strings)
print(filtered_strings)
