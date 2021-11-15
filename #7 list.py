# 07-dars. LIST (RO'YXAT)
# Sana: 18.10.2021

# mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"] # mevalar ro'yxati (matnlar)
# narhlar = [12000, 18000, 10900, 22000] # narhlar ro'yxati (sonlar)
# sonlar = ['bir', 'ikki', 3, 4, 5] # sonlar va matnlar aralash ro'yxat
# ismlar = [] # bo'sh ro'yxat

mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]  # mevalar ro'yxati(matnlar)
print("Birinchi meva: ", mevalar[0])
print("Ikkinchi meva: ", mevalar[1])
# Agar list ichidagi elementlar matn ko'rinishid bo'lsa, ularga string metodlarni qo'llashimiz mumkin:
print("Birinchi meva: ", mevalar[0].title())
print("Ikkinchi meva: ", mevalar[1].upper())

# List elementlari ustida arifmetik amallar bajarish:
narhlar = [12000, 18000, 10900, 22000]
print(narhlar[0] + narhlar[1])
# Pythonda Listning eng oxirgi elementiga `-1` indeksi orqali ham murojat qilish mumkin. Bu usul Listning uzunligini bilmaganda juda asqotadi.
car_models = ['Toyota', 'BMW', 'GM', 'KIA', 'Volvo', 'Hyundai']
print(car_models[-1])

                        ### ELEMENTLARNI QO'SHISH, O'CHIRISH VA O'ZGARTIRISH
### Elementni o'zgartirish
narhlar = [12000, 18000, 10900, 22000]
narhlar[0] = 13000
narhlar[2] = 11000
narhlar[3] = narhlar[3] + 2000
print(narhlar)

## Yangi element qo'shish
# 1 Ro'yxatga yangi element qo'shishning oson usuli bu .append() metodi yordamida ro'yxatning oxiriga qiymat qo'shish:
mevalar = ['olma', 'anjir', 'shaftoli']
mevalar.append('tarvuz')
print(mevalar)

cars = []
cars.append('Lacetti')
cars.append('Captiva')
cars.append('Gentra')
print(cars)

# 2 Ro'yxatning istalgan joyiga yangi element qo'shish uchun .insert() metodidan foydalanamiz.
# .insert() metodi ichida yangi elementning indeksi va qiymati beriladi:
cars = ['Lacetti', 'Captiva', 'Gentra']
cars.insert(0, 'Malibu')
cars.insert(2, 'Damas')
print(cars)

## Elementni o'chirish
# Ro'yxatdan biror elementni olib tashlash uchun uning indeksini yoki qiymatini bilishimiz lozim.
# 1 Indeks yordamida olib tashlash uchun del operatoridan foydalanamiz:
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
del mevalar[1] #anjirni olib tashlaymiz
print(mevalar)

# 2 Element qiymati bo'yichi o'chirish uchun esa .remove(qiymat) metodidan foydalanamiz.
# Buning uchun qavs ichida o'chirib tashlash kerak bo'lgan qiymatni yozamiz
mevalar = ['olma', 'anjir', 'shaftoli', "o'rik"]
mevalar.remove('shaftoli')
print(mevalar)
# .remove(qiymat) metodi ro'yxatda uchragan birinchi mos keluvchi qiymatni o'chiradi. 
# Agar ro'yxatning ichida 2 va undan ko'p bir hil qiymatli elementlar bo'lsa, ulardan eng birinchisi o'chadi.
hayvonlar = ['it', 'mushuk', 'sigir', 'qo\'y', 'quyon', 'mushuk']
hayvonlar.remove("mushuk")
print(hayvonlar)

## Elementni sug'urib olish
# Ba'zida biror elementni butunlay o'chirib tashlash emas, balki uni ro'yxatdan sug'urib olish va undan foydalanish talab qilinishi mumkin.
# Buning uchun Pythonda .pop(indeks) metodidan foydalanmiz.
bozorlik = ["yog'", 'un', 'piyoz', 'banan', "go'sht"]
mahsulot = bozorlik.pop(3)
print("Men " + mahsulot + " sotib oldim")
print("Olinmagan mahsulotlar: ", bozorlik)
# Agar .pop() metodida indeks berilmasa, ro'yxatdan o'xirgi qiymat sug'urib olinadi.

### AMALIYOT
# 1,2
ismlar = ['Ozodbek', 'Aslbek', 'Oybek']
print("Salom " + ismlar[0] + ' qanaysan?')
print(ismlar[1] + ' qachan tashaymiz valorant?')
print(ismlar[2] + " tia portal qanay ketopti hay?")

# 3,4
sonlar = [12, -35, 5.8, -9.1]
print(sonlar[0] + sonlar[-1] * sonlar[2] / sonlar[1])
sonlar[0] = 25
sonlar[1] = -sonlar[0] + 12
print(sonlar)

# 5,6
t_shaxslar = ["Beruniy", "Xorazmiy", "Ibn Sino"]
z_shaxslar = ["Bill Gates", "Jeff Bezos", "Mark Zuckerberg"]
olim = t_shaxslar.pop(0)
milliarder = z_shaxslar[2]
print("Men tarixiy shaxslardan " + olim + " bilan, zamonaviy shaxslardan esa " + milliarder + " bilan suhbat qilishni istar edim!")

# 7,8
friends = []
friends.append('Firdavs')
friends.append('Ozodbek')
friends.append('Aslbek')
friends.append('Mahmud')
print("Men ertaga do'stlarim ", friends, "larni mehmonga aytmoqchi edim")
friends.remove('Ozodbek')
friends.remove('Mahmud')
print("Lekin faqat", friends, "lar kela olarkan")

#9
friends.insert(-1, 'Ali')
friends.insert(0, 'Azizbek')
friends.insert(2, 'Maqsud')
print(friends)

#10
mehmonlar = []
mehmonlar.append(friends.pop(2))
mehmonlar.append(friends.pop(1))
mehmonlar.append(friends.pop(-1))
print("\nKelgan mehmonlar: ", mehmonlar)










