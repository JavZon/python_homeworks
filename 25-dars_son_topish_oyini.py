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
       
            
def son_topadi_komputer(x=10):
    input(f"1 dan {x} gacha son o'ylang. Men topishga harakat qilaman :\n"
          f"Son o'ylagan bo'lsangiz istalgan tugmani bosing.")
    ishora=True
    while ishora:
        
        
    









