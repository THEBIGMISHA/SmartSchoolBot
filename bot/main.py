#####IMPORT-
import datetime				# Time Library
import telebot				# API Library
import config				# Add Config
import datacenter			# Add Datacenter
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
@bot.message_handler(content_types=['text'])
def amogus(message):
	datacenter.schedule('8Б',int(message.text),message.chat.id)
@bot.message_handler(commands=['schedule'])
def monday(message):
	markup=types.InlineKeyboardMarkup()
	buttonA = types.InlineKeyboardButton(text='Понедельник', callback_data='monday')
	markup.add(buttonA)
	bot.send_message(message.chat.id,'<b>Выбери день недели:</b>', parse_mode='html')

#РАСПИСАНИЕ
bot.polling(none_stop=True)	# NONESTOP
#####FUNC-