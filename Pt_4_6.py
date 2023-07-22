enter = input()
letters = list(enter.lower())
for i in range(len(letters)):
    if letters[i] != ' ':
        if ord(letters[i]) > 96 and ord(letters[i]) < 123:
            if ord(letters[i]) + 2  > 122:
                letters[i] = chr(ord(letters[i]) + 2 - 26)
            else:
                letters[i] = chr(ord(letters[i]) + 2)
        if ord(letters[i]) > 1071 and ord(letters[i]) < 1104:
            if ord(letters[i]) + 2 > 1104:
                letters[i] = chr(ord(letters[i]) + 2 - 32)
            else:
                letters[i] = chr(ord(letters[i]) + 2)
print("".join(letters))
