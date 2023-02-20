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
    








