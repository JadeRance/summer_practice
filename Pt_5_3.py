import csv

books_list = []
with open('books.csv') as f:
    reader = csv.reader(f)
    for row in reader:
        books_list.append(row)

low = int(input())
high = int(input())
result = []

for i in range(1, len(books_list)):
    if int(books_list[i][3]) >= low and int(books_list[i][3]) <= high:
        result.append(books_list[i][1])
if not(result):
    print("Нет книг в заданном диапазоне")
else: print(*result, sep=', ')