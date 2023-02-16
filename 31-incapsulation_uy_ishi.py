# 31-incapsulation uy ishi 

class Shaxs:
    __odamlar_soni=0
    
    def __init__(self, ism, familiya, tyil,passport):
        self.name= ism
        self.lastname= familiya
        self.passport= passport
        self.born_year= tyil
        Shaxs.__odamlar_soni+=1
        
    def get_info(self):
        info=f"{self.name} {self.lastname}. "
        info+=f"Born year - {self.born_year}"
        return info

    def get_age(self, current_year):
        return current_year-self.born_year
    
    def get_passport(self):
        return self.passport
    
    @classmethod
    def get_num_odam(cls):
        return cls.__odamlar_soni
    
    
# class Talaba(Shaxs):
#     """Talaba haqida ma'lumot beruvchi klass"""
#     def __init__(self, ism, familiya, passport, tyil, idraqam):
        
#         super().__init__(ism, familiya, passport, tyil)
        
#         self.idnumber= idraqam
#         self.bosqich= 1
#         self.fanlar=[]
        
#     def get_id(self):
#         return self.idnumber

#     def get_bosqich(self):
#         return self.bosqich
    
#     def get_info(self):
#         info=f"{self.name} {self.lastname}. "
#         info+=f"ID number - {self.get_id()}. {self.get_bosqich()} - bosqich talabasi"
#         return info    

shaxs1=Shaxs("Boqivoy","Malbashev",1996,"FCZ48762QA")
shaxs2=Shaxs("Qo'chqor","Qo'yjonov",1995,"FTH85256318")
shaxs3=Shaxs("Hurliqo","Bozorboyeva",2000,"KMN498456")
odam=[shaxs1,shaxs2,shaxs3]
for a in odam:
     print(a.get_passport())
# print(shaxs1.get_info())
# print(Shaxs.odamlar_soni)
# print(Shaxs.get_num_odam())
# print(shaxs1.get_num_odam())
for a in odam:
    print(a.get_info())
    
for a in odam:
      print(f"{a.name} {a.lastname} ning passport raqami - {a.passport}")
    
    
    
    
    
    
    
    
    
    
    

