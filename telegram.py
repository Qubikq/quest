import telebot
from telebot import types

bot = telebot.TeleBot('7198307598:AAGYTPzX3QS-dCryMY5awFsqC2XcuUvJ5EE')


class DB:
    answer_data = []


@bot.message_handler(commands=['start'])
def startBot(message):
    first_mess = f"\nДобро пожаловать в меню создания перосонажа! \nЧто вы хотите сделать?\n"
    markup = types.InlineKeyboardMarkup()
    button_1 = types.InlineKeyboardButton(text='Создать персонажа', callback_data='1')
    markup.add(button_1)
    button_2 = types.InlineKeyboardButton(text='О персонаже', callback_data='2')
    markup.add(button_2)
    button_3 = types.InlineKeyboardButton(text='Редактор класса', callback_data='3')
    markup.add(button_3)
    button_4 = types.InlineKeyboardButton(text='Узнать информацию о персонаже', callback_data='4')
    markup.add(button_4)
    button_5 = types.InlineKeyboardButton(text='Выход', callback_data='5')
    markup.add(button_5)
    bot.send_message(message.chat.id, first_mess, parse_mode='html', reply_markup=markup)


@bot.callback_query_handler(func=lambda call: True)
def response(function_call):
    if function_call.message:
        if function_call.data == "1":
            first_mess = "Выберите класс для Вашего персронажа."
            markup = types.InlineKeyboardMarkup()
            button_1 = types.InlineKeyboardButton(text='Воин', callback_data='1')
            markup.add(button_1)
            button_2 = types.InlineKeyboardButton(text='Маг', callback_data='2')
            markup.add(button_2)
            button_3 = types.InlineKeyboardButton(text='Лучник', callback_data='3')
            markup.add(button_3)
            bot.send_message(function_call.message.chat.id, first_mess, parse_mode='html', reply_markup=markup)

            @bot.callback_query_handler(func=lambda call: True)
            def classes(classes1):
                if classes1.message:
                    if function_call.data == "1":
                        answer = "Вы выбрали класс - Воин."
                        bot.send_message(function_call.message.chat.id, answer)
                    elif function_call.data == "2":
                        answer = "Вы выбрали класс - Маг."
                        bot.send_message(function_call.message.chat.id, answer)
                    elif function_call.data == "3":
                        answer = "Вы выбрали класс - Лучник."
                        bot.send_message(function_call.message.chat.id, answer)
                    else:
                        answer = "Выберите класс из указанного списка."
                        bot.send_message(function_call.message.chat.id, answer)

            @bot.message_handler(content_types=['text'])
            def handle_message(message):
                DB.answer_data.append(message.text)
                bot.send_message(message.chat.id, f'{message.text} - имя Вашего персонажа')
                print(DB.answer_data[0])

            second_mess = "Введите возраст вашего персонажа."
            bot.send_message(function_call.message.chat.id, second_mess)


bot.infinity_polling()
