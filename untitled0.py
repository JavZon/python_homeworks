# 25-dars. son topish o'yini

from random import choice

def son_top(x):
    print("Keling o'ylagan son topish o'ynaymiz.")
    tahmin_soni=0
    son_kiritish=int(input(f"1 dan {x} gacha son o'yladim. Topa olasizmi ? : \n>> "))
    
    while True:
        b=choice(range(1,x+1))
        if b>son_kiritish:
            javob1=input("Xato, men o'ylagan son bundan kattaroq. Yana harakat qiling : \n>> ")
            tahmin_soni+=1
        elif b<son_kiritish:
            javob2=input("Xato, men o'ylagan son bundan kichikroq. Yana harakat qiling : \n>> ")
            tahmin_soni+=1
        else:
            print(f"Topdingiz ! Men {b} sonini o'ylagan edim. "
                  f"{tahmin_soni} ta tahmin bilan topdingiz. Tabriklayman !")
            break
    # return javob1 and javob2 


    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    








