from numbers_filter import command

n = int(input())
command_even = 'even'
command_odd = 'odd'
command_positive = 'positive'
command_negative = 'negative'
numbers = [int(input()) for _ in range(n)]
filtered_numbers = []
command = input()
for num in numbers:
    filtered_numbers = (
        (command == command_even and num % 2 == 0) or
        (command == command_odd and num % 2 != 0) or
        (command == command_positive and num >= 0) or
        (command == command_negative and num < 0)
    )
    if filtered_numbers:
        filtered_numbers.append(num)
print(filtered_numbers)