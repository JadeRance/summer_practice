print("Введите строку: ")
InputString = input()
Words = InputString.split(" ")
for x in range(len(Words)):
    Words[x] = Words[x].capitalize()
print(" ".join(Words))
