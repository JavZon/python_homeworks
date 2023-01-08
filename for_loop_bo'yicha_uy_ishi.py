
#uy ishi for loop mavzusida
cars=['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for a in cars:
    if a=='gm':
        print(a.upper())
    else:
        print(a.title())
        
    
cars=['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for a in cars:
    if a!='gm':
        print(a.title())
    else:
        print(a.upper())
        

cars=['toyota', 'mazda', 'hyundai', 'gm', 'kia']
for a in cars:
    if a!='gm':
        print(a.upper())
    else:
        print(a.title())



login=input("Iltimos loginingizni kiriting : ")
if login.lower()=='admin':
    print("Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi ?")
else:
    print(f" Xush kelibsiz, {login} ! " )
    

print("Hello world !")










