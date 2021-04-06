month_number = input('ВВЕДИТЕ МЕСЯЦ В ВИДЕ ЦЕЛОГО ЧИСЛА ОТ 1 ДО 12: ')

month = ['попробуй попасть сюда!', 'Январь', 'Февраль', 'Март', 'Апрель', 'Май', 'Июнь',
         'Июль', 'Август', 'Сентябрь', 'Октябрь', 'Ноябрь', 'Декабрь']
season = ['попробуй попасть сюда!', 'Зима', 'Зима', 'Весна', 'Весна', 'Весна', 'Лето',
          'Лето', 'Лето', 'Осень', 'Осень', 'Осень', 'Зима']

while month_number.isalpha() or int(month_number) < 0 or int(month_number) > 12 or int(month_number) == 0:
    month_number = input('ВВЕДИТЕ МЕСЯЦ В ВИДЕ ЦЕЛОГО ЧИСЛА ОТ 1 ДО 12: ')

month_number = int(month_number)
print(month[month_number], '-', season[month_number])
