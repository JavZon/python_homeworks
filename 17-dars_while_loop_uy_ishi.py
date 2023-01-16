# 17-dars_while_sikli_uy_ishi

#Foydalanuvchidan yaxshi ko'rgan kitoblarini kiritishni so'rang.
#Foydalanuvchi stop so'zini yozishi bilan dasturni to'xtating


#while True: orqali bajarish >>>
#savol=("Yaxshi ko'rgan kitoblaringizni kiriting ")
#savol+="(dasturni to'xtatish uchun 'stop' deb yozing) : "

#while True:
    #q=input(savol)
    #if q=='stop':
        #break
#print("Dastur tugadi ! ")





#qiymat='' orqali bajarish >>>
#savol=("Yaxshi ko'rgan kitoblaringizni kiriting ")
#savol+="(dasturni to'xtatish uchun 'stop' deb yozing) : "

#qiymat=''
#while qiymat!='stop':
    #qiymat=input(savol)
    #if qiymat=='stop':
        #print("Dastur tugadi !!! ")
        
        
#savol=("Yaxshi ko'rgan kitoblaringizni kiriting ")
#savol+="(dasturni to'xtatish uchun 'stop' deb yozing) : "
#i=True

#while i:
    #qiymat=input(savol)
    #if qiymat=='stop':
        #i=False
#print("Dastur tugadi !!!")        

#Muzeyga chipta narhi foydalanuvchining yoshiga bog'liq: 7 dan yoshlarga - 2000 so'm,
#7-18 gacha 3000 so'm, 18-65 gacha 10000 so'm, 65 dan kattalarga bepul. Shunday while tsikl
#yozingki, dastur foydalanuvchi yoshini so'rasin va chipta narhini chiqarsin.
#Foydalanuvchi exit yoki quit deb yozganda dastur to'xtasin (ikkita shartni ham tekshiring).
#Yuqoridagi dasturni turli usullarda yozib ko'ring (break, ishora, yoki shart tekshirish)




#savol="Yoshingizni nechada "
#savol+="(dasturni to'xtatish uchun 'exit' yoki 'stop' deb yozing ) : "

#while True:
 #   yosh=input(savol)
  #  if yosh=='exit' or yosh=='quit':
   #     print("Dastur tugadi !!! ")
    #    break
    #else:
     #   age=int(yosh)
        
    #if 0<age<=7:
     #   narx=2000
    #elif 7<age<=18:
     #   narx=3000 
    #elif 18<age<=65:
     #   narx=10000
    #else:
     #   narx=0
    
    #if narx==0:   
     #   print("Sizga kirish bepul.")
    #else: 
     #   print(f"Sizga kirish {narx} so'm ")
        

#savol="Yoshingizni nechada "
#savol+="(dasturni to'xtatish uchun 'exit' yoki 'stop' deb yozing ) : "
#c=True

#while c:
    #yosh=input(savol)
    #if yosh=='exit' or yosh=='quit':
      #  c=False
    #else:
     #   age=int(yosh)
    
    #if  0<age<=7:
     #   narx=2000
    #elif 7<age<=18:
     #   narx=3000
    #elif 18<age<=65:
     #   narx=10000
    #else: narx=0
    
    #if narx!=0:
     #   print(f"Sizga kirish {narx} so'm ")
    #else:
     #   print("Sizga kirish bepul")
        

    
#1-dan >>> if qiymat<0 emas if qiymat=='exit' yozish kerak.
#chunki input funksiyasi faqat matn qilib chiqaradi va qiymat<0 shartini tekshirolmaydi
#2-dan >>> 'exit' ni kichkina 'e' bilan yozish kerak
#3-dan >>> break shartini 1- bo'lib tekshirib olish kerak. chunki keyin qiymatni floatga o'tqizib 0 bolan manfiy
# yoki musbat ekanini tekshiramiz



savol ="Kiritilgan sonning ildizini qaytaruvchi dastur.\n"
savol += "Musbat son kiriting "
savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

while True:
    qiymat=input(savol)
    if qiymat=='exit':
        break
    son=float(qiymat)
    
    if son<0:
        continue
    else: 
        print(f"{son} ning ildizi {son**(1/2)} ga teng. ")
        
    
   
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
































