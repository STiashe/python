my_list = [7, 5, 3, 3, 2]

number = input('ВВЕДИТЕ ЛЮБОЕ НАТУРАЛЬНОЕ ЧИСЛО: ')

if number.isalpha() or int(number) < 0 or int(number) == 0:
    print('ВЫ ВВЕЛИ НЕККОРЕКТНОЕ ЧИСЛО!')
else:
    while True:
        for index in range(len(my_list)):
            if my_list[index] == int(number):
                my_list.insert(index+1, number)
                print(my_list)
                break
            elif my_list[0] < int(number):
                my_list.insert(0, number)
                print(my_list)
                break
            # elif my_list[len(my_list)] > int(number):
            #     my_list.insert(len(my_list), number)
            #     print(my_list)
            #     break
            elif my_list[index] > int(number) and int(number) > my_list[index + 1]:
                my_list.insert(index+1, number)
                print(my_list)
                break
