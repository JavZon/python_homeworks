#22-dars. *args va **kwargs


# def yigindi(*sonlar):
#     a=sum(sonlar)
#     return a

# b=yigindi(1,56,89,32,-25,0,41)
# print(b)


# def baba(x,*y):
#     print(x)
#     print(type(y))
    
# baba(2,3)    
    
# def sonlar(*a):
#     for c in a:
#         kvadrat=c**2
#     return kvadrat

# d=sonlar(9)
# print(d)

# def sonlar(*a):
#     y=sum(a)
#     return y
# w=sonlar(2,3,5)
# print(w)

# def fruits(**meva):
#     print(meva)
#     print(type(meva))
    
# fruits(banana=8,apple=5,avocado=3)

# def avto_salon(company,model,color,**x):
#     x['kompaniya']=company
#     x['modeli']=model
#     x['rangi']=color
#     return x


# a=avto_salon('GM','Malibu', 'Qizil', yili=2019, km=0, korobka='avtomat')
# print(a)

# def avto_sal(company,model,price,**information):
    
#     information['kompaniya_nomi']=company
#     information['mash_modeli']=model
#     information['mash_narhi']=price
    
#     return information

# b=avto_sal('Mitsubishi','Watashiwas',25000, karobkasi='avtomat', rangi='Qora')
# c=avto_sal('GM','Cobalt', 15000, km=0, karobka='mexanika', yili=2018, rangi='qizil')

# print(b)
# print(c)


# Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing

# def kopaytir(*sonlar):
#     kopaytma=1
#     for a in sonlar:
#         kopaytma=kopaytma*a
#     return kopaytma

# b=kopaytir(3, 5, 8,10,-2)
# print(b)

# Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi
# funkisya yozing. Talabaning ismi va familiyasi majburiy argument,
# qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.

def talaba_tuz(ism,familiya,**talaba_info):
    """Talaba ismi, familyasi va boshqa
    ma'lumotlarni uzatuvchi funksiya"""
    talaba_info['talaba_ismi']=ism
    talaba_info['talaba_familiyasi']=familiya
    
    return talaba_info

r=talaba_tuz('jovli', "qo'yliyev", yoshi=25, viloyati='samarqand', oqish_joyi='tatu', kursi='2-kurs')
print(r)

def talaba_info(ism, familiya, **kwargs):
    kwargs['ism']=ism
    kwargs['familiya']=familiya
    return kwargs

talaba = talaba_info('olim','olimov',tyil=1995,fakultet='IT',yonalish='AT')
print(talaba)






















