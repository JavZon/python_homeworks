# 36-dars_uy_ishi

def kattasini_top(x,y,z):
    if x>y and x>z:
        return x
    elif y>x and y>z:
        return y
    else:
        return z
    
# print(kattasini_top(-25, 0, -64))

def katta_harf_qil(matn):
    for a in range(len(matn)):
        matn[a]=matn[a].title()
        print(matn[a].title())
w=['olma','anor','uzum','tarvuz']
katta_harf_qil(w)

def juft_son_top(*royxat):
    for son in royxat:
        if son%2==0:
            return son
        

a=juft_son_top(52,35,14,25,19)
print(a)     





