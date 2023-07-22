first = int(input())
second = int(input())
third = int(input())
total = first + second + third
greatest = max(first, second, third)
lowest = min(first, second, third)
middle = total - greatest - lowest
print("Наибольшее число -", greatest)
print(greatest, middle, lowest)
