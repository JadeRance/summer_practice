import csv

books_list = []
with open('books.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        books_list.append(row)

print("Сколько записей вы хотите добавить?")
value = int(input())
number = int(books_list[-1][0])
for i in range(value):
    number += 1
    book = input()
    author = input()
    year = input()
    books_list.append([number, book, author, year])
print("Введите автора:")
author = input()
result = []
for i in range(len(books_list)):
    if author in books_list[i][2]:
        result.append(books_list[i][1])
if result == []:
    print('Такого автора нет в списке')
else:
    print(*result, sep=', ')
