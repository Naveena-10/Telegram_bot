!pip install adafruit-io
import os
x = os.getenv('dhananaveena_26')
y = os.getenv('aio_PNOa12Wx38StY0ahDOte52g426tp')
from Adafruit_IO import Client, Feed
aio = Client(x,y)
new = Feed(name='bot')
result = aio.create_feed(new)
from  import DataAdafruit_IO
!pip install python-telegram-bot
from Adafruit_IO import Client,Data
from telegram.ext import Updater,CommandHandler
def on(bot,update):
  chat_id = update.message.chat_id    
  aio.create_data('bot',Data(value = 1))
  bot.send_message(chat_id =chat_id,text ="Lights On")
  def off(bot,update):
  chat_id = update.message.chat_id
  aio.create_data('bot',Data(value = 0))
  bot.send_message(chat_id =chat_id,text ="Lights Off")
  updater =Updater('1386774726:AAF3ZQqPMhQz7k2ALqX2l3u-LX1gj-frqMs')
dp = updater.dispatcher
dp.add_handler(CommandHandler('on',on))
dp.add_handler(CommandHandler('off',off))
updater.start_polling()
updater.idle()
