import os
#pip install adafruit-io
from Adafruit_IO import Client
username_1= os.getenv('username')
key_1= os.getenv('key')
aio= Client(username_1,key_1)
from telegram.ext import Updater, MessageHandler, Filters

def demo1(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('Light turned on')
  aio.send('light',1)

def demo2(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('Light turned off') 
  aio.send('light',0)

def demo3(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('Fan turned on')
  aio.send('fan',1)

def demo4(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('Fan turned off')
  aio.send('fan',0)

def main(bot,update):
  a= bot.message.text.lower()
  if a =="turn on light":
    demo1(bot,update)
  elif a =="turn off light":
    demo2(bot,update)
  elif a =="turn on fan":
    demo3(bot,update)
  elif a =="turn off fan":
    demo4(bot,update)

bot_token = '2060580694:AAF0H6Ri0hzY7tf5BhjCdBRuuzsuOOufD_4'
u = Updater(bot_token,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()

