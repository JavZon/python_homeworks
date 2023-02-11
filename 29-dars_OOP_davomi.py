# 29-dars.

class Student:
    """ This class is called - Student. There are stored all informations about Students of the school"""
    
    def __init__(self, ism, familiya, tyil):
        self.name= ism
        self.surname= familiya
        self.born_year= tyil
        self.kurs= 3
        
    def get_info(self):
        return f"{self.name} {self.surname}. Currently studying course - {self.kurs}"
    
    def get_full_name(self):
        return f"{self.name} {self.surname}"
        
    def set_bosqich(self, yangi_bosqich):
        self.kurs=yangi_bosqich
        
    def update_bosqich(self):
        self.kurs+=1
            
       
student1=Student("Alijon", "Valiyev", 1995)
student2=Student("Hasan", "Husanov", 2000)
student3=Student("Akrom", "Bo'riyev", 2004)
# # student1.set_bosqich(3)
# # print(student1.get_info())
# student1.update_bosqich()
# print(student1.get_info())


class Fan:
    def __init__(self, fan_nomi):
        self.subject= fan_nomi
        self.talabalar_soni=0
        self.talabalar=[]

    def add_student(self, x):
        self.talabalar.append(x)
        self.talabalar_soni+=1        
        
    def get_students(self):
        return [a.get_info() for a in self.talabalar]
    



matematika=Fan("Oliy Matematika")
student1=Student("Alijon", "Valiyev", 1995)
student2=Student("Hasan", "Husanov", 2000)
student3=Student("Akrom", "Bo'riyev", 2004)

matematika.add_student(student1)        
matematika.add_student(student2)        
matematika.add_student(student3)       
        
print(matematika.talabalar_soni)        
print(matematika.get_students())        
# print(dir(student1))        
        
def see_methods(klass):
    return [x for x in dir(klass) if x.startswith('__') is False]

print(see_methods(Student))        
print(student3.__dict__)
print(student3.__dict__.keys())        
print(student3.__dict__.values())        
        
        
        
        
        
        
        
        
        
        
        
        
        
        








