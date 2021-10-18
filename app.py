import os
#pip install adafruit-io
from Adafruit_IO import Client
aio = Client('harika_31','aio_LNcj32v7bVrqlJeb4n5udx4aXF9H')
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

bot_token = token
u = Updater(bot_token,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()
