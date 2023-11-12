# Сформировать (не программно) текстовый файл.
# В нём каждая строка должна описывать учебный предмет и наличие лекционных,
# практических и лабораторных занятий по предмету.
# Сюда должно входить и количество занятий.
# Необязательно, чтобы для каждого предмета были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество занятий по нему. Вывести его на экран.

with open('Предметы.txt', 'r', encoding='utf-8') as file:
    lines = file.readlines()

subject_dict = {}

for line in lines:
    parts = line.strip().split(": ")

    subject = parts[0]

    description = parts[1]

    total_lectures = 0
    total_practicals = 0
    total_labs = 0

    import re

    numbers = re.findall(r'\d+', description)

    if numbers:
        total_lectures = int(numbers[0]) if len(numbers) > 0 else 0
        total_practicals = int(numbers[1]) if len(numbers) > 1 else 0
        total_labs = int(numbers[2]) if len(numbers) > 2 else 0

    total_lessons = total_lectures + total_practicals + total_labs

    subject_dict[subject] = total_lessons

print("Словарь с информацией о предметах и количестве занятий:")
print(subject_dict)
