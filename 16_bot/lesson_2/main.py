from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler


def echo(update, context):
    update.message.reply_text(update.message.text)


def main():
    updater = Updater(token='912680602:AAFuJ7VF3CuxO2_giada4gqGP_dwfLqkp5c', use_context=True)
    updater.start_polling()

    dp = updater.dispatcher
    text_handler = MessageHandler(Filters.text, echo)

    dp.add_handler(text_handler)
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
