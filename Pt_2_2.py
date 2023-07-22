tv_list = ["Пусть говорят", "Ревизорро", "Орёл и решка", "Кухня"]
for i in range(len(tv_list)):
    print('#', i + 1, ' ', tv_list[i], sep='')
print("Введите название программы: ")
telecast = input()
print("Введите номер для программы в списке: ")
pos = int(input())
tv_list.insert(pos - 1, telecast)
for i in range(len(tv_list)):
    print('#', i + 1, ' ', tv_list[i], sep='')
