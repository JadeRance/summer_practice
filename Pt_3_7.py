x = input()
x_list = list(x.lower())
print(x_list)
check = lambda x: "True" if x in "ауоыиэяюёе" else "False"
dict = {x_list[i]: check(x_list[i]) for i in range(len(x_list))}
print(dict)
