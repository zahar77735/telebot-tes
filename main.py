#!/usr/bin/env python

import telebot
bot = telebot.TeleBot('1638470922:AAHvZSBGw3r4_etE8EY2Fpr1NLXlHg5CqO0')

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
	bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')
	
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
	if message.text.lower() == 'привет':
		bot.send_message(message.from_user.id, 'Привет!')
	else:
		bot.send_message(message.from_user.id, 'Не понимаю!')
		
bot.polling(none_stop=True)

