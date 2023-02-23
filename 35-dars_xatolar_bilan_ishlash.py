# 35-dars.Working on errors.

try:
    son1=input("Istalgan son butun son kiriting : ")
    kvadrat=int(son1)**2
    
except:    
    while True:
        javob=input("Siz butun son kiritmadingiz. Iltimos faqat butun son kiriting >>> \n")
        if javob.isdigit():
            javob=int(javob)
            print(f"Siz kiritgan sonning kvadrati - {javob**2}")
            break                           
else:
    print(f"Siz kiritgan sonning kvadrati - {kvadrat}")

# yosh=input("Yoshingizni kiriting : ")
# try:
#     yosh=int(yosh)
# except ValueError:
#     print("Siz butun son kiritmadingiz.")
# else:
#     print(f"Siz {2023-yosh} - yilda tug'ilgansiz. ")    

# mevalar=['olma','anor','anjir','uzum']
# try:
#     print(mevalar[8])
# except IndexError:
#     print(f"Ro'yxatda {len(mevalar)} ta meva bor xolos")    


# user={'ism':'Alijon',
#       'familiya':'Baltabaev',
#       'tyil':1997,
#       'statusi':'uylangan',
#       'bolalari':[{
#           '1-bola':'Bekturdi',
#           'tyil':2009},
#           {'2-bola':'Galipsatbek',
#            'tyil':2011
#               }]
#       } 
# try:
#     print(f"Foydalanuvchi ismi - {user['name']}")
# except KeyError:
#     print("Bunday kalit yo'q")
    
    
    
    
    
    
    
