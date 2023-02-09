
class Foydalanuvchi:
    
    
    def __init__(self,ism,familiya,username,pochta,tel_raqam):
        
        self.name= ism
        self.surname= familiya
        self.login= username
        self.mail= pochta
        self.phone_num= tel_raqam
        
    def fullname(self):
        return f"{self.name} {self.surname}"
    
    def year(current_year):
        pass
        
    
    def get_info(self):
        
        return f"Foydalanuvchi - {self.login}. Ismi - {self.name} {self.surname}.\nElektron pochtasi - {self.mail}. Tel raqami- {self.phone_num}" 
        
user1=Foydalanuvchi("Ali","Valiyev", "alval_000", "alivali20@mail.ru", 998945210014)    
        
print(user1.get_info())    
print(user1.fullname())    
        
  
        