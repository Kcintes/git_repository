a = int(input("Кількість учнів першого математичного класу :"))
b = int(input("Кількість учнів другого математичного класу :"))
c = int(input("Кількість учнів третього математичного класу :"))
print("Стільки знадобиться парт для першого матетичного класу :", a // 2)
print("Стільки знадобиться парт для другого матетичного класу :", b // 2)
print("Стільки знадобиться парт для третього матетичного класу :", c // 2)
print("Стільки залишиться вільних місць за партою для першого матетичного класу :", a % 2)
print("Стільки залишиться вільних місць за партою для другого матетичного класу :", b % 2)
print("Стільки залишиться вільних місць за партою для третього матетичного класу :", c % 2)