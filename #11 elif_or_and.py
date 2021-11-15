# 11-dars. BIR NECHTA SHARTLARNI TEKSHIRISH. if-elif-else zanjiri, and, or operatorlari bilan tanishamiz
# Sana: 12.11.2021


# yosh = int(input('Yoshingiz nechchida? '))
# if yosh<=4:
#     print('Sizga kirish bepul.')
# elif yosh<=12:
#     print('Sizga kirish 5000 so\'m')
# else:
#     print('Sizga kirish 10000 so\'m')

# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     price = 0
# elif yosh<=12:
#     price = 5000
# else:
#     price = 10000

# print(f"Sizga kirish {price} so'm")

# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     price = 0
# elif yosh<=12:
#     price = 5000
# elif yosh<65:
#     price = 10000
# else:
#     price = 8000
# print(f"Sizga kirish {price} so\'m")


# yosh = int(input('Yoshingiz nechida? '))
# if yosh<=4:
#     price = 0
# elif yosh<=12:
#     price = 5000
# elif yosh<65:
#     price = 10000
# elif yosh>=65:
#     price = 8000
# print(f"Sizga kirish {price} so\'m")


# kun = input('Bugun nima kun?>>>')
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print('Bugun dam olish kuni.')
# else:
#     print('Bugun ish kuni.')

# kun = input('Bugun nima kun? ')
# harorat = float(input('Havo harorati qanday? '))
# if kun.lower()=='yakshanba' and harorat>=30:
#     print("Cho'milgani ketdik!")
# else:
#     print('Uyda dam olamiz!')

# kun = input("Bugun nima kun?")
# harorat = float(input("Havo harorati qanday?"))
# if (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat>=30:
#     print("Cho'milgani ketdik!")
# elif (kun.lower()=='shanba' or kun.lower()=='yakshanba') and harorat<30:
#     print("Uyda dam olamiz!")


                    ### BOOLEAN MA'LUMOTLAR TURI
# narh = 15000
# choy = True     #yoki True o'rniga 1 ni, False o'rniga 0 ni yozishimiz mumkin!
# salat = False
# if choy and salat:
#     narh = narh + 10000
# elif choy or salat:
#     narh = narh + 5000
    
# print(f"Jami {narh} so'm")

# narh = 15000 # mijoz 15 so'mga ovqat oldi
# choy = True
# salat = False
# non = True
# kompot = True
# assorti = False
# if choy:   # agar choy olsa
#     print("Mijoz choy oldi.")
#     narh = narh + 3000
# if salat:  # agar salat olsa
#     print("Mijoz salat oldi.")
#     narh = narh + 5000
# if non:    # agar non olsa
#     print("Mijoz non oldi.")
#     narh = narh + 2000
# if kompot: # agar kompot olsa
#     print("Mijoz kompot oldi.")
#     narh = narh + 5000
# if assorti: # agar assorti olsa
#     print("Mijoz assorti oldi.")
#     narh = narh + 15000
    
# print(f"Jami {narh} so'm")


# RO'YXAT TARKIBINI TEKSHIRISH
# "in" va "not in" OPERATORI

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# ovqat = input("Nima ovqat yeysiz? ")
# if ovqat.lower() in menu:
#     print("Buyurtma qabul qilindi")
# else:
#     print('Afsuski bizda bunday ovqat yo\'q')

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# ovqat = input("Nima ovqat yeysiz? ")
# if ovqat.lower() not in menu:
#     print('Afsuski bizda bunday ovqat yo\'q')
# else:
#     print("Buyurtma qabul qilindi")

# if not a==5 ifodasi if a!=5 ifodasi bilan bir hil natija qaytaradi.

# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ["osh","somsa","manti", "shashlik"]

# for taom in buyurtmalar:
#     if taom in menu:
#         print(f"Menuda {taom} bor")
#     else:
#         print(f"Kechirasiz, menuda {taom} yo'q")

## RO'YXAT BO'SH EMASLIGINI TEKSHIRISH
# menu = ['osh','qazonkabob','shashlik','norin','somsa']
# buyurtmalar = ["osh","somsa","manti", "shashlik"]

# if buyurtmalar: # ro'yxatda biror element bo'lsa bu ifoda TRUE qaytaradi
#     for taom in buyurtmalar:
#         if taom in menu:
#             print(f"Menuda {taom} bor")
#         else:
#             print(f"Kechirasiz, menuda {taom} yo'q")
# else: # agar ro'yxat bo'sh bo'lsa
#     print("Savatchangiz bo'sh!")




                    ### AMALIYOT
#1 
# son = int(input('Juft son kiriting: '))
# if son % 2 == 0:

#     print("Rahmat")
# else:
#      print("Bu son juft emas!")

#2
# yosh = int(input("Yoshingizni kiriting: "))

# if yosh<4 or yosh>60:
#     narh = 0
# elif yosh<18:
#     narh = 10000
# else:
#     narh = 20000
# print(f"Chipta {narh} so'm")
    
#3
# x = int(input("Birinchi sonni kiriting: "))
# y = int(input("Ikkinchi sonni kiriting: "))
# if x==y:
#     print(f"{x}={y}")
# elif x<y:
#     print(f"{x}<{y}")
# else:
#     print(f"{x}>{y}")

#4
# mahsulotlar = ["yog'", 'tuxum', 'sabzi', 'piyoz', 'kadi', 'kartoshka', 'sovun', 'uzum', 'olma', 'rediska']
# savat = []
# for n in range(5):        #for operatori ro'yxatdagi har bir elementni belgilab olish uchun ishlatiladi!
#     savat.append(input(f"Savatga {n+1}-mahsulotni kiriting: "))
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Do'konimizda {mahsulot} bor")
#     else:
#         print(f"Do'konimizda {mahsulot} yo'q")

#5
# mahsulotlar = ['un', "yog'", "sovun", 'tuxum', 'piyoz', 'kartoshka', 'olma', 'banan', 'uzum', 'qovun']
# savat = []

# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing: "))

# bor_mahsulotlar = []
# mavjud_emas = []
# for mahsulot in savat:    #ya'ni savatdagi mahsulot mahsulotlar ichida bo'lsa bor_mahsulotlar ro'yxatiga qo'shilsin
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#     print(f"\nDo'konimizda quyidagi mahsulotlar yo'q:")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#   print("Siz so'ragan barcha mahsulotlar do'konimizda bor")

#6
# users = ['olim', 'abduaziz', 'hacker', 'karim', 'hakim']
# yangi = input("Yangi login kiriting:\n")

# if yangi in users:
#     print("Login band, yangi login tanlang!")
# else:
#     print("Xush kelibsiz, foydalanuvchi!")

#7
# son = int(input('Butun son kiriting: '))

# for n in range(2,11):
#     if not (son%n):
#         print(f"{son} soni {n} ga qoldiqsiz bo'linadi!")




    
































