from telegram.ext import Updater, CommandHandler
from conf import TOKEN


def start(bot, update):
    update.message.reply_text('Chat ID: %s' % update.message.chat_id)


def hello(bot, update):
    update.message.reply_text('Hello %s' % update.message.from_user.first_name)


def echo(bot, update):
    update.message.reply_text(update.message.text.split(' ', 1)[1])


def dump_update(bot, update):
    update.message.reply_text(str(update))


updater = Updater(TOKEN)

updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('hello', hello))
updater.dispatcher.add_handler(CommandHandler('echo', echo))
updater.dispatcher.add_handler(CommandHandler('dump_update', dump_update))

updater.start_polling()
updater.idle()

