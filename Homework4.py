while True:
    try:
        n = int(input("Введите число N (больше 1): "))
        if n > 1:
            break
        else:
            print("Число должно быть больше 1. Попробуйте еще раз.")
    except ValueError:
        print("Некорректный ввод. Введите целое число.")

# Создаем список для отметок, где True означает простое число
sieve = [True] * (n + 1)
sieve[0] = sieve[1] = False  # 0 и 1 не являются простыми числами

# Идем по числам от 2 до корня из n
for i in range(2, int(n**0.5) + 1):
    if sieve[i]:  # Если число простое
        # Помечаем все кратные i как составные
        for j in range(i * i, n + 1, i):
            sieve[j] = False

# Выводим все простые числа от 2 до n
for num in range(2, n + 1):
    if sieve[num]:
        print(num)