mahsulotlar=["kitob", "daftar", "ruchka", "qalam", "o'chirg'ich", "telefon", "noutbuk", "non", "suv", "sochiq"]
savat=[]
for a in range(5):
    savat.append(input(f"Savatga {a+1} - mahsulotni qo'shing : "))
bor_mahsulot=[]
yoq_mahsulot=[]
for b in savat:
    if b in mahsulotlar:
        bor_mahsulot.append(b)
    else:
        yoq_mahsulot.append(b)
if yoq_mahsulot:
    print("Quyidagi mahsulotlar bizda yo'q : \n")
    for c in yoq_mahsulot:
        print(c)
else:
    print("Siz aytgan barcha mahsulotlar bizda bor ")

        