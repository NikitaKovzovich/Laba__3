#Создать программный файл F1 в текстовом формате, записать в него построчно данные, вводимые пользователем.
#Об окончании ввода данных будет свидетельствовать пустая строка.
#Скопировать из файла F1 в файл F2 все строки, которые содержат только одно слово.
#Найти самое короткое слово в файле F2.


with open("F1.txt", "w") as file_f1:
    print("Введите данные, по одной строке. Для завершения введите пустую строку:")
    while True:
        user_input = input()
        if not user_input:
            break
        file_f1.write(user_input + "\n")

with open("F1.txt", "r") as file_f1,open("F2.txt", "w") as file_f2:
    for line in file_f1:
        words = line.split()
        if len(words) == 1:
            file_f2.write(line)

with open("F2.txt", "r") as file_f2:
    shortest_word = None
    for line in file_f2:
        words = line.split()
        if not shortest_word or len(words[0]< len(shortest_word)):
            shortest_word = words[0]

if shortest_word:
    print(f"Самое короткое слово в файле F2: {shortest_word}")
else:
    print("Файл F2 не сожержит одиночных слов.")