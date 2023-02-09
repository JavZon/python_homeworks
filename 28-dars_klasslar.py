# -*- coding: utf-8 -*-
"""
Created on Thu Feb  9 13:30:21 2023

@author: kodir
"""

# x=10
# print(type(x))
# matn='salom'
# print(type(matn))

# def turini_bil(x):
#     print(type(x))

# turini_bil('Assalomu alaykum')  
# turini_bil(261)  
    
# x=10
# print(x**2)
# matn='salom'
# print(matn**2)

# class Student:
#     def __init__(self,ism,familiya,tyil):
#         self.name= ism
#         self.surname= familiya 
#         self.year= tyil
    
#     def tanishtir(self):
#         print(f"Ismim {self.name} {self.surname}. {self.year} da tug'ilganman.")        
    
# talaba1=Student('Ali', 'Tojush Shariah', 1523)
# talaba2=Student('Miqdad', 'Ibn Salaba', 1258)
# talaba1.tanishtir()
# talaba2.tanishtir()


class Student:
    
    def __init__(self,ism,familiya,tyil):
        self.name= ism
        self.surname= familiya 
        self.year= tyil
    
    def get_name(self):
        return self.name
    
    def born_year(self):
        return self.year
    
    def get_age(self, current_year):
        return current_year- self.year
    
    def introduce(self):
        return f"Ismim {self.name} {self.surname}. {self.year} da tug'ilganman." 
    
student1=Student("Tojuddin", "Sodrush Shariah", 1721)    

print(student1.introduce())
print(student1.get_name())
print(student1.get_age())







