from random import randint
colors = ["Зелёный", "Красный", "Синий", "Жёлтый", "Белый"]
print("Угадайте один из загаданных цветов:")
print(*colors, sep=', ')
ColorNumber = randint(0, 4)
Guess = input()
if Guess == colors[ColorNumber]:
    print("Отлично!")
else:
    print("Неправильно. В этом слове", len(colors[ColorNumber]), "букв.")
Guess = input()
if Guess == colors[ColorNumber]:
    print("Отлично!")
else:
    print("Неправильно. Это слово начинается с буквы", colors[ColorNumber][0])
while(Guess != colors[ColorNumber]):
    Guess = input()
    if Guess != colors[ColorNumber]:
        print("Неправильно.")
print("Отлично!")