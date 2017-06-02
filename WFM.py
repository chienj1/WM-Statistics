#{'code': 200,
# 'response': {'buy': [{'count': 1,
#    'ingame_name': 'Neverlight',
#    'online_ingame': False,
#    'online_status': False,
#    'price': 20},
#   {'count': 1,
#    'ingame_name': 'Bress94',
#    'online_ingame': False,
#    ..........................................

import requests, json

item=['Blueprint/Dakra%20Prime%20Blade','Set/Ankyros%20Prime%20Set','Blueprint/Ankyros%20Prime%20Blade']
raw_url="https://warframe.market/api/get_orders/"
for i in iter(item) :
    print(i)
    count = 0
    res = requests.get(raw_url+i)
    data = json.loads(res.text)
    k=[]
    for j in range(len(data['response']['sell'])):
        if data['response']['sell'][j]['online_ingame'] == True:          
            k.append(data['response']['sell'][j]['price'])
            count+=1
    k.sort()
    print(k)
    print('# of sellers : '+str(count))
    
    

# add clock
# let print to be in a list