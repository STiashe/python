n = int(input('ВВЕДИТЕ ВРЕМЯ В СЕКУНДАХ: '))

if n > 86400:
    print('ЗАДАННОЕ ВРЕМЯ В СЕКУНДАХ БОЛЬШЕ 1 ДНЯ')

hours = (n // 3600) % 24
# подсчитываем часы

minutes = (n // 60) % 60
# подсчитываем минуты

seconds = n % 60
# подсчитываем остаток секунд

if hours < 10:
    # если время в часах меньше 10 добавляем ноль впереди
    hours = str('0' + str(hours))
else:
    hours = str(hours)
if minutes < 10:
    # если время в минутах меньше 10 добавляем ноль впереди
    minutes = str('0' + str(minutes))
else:
    minutes = str(minutes)
if seconds < 10:
    # если остаток в секундах меньше 10 добавляем ноль впереди
    seconds = str('0' + str(seconds))
else:
    seconds = str(seconds)

print(str(hours)+':'+str(minutes)+':'+str(seconds))
