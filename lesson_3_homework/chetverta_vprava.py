rik = int(input("Уведіть рік, який вас цікавить :"))
if 1900 < rik < 1000000 and rik % 4 == 0 and rik % 100 != 0 or rik % 400 == 0:
    print("Цей рік є високосний ")
else:
    print("Не відповідає умовам задачи")