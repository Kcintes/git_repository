rik = int(input("Уведіть рік, який вас цікавить :"))
c = rik % 4
b = rik % 100
a = rik % 400
if 1900 < rik < 1000000:
    print("Триває обчислення")
elif c == 0:
    print("Триває обчислення")
elif b == 0:
    print("Триває обчислення")
elif a == 0:
    print("This is leep year")
else:
    print("This is not leep year")