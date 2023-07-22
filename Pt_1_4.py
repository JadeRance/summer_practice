print("Введите число от 10 до 20: ")
InputNumber = int(input())
while(InputNumber < 10 or InputNumber > 20):
    if InputNumber < 10:
        print("Число меньше требуемого диапозона. Повторите попытку: ") 
    if InputNumber > 20:
        print("Число больше требуемого диапозона. Повторите попытку: ") 
    InputNumber = int(input()) 
print("Спасибо")
