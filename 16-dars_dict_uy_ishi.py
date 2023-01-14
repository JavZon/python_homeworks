#16-dars. Lug'at. uy ishi

#Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi
#ma'lumotlarni lug'at ko'rinishida saqlang.Lug'atlarni bitta ro'yxatga
#joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring.

shaxs1={
        'ism':'mozart',
        'tyil':1756,
        'kasb':'muzikant'}

shaxs2={
        'ism':'navoiy',
        'tyil':1441,
        'kasb':'shoir'}

shaxs3={
        'ism':'avaz oxun',
        'tyil':1985,
        'kasb':'qiziqchi'}

person=[shaxs1, shaxs2, shaxs3]

#for a in person:
    #print(f" Ism - {a['ism'].title()}. "
          #f"{a['tyil']} - yilda tug'ilgan. "
          #f"Kasbi - {a['kasb'].title()}")

#Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing. 
#For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.

shaxs1={
        'ism':'bethoven',
        'tyil':1756,
        'kasb':'muzikant',
        'asar':['Moonlight Sonata', 'Fur Elise', 'Simphony N3']}

shaxs2={
        'ism':'navoiy',
        'tyil':1441,
        'kasb':'shoir',
        'asar':['Xamsa','Lison at Tayr', 'Mahbub ul Qulub']}

shaxs3={
        'ism':'ali qushchi',
        'tyil':1403,
        'kasb':'falakiyotshunos',
        'asar':['Hisob Risolasi', 'Astronomiya Risolasi', 'Matematika va Astronomik Jug\'rofiya']}

#person=[shaxs1, shaxs2, shaxs3]
#for b in person:
    #print(f"{b['ism'].title()}. Mashhur asarlari : ")
    #for c in b['asar']:
        #print(c)

#Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang.
#Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida lug'atga saqlang.
#Natijani konsolga chiqaring.

films= {
        'ali':['Titanic', 'Pirates of the Caribbean', 'Forsaj 7'],
        'vali':['Avatar', 'Avatar 2. The water way', 'Rembo'],
        'hasan':['Shaytanat', 'Tom and Jerry', 'Tarzan'] }

#for k,q in films.items():
    #print(f"\n{k.title()}ning sevimli kinolari quyidagilar :")
    #for z in q:
        #print(z)
    

#Davlatlar degan lug'at yarating, lug'at ichida bir nechta
#davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang.
#Har bir davlat haqida ma'lumotni konsolga chiqaring.

mamlakatlar={
    
    'zimbabwe':{'poytaxti':'Harare',
                'pul birligi':'USD',
                'aholisi':'15.9 million kishi',
                'rasmiy tili':'Shona, English'},
    
    "mozambique":{'poytaxti':'Maputo',
                 'pul birligi':'Mozambican metical',
                 'aholisi':'32.8 million kishi',
                 'rasmiy tili':'Portuguese'},
    
    'burkina faso':{'poytaxti':'Ouagadougou',
                    'pul birligi':'West African CFA franc',
                    'aholisi':'22.1 million kishi',
                    'rasmiy tili':'French'},
    
    "côte d'ivoire":{'poytaxti':'Yamoussoukro',
                     'pul birligi':'West African CFA franc',
                     'aholisi':'27.48 million kishi',
                     'rasmiy tili':'French'} 
    }

for k,v in mamlakatlar.items():
    print(f"\nMamlakat nomi : {k.title()}.")
    for a,b in v.items():
        print(f"{a.title()} - {b}")


#Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas,
#foydalanuvchi so'ragan davlat haqida ma'lumot bering. 
#Agar davlat sizning lug'atingizda mavjud bo'lmasa, 
#"Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.


mamlakatlar={
    
    'zimbabwe':{'poytaxti':'Harare',
                'pul birligi':'USD',
                'aholisi':'15.9 million kishi',
                'rasmiy tili':'Shona, English'},
    
    "mozambique":{'poytaxti':'Maputo',
                 'pul birligi':'Mozambican metical',
                 'aholisi':'32.8 million kishi',
                 'rasmiy tili':'Portuguese'},
    
    'burkina faso':{'poytaxti':'Ouagadougou',
                    'pul birligi':'West African CFA franc',
                    'aholisi':'22.1 million kishi',
                    'rasmiy tili':'French'},
    
    "kot divar":{'poytaxti':'Yamoussoukro',
                     'pul birligi':'West African CFA franc',
                     'aholisi':'27.48 million kishi',
                     'rasmiy tili':'French'} 
    }

#dav=input("Istalgan davlat nomini kiriting : ").lower()

#if dav in mamlakatlar:
    #y=mamlakatlar[dav]
    #print(f"\nMamlakat nomi - {dav.title()}"
     #     f"\nPoytaxti - {y['poytaxti']} shahri"
    #      f"\nPul birligi - {y['pul birligi']}"
   #       f"\nAholi soni - {y['aholisi']}"
  #        f"\nRasmiy tili - {y['rasmiy tili']}"
 #         )
#else:
    #print("Bizda bu davlat haqida ma'lumot mavjud emas")        
    
    
    

  
    
    
    





































