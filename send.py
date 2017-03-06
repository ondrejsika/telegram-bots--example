import time
from telegram import Bot

from conf import TOKEN, CHAT_ID

bot = Bot(TOKEN)
chat_id = CHAT_ID


while 1:
    bot.sendMessage(chat_id=chat_id, text="%s" % time.time())
    time.sleep(30)

