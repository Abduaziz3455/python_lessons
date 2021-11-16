# 14-dars. Dictionary
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
    'orif':'nokia 3310'
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
python = {'integer':'butun son', 'float':'ratsional son',\
  'string':'matn', 'title':'1chi harf katta bo\'ladi', \
  'get':'1chi qiymat bo\'lmaganda 2chi qiymat chiqadi', \
  'for':'sikl operatori', 'strip()':'ikala tomondan bo\'shliqni yo\'qotadi', \
  'list':'ro\'yhat yaratadi', 'tuple':'o\'zgartirib bo\'lmaydigan ro\'yhat yaratadi',\
  'try(except)':'xatolik ustida ishlash'}

#4
x = input("Biror atama kiriting: ")
# string = python.get(x, "mavjud emas")
# print(f"{x} ning ma'nosi {string}")

#5
if x = python:
    print(f"{x} ning ma'nosi {string}")




