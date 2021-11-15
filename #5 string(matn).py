# 05-dars. STRING (MATN)
# Sana: 15/10/2021

ism = "Abduaziz"
shahar = "Навоий"
viloyat = "Навои"

matn = "Men yangi 📱 oldim"
print(matn)

# STRING USTIDA AMALLAR
ism = 'Ahmad'
print("Mening ismim " + ism)
ism = 'Ahad'
familiya = 'Qayum'
print(ism + familiya)
# oraga joy tashlash uchun Ahad dan so'ng probel tashlash kk yoki pastdagi usul 
print(ism + ' ' + familiya)
# orani ochishni yana bir usuli f- stringidan foydalanish
ism_sharif = f"{ism} {familiya}"
print(ism_sharif)
ism = "James"
familiya = 'Bond'
print(f"Salom, mening ismim {familiya}. {ism} {familiya}!")

                          ### Maxsus belgilar
print('Hello \tworld')
print('Hello \nworld')
#Matnga bo'shliq qo'shish uchun `\t` belgisidan, yangi qatordan boshlash uchun `\n` belgisidan foydalanamiz:

              # upper() va lower() metodlari
ism = 'Ahad'
familiya = 'Qayum'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif.upper())
#upper() metodi matndagi har bir harfni katta harfga o'zgartiradi.
ism = 'Ahad'
familiya = 'Qayum'
ism_sharif = f"{ism} {familiya}"
print(ism_sharif.lower())

              #title() va capitalize() metodlari
#title() metodi matndagi har bir so'zning birinchi harfini katta harf bilan yozadi.
ism_sharif = 'james bond'
print(ism_sharif.title())
#capitalize() esa faqatgina eng birinchi so'zning birinchi harfini katta bilan yozadi.
ism_sharif = 'james bond'
print(ism_sharif.capitalize())

#Metodlarni faqat o'zgaruvchilarga emas, balki to'g'ridan-to'g'ri matnga ham qo'llash mumkin (aslida o'zgaruvchi ham matnning (yoki boshqa ma'lumotning) manzili xolos)
print('james bond'.title())

## strip(), rstrip() va lstrip() metodlari
#Bu metodlar matnning boshi va oxiridagi bo'sh joylarni olib tashlaydi.
#- `lstrip()` — matn boshidagi bo'shliqni,
meva = "   olma   "
print("men " + meva.lstrip() + 'ni yaxshi ko\'raman' )
#- `rstrip()` – matn oxiridagi bo'shliqni,
meva = "   olma   "
print("men " + meva.rstrip() + 'ni yaxshi ko\'raman' )
#- `strip()` — matn boshi va oxiridagi bo'shliqlarni olib tashlaydi
meva = "   olma   "
print("men " + meva.strip() + 'ni yaxshi ko\'raman' )

## INPUT — FOYDALANUVCHI BILAN MULOQOT
#ism = input("Ismingiz nima?")
#print("Assalomu alaykum," + ism)

#ism = input("Ismingiz nima?\n>>>")
#print("Assalomu alaykum," + ism)



                        ## AMALIYOT
#1
kocha = "Amir temur "
mahalla = "o'zbekiston"
tuman = "navoi"
viloyat = "navoiy"
#Yuqoridagi o'zgaruvchilarni jamlab, quyidagi ko'rinishda konsolga chiqaring:
#Bog'bon ko'chasi, Sog'bon mahallasi, Bodomzor tumani, Samarqand viloyati
#print(kocha.title().strip() + " ko'chasi, " + mahalla.capitalize().strip() + " mahallasi, " + tuman.capitalize() + " tumani, " + viloyat.capitalize() + " viloyati")
#2
#Yuqoridagi o'zgaruvchilarning qiymatini foydalanuvchidan so'rang.
#print("Iltimos, quyidagi ma'lumotlarni kiriting:")
#kocha = input("Ko'changiz: ")
#mahalla = input("Mahallangiz: ")
#tuman = input("Tumaningiz: ")
#viloyat = input("Viloyatingiz: ")
#print(kocha + " ko'chasi, " + mahalla + " mahallasi, " + tuman + " tumani, " + viloyat + " viloyati")
#3
print(kocha + " ko'chasi,\n" + mahalla + " mahallasi,\n" + tuman + " tumani,\n" + viloyat + " viloyati\n")
#4
# Yuqoridagi o'zgaruvchilarni f-string yordamida, yangi manzil deb nomlangan o'zgaruvchiga yuklang
manzil = f"{kocha} ko'chasi, {mahalla} mahallasi, {tuman} tumani, {viloyat} viloyati"
print(manzil)
#5
# manzilga biz yuqorida o'rgangan title(), upper(), lower() , capitalize() metodlarini qo'llab ko'ring.
print(manzil.upper())
print(manzil.lower())
print(manzil.title())
print(manzil.capitalize())


