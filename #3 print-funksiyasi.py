#03-dars. PRINT() funksiyasi
#Sana: 13.10.2021

print("Hello world")
# YOKI
print('Hello world')
# birtirnoq matn ichida qo'shtirnoq qo'llanilsa ishlatiladi 
# misol uchun 
print('Men "Dell" markasidagi noutbook sotib oldim')
# yoki 2ta qo'shtirnoq ishlatilsa, qo'shtirnoqlardan oldin /-drop(backslash) belgisi qo'yiladi
print("Men \"Dell\" markasidagi noutbook sotib oldim")
# qatorga ajratib yozish uchun esa 3talik qo'shtirnoq ishlatiladi ya'ni """
print("""akang kuchaydi uje, 
akangdan zo'ri yoq""")
# qatorga ajratishning yana bir usuli \n belgini ishlatish 
print("""akang kuchaydi uje, \nakangdan zo'ri yoq""") 
# yoki birtirnoq ishlatadigan bo'lsak boshqa birtirnoqlardan ajralib turishi uchun matndagi birtirnoqqa \ belgisi qo'shiladi
print('odami ersang, demagil odami,\nOniki, yo\'q xalq g\'amidin g\'ami') 


# bo'lish amali / belgisi orqali bajariladi va bunda natija misol uchun 20/5 = 4.0 ko'rinishida chiqadi
print(20/5) #javob 4.0
print(15/4) #javob 3.75
# agar 2ta drop amali bajarilsa, natijaning butun qismi ko'rsatiladi
print(15/4) #javob 3
# 2ta ko'paytirish amali darajani beradi
print(5**4) #javob 625
# matnni sonlar bilan birlashtirish uchun oraga vergul qo'yiladi
print("To'qqizning kvadrati", 9**2, "ga teng") #To'qqizning kvadrati 81 ga teng
print('3x3=',3*3) #javob 3x3= 9
# yana bir ishora % ishorasi sonlarni bir-biriga bo'lgandagi qoldiqni ifodalaydi
print(29%3) #qoldiq 2


#Radiusi 5 ga teng bo'lgan aylananing uzunligi quyidagicha hisoblanadi
print(2*5*3.14159) #pi=3.14159




                            #Amaliyot
# 1.Quyidagi matnni aynan shunday ko'rinishda konsolda chiqaring:
# "Nexia", "Tico", 'Damas' ko'rganlar qilar havas
print("\"Nexia\", \"Tico\", 'Damas' ko'rganlar qilar havas")

# 2.Quyidagi misollarga yechimni Pythonda chiqaring. Har bir misoldan avval misol matnini izoh ko'rinishida yozing:
 #1 5ning 4-darajasi
print("5ning 4-darajasi", 5**4,"ga teng")
 #2 22 ni 4 ga bo'lganda qancha qoldiq qoladi?
print('22 ni 4 ga bo\'lganda qoldiq', 22%4)
 #3 Tomonlari 125 ga teng kvadratning yuzi va perimetrini toping
print('Tomonlari 125 ga teng kvadratning yuzi',125**2,'va perimetri', 125*4,'ga teng')
 #4 Diametri 12 ga teng bo'lgan doiraning yuzini toping ( π=3.14 deb oling)
print('Diametri 12 ga teng bo\'lgan doiraning yuzi',12*3.14,'ga teng')
 #5 Katetlari 6 va 7 bo'lgan to'g'ri burchakli uchburchakning gipotenuzasini toping (Pifagor teoremasidan foydalaning)
print('Katetlari 6 va 7 bo\'lgan to\'g\'ri burchakli uchburchakning gipotenuzasi',(6**2+7**2)**(1/2),'ga teng')







