# 24-dars. Funksiyalar.so'ngi so'z


# a=lambda x,y:x+y
# print(a(2,5))

# from math import pi

# b=lambda pi,r:2*pi*r
# print(b(pi,10))

# c=lambda x,y:x**y
# print(c(2,5))

# def daraja(n):
#     return lambda a:a**n

# print(daraja(3))

# from math import sqrt
# sonlar=list(range(11))

# ildiz=list(map(sqrt,sonlar))
# print(ildiz)

# def daraja_kv(x):
#     return x*x
# sonlar=list(range(11))
# # print(list(map(daraja_kv,sonlar)))

# kv=list(map(lambda a:a*a, sonlar))
# print(kv)

# a=[2,5,8]
# b=[4,6,7]

# print(list(map(lambda x,y:x+y,a,b)))

# ism=['hasan','husan','olim']
# print(tuple(map(lambda a:a.upper(),ism)))

# ismlar=[]
# for a in ism:
#     ismlar.append(a.upper())
# print(ismlar)    
    
# ismlar=['ali', 'vali','calvin']
# a=list(map(lambda x:x.upper(), ismlar))
# print(a)

import random as r

# a=r.sample(range(50),6)
# print(a)


# sonlar=list(r.sample(range(101), 10))
# def juftmi(x):
#     return x%2==0

# juft_sonlar=list(filter(juftmi, sonlar))
# print(sonlar)
# print(juft_sonlar)


# sonlar=list(r.sample(range(101), 10))

# def juftmi(*x):
#     for a in x:
#         if a%2==0:
#             kvadrat=a**2
#     return kvadrat  

# juft_sonlar=list(filter(juftmi, sonlar))
# print(sonlar)
# print(juft_sonlar)     


# ismlar=('hasan','husan', 'nodir', 'ahad', 'tojush shariah', 'sadir','komil')
# yangi_ism=list(filter(lambda a:a.startswith('h'),ismlar))
# print(yangi_ism)


# ismlar=('hasan','husan', 'nodir', 'ahad', 'tojush shariah', 'sadir','komil')
# ismlar2=list(filter(lambda x:len(x)<=5,ismlar))
# print(ismlar2)

ismlar=('hasan','husan', 'nodir', 'ahad', 'tojush shariah', 'sadir','komil')
ismlar2=list(filter(lambda x:(x.startswith('n') and x.endswith('r')), ismlar))
print(ismlar2)










