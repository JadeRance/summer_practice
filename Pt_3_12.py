dict = {x: (x + 1) * 2 for x in range(5)}
result = {dict[x]: dict[x] * dict[x] * dict[x] for x in range(len(dict))}
print(result)
