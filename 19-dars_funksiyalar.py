# 19-dars. funksiyalar

#def salom_ber():
 #   """Salom beruvchi funksiya"""
  #  print("Assalomu alaykum !!!")
    

#salom_ber()
    
#def salom_ber(ism):
   #"""Foydalanuvchidan ismini so'rab, keyin shu
    #ism bilan salom beruvchi funksiya"""
    #print(f"Assalomu alaykum, hurmatli {ism.title()}. \nAhvollaringiz yaxshimi ? ")
    

#salom_ber('hasan ash shaybaniy')
#salom_ber("miqdad ibn salaba")
#print(salom_ber.__doc__)

def toliq_ism(ism,familiya):
    """Ism va familiyani chiqaruvchi dastur"""
    print(f"Foydalanuvchi ismi - {ism.title()}.\n"
          f"Foydalanuchi familiyasi - {familiya.title()}.")

#toliq_ism('hasan','aliyev')
#toliq_ism('husanov','botir')



def yosh_hisobla(ism,tugilgan_yil):
    """Yosh hisoblaydigan dastur"""
    print(f"{ism.title()} {2020-tugilgan_yil} yoshda")
    

#yosh_hisobla('botir', 1999)
#yosh_hisobla(1997,'olim')

#yosh_hisobla(ism='tojush shariah', tugilgan_yil=1754)

#toliq_ism(familiya='ahmadov', ism='jovli')














