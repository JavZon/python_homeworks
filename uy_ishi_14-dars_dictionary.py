#14-dars. uy ishi dictionary mavzusida

#ukam={'ism':'aslbek', 't_yil':2004, 'kasb':'talaba'}

#print(f"Ukamning ismi- {ukam['ism'].title()}.\nTug'ilgan yili- {ukam['t_yil']}.\nHozirgi kasbi - {ukam['kasb']}")

#dasturhon={
    #'dadam':'osh',
    #'ayam':'manti', 
    #'ukam':'somsa', 
    #'singlim':'shashlik',
    #'akam':'mastava'
   # }

#print(f"Dadamning sevimli taomi - {dasturhon['dadam']}.\nAyamning sevimli taomi - {dasturhon['ayam']}.\nUkamning sevimli taomi - {dasturhon['ukam']}.")


py_dict={
    'integer':"Butun son degan ma'noni bildiradi",
    'float':"O'nlik son degan ma'noni bildiradi",
    'string':"Matn degan ma'noni bildiradi",
    'for':'Sikl hisoblanadi',
    'and':"Va degan ma'noni bildiradi",
    'or':'Yoki degan ma\'noni bildiradi',
    'append':"Ro'yxatga element qo'shish uchun ishlatiladi"
    }
#o'zim yozgan javob in dan foydalanib yozilgan

user_word=str(input("Istalgan so'z kiriting : ")).lower()
if user_word in py_dict:
    print(py_dict.get(user_word))
else:
    print(py_dict.get(user_word, "Bunday so'z mavjud emas"))    

# not in dan foydalanib yozilgan
#if user_word not in py_dict:
 #   print("Kechirasiz siz yozgan so'z lug'atda mavjud emas")
#else:
 #   print(py_dict.get(user_word))    


#ustoz yozgan javob
#kalit = input("Kalit so'z kiriting:").lower()
#tarjima = py_dict.get(kalit)
#if tarjima==None:
   # print("Bunday so'z mavjud emas")
#else:
    #print(f"{kalit.title()} so'zi {tarjima} deb tarjima qilinadi")
    












