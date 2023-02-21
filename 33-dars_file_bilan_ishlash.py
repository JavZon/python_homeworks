# 33-lesson. working on files

# file=open('lolo.txt')
# PI=file.read()
# print(PI)
# file.close()

# with open('lolo.txt') as bizning_fayl:
#     pi=bizning_fayl.read()
#     pi=pi.rstrip()
#     pi = pi.replace('\n','')
#     pi = float(pi)
    

    
# print(pi)

# filename='C:/Users/kodir/GitHub_repository/lolo.txt'
# with open(filename) as file:
#     pi=file.read()
    
# pi=pi.rstrip()
# pi=pi.replace('\n','')
# pi=float(pi)
# print(pi)

# filename='talabalar.txt'
# with open(filename) as file:
#     for a in file:
#         print(a.upper())
        
# with open(filename) as file:
#     talabalar=file.readlines()

# talabalar=[a.rstrip() for a in talabalar]
# print(talabalar)
        
filename='new_file.txt'
name="Boychibor Sarageldiyev"
born_year=1974

with open(filename,'w') as file:
    file.write(name+'\n')
    file.write(str(born_year)+'\n')

with open(filename,'a') as file:
    file.write("Qayumbergen G'azibgasayev\n")
    file.write('2001')

import pickle

talaba1={'ism':"Qo'ylivoy", 'familiya':"Jovliyev", 'tyil':2001,'kurs':2}
talaba2={'ism':"Boychibor", 'familiya':"Sarageldiyev",'tyil':2003,'kurs':1}
talaba3={'ism':"Qayumbergen",'familiya':"G'azibgasayev",'tyil':1997,'kurs':4}

with open('info_talaba','wb') as file:
    pickle.dump(talaba1,file)
    pickle.dump(talaba2,file)
    pickle.dump(talaba3,file)

with open('info_talaba','rb') as file:
    talaba1=pickle.load(file)
    talaba2=pickle.load(file)
    talaba3=pickle.load(file)

print(talaba1)
print(talaba2)
print(talaba3)







    








