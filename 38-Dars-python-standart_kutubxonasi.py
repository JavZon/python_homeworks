import datetime as dt

# hozir=dt.datetime.now()
# print(hozir)
# print(hozir.date())
# print(hozir.hour)
# print(hozir.second)

# bugun=dt.date.today()
# print(bugun)
# ertaga=dt.date(2023,3,27)
# print(f"Ertangi sana : {ertaga}")

# hozir=dt.datetime.now()
# hozirgiVaqt=hozir.time()
# print(f"Hozirgi soat : {hozirgiVaqt}")
# kelasi_vaqt=dt.time(23,45,28)
# print(kelasi_vaqt)


# bugun=dt.date.today()
# kelasi_oy=dt.date(2023,4,15)
# farq=kelasi_oy-bugun
# print(farq)

# hozir=dt.datetime.now()
# futbol=dt.datetime(2023,4,6,4,00,00)
# farq=futbol-hozir
# kun=farq.days
# sekund=farq.seconds
# minut=int(sekund/60)
# soat=int(minut/60)
# print(f"Futbol boshlanishiga {kun} kun, {soat} soat, {minut} minut, {sekund} sekund qoldi")


# vaqtni millisekundsiz chiqaramiz
# vaqt = hozir.strftime("%H:%M:%S")
# print(f"Hozir soat: {vaqt}")

# sanani kun-oy-yil koʻrinishida chiqaramiz
# sana = hozir.strftime("%d__%m__%Y")
# print(f"Bugun sana: {sana}")

# sanani kun/oy/yil koʻrinishida chiqaramiz
# sana_vaqt = hozir.strftime("%d__%m__%Y, %H:%M")
# print(sana_vaqt)
# import math
# PI=math.pi
# print(f"PI ning qiymati - {PI}")
# E=math.e
# print(f"E ning qiymati - {E}")
# x=4.6
# print(math.ceil(x))
# print(math.floor(x))
# y=81
# print(math.sqrt(y))
# print(math.pow(2, 15))
# from pprint import pprint
# import json
# filename='applicant.json'
# with open(filename) as f:
#     applicant=json.load(f)
# # print(applicant)
# pprint(applicant)
import re

# pattern="^t...r$"
# word1='temir'
# word2='tomir'
# word3='tulpor'
# print(re.match(pattern,word1))
# print(re.match(pattern,word2))
# print(re.match(pattern,word3))
# from engwords import dictionary
# andoza="^m...e$"
# englishwords=['apple','computer','pen','change','chance', 'bread', 'colorful']
# mos_sozlar=[]
# for x in dictionary['commonWords']:
#     if re.match(andoza, x):
#         mos_sozlar.append(x)
# print(mos_sozlar)

# pattern='[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
# matn = """Maqolalar  2020-yilning 20-martiga qadar rtmkonferensiya2021@mail.ru elektron pochtasida qabul qilinadi.
# Quyidagi yo'nalishdagi maqolalar qabul qilinadi:
# 👉 Aniq va tabiiy fanlarni zamonaviy pedagogik texnologiyalar asosida o‘qitish  metodikasi.
# 👉 Umumta’lim  fanlarini o‘qitishda  STEAM yondashuvning o’rni va ahamiyati. """
# email=re.findall(pattern,matn)
# print(email)
# password='^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'
# msg="Iltimos eng kamida 8 xonalik parol kiriting. "
# msg+="(kamida 8 belgidan iborat, kamida 1 ta lotin bosh harf, 1 ta kichik harf, "
# msg += "1 ta son va 1 ta maxsus belgi boʻlishi kerak): " 
# while True:
#     parol=input(msg)
#     if re.match(password,parol):
#         break
#     print("Maxfiy so'z talabga javob bermadi.")
    










