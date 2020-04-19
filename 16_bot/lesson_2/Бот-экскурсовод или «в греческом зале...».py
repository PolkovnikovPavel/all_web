from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CommandHandler
from telegram import ReplyKeyboardMarkup


mapp = [[2, 3],
        [1, 4]]

description = {1: ['зал ожидания', 'Пожалуйста ожидайте своей очереди', [3, 4], [2]],
               2: ['выставка изобретений', 'В данном зале представлены величайшие изобретения', [1], [3]],
               3: ['выставка искуссива', 'В данном зале представлены величайшие произвеления', [2], [1, 4]],
               4: ['выставка скульптур', 'В данном зале представлены величайшие скульптуры', [3], [1]]
               }
room = 0


def get_keybord():
    can_go = description[room][3]
    reply_keyboard = []
    for line in mapp:
        reply_keyboard.append([])
        for num in line:
            if num in can_go:
                reply_keyboard[-1].append(description[num][0])
            elif num == room:
                reply_keyboard[-1].append(f'Вы здесь,\n{description[num][0]}')
            else:
                reply_keyboard[-1].append(f'Прохода нет,\n{description[num][0]}')
    if room == 1:
        reply_keyboard.append(['/exit'])

    markup = ReplyKeyboardMarkup(reply_keyboard)
    return markup


def go_to(rom, update):
    global room
    room = rom
    update.message.reply_text(description[room][1],
                              reply_markup=get_keybord())


def start(update, context):
    update.message.reply_text('Добро пожаловать! Пожалуйста, сдайте верхнюю одежду в гардероб!')
    go_to(1, update)


def made_exit(update, context):
    global room
    room = 0
    reply_keyboard = [['/inlet']]
    markup = ReplyKeyboardMarkup(reply_keyboard, one_time_keyboard=False)
    update.message.reply_text('Всего доброго, не забудьте забрать верхнюю одежду в гардеробе!',
                              reply_markup=markup)


def to_ring(context):
    cont = context.job.context
    context.bot.send_message(cont[0], text=cont[1])


def made_step(update, context):
    new_room = 0
    for key in description:
        if description[key][0] == update.message.text:
            new_room = key
            break
    if new_room not in description[room][3] or new_room == 0:
        return
    go_to(new_room, update)


def main():
    updater = Updater('token', use_context=True)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("inlet", start))   # вход
    dp.add_handler(CommandHandler("exit", made_exit))   # выход

    dp.add_handler(MessageHandler(Filters.text, made_step))

    updater.start_polling()
    updater.idle()


if __name__ == '__main__':
    main()
