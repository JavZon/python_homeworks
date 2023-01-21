# 19-dars. funksiyalar

#def salom_ber():
 #   """Salom beruvchi funksiya"""
  #  print("Assalomu alaykum !!!")
    

#salom_ber()
    
#def salom_ber(ism):
  # """Foydalanuvchidan ismini so'rab, keyin shu
 #   ism bilan salom beruvchi funksiya"""
#   print(f"Assalomu alaykum, hurmatli {ism.title()}. \nAhvollaringiz yaxshimi ? ")
    

#salom_ber('hasan ash shaybaniy')
#salom_ber("miqdad ibn salaba")
#print(salom_ber.__doc__)

#def toliq_ism(ism,familiya):
 #   """Ism va familiyani chiqaruvchi dastur"""
  #  print(f"Foydalanuvchi ismi - {ism.title()}.\n"
   #       f"Foydalanuchi familiyasi - {familiya.title()}.")

#toliq_ism('hasan','aliyev')
#toliq_ism('husanov','botir')



#def yosh_hisobla(ism,tugilgan_yil):
  #  """Yosh hisoblaydigan dastur"""
  #  print(f"{ism.title()} {2020-tugilgan_yil} yoshda")
    

#yosh_hisobla('botir', 1999)
#yosh_hisobla(1997,'olim')

#yosh_hisobla(ism='tojush shariah', tugilgan_yil=1633)

#toliq_ism(familiya='ahmadov', ism='jovli')

def age_counter(t_yil, current_year=2022):
    """Foydalanuvchi yoshini hisoblaydi"""
    print(f"Siz {current_year-t_yil} yoshdasiz.")
    
#age_counter(1998,2022)    
#age_counter(1968)
#age_counter(1998,2008)


#def yosh_hisobla(tugilgan_yil, joriy_yil=2020):
    #"""Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
    #print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")
    
#tyil = int(input("Tug'ilgan yilingizni kiriting: "))
#yosh_hisobla(tyil)

#yosh_hisobla(20,2000)


#def yosh_hisobla(tugilgan_yil, joriy_yil):
  #  """Foydalanuvchi tug'ilgan yilidan uning yoshini hisoblaydi"""
 #   print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz")

#yosh_hisobla(1993,2021)


def salom_ber():
    """Salom beruvchi funksiya"""
    print("Assalomu alaykum!")

salom_ber()

def toliq_ism(ism, familiya):
    """Foydalanuvchi ism va familiyasini jamlab chiqaruvchi funksiya"""
    print(f"Foydalanuvchi ismi: {ism.title()}\n"
          f"Foydalanuvchi familiyasi: {familiya.title()}")
 
toliq_ism('olim','tojush shariah')















