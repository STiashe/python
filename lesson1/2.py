timesec = int(input('Введите время в секундах - '))
timeminute = int(0)
timehour = int(0)

while timesec > 60:
    timeminute = timeminute + (timesec / 60)
    continue
while timeminute > 60:
    timehour = timehour + (timeminute / 60)
    continue
#if timesec < 60:
    print('Время - 00:00:', timesec)#

print('Время - ', timehour %d, ':', timeminute %d, ':', timesec %d)




