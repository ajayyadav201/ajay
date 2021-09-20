import os
Active_key = os.getenv('Active_key') 
Username = os.getenv('Username')
bot_token = os.getenv('bot_token')

from telegram.ext  import Updater, MessageHandler, Filters
 
from Adafruit_IO import Client   
aio = Client(Username,Active_key)
 
 
def Ajayyadavbot1(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('light turned on')
  aio.send('ajaymajor2',1)
 
def Ajayyadavbot2(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('light turned off')
  aio.send('ajaymajor2',0)
 
def Ajayyadavbot3(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('Fan turned on')
  aio.send('ajaymajor2',2)
 
def Ajayyadavbot4(bot,update):
  chat_id = bot.message.chat_id
  bot.message.reply_text('Fan turned off')
  aio.send('ajaymajor2',3)
 
 
def main(bot,update):
  a= bot.message.text.lower()
  
  if a =="turn on light":
    Ajayyadavbot1(bot,update)
  elif a =="turn off light":
    Ajayyadavbot2(bot,update)
  elif a =="turn on fan":
    Ajayyadavbot3(bot,update)
  elif a =="turn off fan":
    Ajayyadavbot4(bot,update) 
     
 
u = Updater(bot_token,use_context=True)
dp = u.dispatcher
dp.add_handler(MessageHandler(Filters.text,main))
u.start_polling()
u.idle()      
      
