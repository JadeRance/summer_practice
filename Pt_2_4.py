print("Введите коэффиценты для квадратного уравнения: ")
a = int(input())
b = int(input())
c = int(input())
dis = b**2 - 4*a*c
if dis > 0:
    x1 = (-b + dis)/(2*a)
    x2 = (-b - dis)/(2*a)
    print("У уравнения два корня:", '\n', "x1 =", x1, '\n', "x2 =", x2)
elif dis == 0:
    x1 = -b/(2*a)
    print("У уравнения один корень:", '\n', "x1 =", x1)
else:
    print("У уравнения нет корней")