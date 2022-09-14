#####IMPORT-
import datetime				# Time Library
import telebot				# API Library
import config				# Add Config
import schedule				# Add Schedule
import os					# OS Library
from telebot import types 	# Button Library
#####SETUP-
bot = telebot.TeleBot(config.token) # Token
print('start bot')					# Print
#####BOT-
#ПРИВЕТСТВИЕ
@bot.message_handler(commands=['start', 'restart'])
def welcome(message):
	markup=types.InlineKeyboardMarkup()
	buttonA = types.InlineKeyboardButton(text='Продолжить', url='porn.hub')
	markup.add(buttonA)
	bot.send_message(message.chat.id,'<b>Привет</b> '+str(message.from_user.first_name)+'!\n<b>Я сделан чтобы давать расписание уроков!</b>\n(Пока что)', parse_mode='html', reply_markup=markup)
#ИНЛАЙН-КНОПКИ
#МЕНЮ
@bot.message_handler(commands=['schedule'])
def monday(message):
	markup=types.InlineKeyboardMarkup()
	buttonA = types.InlineKeyboardButton(text='Понедельник', callback_data='monday')
	markup.add(buttonA)
	bot.send_message(message.chat.id,'<b>Выбери день недели:</b>', parse_mode='html')
	schedule(1, message.chat.id)
#РАСПИСАНИЕ
#1---
def schedule(day, message_id):
#1---
	if day == 1:
		bot.send_message(message_id, schedule.monday, parse_mode='html')
#2---
	elif day == 2:
		bot.send_message(message_id, schedule.tuesday, parse_mode='html')
#3---
	elif day ==	3:
		bot.send_message(message_id, schedule.wednesday, parse_mode='html')
#4---
	elif day == 4:
		bot.send_message(message_id, schedule.thursday, parse_mode='html')
#5---
	elif day == 5:
		bot.send_message(message_id, schedule.friday, parse_mode='html')
	else:
		print('error')
bot.polling(none_stop=True)	# NONESTOP
#####FUNC- 
