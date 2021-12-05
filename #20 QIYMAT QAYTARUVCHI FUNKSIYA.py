# 20-dars. QIYMAT QAYTARUVCHI FUNKSIYA
# 23.11.2021

# def toliq_ism_yasa(ism,familiya):
#     """Toliq ism qaytaruvchi funksiya"""
#     toliq_ism = f"{ism.title()} {familiya.title()}"
#     return toliq_ism
# talaba1 = toliq_ism_yasa('abduaziz','abduraxmonov')
# talaba2 = toliq_ism_yasa('olim','hakimov')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")


# def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#     """Toliq isma qaytaruvchi funksiya"""
#     if otasining_ismi: # otasining_ismi mavjudligini tekshiramiz
#         toliq_ism = f"{ism} {otasining_ismi} {familiya}"  ## mahalliy o'zgaruvchilar
#     else:
#         toliq_ism = f"{ism} {familiya}"
#     return toliq_ism.title()

# talaba1 = toliq_ism_yasa('olim','hakimov') #otasining_ismi kiritilmadi
# talaba2 = toliq_ism_yasa('hakim','olimov','abrorovich')
# print(f"Darsga kelmagan talabalar: {talaba1} va {talaba2}")

# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=''):
#     avto = {'kompaniya':kompaniya,
#             'model':model,
#             'rang':rangi,
#             'korobka':korobka,
#             'yil':yili,
#             'narh':narhi}
#     return avto

# avto1 = avto_info('GM','Malibu','Qora','Avtomat',2018)
# avto2 = avto_info('GM','Gentra','Oq','Mexanika',2016,15000)
# avtolar = [avto1, avto2]
# print('Onlayn bozordagi mavjud avtomashinalar:')
# for avto in avtolar:
#     if avto['narh']:
#         narh = avto['narh']
#     else:
#         narh = "Noma'lum"
#     print(f"{avto['rang']} {avto['model']}. Narhi: {narh}")

# FUNKSIYADAN RO'YXAT QAYTARAMIZ
# def oraliq(min,max,qadam):
#     sonlar = []
#     while min<max:
#         sonlar.append(min)
#         min += qadam
#     return sonlar
# print(oraliq(0,10,2))
# print(oraliq(10,21,4))

## FUNKSIYALARNI TSIKLDA ISHLATISH

# print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")
# avtolar=[] # salondagi avtolar uchun bo'sh ro'yxat
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting",end='')
#     kompaniya=input("Ishlab chiqaruvchi: ")
#     model=input("Modeli: ")
#     rangi=input("Rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("Narhi: ")
    
#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))
    
#     javob = input("Yana avto qo'shasizmi (yes\no)?")
#     if javob == 'no':
#         break
# for avto in avtolar:
#     if avto['narh']:
#         print(f"{avto['rang'].title()} {avto['model'].title()} {avto['korobka']}. Narhi: {avto['narh']}$")
#     else:
#        print(f"{avto['rang'].title()} {avto['model'].title()} {avto['korobka']}.") 


                                    ### AMALIYOT
# Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini qabul qilib,
# lug'at ko'rinishida qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin.
# Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)
#1

# def foydalan_info(ism, familiya, tyil, email='', tel=None):
#     foydalan = {'ismi':ism,
#             'familiyasi':familiya,
#             "tyil":tyil,
#             'emaili':email,
#             'telefoni':tel,
#             'yoshi':2021-tyil}
#     return foydalan
# foy_lar = []
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting",end='')
#     ismi = input("Ismingizni kiriting: ")
#     familiyasi = input("Familiyangizni kiriting: ")
#     tyil = int(input("Tug'ilgan yilingizni kiriting: "))
#     emaili = input("Emailingizni kiriting: ")
#     telefoni = input("Telefon raqamingizni kiriting: ")
#     foy_lar.append(foydalan_info(ismi, familiyasi, tyil, emaili, telefoni))
#     javob = input("Davom etasizmi? (ha/yo'q)")
#     if javob!='ha':
#         break
# print("Foydalanuvchilar: ")
# for foyda in foy_lar:
#     print(f"{foyda['ismi'].title()} {foyda['familiyasi'].title()}, {foyda['yoshi']} yoshda, telefoni:{foyda['telefoni']}")

#2
# def kattasi(x,y,z):
#     max=x
#     if y>=max:
#         max=y
#     elif z>=max:
#         max=z
#     return max
# print(kattasi(12, 20, -151))

#3
# def aylana_info(radius, pi=3.14159):
#     aylana = {'radius':radius,
#               'diametr':radius*2,
#               'uzunlik':2*pi*radius,
#               'yuza':pi*radius**2}
#     return aylana
# print(aylana_info(5))

#4 Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing
# (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)
# def tub_sonlar_top(min,max):
#     tub_sonlar = []
#     for n in range(min,max+1):
#         tub = True
#         if n==1:
#             tub=False
#         elif n==2:
#             tub=True
#         else:
#             for x in range(2,n):
#                 if n%x==0:
#                     tub = False
#         if tub:
#             tub_sonlar.append(n)
#     return tub_sonlar
# print(tub_sonlar_top(9, 6065))

#5  F(n) = F(n-1) + F(n-2) va F(0) = 0, F(1) = 1 Fibonachchi ketma-ketligi
# def fibonacci(n):
#     sonlar = []
#     for x in range(n):
#         if x==0 or x==1:
#             sonlar.append(1)        
#         else:
#             sonlar.append(sonlar[x-1]+sonlar[x-2])
#     return sonlar

# print(fibonacci(10))












