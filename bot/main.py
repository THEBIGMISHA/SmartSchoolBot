#####IMPORT-
import telebot				# АПИ
import config				# Добавление конфиг файла
import logger 				# Добавление логирования
import datacenter			# Добавление дата файла
import os					# Библиотека системы
from telebot import types 	# Библиотека кнопок
#####SETUP-
team = 0
os.system('cls||clear')				# Очистка консоли
bot = telebot.TeleBot(config.token) # Token
print('start bot')					# Print
logger.work('a','sus','fff',0)
#####BOT-
#ПРИВЕТСТВИЕ
@bot.message_handler(commands=['start', 'restart'])
def welcome(message):
	bot.send_message(message.chat.id,f'<b>Привет, {str(message.from_user.first_name)}!\nЯ бот школы (не официальный)\nЧтобы продолжить нажмите меню</b>', parse_mode='html')
@bot.message_handler(commands=['s'])
def monday(message):
	if team == 0:
		bot.send_message(message.chat.id,f'Выберите класс')
	else:
		datacenter.schedule(team,1,message.chat.id)
#МЕНЮ
@bot.message_handler(commands=['settings'])
def monday(message):
	markup=types.InlineKeyboardMarkup()
	buttonA = types.InlineKeyboardButton(text='Выбрать свой класс', callback_data='team_set')
	markup.add(buttonA)
	bot.send_message(message.chat.id,'<b>Что вы хотите настроить:</b>', parse_mode='html',  reply_markup=markup)
#ИНЛАЙН-КНОПКИ
@bot.callback_query_handler(func=lambda call: True)
def handle(call):
	if call.message:
		if call.data == 'team_set':
			markup=types.InlineKeyboardMarkup()
			buttonA = types.InlineKeyboardButton(text='8Б', callback_data="team_8Б")
			markup.add(buttonA)
			bot.send_message(call.message.chat.id,'<b>Выберете класс:</b>', parse_mode='html',reply_markup=markup)
		elif call.data == 'team_8Б':
			team = '8Б'
			bot.send_message(call.message.chat.id,f'Готово ваш класс {team}')
		elif call.data == 'team_8A':
			team = '8А'
#РАСПИСАНИЕ
bot.polling(none_stop=True)	# NONESTOP