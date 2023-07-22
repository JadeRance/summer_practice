dict = {x: x + 1 for x in range(10)}
result = {dict[x]: dict[x] * dict[x] for x in range(len(dict))}
print(result)
