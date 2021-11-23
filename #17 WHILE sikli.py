# 17-dars. While sikli
# 20.11.2021

# yana input haqida
# ism = input("Ismingiz nima? ")
# savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
# yosh = input(savol)

# ism = input("Ismingiz nima? ")
# savol = f"Salom, {ism.title()}. Yoshingiz nechida? "
# yosh = input(savol)
# yosh = int(yosh) # yosh ni butun songa o'tkazamiz
# height = input("Bo'yingiz necha metr? ")
# height = float(height) # bo'yni o'nlik songa o'tkazamiz

## WHILE sikli
# son = 1 # son ga 1 qiymatini beramiz
# while son<=5: # toki son 5 dan kichik yoki teng ekan...
#     print(son, end=' ') # son ni konsolga chiqaramiz,
#     son = son+1 # songa 1 qo'shamiz.
# # son = son + 1 o'rniga son += 1 yozish m-n

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# qiymat = ''
# while qiymat != 'exit':
#     qiymat = input(savol)
#     if qiymat.lower() != 'exit':
#         print(float(qiymat)**2)
        
# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# ishora = True
# while ishora:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         ishora = False
#     else:
#         print(float(qiymat)**2)


## BREAK
# Break operatori yordamida ma'lum bir shartni tekshirish va whiletsikli bajarilishini to'xtatib qo'yish mumkin.

# print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
# savol = "Istalgan son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "
# while True:  #abadiy tsikl
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     else:
#         print(float(qiymat)**2)


# Break operatori for tsiklini to'xtatish uchun ham ishlatiladi.
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5:
#         break
#     print(f"{son}ning kvadrati {son**2} ga teng")

# CONTINUE
# Continue operatori esa aksincha, ma'lum bir shart bajarilganda qadam tashlab o'tish uchun mo'ljallangan.
# sonlar = list(range(1,11))
# for son in sonlar:
#     if son == 5: # son 5 ga teng bo'lsa tiskl boshiga qaytadi
#         continue
#     print(f"{son} ning kvadrati {son**2} ga teng")

# son = 0
# while son<10:
#     son += 1
#     if son%2!=0:    #ya'ni sonni 2ga bulganda qoldiq qolsa, usha sonlarni continue tufayli tashlab ketdi
#         continue
#     else:
#         print(son)

## ABADIY TSIKL TUZOG'I
# son = 1 
# while son>0:
#     son += 1
#     if son%2!=0:
#         continue
#     else:
#         print(son)

                    ### AMALIYOT
#1
# savol = "Sevgan kitobingizni kiriting"
# savol += "(barcha kitoblarni kiritib bo'lgach 'stop' deb yozing): "

# while True:
#     kitob = input(savol)
#     if kitob == 'stop':
#         break
# print('Rahmat!')       

#2
# savol = 'Iltimos, yoshingizni kiriting '
# savol += "(dasturdan chiqish uchun 'exit' yoki 'quit' ni bosing): "
# while True :
#     qiymat = input(savol)
#     if qiymat == 'exit' or qiymat == 'quit':
#         break
#     yosh = int(qiymat)
#     if yosh < 7:
#         narh = 2000
#     elif 7<=yosh<18:
#         narh = 3000
#     elif 18<=yosh<65:
#         narh = 10000
#     else:
#         narh = 0
        
        
#     if narh != 0:
#         print(f"Sizga kirish: {narh} so'm")
#     else:
#         print("Sizga kirish bepul!")

#3
# savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
# savol += "Musbat son kiriting "
# savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

# while True:
#     qiymat = input(savol)
#     if qiymat == 'exit':
#         break
#     son = int(qiymat)
    
#     if son<0:
#         print(f"{son}ning ildizi mavjud emas") #yoki continue
#     else:
#         ildiz = son**(0.5)
#         print(f"{son} ning ildizi {ildiz} ga teng")




        
        

        



        
