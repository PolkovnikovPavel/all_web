from telegram.ext import Updater
from telegram.ext import CommandHandler

import time


def set_timer(update, context):
    chat_id = update.message.chat_id
    try:
        due = int(context.args[0])
        if due < 0:
            update.message.reply_text(
                'Извините, не умеем возвращаться в прошлое')
            return

        if 'job' in context.chat_data:
            old_job = context.chat_data['job']
            old_job.schedule_removal()
        new_job = context.job_queue.run_once(task, due, context=chat_id)
        context.chat_data['job'] = new_job
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
    if 'job' not in context.chat_data:
        update.message.reply_text('Нет активного таймера')
        return
    job = context.chat_data['job']
    job.schedule_removal()

    del context.chat_data['job']
    update.message.reply_text('Хорошо, вернулся сейчас!')


def main():
    updater = Updater('token', use_context=True)
    dp = updater.dispatcher

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
