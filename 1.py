#   Открытие файла
open(имя_файла, режим, кодировка)

file = open("notes.txt", "r", encoding="utf-8")
#...
file.close()   # обязательно закрыть!

with open("notes.txt", "r", encoding="utf-8") as file:
    text = file.read()
# здесь файл уже закрыт автоматически

#   Чтение
with open("hello.txt", "r", encoding="utf-8") as file:
    text = file.read()
print(text)
print("Длина текста:", len(text))

with open("hello.txt", "r", encoding="utf-8") as file:
    line1 = file.readline()
    line2 = file.readline()
print("Строка 1:", line1.strip())  # strip() убирает \n
print("Строка 2:", line2.strip())

with open("hello.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()
print(lines)

with open("hello.txt", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip())

#   Запись
with open("output.txt", "w", encoding="utf-8") as file:
    file.write("Первая строка\n")
    file.write("Вторая строка\n")
    file.write("Третья строка\n")

lines = ["яблоко\n", "банан\n", "вишня\n"]
with open("fruits.txt", "w", encoding="utf-8") as file:
    file.writelines(lines)

with open("diary.txt", "a", encoding="utf-8") as file:
    file.write("12 марта: выучил Python-файлы\n")

# Вариант w
with open("log.txt", "w", encoding="utf-8") as f:
    f.write("Запись 2\n")
# В файле теперь: "Запись 2"

# Вариант a
with open("log.txt", "a", encoding="utf-8") as f:
    f.write("Запись 2\n")
# В файле теперь: "Запись 1\nЗапись 2"

