your_list = input('ЗАПОЛНИТЕ СПИСОК ЭЛЕМЕНТАМИ: ')

your_list = list(your_list)

index = 0
for i in range(int(len(your_list) / 2)):
    your_list[index], your_list[index + 1] = your_list[index + 1], your_list[index]
    index += 2

print(your_list)
