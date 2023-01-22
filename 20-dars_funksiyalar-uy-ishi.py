#20-dars. funksiyalar. uy ishi 

#Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi,
#email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida
#qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin.
#Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)

#def dastur_tuz(ism,familiya,t_yil,t_joy,el_pochta,tel_raqam=''):
 #   jami_lugat={
  #      'f_ismi':ism,
   #     'f_familiyasi':familiya,
    #    'f_tyili':t_yil,
     #   'f_yoshi':2023-int(t_yil),
      #  'f_tjoyi':t_joy,
       # 'f_elpochtasi':el_pochta,
        #'f_telraqami':tel_raqam }
    #return jami_lugat

#yangi_lugat=[]
#while True:
 #   print("Quyidagi ma'lumotlarni kiriting : ")
  #  ism=input("Foydalanuvchining ismi : ")
   # familiya=input("Foydalanuvchining familiyasi : ")
    #t_yil=input("Foydalanuvchining tug'ilgan yili : ")
    #t_joy=input("Foydalanuvchining tug'ilgan joyi : ")
    #el_pochta=input("Foydalanuvchining elektron pochtasi : ")
    #tel_raqam=input("Foydalanuvchining telefon raqami : ")
    
    #yangi_lugat.append(dastur_tuz(ism, familiya, t_yil, t_joy, el_pochta,tel_raqam))
    #savol=input("Yana ma'lumot qo'shasizmi ? (yes/no) : ")
    #if savol=='no':
   #     break
#print("Bizda quyidagicha lu'gat shakllandi : ")
#for w in yangi_lugat:
 #   print(f"Foydalanuvchi ismi - {w['f_ismi'].title()}. Familiyasi - {w['f_familiyasi'].title()}. {w['f_tyili']}-yilda tug'ilgan.\n"
  #        f"Hozir {w['f_yoshi']} yoshda. Telefon raqami : {w['f_telraqami']}")
        

#Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing

#def kattasini_top(s1,s2,s3):
 #   while True:
  #      max=s1
   #     if s2>max:
    #        max=s2
     #   elif s3>max:
      #      max=s3
       # return max
#a=kattasini_top(10,29,-36)
#print(f"Siz kiritgan sonlardan eng kattasi : {a} ") 
   

#Foydalanuvchidan aylaning radiusini qabul qilib olib,
#uning radiusini, diametrini, perimetri va yuzini 
#lug'at ko'rinishida qaytaruvchi funksiya yozing.
#yuz=pi*(r**2) / dimetr=r*2 / aylana_uzunligi=pi*diametr

#def aylana(radius):
 #   """Aylananing radiusini qabul qilib, uning yuzini, 
  #  diametrini va uzunligini chiqarib beruvchi funksiya"""
   # formula={
    #    'aylana_radiusi':radius,
     #   'aylana_diametri':float(radius)*2,
      #  'aylana_uzunligi':3.14*2*float(radius),
       # 'aylana_yuzi':3.14*(float(radius)**2)
       # }
    #return formula


#a=aylana(6)
#print(f"Doira radiusi- {a['aylana_radiusi']} ga teng.\nDoira diametri - {a['aylana_diametri']} ga teng.\n"
 #     f"Doira uzunligi - {a['aylana_uzunligi']} ga teng.\nDoira yuzi - {a['aylana_yuzi']} ga teng.")

#print(a)

#Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi
#funksiya yozing (tub sonlar —faqat birga va o'ziga 
#qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)

#def tub_son_qaytar(n1,n2):
 #   tub_sonlar=[]
  #  for n in range(n1,n2+1):
   #     tub=True
    #    if (n==1):
     #       tub=False
      #  elif (n==2):
       #     tub=True
        #else:
         #   for x in range(2,n):
          #      if n%x==0:
           #         tub=False
        #if tub:
         #   tub_sonlar.append(n)
    #return tub_sonlar            
           
           
#a=tub_son_qaytar(3, 56)
#print(a)

#Foydalanuvchidan son qabul qilib,Fibonachchi ketma-ketligidagi
#sonlar royxatni qaytaruvchi funksiya yozing. 

        
def fibonacci(n):
    sonlar = []
    for x in range(n):
        if x==0 or x==1:
            sonlar.append(1)        
        else:
            sonlar.append(sonlar[x-1]+sonlar[x-2])
    return sonlar

b=fibonacci(10)
print(b)

    















