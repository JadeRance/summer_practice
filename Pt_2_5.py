import random
win_count = lose_count = lose = 0
while (lose < 3):
    turn = random.randint(0, 1)
    print("Орёл или решка?")
    player = int(input())
    if player != 0 and player != 1:
        break
    if player == turn:
        print("Верно!")
        win_count += 1
        lose = 0
    else:
        print("Неверно!")
        lose_count += 1
        lose += 1
print("Конец игры")
print("Количество побед:", win_count)
print("Количество поражений:", lose_count)
