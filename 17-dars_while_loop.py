# 17-dars. While loop

#ism=input("Ismingiz nima ? ")
#print(f"Salom, {ism.title()}")


#ism=input("Ismingiz nima ? ")
#savol=f"Salom, {ism.title()}. Yoshingiz nechada ? "
#yosh=int(input(savol))
#if yosh<18:
    #print(f"Kechirasiz, {ism.title()}. Sizning yoshingiz 18 dan kichik ekan. Sizga kirish mumkin emas.")
#else:
    #print(f"Saytimizga xush kelibsiz - {ism.title()}")
    

#name=input("What is your name ? ")
#age=int(input(f"Hello, {name.upper()}. How old are you ? "))
#if age<20:
    #print(f"Sorry, {name.upper()} you can not enter as you are under 20.")
#else:
    #print(f"Welcome to our website - {name.upper()}")    


#son=3
#while son<30:
    #print(son)
    #son+=5


#print("Kiritilgan sonning kubini hisoblovchi dastur.")
#savol="Istalgan sonni kiriting (dasturni tugatish uchun 'exit' deb yozing) : "
#k=''
#while k!='exit':
    #k=input(savol)
    #if k!='exit':
      #  print(float(k)**3)
#print("Dastur tugadi.") 
       

#print("Kiritilgan sonning kubini hisoblovchi dastur.")
#savol="Istalgan sonni kiriting (dasturni tugatish uchun 'exit' deb yozing) : "
#i=True
#while i:
    #qiymat=input(savol)
    #if qiymat!='exit':
       # print(float(qiymat)**3)
    #else:
        #i=False
        #print("Dastur tugadi.")
                
            
#while True:
    #number=float(input("Enter a negative number : "))
    #if number<0:
        #break 
    #print("You entered a positive number. Please enter a negative number ")
        

#while True:
   #number=float(input("Enter a negative number : "))
   
    #if number<0:
        #print("Thank YOU !!! ")
        #break
    #print("You entered a positive number. Please enter a negative number") 


#print("Kiritilgan sonning kvadratini qaytaruvchi dastur.")
#savol = "Istalgan son kiriting "
#savol += "(dasturni to'xtatish uchun 'exit' deb yozing): "

#while True: # abadiy tsikl davom etaveradi, hech achon to'xtamaydi. Qachonki to'xtash sharti topilmaguncha.
    #qiymat = input(savol)
    #if qiymat != 'exit':
        
        #print(float(qiymat)**2)
    #else:
        #break


f=['apple', 'grape', 'banana', 'apricot']
for a in f:
    if a=='banana':
        break
    print(a.upper())        











    
    
    
    
    