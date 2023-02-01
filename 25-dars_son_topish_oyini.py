# 25-dars. son topish o'yini'
from random import choice

def son_top(x=10):
    tasodifiy_son=choice(range(1,x+1))
    print(f"Men 1 dan {x} gacha son o'yladim. Topa olasizmi ?\nO'ylagan tahminiy soningizni kiriting : ")
    tahminlar_soni=0
    while True:
        tahminlar_soni+=1
        tahmin=int(input(">>> "))
        if tahmin<tasodifiy_son:
            print("Xato, men o'ylagan son bundan kattaroq. Yana harakat qiling :")
        elif tahmin>tasodifiy_son:
            print("Xato, men o'ylagan son bundan kichikroq. Yana harakat qiling :")
        else:
            print(f"Tabriklaymiz. Siz {tahminlar_soni} ta tahmin bilan topdingiz !")
            break
    return tahminlar_soni
       
import random
def son_topadi_pc(x=10):
    input(f"1 dan {x} gacha son o'ylang. Men uni topishga harakat qilaman."
          f"Agar tayyor bo'lsangiz istalagan tugmani bosing: ")
    quyi=1
    yuqori=x
    tahminlar_soni_pc=0
    while True:
        tahminlar_soni_pc+=1
        if quyi!=yuqori:
            tahmin=random.randint(quyi, yuqori)
        else:
            tahmin=quyi
        javob=input(f"Siz {tahmin} sonini o'yladingiz. Agar to'g'ri bo'lsa (t) ni bosing, "
                    f"Agar siz o'ylagan son kattaroq bo'lsa (+), "
                    "siz o'ylagan son kichikroq bo'lsa (-) bosing : ")
        if javob=="-":
            yuqori=tahmin-1
        elif javob=="+":
            quyi=tahmin+1
        else:
            break
    print(f"Men topdim. Men {tahminlar_soni_pc} ta urinishda topdim !!! ")
    return tahminlar_soni_pc        
            
            
def play(x):
    
    ishora=True
    
    while ishora:
        taxmin_user=son_top(x)
        taxmin_pc=son_topadi_pc(x)
        
        if taxmin_pc>taxmin_user:
            print(f"Siz {taxmin_user} ta urinishda topib yutdingiz.Tabriklaymiz !!! ")
        elif taxmin_pc<taxmin_user:
            print(f"Men {taxmin_pc} ta urinishda topdim va yutdim.")
        else:
            print("Durrang")
        ishora=int(input("Yana o'ynaysizmi ? ha(1)/yo'q(0) : "))
        
        
        
        
play(25)        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        








