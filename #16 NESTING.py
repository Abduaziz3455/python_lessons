# 16-dars. NESTING (ro'yxatni ichiga ro'yxat yaratish)
# Sana: 16.11.2021

car0 = {
        'model':'lacetti',
        'rang':'oq',
        'yil':2018,
        'narh':13000,
        'km':50000,
        'korobka':'avtomat'
        }

car1 = {
        'model':'nexia 3',
        'rang':'qora',
        'yil':2015,
        'narh':9000,
        'km':89000,
        'korobka':'mexanika'
        }

car2 = {
        'model':'gentra',
        'rang':'qizil',
        'yil':2019,
        'narh':15000,
        'km':20000,
        'korobka':'mexanika'
        }
#Agar biz har bir lug'atga alohida murojat qiladigan bo'lsak, lug'atlarning nomlarini yodlab qolishimiz talab qilinar edi:
# car = car0
# print(f"{car['model'].title()},\
#    {car['rang']} rang,\
#    {car['yil']}-yil, {car['narh']}$")

# car = car1
# print(f"{car['model'].title()},\
#    {car['rang']} rang,\
#    {car['yil']}-yil, {car['narh']}$")

# car = car2
# print(f"{car['model'].title()},\
#    {car['rang']} rang,\
#    {car['yil']}-yil, {car['narh']}$")

#Keling, barcha avtolarni bitta ro'yxatga joylaymiz, va for tsikli yordamida birma-bir konsolga chiqaramiz:
# cars = [car0, car1, car2]
# for car in cars:
#     print(f"{car['model'].title()}, "
#         f"{car['rang']} rang,"
#         f"{car['yil']}-yil, {car['narh']}$")
    
# print(cars[0])
#Biror lug'atdagi elementga murojat qilish uchun esa quyidagi usuldan foydalanishimiz mumkin:
# print(cars[0]['model'])

# print(f"{cars[0]['rang'].title()} "
#       f"{cars[0]['model']}")

# malibus = []
# for n in range(10):
#     new_car = { # har bir yangi mashina uchun lug'at yaratamiz
#         'model':'malibu',
#         'rang':None, # rangi noaniq
#         'yil':2020,
#         'narh':None, # narhi belgilanmagan
#         'km':0,
#         'korobka':'avto'
#         }
#     malibus.append(new_car)  # yangi lug'atni ro'yxatga qo'shamiz

# for malibu in malibus[:3]:
#     malibu['rang'] = 'qizil'

# for malibu in malibus[3:6]:
#     malibu['rang'] = 'qora'
    
# for malibu in malibus:
#     if malibu['korobka'] == 'avto':
#         malibu['narh'] = 40000
#     else:
#         malibu['narh'] = 35000
        
# for malibu in malibus:
#     print(malibu)


                     ### LUG'AT ICHIDA RO'YXAT
                     
# dasturchilar = {
#     'ali':['python','css'],
#     'vali':['css', 'js', 'html'],
#     'hasan':['php', 'sql'],
#     'husan':['python', 'php'],
#     'maryam':['c++', 'c#']}
# for ism, tillar in dasturchilar.items():
#     print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:", end='')
#     for til in tillar:
#         print(f'{til.upper()} ', end='')

                     ### LUG'AT ICHIDA LUG'AT
# hamkasblar = {
#     'ali':{'familiya':'valiyev',
#            'tyil':1995,
#            'malumot':'oliy',
#            'tillar':['python','c++']
#            },
#     'vali':{'familiya':'aliyev',
#             'tyil':2001,
#             'malumot':"o'rta-maxsus",
#             'tillar':['html', 'css', 'js']},
#     'hasan':{'familiya':'husanov',
#              'tyil':1999,
#              'malumot':'maxsus',
#              'tillar':['python','php']}
#     }

# for ism,info in hamkasblar.items():
#     print(f"\n{ism.title()} {info['familiya'].title()} "
#           f"{info['tyil']}-yilda tug'ilgan. "
#           f"Ma'lumoti: {info['malumot']}")
#     print(f"Quyidagi dasturlash tillarini biladi:", end='')
#     for til in info['tillar']:
#         print(f"{til.upper()} ", end='')



                     ###AMALIYOT
# #1
# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#            'tyil':810,
#            'vyil':870,
#            'tjoy':'Buxoro'
#            }

# qodiriy = {'ism':'Abdulla Qodiriy',
#            'tyil':1894,
#            'vyil':1938,
#            'tjoy':'Toshkent'
#            }

# vohidov = {'ism':'Erkin Vohidov',
#            'tyil':1936,
#            'vyil':2016,
#            'tjoy':"Farg'ona"
#            }

# navoiy = {'ism':'Alisher Navoiy',
#            'tyil':1441,
#            'vyil':1501,
#            'tjoy':"Xirot"
#            }
# shaxslar = [buxoriy, qodiriy, vohidov, navoiy]
# for shaxs in shaxslar:
#     ism = shaxs['ism']
#     tyil = shaxs['tyil']
#     vyil = shaxs['vyil']
#     tjoy = shaxs['tjoy']
#     print(f"\n{ism} {tyil}-yilda {tjoy}da tug'ilgan "
#           f"va {vyil}-yilda vafot etgan.")

# #2
# buxoriy = {'ism':'Abu Abdulloh Muhammad ibn Ismoil',
#            'tyil':810,
#            'vyil':870,
#            'tjoy':'Buxoro',
#            'asarlar':["Al-jome’ as-sahih", "Al-adab al-mufrad", "At-tarix al-kabir", "At-tarix as-sag‘ir"]
#            }

# qodiriy = {'ism':'Abdulla Qodiriy',
#            'tyil':1894,
#            'vyil':1938,
#            'tjoy':'Toshkent',
#            'asarlar':["O'tkan kunlar","Mehrobdan Chayon",'Obid ketmon']
#            }

# vohidov = {'ism':'Erkin Vohidov',
#            'tyil':1936,
#            'vyil':2016,
#            'tjoy':"Farg'ona",
#            'asarlar':["Tong nafasi","Qo'shiqlarim sizga","O'zbegim","Qiziquvchan Matmusa"]
#            }

# navoiy = {'ism':'Alisher Navoiy',
#            'tyil':1441,
#            'vyil':1501,
#            'tjoy':"Xirot",
#            'asarlar':["Xamsa","Lison ut-Tayr","Mahbub Al-Qulub",'Munojot']
#            }

# shaxslar = [buxoriy, qodiriy, vohidov, navoiy]
# for shaxs in shaxslar:
#     ism = shaxs['ism']
#     print(f"\n{ism}ning mashhur asarlari quyidagilar:")
#     asarlar = shaxs['asarlar']
#     for asar in asarlar:
#         print(asar)

# #3
# kinolar = {
#     'ali':['Terminator','Rambo','Titanic'],
#     'vali':['Tenet','Inception','Interstellar'],
#     'hasan':['Abdullajon','Bomba','Shaytanat'],
#     'husan':['Mahallada duv-duv gap','John Wick']
#     }
# for ism, kinolar in kinolar.items():
#     print(f"\n{ism.title()}ning sevimli kinolari quyidagilar:")
#     for kino in kinolar:
#         print(f"{kino.title()}")
        
#4
davlatlar = {
    "o'zbekiston":{'poytaxt':"toshkent",
                   'maydon':448978,
                   'aholi':33_000_000,
                   'pul birligi':"so'm"
                   },
    "rossiya":{'poytaxt':"moskva",
                   'maydon':17_098_246,
                   'aholi':144_000_000,
                   'pul birligi':"rubl"
                   },
    "aqsh":{'poytaxt':"vashington",
                   'maydon':9_631_418,
                   'aholi':327_000_000,
                   'pul birligi':"dollar"},
    "malayziya":{'poytaxt':"kuala-lumpur",
                   'maydon':329750,
                   'aholi':25_000_000,
                   'pul birligi':"rinngit"}
    }
# for davlat, info in davlatlar.items():
#     poytaxt = info['poytaxt']
#     maydon = info['maydon']
#     aholi = info['aholi']
#     puli = info['pul birligi']
#     print(f"\n{davlat.capitalize()} davlatining poytaxti - {poytaxt.title()} shahri. \n"
#           f"Davlat maydoni: {maydon} km^2 \n"
#           f"Aholisi: {aholi} kishi\n"
#           f"Pul birligi: {puli.capitalize()} ")

# #5
# davlat = input('Qaysi davlat haqida ma\'lumot izlayapsiz?\n>>> ').lower()
# for mamlakatlar, info in davlatlar.items():
#     if davlat in mamlakatlar:
#         poytaxt = info['poytaxt']
#         maydon = info['maydon']
#         aholi = info['aholi']
#         puli = info['pul birligi']
#         print(f"\n{davlat.capitalize()} davlatining poytaxti - {poytaxt.title()} shahri. \n"
#               f"Davlat maydoni: {maydon} km^2 \n"
#               f"Aholisi: {aholi} kishi\n"
#               f"Pul birligi: {puli.capitalize()} ")

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    