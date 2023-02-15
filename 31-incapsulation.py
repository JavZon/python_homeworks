# 31-dars. Incapsulation

from uuid import uuid4

# print(uuid4())

# class Avto:
#     def __init__(self, zavod, model, rang, narh, yil, km=0):
#         self.producer= zavod
#         self.model=model
#         self.color=rang
#         self.price=narh
#         self.year=yil
#         self.__km=km
#         self.__id=uuid4()
        
#     def get_km(self):
#         return self.__km
    
#     def get_id(self):
#         return self.__id
    
#     def add_km(self, a):
#         if a>=0:
#             self.__km+=a
#         else:
#             print("Mashinaning km ni o'zgartirib bo'lmaydi.")
    

# avto1=Avto("Mitsubishi","Watashiwas","Qora",25000, 2021, 2000)

# # print(avto1.color)    
# # print(avto1.price)
# print(avto1.get_id())
# print(avto1.get_km())

class Avto:
    num_avto=0
    def __init__(self, zavod, model, rang, narh, yil, km=0):
        self.producer= zavod
        self.model=model
        self.color=rang
        self.price=narh
        self.year=yil
        self.__km=km
        Avto.num_avto+=1
        
avto1=Avto("GM","Cobalt","Oq",25000,2021,500)
avto2=Avto("KIA","Carnival","Black",75000,2023,300)
avto3=Avto("Mitsubishi","Watashiwas","Silver",22000,2022,6200)

print(avto1.num_avto)
print(avto2.num_avto)
print(avto3.num_avto)
print(Avto.num_avto)        




















