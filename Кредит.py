
Зарплата = int(input("Введите зарплату $: "))
Кредит = int(input("Введите кредитный рейтинг:"))
if Зарплата > 50000:
    if Кредит >  700: 
     print("Кредит одобрен с низкой процентной ставкой.")
else:
    print("Кредит одобрен,но с высокой процентной ставкой.")

if Зарплата < 50000:
   if Кредит > 700:
      print("Кредит одобрен,но жесткими условями.")
   else:
      print("Кредит отклонен из-за низкой зарплаты и рейтинга")
