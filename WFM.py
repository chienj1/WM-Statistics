import requests, json
import datetime

BP=['Dakra Prime Blade','Ankyros Prime Blade']
Set=['Dakra Prime Set']
Mod=[]
Cate={'Blueprint':BP_item,'Mod':Mod_item,'Set':Set_item}
raw_url="https://warframe.market/api/get_orders/"
date = str(datetime.datetime.now())[0:13]                                   #
for cate in iter(Cate):  
    for item in iter(Cate[cate]):
        count = 0
        price_list=[]
        file = open(item+'.txt', 'a+')
        res = requests.get(raw_url+cate+'/'+item)
        data = json.loads(res.text)
        for i in range(len(data['response']['sell'])):
            if data['response']['sell'][i]['online_ingame'] == True:        #alter : sell, buy
                price_list.append(data['response']['sell'][i]['price'])      #alter : price, count, ingame_name, online_ingame, online_status
                count+=1
        price_list.sort()
        print(date + '\t' + str(price_list[0])+ '\t' + str(count) +'\n')        
        # file format: date, lowest price, number of sellers 
        file.close() 
