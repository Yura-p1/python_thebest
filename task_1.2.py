time = int(input("Пользователь ввел время в секундах: "))
user_time = time
if user_time >= 3600:
    hour = user_time // 3600
    minute = (user_time - (3600 * hour)) // 60
    seconds = user_time % 60
    our_time = "Точное время: {}:{}:{}".format(f"{hour:02d}", f"{minute:02d}", f"{seconds:02d}")
    print(our_time)
if user_time < 3600:
    hour = 00
    minute = user_time // 60
    seconds = user_time % 60
    our_time = "Точное время: {}:{}:{}".format(f"{hour:02d}", f"{minute:02d}", f"{seconds:02d}")
    print(our_time)