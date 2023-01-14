#16-dars. nesting

car0 = {
        'model':'lacetti',
        'rang':'oq',
        'yil':2018,
        'narh':13000,
        'km':50000,
        'korobka':'avtomat' }
car1={
      'model':'nexia3',
      'rang':'qora',
      'yil':2019,
      'narh':15000,
      'km':36000,
      'korobka':'avtomat' }
car2={
        'model':'spark',
        'rang':'qizil',
        'yil':2022,
        'narh':11000,
        'km':12000,
        'korobka':'mexanika'}


cars=[car0,car1,car2]

#for a in cars:
   #print(f"{a['model'].title()}, {a['yil']} - yil, {a['narh']} $")
    

#print(cars[1]['km'])

#print(cars[2]['yil'])

malibus=[]
for a in range (10):
    new_car={
        'model':'malibu',
        'rang':None,
        'yil':2022,
        'narh':None,
        'km':0,
        'karobka':'avtomat' }
    malibus.append(new_car)
    
for b in malibus[0:3]:
    b['rang']='qizil'
#print(malibus[0:3])    
    
for c in malibus[3:6]:
    c['rang']='qora'
#print(malibus[3:6])
   
for  d in malibus[6:]: 
    d['rang']='yashil'
    d['karobka']='mexanika'
#print(malibus[6:])

for w in malibus:
    if w['karobka']=='avtomat':
        w['narh']=40000
    else:
        w['narh']=35000
#print(malibus)        


footbalers={
    'messi':['fcbarcelona','psg'],
    'suarez':['liverpool', 'atletico'],
    'ibrahimovic':['ajax', 'inter', 'psg', 'milan']
    }
#print(footbalers.items())
#for k,q in footbalers.items():
    #print(f"\n{k.title()} to'p surgan klublari : ", end='')
    #for a in q:
       # print(f"{a.upper()}, ", end='')


dasturchilar={
    'ali': {'familya':'valiyev',
            'tyil':1995,
            'malumot':'oliy',
            'tillar':['python',"c++"] },
    
    'vali': {'familya':'turopov',
            'tyil':2001,
            'malumot':"o'rta",
            'tillar':['html','css'] },
    
    'hasan': {'familya':'husanov',
             'tyil':1998,
             'malumot':'oliy',
             'tillar':['php', 'sql']}
    }

for k,q in dasturchilar.items():
    print(f"{k.title()} {q['familya']}. "
          f"{q['tyil']}-yilda tug'ilgan. "
          f"Ma'lumoti : {q['malumot']}.\n"
          "Quyidagi dasturlash tillarini biladi :"
          )
    for a in q['tillar']:
        print(a.upper())
        
        














