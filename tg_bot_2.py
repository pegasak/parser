# -*- coding: utf-8 -*-

import telebot
from telebot import types
import webbrowser
from parser_function import get_crypto_info
import time

bot = telebot.TeleBot('6737124110:AAEYM3CyRUW94NBajKniLnrMCnRlxWwBq90')


@bot.message_handler(commands=['start'])
def main(message):
    """
        Обработчик команды /start.

        Отправляет приветственное сообщение и описание функций бота пользователю.
        :param message:
    """
    bot.send_message(message.chat.id,
                     f'Здравствуйте,{message.from_user.first_name} {message.from_user.last_name}, я бот, который поможет вам следить за курсом криптовалют.'
                     '\nФункции моей работы:'
                     '\n1) /get_price - команда, отправив которую вы получите информацию о текущей цене топа 10 криптовалют и их капитализации'
                     '\n2) /set_time_reminder - команда, которая поможет вам мониторить цены криптовалют в течении заданного вами времени.'
                     '\n3) /coinmarketcap - автоматически переносит вас на сайт, где вы можете уже без помощи бота изучить обстановку на рынке'
                     '\nКак это работает: вы устанавливаете период времени, через который я буду отправлять вам уведомление о текущей ситуации на рынке криптовалют.')


@bot.message_handler(commands=['get_price'])
def price(message):
    """
        Обработчик команды /get_price.

        Вызывает функцию get_crypto_info() для получения информации о курсе криптовалют и отправляет результат пользователю.
        :param message:
    """
    result_str = get_crypto_info()

    bot.send_message(message.chat.id, result_str)


a = 0


@bot.message_handler(commands=['set_time_reminder'])
def remind(message):
    """
        Обработчик команды /set_time_reminder.

        Отправляет клавиатуру с вопросом о промежутке времени, через который пользователь хочет получать уведомления.
        Затем устанавливает обработчик для обработки выбора времени.
        :param message:
    """
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    button1 = types.KeyboardButton("1 минута")
    button2 = types.KeyboardButton("Пол часа")
    button3 = types.KeyboardButton("2 часа")
    markup.add(button1, button2, button3)

    msg = bot.send_message(message.chat.id, "Через какой промежуток времени вы хотите получать сообщения?",
                           reply_markup=markup)

    bot.register_next_step_handler(msg, process_time_choice)


def process_time_choice(message):
    """
        Обработчик выбора времени для напоминаний.

        Устанавливает заданный пользователем промежуток времени и отправляет подтверждение.
        :param message:
    """
    global a
    if message.text == "1 минута":
        a = 60
    elif message.text == "Пол часа":
        a = 1800
    elif message.text == "2 часа":
        a = 7200

    bot.send_message(message.chat.id, f"Напоминания будут приходить каждые {a} секунд")

    while True:
        result_str = get_crypto_info()

        bot.send_message(message.chat.id, result_str)

        time.sleep(a)


@bot.message_handler(commands=['coinmarketcap'])
def get_inf(message):
    """
        Обработчик команды /coinmarketcap.

        Открывает веб-браузер и перенаправляет пользователя на сайт coinmarketcap.com.
        :param message:
    """
    webbrowser.open('https://coinmarketcap.com/')


bot.polling(none_stop=True)
