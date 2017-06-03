import requests, json
import datetime

# blueprint items
bp=['Dakra Prime Blade',
    'Vauban Prime Systems',
    'Tigris Prime Blueprint',
    'Nekros Prime Blueprint',
    'Nekros Prime Systems',
    'Valkyr Prime Chassis',
    'Valkyr Prime Systems',
    'Banshee Prime Systems',
    'Reaper Prime Blade',
    'Soma Prime Stock',
    'Dual Kamas Prime Blade',
    'Galatine Prime Blueprint']
# Set items
st=['Dakra Prime Set',
    'Mag Prime Set',
    'Nova Prime Set',
    'Nyx Prime Set',
    'Scindo Prime Set',
    'Reaper Prime Set',
    'Soma Prime Set']
# Mod items
md=['Vengeful Revenant',
    'Sovereign Outcast',
    'Empowered Blades',
    'Growing Power',
    'Enduring Affliction']
Cate={'Blueprint':bp,'Mod':md,'Set':st}
# warframe market
raw_url="https://warframe.market/api/get_orders/"
# current time, up to Hour
date = str(datetime.datetime.now())[0:13]

for cate in iter(Cate):  
    for item in iter(Cate[cate]):
        count = 0
        price_list=[]
        res = requests.get(raw_url+cate+'/'+item)
        print(item)
        data = json.loads(res.text)
        #file = open(item+'.txt', 'a+')
        for i in range(len(data['response']['sell'])):
            if data['response']['sell'][i]['online_ingame'] == True:        #alter : sell, buy
                price_list.append(data['response']['sell'][i]['price'])     #alter : price, count, ingame_name, online_ingame, online_status
                count+=1
        #price_list.sort()
        #print(date + '\t' + str(price_list[0])+ '\t' + str(count) +'\n')    # file format: date, lowest price, number of sellers     
        #file.close()
