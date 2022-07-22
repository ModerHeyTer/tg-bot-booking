import requests
from datetime import datetime
import telebot
from auth_data import token
from telebot import types
from available_dates import dates, times



def telegram_bot(token):
    bot = telebot.TeleBot(token)

    @bot.message_handler(content_types=['text'])
    def start_message(message):
        kb = types.InlineKeyboardMarkup()
        btn1 = types.InlineKeyboardButton(text='Забронировать', callback_data='Booking')
        kb.add(btn1)
        bot.send_message(message.chat.id, "Привет! Здесь можно забронировать поездку!", reply_markup=kb)


    @bot.callback_query_handler(func=lambda callback: callback.data)
    def check_callback_data(callback):

        if callback.data == 'Booking':
            kb = types.InlineKeyboardMarkup(row_width=3)
            btn1 = types.InlineKeyboardButton(text=dates[0], callback_data=dates[0])
            btn2 = types.InlineKeyboardButton(text=dates[1], callback_data=dates[1])
            btn3 = types.InlineKeyboardButton(text=dates[2], callback_data=dates[2])
            btn4 = types.InlineKeyboardButton(text=dates[3], callback_data=dates[3])
            btn5 = types.InlineKeyboardButton(text=dates[4], callback_data=dates[4])
            btn6 = types.InlineKeyboardButton(text=dates[5], callback_data=dates[5])
            btn7 = types.InlineKeyboardButton(text=dates[6], callback_data=dates[6])
            kb.add(btn1, btn2, btn3, btn4, btn5, btn6, btn7)
            bot.send_message(callback.message.chat.id, 'Выберите дату:', reply_markup=kb)

        for i in range(7):
            if callback.data == dates[i]:
                kb = types.InlineKeyboardMarkup(row_width=3)
                btn1 = types.InlineKeyboardButton(text=times[0], callback_data=times[0])
                btn2 = types.InlineKeyboardButton(text=times[1], callback_data=times[1])
                btn3 = types.InlineKeyboardButton(text=times[2], callback_data=times[2])
                btn4 = types.InlineKeyboardButton(text=times[3], callback_data=times[3])
                btn5 = types.InlineKeyboardButton(text=times[4], callback_data=times[4])
                kb.add(btn1, btn2, btn3, btn4, btn5)
                bot.send_message(callback.message.chat.id, 'Выберите время:', reply_markup=kb)

        for i in range(5):
            if callback.data == times[i]:
                kb = types.InlineKeyboardMarkup(row_width=1)
                btn1 = types.InlineKeyboardButton(text='Забронировать и оплатить', url='www.google.com')
                kb.add(btn1)
                bot.send_message(callback.message.chat.id, f'На текущие дату и время осталось {10} мест\nНажмите кнопку, чтобы перейти к оплате!', reply_markup=kb)


    bot.polling()


if __name__ == '__main__':
    telegram_bot(token)