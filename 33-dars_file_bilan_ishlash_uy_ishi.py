# 33-dars.files. uy ishi 

# filename='new_file2.txt'
# ism="Qo'ylibek"
# familiya="Jovdarov"
# tyil='2006'
# with open(filename,'w') as file:
#     file.write(ism+' ')
#     file.write(familiya+'\n')
#     file.write(tyil)


# filename='pi_5000.txt'

# with open(filename) as file:
#     pi=file.read()
    
# pi=pi.rstrip() # qator ohiridagi bo'shliqlarni olib tashlaymiz
# pi =pi.replace('\n','') # qator tashlash belgisini almashtiramiz
# pi =pi.replace(' ','')

# bdate = '16081995'
# if bdate in pi:
#     print("Sizning tug'ilgan sanangiz ushbu raqamlar ichida mavjud.")
# else:
#     print("Afsuski, bu sana ushbu raqamlar ichida mavjud emas")
    
# pi = float(pi) # matnni float (o'nlik) songa o'tkazamiz

# import pickle
# with open('pi_5000','wb') as file:
#     pickle.dump(pi,file)
    
  
while True:
    savol=input("What is your favorite color ? <<< To stop this execution please press 0 >>> ")
    if savol==str(0):
        break
    else:
        with open('new_file3.txt','a') as file:
            file.write(savol+'\n')
    










