def convert_temperature():
    temp_input = input("Введите температуру в C или F c единицей измерения (например, 40C или 104F): ").strip()
    
    # Проверка на корректность ввода
    if not temp_input[:-1].isdigit() or temp_input[-1].upper() not in ["C", "F"]:
        print("Ошибка: Введите значение в формате 40C или 104F.")
        return

    temp_value = int(temp_input[:-1])  # Извлекаем числовое значение
    unit = temp_input[-1].upper()      # Извлекаем единицу измерения

    # Конвертация
    if unit == "C":
        converted_temp = temp_value * 9 / 5 + 32
        print(f"{int(converted_temp)}F")
    elif unit == "F":
        converted_temp = (temp_value - 32) * 5 / 9
        print(f"{int(converted_temp)}C")

# Запуск функции
convert_temperature()