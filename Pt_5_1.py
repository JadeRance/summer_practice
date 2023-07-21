import csv

data = [['', 'Книга', 'Автор', 'Год выпуска'],
        ['0', 'Dishonored: Возвращение Дауда', 'Адам Кристофер', '2018'],
        ['1', 'World of Warcraft: Иллидан', 'Уильям Кинг', '2016'],
        ['2', 'Преступление и наказание', 'Фёдор Достоевский', '1866'],
        ['3', 'Приключения Тома Сойера', 'Марк Твен', '1876'],
        ['4', 'Dragon Age: The World of Thedas Volume 2', 'Дэвид Гейдер', '2015']]

with open('books.csv', 'w+', encoding='cp1251', newline='') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow(row)