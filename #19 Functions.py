# 19-dars. Funksiyalar
# 23.11.2021

# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum")

# def salom_ber(ism):
#     """Fodyalanuvchi ismini qabul qilib, unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")
# salom_ber('hasan')

# def salom_ber(ism):
#     """Fodyalanuvchi ismini qabul qilib, 
#         unga salom beruvchi funksiya"""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}!")
    
# print(salom_ber.__doc__)    #funksiya haqida ma'lumotni chiqaradi

### FUNKSIYAGA BIR NECHTA ARGUMENT UZATISH
# TO'G'RI TARTIBDA UZATISH
# def toliq_ism(ism,familiya):
#         """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#         print(f"Foydalanuvchining familiyasi: {familiya.title()} \n"
#               f"Foydalanuvchining ismi: {ism.title()}")
# toliq_ism('abduziz', 'abduraxmonov')

# def yosh_hisobla(ism, tugilgan_yil):
#         """Foydalanuvchi yoshini hisoblaydigan dastur"""
#         print(f"{ism.title()} {2021-tugilgan_yil} yoshda")
# yosh_hisobla('abduaziz', 2002)

# KALIT SO'Z BILAN UZATISH
# yosh_hisobla(ism='abduaziz', tugilgan_yil=2002)
# toliq_ism(familiya='abduraxmonov', ism='abduaziz')

# STANDART QIYMAT
# def yosh_hisobla(tugilgan_yil, joriy_yil=2021): # joriy yil uchun st.qiymat 2020
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
# yosh_hisobla(2002)

# FUNKSIYAGA MUROJAT QILISHDA XATOLIKLAR
# def yosh_hisobla(tugilgan_yil, joriy_yil=2021):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
    
# tyil = int(input("Tug'ilgan yilingizni kiriting: "))
# yosh_hisobla(tyil)

# def yosh_hisobla(tugilgan_yil, joriy_yil):
#     """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
#     print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

# yosh_hisobla(2002,2021)

# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum!")

# salom_ber('hasan')

# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#           f"Foydalanuvchi familiyasi: {familiya.title()}")
 
# toliq_ism('olim', 'hakimov')

                    ### AMALIYOT
#1 Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
# def tyiltop(ism, yosh):
#     print(f"{ism.title()} {2021-yosh} yoshda")

# tyiltop('abduaziz',2002)

#2
#Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
# def kvad_kub(son):
#     print(f"{son}ning kvadrati {son**2}ga, kubi {son**3}ga teng")
# kvad_kub(5)

#3
#Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.
# def juftmi(son):
#     """Kiritilgan son juft yoki toqligini konsolga chiqaruvchi funksiya"""
#     if son%2:
#         print(f"{son} toq son")
#     else:
#         print(f"{son} juft son")
# juftmi(20)
# juftmi(151)

#4
# Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing.
# Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
# def kat_kich(x,y=25):
#     """Ikki sonni solishtiruvchi funksiya"""
#     if x>y:
#         print(f"{x}>{y}")
#     elif x<y:
#         print(f"{x}<{y}")
#     else:
#         print("Sonlar teng")
# kat_kich(15)

#5
# Foydalanuvchidan x va y sonlarini olib, x^y ni konsolga chiqaruvchi funksiya yozing.
# Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.
# def daraja(x,y=2):
#     print(f"{x}ning {y}-darajasi {x**y}ga teng")
# daraja(51)

#6
# Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga 
# qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.
# def qoldiqsiz(x):
#     for n in range(2,11):
#         if not x%n:
#             print(f"{x} soni {n}ga qoldiqsiz bo'linadi")
# qoldiqsiz(36)








