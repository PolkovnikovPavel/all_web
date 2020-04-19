from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup
import random


def throw_a_cube(num, count=1):
    sequence = list(range(1, num + 1))
    return list(map(lambda x: str(random.choice(sequence)), range(count)))


def start(update, context):
    reply_keyboard = [['/dice', '/timer']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=True)

    update.message.reply_text('Выбирете действие',
                              reply_markup=markup)


def timer(update, context):
    reply_keyboard = [['30 секунд', '1 минута'],
                      ['5 минут', 'вернуться назад']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

    update.message.reply_text('Сколько засечь?',
                              reply_markup=markup)


def to_ring(context):
    cont = context.job.context
    context.bot.send_message(cont[0], text=cont[1])


def dice(update, context):
    reply_keyboard = [['кинуть один шестигранный кубик', 'кинуть 2 шестигранных кубика одновременно'],
                      ['кинуть 20-гранный кубик', 'вернуться назад']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

    update.message.reply_text('Как кинуть кубик?',
                              reply_markup=markup)


def text_commands(update, context):
    string = None
    if update.message.text == 'вернуться назад':
        start(update, context)
    elif update.message.text == 'кинуть один шестигранный кубик':
        string = ' '.join(throw_a_cube(6))
    elif update.message.text == 'кинуть 2 шестигранных кубика одновременно':
        string = ' '.join(throw_a_cube(6, 2))
    elif update.message.text == 'кинуть 20-гранный кубик':
        string = ' '.join(throw_a_cube(20))
    elif update.message.text == '30 секунд':
        new_job = context.job_queue.run_once(to_ring, 30,
                                             context=[update.message.chat_id,
                                                      '30 секунд истекло'])
        context.chat_data['job'] = new_job
        string = 'засек 30 секунд'
    elif update.message.text == '1 минута':
        new_job = context.job_queue.run_once(to_ring, 60,
                                             context=[update.message.chat_id,
                                                      '1 минута истекла'])
        context.chat_data['job'] = new_job
        string = 'засек 1 минуту'
    elif update.message.text == '5 минут':
        new_job = context.job_queue.run_once(to_ring, 300,
                                             context=[update.message.chat_id,
                                                      '1 минут истекло'])
        context.chat_data['job'] = new_job
        string = 'засек 5 минут'

    if string:
        update.message.reply_text(string)


def main():
    updater = Updater('token', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("dice", dice))
    dp.add_handler(CommandHandler("timer", timer))

    dp.add_handler(MessageHandler(Filters.text, text_commands))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
