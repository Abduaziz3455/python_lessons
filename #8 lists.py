# 08-dars. LISTS(RO'YXATLAR BILAN ISHLASH)
# Sana: 19.10.2021


## RO'YXATNI TARTIBLASH
# sort() metodi alifbo ketma-ketligida tartiblaydi
cars = ['bmw', 'mersedes benz', 'volvo', 'general motors', 'tesla', 'audi']
cars.sort()
print(cars)
# Matndagi so'zlarning bosh harfi katta-kichik harf bilan bilan yozilgan bulmasligi kk
cars = ['Bmw', 'mersedes benz', 'volvo', 'general motors', 'tesla', 'audi']
cars.sort()
print(cars)
# Yuqoridagi misolda 'Bmw' elementi katta harf bilan boshlangani uchun ro'yxatning boshidan joy oldi.

# Ro'yxatni teskari alifbo tartibda saqlash uchun .sort() metodi ichida reverse=True argumentini ham kiritamiz.
cars = ['bmw', 'mersedes benz', 'volvo', 'general motors', 'tesla', 'audi']
cars.sort(reverse=True)
print(cars)
# O'zgaruvchi qiymatini o'zgartirmasdan ro'yxatni tartiblash uchun sorted() funksiyasidan foydalanamiz
mehmonlar = ['Odil', 'Farruh', "Temur", 'Maqsud', 'Hamid', 'Shamsiddin']
print("sorted() qaytagan ro'yxat:", sorted(mehmonlar) )
print("Asl ro'yxat:", mehmonlar)
# sorted() funktsiyasi yordamida teskari tartiblash uchun ham reverse=True argumentini beramiz:
print(sorted(mehmonlar, reverse=True))
# Yuqoridagi ikki usul bilan sonli ro'yxatlarni ham tartiblashimiz mumkin:
ages = [12, 56, -5.5, -32, 48]
ages.sort()
print(ages)
print(sorted(ages, reverse=True))

## RO'YXATNI AYLANTIRISH
# Ba'zida ro'yxatni aylantirish (boshini oxiriga, oxirini boshiga) talab qilinishi mumkin. Buning uchun .reverse() metodidan foydalanamiz.
fruits = ['apple', 'pear', 'watermelon', 'lemon', 'banana']
fruits.reverse()
print(fruits)

## RO'YXATNING UZUNLIGINI BILISH
# Ro'yxatning uzunligi, ya'ni uning ichidagi elementlar sonini aniqlash uchun len() funktsiyasidan foydalanamiz:
fruits = ['apple', 'pear', 'watermelon', 'lemon', 'banana']
print("Elementlar soni: ", len(fruits))

## range() FUNKTSIYASI
# Bu funktsiya yordamida biz ma'lum oraliqdagi sonlar ketma-ketligini yaratishimiz mumkin. list() funktsiyasi yordamida esa bu oraliqni ro'yxat shaklida saqlab olamiz:
sonlar = list(range(0,10))
print(sonlar)
# E'tibor qiling range() funktsiyasi ikkinchi indeksdan bitta avval to'xtaydi.
# range() yordamida qadamni ham berishimiz mumkin:
juft_sonlar = list(range(0,20,2)) # 0dan 20gacha bo'lgan sonlarni 2ta qadam bilan
toq_sonlar = list(range(1,20,2)) # 1dan 20gacha bo'lgan sonlarni 2ta qadam bilan
print('Juft sonlar: ', juft_sonlar)
print('Toq sonlar: ', toq_sonlar)
# Agar sonlar ketma-ketligi 0 dan boshlansa, range() funktsiyasida yakuniy indeksni ko'rsatish kifoya. Misol uchun range(0,10) emas range(10) deb yozsak ham bo'laveradi.

## SONLI RO'YXAT USTIDA SODDA AMALLAR
# ro'yxatdagi eng kichik sonni topish uchun min() funktsiyasidan, eng katta sonni topish uchun esa max() funktsiyasidan, sonlarning yig'indisini topish uchun esa sum() funktsyasidan foydalansak bo'ladi:
narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
arzon = min(narhlar)
qimmat = max(narhlar)
jami = sum(narhlar)
print("Eng arzon narh ", arzon, ". Eng qimmat narh ", qimmat, "\nJami: ", jami)
 ## RO'YXATNI KESISH
cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
my_cars = cars[0:3] # 0-indeskdan boshlab 3 ta element ajratib olamiz
print(my_cars)
# Python 3-indeksdan bitta avval to'xtaydi. Yuqoridagi misolda ham 0,1,2-elementlar ajratib olindi.
print(cars[2:5]) # 2-3-4-elementlarni ajratib olamiz (5 kirmaydi)
# Agar boshlang'ich indeksni bermasangiz, Python avtomat ravishda 0 indeksdan boshlab kesadi. Agar 2-indeksni kiritmasangiz, ro'yxat oxirigacha kesadi:
print(cars[:4]) # Ro'yxat boshidan 4-gacha kesadi 4 kirmaydi
print(cars[2:]) # 2-elementdan boshlab ro'yxat oxirigacha kesib oladi

## RO'YXATDAN NUSXA OLISH
sonlar = [1,2,3,4,5]
sonlar2 = sonlar
sonlar2.append(6)
sonlar2.append(7)
print("Bu sonlar ro'yxati:", sonlar)
print("Bu sonlar2 ro'xati:", sonlar2)
# sonlar2=sonlar deb yozgan komandamiz yangi ro'yxat yaratish o'rniga, ikkala o'zgaruvchini ham bitta ro'yxatga bog'lab (yo'naltirib) qo'ydi. Biz sonlar yoki sonlar2 ustida bajargan amallarimiz aslida bitta ro'yxat ustida bajarilyapti.

# Roy'xatdan nuxsa olish uchun esa yuqoridagi kabi ro'yxatni kesish usulidan foydalanamiz.
# Faqatgina, kvadrat qavs ichida ikkala indeksni ham ko'rsatmasdan, bo'sh qoldiramiz:
sonlar = [1,2,3,4,5]
sonlar2 = sonlar[:]
sonlar2.append(6)
sonlar2.append(7)
print("Bu sonlar ro'yxati:", sonlar)
print("Bu sonlar2 ro'xati:", sonlar2)

## TUPLES - O'ZGARMAS RO'YXAT
# Tuple ichidagi qiymatlarni bir marta, dastur boshida beriladi va so'ngra o'zgartirib bo'lmaydi. List dan farqli ravishda, Tuple e'lon qilishda kvadrat qavslar [] o'rniga oddiy qavslar () ishlatiladi:
tomonlar = [20, 55.2, 39]
print(tomonlar)
# Tuple ichidagi elementlarga huddi ro'yxat elementlariga murojat qilingani kabi murojat qilinaveradi:
tomonlar[2] = tomonlar[1] + 25
print(tomonlar[0])

toys = ('bus','car','bear','dino','snake','lizard')
print(toys[0])
print(toys[-3])
print(toys[2:5])
# toys[3] = 'dragon' ya'ni xatolik tuple turini o'zgartirib bulmaydi
toys = ('bus','car','bear','dino','snake','lizard')
toys = list(toys) # o'zgarmas ro'yxatni oddiy ro'yxatga (List) aylantiramiz
toys.append('dragon')
toys.remove('bus')
toys[1] = 'mcqueen'
toys = tuple(toys)
print(toys)


                            ### AMALIYOT
#1 O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
cities = ['Russia', 'Uzbekistan', 'Canada', 'USA']
# print(cities)
# print("Davlatlar soni:", len(cities))
# print(sorted(cities))
# print(sorted(cities, reverse=True))
# print(cities)
# cities.reverse()
# print(cities)
cities.sort()
print(cities)
cities.sort(reverse=True)
print(cities)
print(list(range(120,1201,2)))
print(sum(range(120,1201,2)))
print(max(range(120,1201,2)) - min(range(120,1201,2)))
print(len(range(120,1201,2)))
x = range(120,1201,2)
print(list(x[:20]))
print(list(x[270:290]))
print(list(x[521:]))

taomlar = ['manti', 'osh', 'kabob', 'pelmen', 'xonim']
nonushta = taomlar[:]
del nonushta[0]
del nonushta[2]
nonushta.append('tuxum')
nonushta.append('sut')
print(taomlar)
print(nonushta)
nonushta = tuple(nonushta)
nonushta[0] = "qaymoq va non" # xatolik o'zgartirib bo'lmaydi







