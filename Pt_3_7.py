x = input()
x_list = list(x.lower())
print(x_list)
check = lambda x: "Гласная" if x in "ауоыиэяюёе" else "Согласная"
dict = {x_list[i]: check(x_list[i]) for i in range(len(x_list))}
print(dict)