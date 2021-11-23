# 18-dars. WHILE, RO'YXATLAR VA LUG'ATLAR
# 22.11.2021

# ismlar = []

# print("Yaqin do'stlaringiz ro'yxatini tuzamiz.")
# n=1
# while True:
#     savol = f"{n}-do'stingiz ismini kiriting:"
#     ism = input(savol)
#     ismlar.append(ism)
#     javob = input("Yana ism qo'shasizmi(ha/yo'q)? ")
#     if javob == 'ha':
#         n+=1
#         continue
#     else:
#         break
# print("Do'stlaringiz ro'yxati:")
# for ism in ismlar:
#     print(ism.title())

# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar = {}
# ishora = True
# while ishora:
#     ism = input("Do'stingiz ismini kiriting: ")
#     yosh = input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism] = int(yosh)
    
#     javob = input("Yana ma'lumot qo'shasizmi(ha/yo'q)? ")
#     if javob == "yo'q":
#         ishora = False
        
# for ism, yosh in dostlar.items():
#     print(f"{ism.title()} {yosh} yoshda")

# cars = ['lacetti','nexia','toyota','nexia','audi','malibu','nexia']
# while 'nexia' in cars:
#     cars.remove('nexia')
# print(cars)     #Yuqoridagi tsikl toki cars degan ro'yxatda 'nexia' qiymati tugagunga qadar takrorlanaveradi.


                     ### AMALIYOT
# Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing.
# Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.
#1
# savat = []
# while True:
#     mahsulot = input("Savatga mahsulot qo'shing: ")
#     savat.append(mahsulot)
#     javob = input("Yana mahsulot qo'shasizmi(ha/yo'q)? ")
#     if javob != 'ha':
#         break

#2
# e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing.
# Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.  

# mahsulotlar = {}
# while True:
#     mahsulot = input('Mahsulot nomini kiriting: ')
#     narh = input(f"{mahsulot.capitalize()}ning narhini kiriting: ")
#     mahsulotlar[mahsulot] = narh
#     javob =  input("Yana mahsulot qo'shasizmi(ha/yo'q)? ")
#     if javob != 'ha':
#         break
# print("\nRo'yxatdagi mahsulotlar: ")
# for mahsulot in  mahsulotlar:
#     print(f"{mahsulot.capitalize()} ning narhi: {narh}so'm")

#3
# buyurtmalar = []
# mahsulotlar = {'olma':20000,
#                'shaftoli':25000,
#                'tarvuz':18000,
#                'uzum':22000}

# while True:
#     buyurtma = input('Qaysi mahsulot xohlaysiz? ')
#     buyurtmalar.append(buyurtma)
#     while buyurtmalar:
#         buyurtma = buyurtmalar.pop()
#         if buyurtma in mahsulotlar.keys():
#             narh = mahsulotlar[buyurtma]
#             print(f"{buyurtma.title()} - {narh} so'm")
#         else:
#             print(f"Bizda {buyurtma} yo'q")
        
#     javob = input("Yana mahsulot qo'shasizmi(ha/yo'q)? ")
#     if javob != 'ha':
#         break

