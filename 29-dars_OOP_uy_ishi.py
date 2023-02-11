# 29-dars_OOP_uy_ishi

class Avto:
    def __init__(self, model, rang, korobka, narh):
        self.model= model
        self.color= rang
        self.transmission= korobka
        self.price= narh
        self.distance= 0
        
    def car_model(self):
        return self.model

    def car_color(self):
        return self.color

    def car_transmission(self):
        return self.transmission

    def car_price(self):
        return self.price

    def car_distance(self):
        return self.distance
    
    def get_info(self):
        return f"Model- {self.model}. Color - {self.color}. Korobka - {self.transmission}. Price - {self.price}"

    def update_km(self, masofa):
        self.distance+=masofa


# car1=Avto("Genesis G90", "Blue", "Avtomat", 100000)        
# car1.update_km(22500)
# print(car1.car_distance())        
        



class Avtosalon:
    def __init__(self, nomi, manzili, sotuvdagi_avtomobillar, tolov_turi):
        self.name= nomi
        self.adress= manzili
        self.sale_cars= sotuvdagi_avtomobillar
        self.payment= tolov_turi
        self.avtolar_royxati=[]
        
    def get_name(self):
        return self.name

    def get_adress(self):
        return self.adress
    
    def get_sale_cars(self):
        return self.sale_cars

    def get_payment(self):
        return self.payment
    
    def get_salon_info(self):
        return f"Salon nomi- {self.name}. Manzili- {self.adress}. "
    
    def add_cars(self, x):
        self.avtolar_royxati.append(x)

    def see_cars(self):
        return [a.upper() for a in self.avtolar_royxati]        

avtosalon1= Avtosalon("Tinchlik","Beruniy ko'chasi 25", "Spark", "Istalgan to'lov turi orqali")       
        
# print(avtosalon1.get_salon_info())  
avtosalon1.add_cars("Cobalt")
avtosalon1.add_cars("Malibu")
avtosalon1.add_cars("Traverse")
avtosalon1.add_cars("Gentra")

# print(avtosalon1.see_cars())
# print(avtosalon1.name)  
# print(avtosalon1.get_sale_cars())
# print(avtosalon1.get_payment())


def see_methods(klass):
    return [a for a in dir(klass) if a.startswith('__') is False]


print(see_methods(Avtosalon))
# print(avtosalon1.__dict__)
print(avtosalon1.__dict__.keys())
print(avtosalon1.__dict__.values())



















