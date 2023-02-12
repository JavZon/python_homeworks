# 30-dars. Vorislik va Polymorphism uy ishi 

class Person:
    def __init__(self, ism, familiya, passport, tyil):
        self.name= ism
        self.lastname= familiya
        self.passport= passport
        self.born_year= tyil
        
    def get_info(self):
        info=f"{self.name} {self.lastname}. "
        info+=f"Passport number : {self.passport}. Born year - {self.born_year}"
        return info

    def get_age(self, current_year):
        return current_year-self.born_year 
    
class Talaba(Person):
    """Talaba haqida ma'lumot beruvchi klass"""
    def __init__(self, ism, familiya, passport, tyil, idraqam):
        
        super().__init__(ism, familiya, passport, tyil)
        
        self.idnumber= idraqam
        self.bosqich= 1
        self.fanlar=[]
        
    def get_id(self):
        return self.idnumber

    def get_bosqich(self):
        return self.bosqich
    
    def get_info(self):
        info=f"{self.name} {self.lastname}. "
        info+=f"ID number - {self.get_id()}. {self.get_bosqich()} - bosqich talabasi"
        return info
    
    def fanga_yozil(self,subject):
        return [self.fanlar.append(subject)]
    
    def display_subject(self):
        fanlar=[a.get_sub().upper() for a in self.fanlar]
        return fanlar
    
    def remove_fan(self,fan):
        if fan not in self.fanlar:
            javob=print("Siz bu fanga yozilmagansiz")
        else:
            self.fanlar.remove(fan)
            
        return javob         
        
        
class Fan:
    def __init__(self, fan):
        self.sub= fan
        
    def get_sub(self):
        return self.sub
    
fan1=Fan("Fizika")
fan2=Fan("Algebra")
fan3=Fan("English")
   

talaba1=Talaba("Alijon", "Valiyev", "FA562123", 1995,"TLB25321")        
print(talaba1.get_info())        

talaba1.fanga_yozil(fan1)
talaba1.fanga_yozil(fan2)
talaba1.fanga_yozil(fan3)        

        
print(talaba1.remove_fan("Matematika"))
print(talaba1.display_subject())        
 
 




