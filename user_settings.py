from database import changes_from_user


def get_changes(bot, msg, id_):
    match msg.text.lower():
        case "время -> чисел":
            msg_ = bot.reply_to(msg, 'Введите новое значение')
            bot.register_next_step_handler(msg_, lambda x: changes_from_user(id_, 'number_time', int(x.text)))
            #bot.send_message(msg.chat.id, "Готово")
        case "кол-во -> чисел":
            msg_ = bot.reply_to(msg, 'Введите новое значение')
            bot.register_next_step_handler(msg_, lambda x: changes_from_user(id_, 'number_quantity', int(x.text)))
            #bot.send_message(msg.chat.id, "Готово")
        case "время -> слов":
            msg_ = bot.reply_to(msg, 'Введите новое значение')
            bot.register_next_step_handler(msg_, lambda x: changes_from_user(id_, 'words_time', int(x.text)))
            #bot.send_message(msg.chat.id, "Готово")
        case "кол-во -> слов":
            msg_ = bot.reply_to(msg, 'Введите новое значение')
            bot.register_next_step_handler(msg_, lambda x: changes_from_user(id_, 'words_quantity', int(x.text)))
            #bot.send_message(msg.chat.id, "Готово")

        case _:
            bot.reply_to(msg, 'Не понял команды')