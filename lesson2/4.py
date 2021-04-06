your_words = list(input('ВВЕДИТЕ НЕСКОЛЬКО СЛОВ ЧЕРЕЗ ПРОБЕЛ: ').split())

for i in range(0, len(your_words)):
    print(i+1, your_words[i][:10])
