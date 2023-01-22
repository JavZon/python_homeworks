#20-dars. qiymat qaytaruvchi funksiya

#def son(a,b):
  #  multiple= a*b
 #   return multiple

#w=son(22,30)
#print(w)

#def student_name(ism,familiya):
 #   toliq_ism=f"{ism.title()} {familiya.upper()}"
  #  return toliq_ism

#student1=student_name('bilol', 'al javziy')
#student2=student_name('victor', 'moses')

#print(f"{student1} is knowledgible than {student2}")


#def raqamlar_yig(x,y,z=''):
 #   if z:
  #      yigindi=x+y+z
   # else:
    #    yigindi=x+y
    #return yigindi    

#son1=raqamlar_yig(9,5,2)
#son2=raqamlar_yig(14,31)
#print(f" Son1 ning yigindisi- {son1}. Son2 ning yig'indisi - {son2}")


#def raqamlar_yig(x,y,z=10):
 #   if z:
  #     yigindi=x+y+z
   # else:
    #    yigindi=x+y+10
    #return yigindi    

#son1=raqamlar_yig(25,11,3)
#son2=raqamlar_yig(9,51)
#print(f" Son1 ning yigindisi- {son1}. Son2 ning yig'indisi - {son2}")


#def avto_salon(company,model,color,year,price=None):
 #   car={
  #      'kompaniya_nomi':company,
   #     'mash_modeli':model,
    #    'mash_rangi':color,
     #   'mash_yili':year,
      #  'mash_narhi':price
       # }

    #return car

#mashina1=avto_salon('Mitsubishi','Watashiwas','Red',2022)
#mashina2=avto_salon('Audi','Q7','black',2021,18000)
#cars=[mashina1,mashina2]
    
#for b in cars:
 #   if b['mash_narhi']:
  #      qiymat=b['mash_narhi']
   # else:
    #    qiymat="Hozircha noma'lum"
    #print(f"{b['mash_modeli']}, rangi- {b['mash_rangi']}. Narxi - {qiymat}")        
    

 
#def yangi_range(son1,son2):
    #sonlar=[]
    #while son1<son2:
   #     sonlar.append(son1)
  #      son1+=1
 #   return sonlar
    
#b=yangi_range(-4, 11) 
#print(b)
    

#def oraliq(s1,s2,s3=''):
 #   raqamlar=[]
  #  while s1<s2:
   #     raqamlar.append(s1)
    #    if s3:
     #       s1+=s3
      #  else:
       #     s1+=1
    #return raqamlar

#qw=oraliq(42,75,7)
#print(qw)
            
#def y_o(n1,n2,n3=None):
 #   num_bers=[]
  #  while n1<n2:
   #     if n3:
    #        num_bers.append(n1)
     #       n1+=n3
      #  else:
       #     num_bers.append(n1)
        #    n1+=1
    #return num_bers

#yyy=y_o(7,25)            
#print(yyy)


def avto_salon(company,model,color,year,price=None):
    car={
       'kompaniya_nomi':company,
       'mash_modeli':model,
       'mash_rangi':color,
       'mash_yili':year,
       'mash_narhi':price
        }

    return car

print("Saytimizdagi avtolar ro'yxatini shakllantiramiz.")

cars=[] # salondagi avtolar uchun bo'sh ro'yxat

while True:
    print("\nQuyidagi ma'lumotlarni kiriting",end='')
    company=input("Ishlab chiqaruvchi: ")
    model=input("Modeli: ")
    color=input("Rangi: ")
    year=input("Ishlab chiqarilgan yili: ")
    price=input("Narhi: ")
    
    cars.append(avto_salon(company,model,color,year,price))
    
    savol = input("Yana avto qo'shasizmi? (yes/no): ")
    if savol=='no':
        break  

          
print("Biz quyidagi avtomobillarni taqdim etamiz : ")    
for a in cars:
    print(f"{a['kompaniya_nomi']}. Modeli - {a['mash_modeli']}. Yili - {a['mash_yili']}. Narhi - {a['mash_narhi']}.")
    
 
    
 
    
    
    
    
    
    
    
    
    
    
    
    
    
    









