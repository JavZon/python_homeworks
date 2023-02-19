# 32-dars. Dunder metodlari

class Avto:
    """Avto klassi"""
    __num_avto=0
    def __init__(self, zavod, model, rang, narh, yil, km=0):
        self.producer= zavod
        self.model=model
        self.color=rang
        self.price=narh
        self.year=yil
        self.__km=km
        Avto.__num_avto+=1
        
    def __repr__(self):
        return f" Avto : {self.producer} {self.color} {self.model}"

    def get_price(self):
        return f"{self.producer} {self.model}- {self.price} $"
    
    def __eq__(self, y):
        return self.price==y.price

    def __lt__(self, y):
        return self.price<y.price 

    def __le__(self,y):
        return self.price<=y.price
    
        
        
avto1=Avto("Mitsubishi","Watashiwas","Black",35000,2023,1200)
avto2=Avto("KIA","Sportage","Silver",22000,2023,200)
avto3=Avto("Toyota","Corolla","Ruby Flare Pearl",25000,2023,300)

# avtolar=[avto1,avto2,avto3]
# print(avtolar)        
        
# for a in avtolar:
#      print(f"{a.get_price()}")
# print(dir(Avto))

# print([a for a in dir(Avto)])
# print(avto1.get_price())    

class AvtoSalon:
    """Avtosalon klassi"""
    def __init__(self, ism):
        self.name= ism
        self.avtolar=[]

    def __repr__(self):
        return f"{self.name} avtosaloni."
    
    def add_avto(self,*qiymat):
        for avto in qiymat:
            if isinstance(avto,Avto):
                self.avtolar.append(avto)
            else:
                print("Avto klassiga oid obyekt kiriting")
                
    def __len__(self):
        return len(self.avtolar)

    def __getitem__(self, index):
        return self.avtolar[index]

    def __setitem__(self,index,value):
        if isinstance(value, Avto):
            self.avtolar[index]=value 
            
    def __call__(self,*qiymat):
        if qiymat:
            for car in qiymat:
                print(f"{car.model} - {car.price}")
        else:
            return [car for car in self.avtolar]

    def __add__(self,y):
        if isinstance(y, AvtoSalon):
            yangi_salon=AvtoSalon(f"{self.name} {y.name}")
            yangi_salon.avtolar=self.avtolar+y.avtolar
            return yangi_salon
        elif isinstance(y, Avto):
            self.add_avto(y)
                
salon1=AvtoSalon("MaxAvto")
print(salon1)        

salon2=AvtoSalon("LIDER Avto Lising")


# print(isinstance("matn", str))        
avto5 = Avto("Volkswagen","Polo",'Qora',30000,2022,500)
avto6 = Avto("Honda","Accord","Oq",42000,2021,420)
avto4=Avto("Honda","HR-V", "Silver Magnetic",32000,2023,500)
# print(salon1.avtolar)
# print(len(salon1))
# print(salon1[0])


# salon1[0]=avto4

salon1.add_avto(avto1,avto2,avto3)
print(salon1.avtolar)
salon2.add_avto(avto4,avto5,avto6)
print(salon2.avtolar)
salon3=salon1+salon2
babushka=salon1+avto5








