print("Введите баллы команды: ")
points = int(input())
possible_case = [0, 1, 3]
while(not(points in possible_case)):
    print("Указано неверное число, повторите попытку: ")
    points = int(input()) 
if points == 0:
    print("Команда проиграла.") 
if points == 1:
    print("Команда сыграла вничью.") 
if points == 3:
    print("Команда выиграла.") 
