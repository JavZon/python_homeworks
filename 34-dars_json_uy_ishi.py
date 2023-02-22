# 34-dars_uy_ishi

import json

data={"Model" : "Malibu",
      "Rang" : "Qora",
      "Yil":2020,
      "Narh":40000 }


data_json=json.dumps(data)
# print(data_json)
# print(type(data_json))

 # va talabaning ismi va familiyasini konsolga chiqaring: 
talaba= {"ism":"Hasan",
         "familiya":"Husanov",
         "tyil":2000
         }

# print(f"Talabaning ismi - {talaba['ism']}."
#       f"\nTalabaning familiyasi - {talaba['familiya']}")


# Yuqoridagi ikki o'zgaruvchini alohida JSON fayllarga saqlang.
with open("data.json",'w') as file:
    json.dump(data,file)
    
with open('talaba.json','w') as f:
    json.dump(talaba,f)
    
# talaba1_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""

# talaba2=json.loads(talaba1_json)
# print((talaba2))

filename='applicant.json'
with open(filename) as f:
    applicant1=json.load(f)
# print(applicant1)
# print(type(applicant1)) 



# applicant={
#        'name':"Jovlibek Qo'yliyev",
#        'age':45,
#        'family_status':True,
#        'kids':("Anvar", "Gulnoza"),
#        'graduated_universities':["Financial","Diplomacy University"],
#        'cars':[
#            {'model':"BMW Black X7"},
#             {'model':"KIA Sportage Silver"}
#             ]
#        }

# for k,v in applicant['cars'][0].items():
#     print(f"{k}- {v}")

# Faylni Pythonda oching va konsolga maqolaning
# sarlavhasi (title) va qisqa matnini (extract) chiqaring:

with open('maqola.json') as file:
    maqola1=json.load(file)




sarlavha= maqola1['query']['pages']['13801']['title']
matn= maqola1['query']['pages']['13801']['extract']
print(f"Maqolaning sarlavhasi - {sarlavha}.\nMaqalaning matni- {matn}")

















   


