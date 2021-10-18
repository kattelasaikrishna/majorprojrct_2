import os
#pip install adafruit-io
from Adafruit_IO import Client
username = os.getenv('username')
key = os.getenv('key')
token=os.getenv('token')
aio = Client(username,key)
#pip install python-telegram-bot==13.0

from telegram.ext import Updater, MessageHandler, Filters

def demo1(bot,update):
  chat_id=bot.message.chat_id
  bot.message.reply_text('Turning on the Light')
  aio.send('light',1)

def demo2(bot,update):
  chat_id=bot.message.chat_id
  bot.message.reply_text('Turning off the Light')
  aio.send('light',0)

def demo3(bot,update):
  chat_id=bot.message.chat_id
  bot.message.reply_text('Turning on the Fan')
  aio.send('fan',1)

def demo4(bot,update):
  chat_id=bot.message.chat_id
  bot.message.reply_text('Turning off the Fan')
  aio.send('fan',0)

def main(bot,update):
  a= bot.message.text.lower()
  if a=='lights on' or a==' turn on lights' or a==' turn lights on' or a==' turn on light' or a=='on light' or a=='light on' or a=='on lights' :
    demo1(bot,update)
  elif a=='lights off' or a==' turn off lights' or a==' turn lights off' or a==' turn off light' or a=='off light' or a=='light off' or a=='off lights' :
    demo2(bot,update)
  elif a=='lights off' or a==' turn off lights' or a==' turn lights off' or a==' turn off light' or a=='off light' or a=='light off' or a=='on fans' :
    demo3(bot,update)
  elif a=='fans off' or a==' turn off fans' or a=='turn fans off' or a==' turn fan off ' or a=='off fan' or a=='fan off'  or a=='off fans' :
    demo4(bot,update)


bot_token = token
u = Updater(bot_token,use_context=True)
dp=u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()

