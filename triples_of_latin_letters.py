triples = int(input())
for one in range(97, 97 + triples):
    for two in range(97, 97 + triples):
        for three in range(97, 97 + triples):
            print(f'{chr(one)}{chr(two)}{chr(three)}')


