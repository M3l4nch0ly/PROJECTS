new_year = int(input()) + 1

while len(set(str(new_year))) != len(str(new_year)):
    new_year += 1

print(new_year)