height = int(input("Введите свой рост:"))
weight = int(input("Введите ваш вес:"))

bmi = weight  / (height / 100) ** 2
print(bmi)

if bmi <18.5:
	print("Недостаток веса")
elif bmi >= 18.5 and bmi < 24.9:
	print("Нормальный вес")
elif bmi >= 25.0 and bmi < 29.9:
	print("Предожирение")
elif bmi >= 30.0 and bmi < 34.9:
	print("1 степень ожирения")
elif bmi >= 35.0 and bmi < 39.9:
	print("Ожирение 2 степени")
else:
	print("Ожирение 3 степени")
