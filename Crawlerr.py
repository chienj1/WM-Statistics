import requests, json
import datetime

#DakraBl VaubSys TigrBp  NekrBp  NekrSys ValkCh  ValkSys BansSys ReapBl  SomaSt  DKamabl GalaBp  Dakr    Mag     Nova    Nyx     Scindo  Reaper  Soma    VengRev SovOutc EmpBls  GrowPow EndAff

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
Cate={'Set':st,'Mod':md,'Blueprint':bp}
# warframe market
raw_url="https://warframe.market/api/get_orders/"
# current time, up to Hour
date = str(datetime.datetime.now())[0:13]

summary_file=open('summary.txt', 'a+')
summary_file.write('\n')
summary_file.write(date+'\t')
for cate in iter(Cate): 
    print(cate)
    for item in iter(Cate[cate]):
        count = 0
        price_list=[]
        res = requests.get(raw_url+cate+'/'+item)
        text_res = json.loads(res.text)
        #file = open(item+'.txt', 'a+')
        for i in range(len(text_res['response']['sell'])):
            if (text_res['response']['sell'][i]['online_ingame'] == True) and (text_res['response']['sell'][i]['ingame_name'][0:5]!=('(PS4)' or'(XB1)')):            #alter : sell, buy
                price_list.append(text_res['response']['sell'][i]['price'])     #alter : price, count, ingame_name, online_ingame, online_status
                count+=1
        cheapest=min(price_list)
        summary_file.write(str(cheapest)+'\t')
        #file.write(date + '\t' + str(price_list[0])+ '\t' + str(count) +'\n')    # file format: date, lowest price, number of sellers     
        #file.close()
        print(item+str(cheapest))
summary_file.close()
print('done!')