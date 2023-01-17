# 18-dars. while sikli va lug'at va ro'yxat
 
#names=[]

#print("We will print names of your friends'")
#n=1

#while True:
 #   savol=f"{n}- do'stingizning ismini kiriting : "
  #  ism=input(savol)
   # names.append(ism)
    #javob=input("Yana ism qo'shishni xohlaysizmi ? (ha/yo'q) >>> ")
    #if javob=='ha':
     #   n+=1
      #  continue
    #else:
     #   break

#print("\nSizning do'stlaringiz ro'yxati : ")
#for a in names:
 #   print(a.title()) 
 

#print("Do'stlaringiz yoshini hisoblaymiz.")
#dostlar={}
#ishora=True

#while ishora:
    #name=input("Do'stingizning ismini kiriting : ")
    #age=int(input(f"{name.title()}ning yoshini kiriting : "))
    #dostlar[name]=age
    #answer=input("Yana ma'lumot qo'shishni xohlaysizmi ? (ha/yo'q) >>> ")
    #if answer=='ha':
        #continue
    #else:
        #ishora=False

#print("\nDo'stlaringiz va ularning yoshi quyidagicha : ")
#for a,b in dostlar.items():
    #print(f"{a.title()} {b} yoshda. ")
     
    
    
#cars=['lacetti', 'nexia', 'audi', 'gm', 'nexia', 'bmw', 'nexia', 'bentley']
#while 'nexia' in cars:
 #       cars.remove('nexia')

#print("Yangilangan ro'yxatimiz quyidagicha : ")
#for b in cars:
 #   print(b.title())        




students=['ali', 'vali', 'hasan', 'husan']
marked_students={}

while students:
    name=students.pop()
    mark=input(f"{name.title()}ning bahosiini kiriting : ")
    print(f"{name.title()} baholandi.\n")
    marked_students[name]=mark

print(marked_students)
    
    
    
    
    
    
    
    
    
    
    
    






















   










