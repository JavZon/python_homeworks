# 30-dars. Vorislik va Polymorphism uy ishi 

class Shaxs:
    def __init__(self, ism, familiya, tyil):
        self.name= ism
        self.lastname= familiya
        # self.passport= passport
        self.born_year= tyil
        
    def get_info(self):
        info=f"{self.name} {self.lastname}. "
        info+=f"Born year - {self.born_year}"
        return info

    def get_age(self, current_year):
        return current_year-self.born_year 
    
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
    
#     def fanga_yozil(self,subject):
#         return [self.fanlar.append(subject)]
    
#     def display_subject(self):
#         fanlar=[a.get_sub().upper() for a in self.fanlar]
#         return fanlar
    
#     def remove_fan(self,fan):
#         if fan not in self.fanlar:
#             javob=print("Siz bu fanga yozilmagansiz")
#         else:
#             self.fanlar.remove(fan)
            
#         return javob         
        
        
# class Fan:
#     def __init__(self, fan):
#         self.sub= fan
        
#     def get_sub(self):
#         return self.sub
    
# fan1=Fan("Fizika")
# fan2=Fan("Algebra")
# fan3=Fan("English")
   

# talaba1=Talaba("Alijon", "Valiyev", "FA562123", 1995,"TLB25321")        
# print(talaba1.get_info())        

# talaba1.fanga_yozil(fan1)
# talaba1.fanga_yozil(fan2)
# talaba1.fanga_yozil(fan3)        

        
# print(talaba1.remove_fan("matem"))
# print(talaba1.display_subject())        
 
 
class Professor(Shaxs):
    """Professor haqida class"""
    def __init__(self, ism, familiya, tyil, otadigan_fani, yillik_tajribasi):
        super().__init__(ism, familiya, tyil)
        self.subject= otadigan_fani
        self.experience= yillik_tajribasi
        
    def get_info(self):
        malumot= f"Professor - {self.name} {self.lastname}. {self.born_year}- yilda tug'ilgan."
        malumot+=f"\nMa'lumoti oliy. O'tadigan fani- {self.subject}. {self.experience} yillik tajribaga ega."
        return malumot


pr1=Professor("Shodi","Burhonov", 1978, "Oliy Matematika", 12)

# print(pr1.experience)
# print(pr1.name)
# print(pr1.lastname)
# print(pr1.born_year)
# print(pr1.subject)
# print(pr1.get_age(2023))
# print(pr1.get_info())           

class Teacher(Professor):
    def __init__(self, ism, familiya, tyil, otadigan_fani, yillik_tajribasi, oquvchilar_bahosi):
        super().__init__(ism, familiya, tyil, otadigan_fani, yillik_tajribasi)
        self.quality= oquvchilar_bahosi
        
    def give_quality(self):
        return f"Talabalar uning dars o'tishiga bo'lgan munosabati - {self.quality}"
    
teacher1=Teacher("Ketmonboy","Jovdarip",1986,"Fizika",5,"qoniqarli")
print(teacher1.get_info())
print(teacher1.get_age(2023))
print(teacher1.give_quality())

        
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 
 




