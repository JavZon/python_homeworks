

def avto_salon(company,model,color,year,price=None):
    car={
       'kompaniya_nomi':company,
       'mash_modeli':model,
       'mash_rangi':color,
       'mash_yili':year,
       'mash_narhi':price
        }

    return car



def avto_kirit():
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

def avto_print(avto_salon):          
    print("Biz quyidagi avtomobillarni taqdim etamiz : \n")    
    print(f"{avto_salon['kompaniya_nomi'].title()}. Modeli - {avto_salon['mash_modeli'].title()}."
          f"\nYili - {avto_salon['mash_yili']}. Rangi- {avto_salon['mash_rangi'].title()}. Narhi - {avto_salon['mash_narhi']}.")
 
    
def qoshish(x,y,*z):
    return x+y+sum(z)

def kopaytir(x,y,*z):
    a=x*y
    for b in z:
        a*=b
    return a

ddd=[2,5,]






