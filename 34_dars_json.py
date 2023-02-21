
import json

# x=5
# x_json=json.dumps(x)
# print(type(x_json))
# print(x_json)

# ism='anvar'
# ism_json=json.dumps(ism)
# print(type(ism_json))
# print(ism_json)
# num=(1,2,3,4)
# num_json=json.dumps(num)
# print(type(num_json))
# print(num_json)

applicant={
       'name':"Jovlibek Qo'yliyev",
       'age':45,
       'family_status':True,
       'kids':("Anvar", "Gulnoza"),
       'graduated_universities':["Financial","Diplomacy University"],
       'cars':[
           {'model':"BMW Black X7"},
            {'model':"KIA Sportage Silver"}
            ]
       }

# app_json=json.dumps(applicant,indent=4)
# print(app_json)
with open('applicant.json','w') as file:
    json.dump(applicant,file)
    
app_json=json.dumps(applicant,indent=4)
app2=json.loads(app_json)
# print(app2)
# print(type(app2))

filename='applicant.json'
with open(filename) as f:
    bemor=json.load(f)

print(bemor)    

    
    

    
    
























