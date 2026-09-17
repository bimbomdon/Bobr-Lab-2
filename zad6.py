a = float(input("Введите первое число: "))
b = float(input("Введите второе число: "))

# Находим минимум и максимум
if a > b:
    maximum = a
    minimum = b
else:
    maximum = b
    minimum = a

# Считаем разность
raznost = maximum - minimum

print(f"Максимум: {maximum}")
print(f"Минимум: {minimum}")
print(f"Разность: {raznost}")