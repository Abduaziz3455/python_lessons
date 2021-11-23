# 14-15-dars. Dictionary
# Sana: 15.11.2021

# car_0 = {'model':'ferrari', 'rang':'qizil'}
# print(car_0['model'])
# print(car_0['rang'])

# en_uz = {'apple':'olma', 'apricot':"o'rik", 'banana':'banan'}
# talaba_0 = {'ism':'abduaziz abduraxmonov', 'yosh':19, 't_yil':2002}
# print(f"{talaba_0['ism'].title()},\
#   {talaba_0['yosh']} yoshda,\
#   {talaba_0['t_yil']}-yilda tug'ilgan")
# talaba_0['kurs'] = 2
# talaba_0['fakultet']='energo-mexanika'
# print(talaba_0)
# talaba_1 = {}
# talaba_1['ism'] = 'abduaziz abduraxmonov'
# talaba_1['kurs'] = 2
# talaba_1['yosh'] = 19
# print(talaba_1)
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")  
# del talaba_0['yosh']
# print(talaba_0)
telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'elshod':'nokia 2213',
    'maryam':'iphone x',
    'xurshid':'galaxy s9',
    'ozod':'iphone x'
    }

# phone = telefonlar['ali']
# print(f"Alining telefoni {phone}")
# phone = telefonlar['hasan']
# print(f"Hasanning telefoni {phone}")    #KeyError: 'hasan'

# phone = telefonlar.get('hasan', 'Bunday ism mavjud emas')       #ya'ni 1chi qiymat bo'lmaganda 2chi qiymat chiqadi
# print(phone)


                     ###AMALIYOT
#1
onam = {'ism':'nodira', 't_yil':1978, 'viloyat':'navoiy'}
# print(f"Onamning ismi {onam['ism'].title()}, u {onam['t_yil']}-yil va {onam['viloyat']}da yashaydi")

#2
s_taom = {'taom1':'osh', 'taom2':'manti', 'taom3':'kabob', 'taom4':'norin', 'taom5':'lag\'mon'}
# print(f"Alining sevimli taomi {s_taom['taom1']}")
# print(f"Ozodning sevimli taomi {s_taom['taom2']}")
# print(f"Orifning sevimli taomi {s_taom['taom3']}")

#3
# python = {'integer':'butun son', 'float':'ratsional son',\
#   'string':'matn', 'title':'1chi harf katta bo\'ladi', \
#   'get':'1chi qiymat bo\'lmaganda 2chi qiymat chiqadi', \
#   'for':'sikl operatori', 'strip()':'ikala tomondan bo\'shliqni yo\'qotadi', \
#   'list':'ro\'yhat yaratadi', 'tuple':'o\'zgartirib bo\'lmaydigan ro\'yhat yaratadi',\
#   'try(except)':'xatolik ustida ishlash'}

#4
# x = input("Biror atama kiriting: ")
# string = python.get(x, "mavjud emas")
# print(f"{x} ning ma'nosi {string}")

#5
# kalit = input("Kalit so'z kiriting: ").lower()
# tarjima = python.get(kalit)

# if tarjima==None:
#     print("Bunday so'z mavjud emas")
# else:
#     print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")




### Davomi...

##.items() metodi lug'atni chiroyli kurinishda yozish

# print(python.items())
# YOKI
# for key, value in python.items():
#     print(f"Kalit: {key}")
#     print(f"Qiymat: {value} \n")
    
    
# telefonlar = {
#     'ali':'iphone x',
#     'vali':'galaxy s9',
#     'olim':'mi 10 pro',
#     'orif':'nokia 3310'
#     }

# for k,q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}")

##.keys() metodi
mahsulotlar = {
    'olma' : 10000,
    'anor' : 20000,
    'uzum' : 40000,
    'anjir' : 25000,
    'shaftoli' : 30000}
# print(mahsulotlar.keys())
# print('Do\'kondagi mahsulotlar:')
# for mahsulot in mahsulotlar.keys():     #yoki keys ni yozmasak ham shu natijani beradi
#     print(mahsulot.title())

# bozorlik = ['anor', 'uzum', 'non', 'baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")
        
# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos, do'koningizga {buyum} ham olib keling")

## Lug'at elementlarini tartib bilan chiqarish
# print('Do\'konimizdagi mahsulotlar:')
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())

##.values() metodi
# print('Foydalanuvhilar quyidagi telefonlar ishlatishadi:')
# for tel in telefonlar.values():
#     print(tel)
    
## set() funksiyasi  list tuple kabi ro'yxat turi. farqi bir xil elementlarni olmaydi
# print('Foydalanuvhilar quyidagi telefonlar ishlatishadi:')
# for tel in set(telefonlar.values()):
#     print(tel)

toys = {'ball', 'car', 'lamp', 'ball', 'bear', 'car'}



                         ### AMALIYOT
#1                 
python = {'integer':'butun son', 'float':'ratsional son',\
  'string':'matn', 'title':'1chi harf katta bo\'ladi', \
  'get':'1chi qiymat bo\'lmaganda 2chi qiymat chiqadi', \
  'for':'sikl operatori', 'strip()':'ikala tomondan bo\'shliqni yo\'qotadi', \
  'list':'ro\'yhat yaratadi', 'tuple':'o\'zgartirib bo\'lmaydigan ro\'yhat yaratadi',\
  'try(except)':'xatolik ustida ishlash'}
# for key,value in sorted(python.items()):
#     print(f"{key.title()} - {value} ")

#2
poytaxtlar = {'uzbekiston':'tashkent', 'malayziya':'kuala-lumpur', 'aqsh':'vashington',\
              'canada':'ottava', 'avstraliya':'kanberra', 'yaponiya':'tokio'}
# print('Davlatlar:')
# for davlat in sorted(poytaxtlar.keys()):
#     if davlat == 'aqsh':
#         print(davlat.upper())
#     else:
#         print(davlat.title())
        
# print('\nPoytaxtlar:')
# for poytaxt in sorted(poytaxtlar.values()):
#     print(poytaxt.title())
    
#3
# davlat = input('Biror davlat nomini kiriting: ').lower()
# poytaxt = poytaxtlar.get(davlat, "Bizda bunday ma'lumot yo'q")
# print(f"{davlat.title()} poytaxti - {poytaxt.title()}")

#4  Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). 
# Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. 
# Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, 
# agar taom menuda bo'lsa narhini ko'rsating, 
# aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.
r_taomlar = {'osh':10000,\
  'manti':12000,\
  'kabob':35000,\
  'sho\'rva':10000,\
  'norin':20000,\
  'lag\'mon':22000,\
  'grechka':15000,\
  'somsa':8000,\
  'xonim':24000,\
  'bichak':5000}
    
print('3ta taom buyurtma bering.')
buyurtmalar = []
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom: ").lower())

for buyurtma in buyurtmalar:
    if buyurtma in r_taomlar:
        print(f"{buyurtma.title()}ning narxi {r_taomlar[buyurtma]} so'm")
    else:
        print(f"Kechirasiz, bizda {buyurtma} yo'q")


    

