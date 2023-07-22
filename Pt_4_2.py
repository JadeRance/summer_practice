enter = input()
words = enter.split(" ")
polyndrom_count = 0
for i in range(len(words)):
    if list(words[i]) == list(words[i])[::-1]:
        polyndrom_count += 1
print(polyndrom_count)
