# 32-dars_uy_ishi_dunder_methods

class Shaxs:
    """Shaxs haqida klass"""
    
    def __init__(self, ism, familiya, yoshi,passport):
        self.name= ism
        self.lastname= familiya
        self.passport= passport
        self.age= yoshi
        self.shaxslar=[]
        
    def get_info(self):
        info=f"{self.name} {self.lastname}. "
        info+=f"Born year - {self.born_year}"
        return info

    def get_bor_year(self, current_year):
        return current_year-self.age
    
    def get_passport(self):
        return self.passport
    
    def __repr__(self):
        return f"{self.name} {self.lastname}"
    
    def __call__(self):
        return self.passport
    
    def __len__(self):
        return len(self.name)
    
    def __lt__(self,y):
        return self.age<y.age
    
    def __eq__(self,y):
        return self.age==y.age
    
    def add_shaxs(self,*qiymat):
        for a in qiymat:
            if isinstance(a,Shaxs):
                self.shaxslar.append(a)
    
    def __getitem__(self,index):
        return self.shaxslar[index]

    def display(self):
        for a in self.shaxslar:
            print(f"{self.name} {self.lastname}.\nPassport raqami - {self.passport}")                

    
shaxs1=Shaxs("Qo'ylivoy","Jovliyev",59,"FAZ94454CW")
shaxs2=Shaxs("Boychibor","Sarageldiyev",65,"FW13243YR")
shaxs3=Shaxs("Qayumbergen","G'azibgasayev",23,"PLL564654ZN")
shaxs1.add_shaxs(shaxs2,shaxs3)


   











