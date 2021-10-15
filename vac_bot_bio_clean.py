#check all doctolib doctors that offer biontech
#telegram bot sends an alert message with the doctolib website if there is an available termin


# Importing libraries
import requests
import time
import hashlib
from urllib.request import urlopen, Request

# bot sending function
def telegram_bot_sendtext(bot_message, bot_token, bot_chatID):
   

   send_text = 'https://api.telegram.org/bot' + bot_token + '/sendMessage?chat_id=' + bot_chatID + '&parse_mode=Markdown&text=' + bot_message

   response = requests.get(send_text)

   return response.json()
   
# get number of total termins
# alert in telegram chat
def alert_termins(url_doc, payload):

   resp = requests.get(url=url, headers=headers, params=payload)
    
# only alert if there are more then one total termin
   if resp.json()['total'] > 0:


      alert = str(resp.json()['total']) + ' appointments available: '+ str(url_doc)

      telegram_bot_sendtext(str(alert), bot_token, bot_chatID)
      print(alert) 

#how long to wait after checking the list
check_interval = 30
	  
# bot details	  
#create a bot with BotFather and set the details here
bot_token = 'fill me'
#chat directly to me
bot_chatID = 'fill me'

# site details
url = 'https://www.doctolib.de/availabilities.json'
headers= headers={'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:88.0) Gecko/20100101 Firefox/88.0'}	


#dict with docs of Berlin docs that offer 1st shot biontech


docs = {'doc1': {'url_doc': 'https://www.doctolib.de/gemeinschaftspraxis/berlin/bonedoctor-christian-rose-baharak-djohar?insurance_sector=public&vmid=2774169',
'payload': {'start_date': '2021-05-31',
'visit_motive_ids': '2797297',
'agenda_ids':  '462529',
'insurance_sector': 'public',
'practice_ids': '181755',
'limit':'20'}},
'doc2': {'url_doc': 'https://www.doctolib.de/praxis/berlin/dr-burkhard-schlich-dr-kai-schorn',
'payload': {'start_date': '2021-05-31',
'visit_motive_ids': '2884324',
'agenda_ids':  '444401',
'insurance_sector': 'public',
'practice_ids': '141729',
'limit':'20'}},
'doc3': {'url_doc': 'https://www.doctolib.de/frauenarzt/berlin/susanne-eipper?insurance_sector=public&vmid=2828563',
'payload': {'start_date': '2021-05-31',
'visit_motive_ids': '2769431',
'agenda_ids':  '466062',
'insurance_sector': 'public',
'practice_ids': '23239',
'limit':'20'}},
'doc4': {'url_doc': 'https://www.doctolib.de/allgemeinmedizin/berlin/benjamin-lott',
'payload': {'start_date': '2021-05-31',
'visit_motive_ids': '2754056',
'agenda_ids':  '452595',
'insurance_sector': 'public',
'practice_ids': '132888',
'limit':'20'}}}


for i in range(1,50000):
   for i in docs:
      url_doc = docs[i]['url_doc']
      payload = docs[i]['payload']
      alert_termins(url_doc=url_doc, payload=payload) 
	
   print("checking")
   time.sleep(check_interval)




 

