# 18-dars. while_lug'at_list

#Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. 
#Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.

#buyurtmalar=[]
#while True:
 #   mahsulot=input("Nima buyurtma berasiz ? ")
  #  buyurtmalar.append(mahsulot)
   # javob=input("Yana buyurtma berasizmi ? (ha/yo'q) >>> ")
    #if javob=='ha':
     #   continue
    #break
#print("\nSiz quyidagilarni buyurtma qildingiz :")
#for a in buyurtmalar:
 #   print(a.upper())


#e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing.
#Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.


#e_bozor={}
#while True:
    #mah_nomi=input("Savatga mahsulot qo'shing : ")
    #mah_narhi=float(input(f"{mah_nomi.title()} necha so'm ? "))
    #e_bozor[mah_nomi]=mah_narhi
   # savol=input("Yana mahsulot qo'shasizmi ? (ha/yo'q) >>> ")
 #   if savol!='ha':
  #      break
#print("Siz kiritgan mahsulotlar : ")
#print(e_bozor)    

#Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir
#mahsulotni e-bozordagi mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin). 
#Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, 
#aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.

zakaz=['olma', 'anor', 'uzum', 'banan']
menu={
      'olma':5000,
      'tarvuz':7400,
      'banan':9800,
      'shaftoli':12000
      }

while zakaz:
    a=zakaz.pop()
    if a in menu.keys():
        print(f"{a.title()} {menu[a]} so'm")
    else:
        print(f"Afsuski bizda {a.title()} yo'q")
                    







