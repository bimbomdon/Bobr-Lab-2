num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))

# Вводим знак операции
operation = input("Выберите операцию (+, -, *, /): ")

# Логика вычислений
if operation == '+':
    result = num1 + num2
    print(f"Результат: {result}")

elif operation == '-':
    result = num1 - num2
    print(f"Результат: {result}")

elif operation == '*':
    result = num1 * num2
    print(f"Результат: {result}")

elif operation == '/':
    # Защита от деления на ноль
    if num2 == 0:
        print("Ошибка: На ноль делить нельзя!")
    else:
        result = num1 / num2
        print(f"Результат: {result}")

else:
    # Если ввели что-то кроме +-*/
    print("Неверная операция. Попробуйте еще раз.")