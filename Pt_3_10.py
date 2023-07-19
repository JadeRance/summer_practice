from collections import Counter
enter = input()
letter_list = []
while enter:
    letters = list(enter.lower())
    for i in range(len(letters)):
        if letters[i] != ' ':
            letter_list.append(letters[i])
    enter = input()
slovar = Counter(letter_list)
print(dict(slovar))