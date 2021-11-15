# 10-dars. IF-ELSE Dasturni tarmoqlashni o'rganamiz
# Sana: 12.11.2021

# if OPERATORI
# avtolar = ['audi','bmw','volvo','kia','hyundai']

# for avto in avtolar:
#     if avto=='bmw':
#         print(avto.upper())
#     else:
#         print(avto.title())
# # ism = 'Ali'
# # ism.lower() == 'ali'    == belgisi tengmi degani
# # True                    != belgisi esa teng emasmi degani
# ism = input('Ismingiz nima?\n>>>')  
# if ism.lower() != 'ali':
#     print(f"Uzr {ism.title()}, biz Alini kutyapmiz.")
# else:
#     print('Salom, Ali')


                ### SONLARNI SOLISHTIRISH
# Kichik: a<b
# Kichik yoki teng: a<=b
# Katta: a>b
# Katta yoki teng: a>=b
# javob = float(input('12x6 nechchiga teng?>>>'))
# if javob != 72:
#     print('Javob xato!')
    
# yosh = int(input('Yoshingiz nechchida?>>>'))
# if yosh>=18:
#     print('Xush kelibsiz!')
# else:
#     print('Kirish mumkin emas!')
    
# login = input("Yangi login tanlang:")
# if len(login)<=5:
#     print("Login 5ta harfdan ko'proq bo'lishi shart!")

# yil = int(input('Tug\'ilgan yilingizni kiriting:>>>'))
# if 2021-yil<18:
#     print(f"Yoshingiz {2021-yil}da ekan.")
#     print('Kirish mumkin emas!')
# else:
#     print('Xush kelibsiz')

                ## Bir qatorga yozish!!!
# yosh = int(input('Yoshingiz nechchida?>>>'))
# if yosh>65: print('Siz COVID-19 risk guruhida ekansiz!')

# x, y = 25, 50
# print('x>y') if x>y else print('x<y')


                            ### AMALIYOT

##1
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car == 'gm':
#         print(car.upper())
#     else:
#         print(car.title())
        
##2
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car != 'gm':
#         print(car.title())
#     else:
#         print(car.upper())
   
##3     
# login = input('Loginni kiriting?>>>') 
# if login.lower() == 'admin':
#     print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz, {login}!")

##4
# x = int(input('Birinchi sonni kiriting:\n>>>'))
# y = int(input('Ikkinchi sonni kiriting:\n>>>'))
# if x==y:
#     print('Sonlar teng!')
    
##5 
# x = int(input('Istalgan sonni kiriting:\n>>>'))
# print("Manfiy son") if x<0 else print("Musbat son")

##6
# x = int(input('Istalgan sonni kiriting:\n>>>'))
# if x>0:
#     print(x**(1/2))
# else:
#     print('Musbat son kiriting!')



    




