#21-dars. funksiyalar davomi va uy ishi 


#def baho_qoy(talabalar_royxati):
#    baholar={}
#    while talabalar_royxati:
#        talaba_ismi=talabalar_royxati.pop()
#        talaba_bahosi=input(f"Talaba {talaba_ismi.title()} ning bahosini kiriting : ")
#        baholar[talaba_ismi]=int(talaba_bahosi)
#    return baholar
   
 
#students=['Tojush shariah', 'sodru shariah', 'viktor kumkiov', 'sardor cholqonoglu']
#a=baho_qoy(students)

#print(f"\n{a}")

#Matnlardan iborat ro'yxat qabul qilib, ro'yxatdagi har bir 
#matnning birinchi harfini katta harfga o'zgatiruvchi funksiya yozing.    



#def katta_harf(x):
#    royxat2=[]
#    while x:
#        a=x.pop()
#        royxat2.append(a.title())
#    return royxat2

#royxat=['olma', 'anor', 'sabzi', 'piyoz', 'qovun', 'tarvuz']

#b=katta_harf(royxat)    
#print(b)
#print(royxat)


#def katta_harf(x):
#    royxat2=[]
#    while x:
#        a=x.pop()
#        royxat2.append(a.title())
#    return royxat2

#royxat=['olma', 'anor', 'sabzi', 'piyoz', 'qovun', 'tarvuz']

#b=katta_harf(royxat[:])    
#print(b)
#print(royxat)


#def katta_harf(matnlar):
#    for i in range(len(matnlar)):
#        matnlar[i]=matnlar[i].title()   

#ismlar = ['ali', 'vali', 'hasan', 'husan']
#katta_harf(ismlar)
#print(ismlar)

#Darsimiz davomida yozgan bahola funksiyasini
#.pop() metodidan foydalanmasdan va asl ro'yxatga 
#o'zgartirish kiritmasdan faqat lug'at qaytaradigan qilib yozing.

#def bahola(ismlar):
#    baholar = {}
#    while ismlar:
#        ism = ismlar.pop()
#        baho = input(f"Talaba {ism.title()}ning bahosini kiriting: ")
#        baholar[ism]=baho
#    return baholar

#talabalar = ['ali', 'vali', 'hasan', 'husan']
#baholar = bahola(talabalar)
#print(baholar)


#o'zim yozgan usul
talabalar = ['ali', 'vali', 'hasan', 'husan']
# def bahola(x):
#     baholar={}
#     x=talabalar[:]
#     for a in range(len(x)):
#         ism=x[a]
#         baho=input(f"{x[a].title()}ning bahosi kiriting : ")
#         baholar[ism]=int(baho)
#     return baholar

# a=bahola(talabalar)
# print(a)  
# print(f"\n{talabalar}")          
        

#sariq dev yozgan usul        
def baho_la(z):
    marks={}
    for a in z:
        baho=input(f"Talaba {a.title()}ning bahosini kiriting : ")
        marks[a]=baho
    return marks

s=baho_la(talabalar)
print(s)
print(talabalar)
        






























