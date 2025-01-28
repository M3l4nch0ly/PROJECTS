list_integers = list(map(int, input().strip().split(" ")))
n = int(input())
for missing in range(n):
    list_integers.remove(min(list_integers))
print(", ".join(str(x) for x in list_integers))




