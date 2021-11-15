# 09-dars. for TAKRORLASH OPERATORI
# Sana: 19.10.2021

mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
for mehmon in mehmonlar:
    print("Salom", mehmon)
    print("Hayr,", mehmon)    # agar printdan oldin  joy tashalmasa faqat bir marta Hayr {mehmon} chiqadi}

mehmonlar = ['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
for mehmon in mehmonlar:
    print(f"Hurmatli {mehmon}, sizni 20-dekabr kuni nahorgi oshga taklif qilamiz")
    print("Hurmat bilan, Palonchiyevlar oilasi\n")
    
sonlar = list(range(1,11))
for son in sonlar:
    print(f"{son} ning kvadrati {son**2} ga teng")
sonlar = list(range(11))
sonlar_kvadrati = []
for son in sonlar:
    sonlar_kvadrati.append(son**2)
    
print(sonlar)
print(sonlar_kvadrati)
dostlar = []
print("5ta eng yaqin do'stingizni kiriting: ")
for n in range(5):
    dostlar.append(input(f"{n+1}-do'stingizni ismini kiriting: "))
print(dostlar)


                            ##AMALIYOT
ismlar = ['Ozod', 'Alisher', 'Avaz', 'Javohir', 'Olim']
for ism in ismlar:
    print(f"Hurmatli kursdosh '{ism}' ertaga 20000 qarzingni olib kel")
print("Kod", len(ismlar), "marta takrorlandi")

a = list(range(11,100,2))
for son in a:
    print(f"{son}ning kvadrati {son**3} ga teng")

kinolar = []
print("5 ta sevimli kinoingiz qaysilar?")
for k in range(5):
    kinolar.append(input(f"{k+1}-kino: "))
print(kinolar)

n_people = int(input("Bugun nechta odam bilan so'rashdingiz?>>>"))
ismlar = []
for n in range(n_people):
    ismlar.append(input(f"{n+1}-suhbat qilgan odamingiz kim edi: "))
print(ismlar)


 