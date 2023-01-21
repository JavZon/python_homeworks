""" 19-dars. funksiyalar uy ishi """

#Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.

#def yosh_hisobla(ism,yosh):
   # """Foydalanuvchidan ism va yosh qabul qilib,
    #uning tug'ilgan yilini hisoblovchi funksiya"""
    #print(f"Salom {ism.title()}. Siz {2022-yosh} -yilda tug'ilgansiz.")
    
#a=input("Salom. Ismingizni kiriting : ")
#b=int(input(f"Hurmatli {a.title()} endi yoshingizni kiriting : "))
#yosh_hisobla(a,b)    


#Foydalanuvchidan son olib, uning kvadrati
#va kubini konsolga chiqaruvchi funksiya yozing.

#def son_kv(son):
   # """Foydalanuvchidan son qabul qilib uning kvadrati
  #  va kubini hisoblovchi funksiya"""
 #   print(f"{son} ning kvadrati- {son**2} ga teng.\n{son} ning kubi- {son**3} ga teng")
    
#son_kirit=float(input("Istalgan son kiriting : "))
#son_kv(son_kirit)    


#Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.

#def juft_toq(son):
 #   """Foydalanuvchidan son olib, son juft yoki
  #  toqligini konsolga chiqaruvchi funksiya"""
   # if son%2==0:
    #    print("Siz kiritgan son juft sondir.")
    #else:
     #   print("Siz kiritgan son toq sondir.")
        
#son_yoz=float(input("Istalgan son kiriting : "))
#juft_toq(son_yoz)

#Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi
#funksiya yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.

#def katta_kichik(son1,son2):
    #"""Foydalanuvchidan ikkita son olib, ulardan kattasini 
    #konsolga chiqaruvchi funksiya"""
    #if son1>son2:
    #    print(f"{son1} > {son2}")
   # elif son2>son1:
   #     print(f"{son2} > {son1}")
  #  else:
 #       print("Sonlar teng.")
    
#katta_kichik(25,25)    





#def son_chiqar(x,y=2):
  #  """Foydalanuvchidan x va y sonlarini olib, x*y konsolga chiqaruvchi funksiya"""
 #   print(f"Natija = {x**(y)}")
    
#son_chiqar(2,5)
#son_chiqar(2)

#Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz
#bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.

def son_ol(s):
    if s%10==0:
        print(f"{s} 2 va 5 ga qoldiqsiz bo'linadi.")
    elif s%9==0:
        print(f"{s} 3 ga qoldiqssiz bo'linadi.")
    elif s%8==0:
        print(f"{s} 2 va 4 ga qoldiqsiz bo'linadi.")
    elif s%6==0:
        print(f"{s} 2 va 3 ga qoldiqsiz bo'linadi.")
    elif s%7==0:
        print(f"{s} 7 ga qoldiqsiz bo'linadi")        


son_ol(90)

def bolinish_alomatlari(son):
    for n in range(2,11):
        if son%n:
            print(f"{son} {n} ga qoldiqli bo'linadi")

bolinish_alomatlari(170)














