# import   requests
# #
# # url=["https://cbu.uz/uz/arkhiv-kursov-valyut/json/"]
# #
# # data=requests.get(url).json()
# #
# #
# # print(data)
# #
# # import requests
# #
# #
# # url="https://cbu.uz/uz/arkhiv-kursov-valyut/json/"
# #
# #
# # data=requests.get(url).json()
# #
# #
# # def get_foragn_money(uzs):
# #
# #     summa=float(input("Sumni kiriting:"))
# #     davlatlar= ["USD", "EUR", "RUB"]
# #     for money in data:
# #         if money["Ccy"] in davlatlar:
# #             if summa in data:
# #                 print("100$","50$","20$",)
# #     for money in data:
# #         if "Rate" in url:
# #             return money
# # print(get_foragn_money())
#
# # <”O’zbekiston Vatan”im meni!!!> so’zini console’ga chiqaramiz.
#
# matn="O’zbekiston Vatanim meni!!!"
# print(matn)
# masofa=float(input("Masofani kiriting (km):"))
# tezlik=float(input("Tezlikni kiriting (km/soat):"))
# vaqt=masofa/tezlik
# print(f"Mashina {masofa} km masofani {tezlik} km/soat tezlik bilan {vaqt} soatda bosib o'tadi.")

matn="O’zbekiston Vatanim meni!!!"
print(matn)
masofa=float(input("Masofani kiriting (km):"))
tezlik=float(input("Tezlikni kiriting (km/soat):"))
vaqt=masofa/tezlik
print(f"Mashina {masofa} km masofani {tezlik} km/soat tezlik bilan {vaqt} soatda bosib o'tadi.")


# foydalanuvchidan mafosani kiritishni soraymiz(km)
# foydalanuvchidan tezlikni so'raymiz (km/soat da)
#  Vaqtni hisoblaymiz (formula: t = masofa / tezlik)
#  Natijani f-string yordamida chiqaramiz

print("Notes from Day1")
print("The print statement is used to output strings")
print("Strings are strings of characters")
print("String Concatenation is done with the+sing")
print("New lines can be created with a\and the letter n")

a=5.3
b=7.2
a, b = b, a
print("a =", a)
print("b =", b)

kocha="Bog'bon"
mahalla="Sog'bon"
tuman="Bodomzor"
viloyat="Samarqand"
manzil=(f"{kocha} kochasi, {mahalla} mahalla, {tuman} tuman, {viloyat} viloyat")
print(manzil.upper())
print(manzil.lower())
print(manzil.title())
print(manzil.capitalize())

a = 10
b = 3

print("Qo'shish:", a + b)
print("Ayirish:", a - b)
print("Ko'paytirish:", a * b)
print("Bo'lish:", a / b)
print("Qoldiqli bo'lish:", a % b)
print("Daraja:", a ** b)



# 2= mashaqlar

sonlar=[1,2,7,10,8]
eng_katta=sonlar[0]
for son in sonlar:
     if son > eng_katta:
        eng_katta = son

print("Eng katta son:", eng_katta)
sonlar = [1, 2, 7, 10, 8]

yigindi = 0

for son in sonlar:
    yigindi += son

print("Yig'indi:", yigindi)
for i in range(1, 11):
    for j in range(1, 11):
        print(f"{i} x {j} = {i*j}")
    print()


# 3 mashqalar





















