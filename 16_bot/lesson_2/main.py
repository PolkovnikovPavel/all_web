from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler
from telegram import ReplyKeyboardMarkup
from telegram import ReplyKeyboardRemove
import time


def set_timer(update, context):
    """Добавляем задачу в очередь"""
    chat_id = update.message.chat_id
    try:
        # args[0] должен содержать значение аргумента (секунды таймера)
        due = int(context.args[0])
        if due < 0:
            update.message.reply_text(
                'Извините, не умеем возвращаться в прошлое')
            return

        # Добавляем задачу в очередь
        # и останавливаем предыдущую (если она была)
        if 'job' in context.chat_data:
            old_job = context.chat_data['job']
            old_job.schedule_removal()
        new_job = context.job_queue.run_once(task, due, context=chat_id)
        # Запоминаем созданную задачу в данных чата.
        context.chat_data['job'] = new_job
        # Присылаем сообщение о том, что всё получилось.
        update.message.reply_text(f'Вернусь через {due} секунд')

    except (IndexError, ValueError):
        update.message.reply_text('Использование: /set <секунд>')


def task(context):
    job = context.job
    context.bot.send_message(job.context, text='Вернулся!')


def get_time(update, context):
    t = time.gmtime()
    update.message.reply_text(f'{t.tm_hour}-{t.tm_min}-{t.tm_sec}')


def get_date(update, context):
    t = time.gmtime()
    update.message.reply_text(f'{t.tm_mday}.{t.tm_mon}.{t.tm_year}')


def unset_timer(update, context):
    # Проверяем, что задача ставилась
    if 'job' not in context.chat_data:
        update.message.reply_text('Нет активного таймера')
        return
    job = context.chat_data['job']
    # планируем удаление задачи (выполнится, когда будет возможность)
    job.schedule_removal()
    # и очищаем пользовательские данные
    del context.chat_data['job']
    update.message.reply_text('Хорошо, вернулся сейчас!')


def main():
    global markup
    updater = Updater('912680602:AAFuJ7VF3CuxO2_giada4gqGP_dwfLqkp5c', use_context=True)
    dp = updater.dispatcher

    reply_keyboard = [['/address', '/phone'],
                      ['/site', '/work_time', '/close']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)

    dp.add_handler(CommandHandler("set", set_timer,
                                  pass_args=True,
                                  pass_job_queue=True,
                                  pass_chat_data=True))
    dp.add_handler(CommandHandler("unset", unset_timer,
                                  pass_chat_data=True))
    dp.add_handler(CommandHandler("time", get_time))
    dp.add_handler(CommandHandler("date", get_date))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
