балл = int(input("Введите оценку за тест (0-100:"))
if балл >= 90:
    дз = input("Сдал ли студент все домашние задание? (да/нет:)")
    if дз == "Да":
        print("Отлично! Оценка:А+")
    else:
        print("Хорошая работа,но сдайте все задание Оценка: A")
Посещение = (input("Посещал ли он более 75% занятий (да /нет)"))
if балл >= 80 and балл <= 89:
    if Посещение == "Да":
        print("Хорошо! Оценка В")
    else:
        print("Нужно посещать занятия! Оценка С")
else: 
        print("Страйтесь лучше!")



