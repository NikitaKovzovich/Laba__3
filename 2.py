# Имеется текстовый файл «Вокзал», который содержит в себе информацию:
# номер поезда, пункт назначения, день недели, время отправления, стоимость билета.
# Вывести на экран все поезда, поопределенному пункту назначения.
# Вывести все поезда стоимость билета, которых меньше 50 р. Файл заполнить заранее(не программно).


with open('Вокзал.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

destination = input("Введите пункт назначения: ")

found_destination = False

print(f"Поезда с пунктом назначения '{destination}':")
for line in lines:
    train_info = line.split()
    if train_info[1] == destination:
        print(line, end='')
        found_destination = True

if not found_destination:
    print(f"Поездов с пунктом назначения '{destination}' не найдено.")

print("\nПоезда с билетами менее 50 рублей:")
found_price = False
for line in lines:
    train_info = line.split()
    if int(train_info[4]) < 50:
        print(line, end='')
        found_price = True

if not found_price:
    print("Поездов с билетами менее 50 рублей не найдено.")
