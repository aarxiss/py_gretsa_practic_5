# Запитуємо у користувача температуру та вологість
temperature = float(input("Введіть температуру в градусах Цельсія: "))
humidity = float(input("Введіть відносну вологість у відсотках: "))

# Перевіряємо умови для активації системи охолодження
if temperature > 30 and humidity > 70:
    print("Активація системи охолодження")
else:
    print("Умови нормальні")
