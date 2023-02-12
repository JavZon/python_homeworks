# 30-dars.OOP Inheritance and Polymorphism

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

# person1=Person("Alijon", "Valiyev", "FC21184Z", 1995)
# print(person1.get_info())
# print(f"{person1.get_age(2023)} years old.")
        
class Talaba(Person):
    """Talaba haqida ma'lumot beruvchi klass"""
    def __init__(self, ism, familiya, passport, tyil, idraqam, adress):
        
        super().__init__(ism, familiya, passport, tyil)
        
        self.idnumber= idraqam
        self.bosqich= 1
        self.adress= adress
    def get_id(self):
        return self.idnumber

    def get_bosqich(self):
        return self.bosqich
    
    def get_info(self):
        info=f"{self.name} {self.lastname}. "
        info+=f"ID number - {self.get_id()}. {self.get_bosqich()} - bosqich talabasi"
        return info

        
# talaba1=Talaba("Jovlibek", "Qo'ychiyev", "FCZ54566285W",1905, "TMI5200")
# print(talaba1.born_year)
# print(talaba1.get_info())
# print(talaba1.idnumber)
# print(talaba1.get_bosqich())    
# print(talaba1.get_age(2023))
# print(talaba1.lastname)


class Adress:
    def __init__(self, viloyat, tuman, kocha, uy):
        self.province= viloyat
        self.city= tuman
        self.street= kocha
        self.home= uy

    def get_adress(self):
        manzil=f"{self.province} viloyati, {self.city} tumani, "
        manzil+=f"{self.street} ko'chasi, {self.home} - uy."
        return manzil
        
talaba_adress=Adress("Samarqand", "Badaxshon", "Farobiy", "289-5")
talaba1=Talaba("Jovlibek","Qo'ychiyev","FCZ984541W",1995,"NA562478",talaba_adress)        

print(talaba1.get_info())
print(talaba1.adress.get_adress()) 
       
        
        
        
        
        
        































