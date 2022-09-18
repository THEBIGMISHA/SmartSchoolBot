#####IMPORT
import telebot				
import config				
import logger 				
import datacenter			
import os
import time				
from telebot import types 	
#####SETUP
logger.log('WS','BOT','WORKING')
bot = telebot.TeleBot(config.token)
#####CODE
@bot.message_handler(commands=['start', 'restart'])
def START(message):
	sticker=open(f"{config.media}Swelcome.webp", "rb")
	bot.send_sticker(message.chat.id, sticker)
	logger.log('W','BOT',f'start,restart: NAME: {str(message.from_user.first_name)} USER-ID: {str(message.from_user.id)} CHAT-ID: {str(message.chat.id)}')
	bot.send_message(message.chat.id,f'<b>Привет, {str(message.from_user.first_name)}!\n Я бот помощьник класса\n Все мои функии в кнопке "меню"</b>', parse_mode='html')
	if message.chat.type == 'private':
		bot.send_message(message.chat.id,'<b>↓↓↓↓↓</b>',parse_mode='html')
@bot.message_handler(commands=['settings'])
def SETTINGS(message):
	logger.log('W','BOT',f'settings: NAME: {str(message.from_user.first_name)} USER-ID: {str(message.from_user.id)} CHAT-ID: {str(message.chat.id)}')
	bot.send_message(message.chat.id,'<b>СКОРО</b>',parse_mode='html')
@bot.message_handler(commands=['ping' , 'test'])
def PING(message):
	bot.send_message(message.chat.id, '<b>БОТ РАБОТАЕТ!</b>', parse_mode='html')
@bot.message_handler(commands=['schedule'])
def SCHEDULE(message):
	markup = types.InlineKeyboardMarkup()
	buttonA = types.InlineKeyboardButton(text='Понедельник', callback_data='schedule/1')
	buttonB = types.InlineKeyboardButton(text='Вторник', callback_data='schedule/2')
	buttonC = types.InlineKeyboardButton(text='Среда', callback_data='schedule/3')
	buttonD = types.InlineKeyboardButton(text='Четверг', callback_data='schedule/4')
	buttonE = types.InlineKeyboardButton(text='Пятница', callback_data='schedule/5')
	markup.add(buttonA)
	markup.add(buttonB)
	markup.add(buttonC)
	markup.add(buttonD)
	markup.add(buttonE)
	logger.log('W','BOT',f'schedule: NAME: {str(message.from_user.first_name)} USER-ID: {str(message.from_user.id)} CHAT-ID: {str(message.chat.id)}')
	bot.send_message(message.chat.id,'<b>Выбери день недели:</b>',parse_mode='html', reply_markup=markup)
@bot.callback_query_handler(func=lambda call: True)
def CALL(call):
	if call.message:
		#SCHEDULE
		if   call.data == 'schedule/1':
			markup = types.InlineKeyboardMarkup()
			buttonA = types.InlineKeyboardButton(text='Прошлый день', callback_data='schedule/5')
			buttonB = types.InlineKeyboardButton(text='Следующий день', callback_data='schedule/2')
			markup.add(buttonA,buttonB)
			logger.log('W','BOT',f'schedule/1: NAME: {str(call.message.from_user.first_name)} USER-ID: {str(call.message.from_user.id)} CHAT-ID: {str(call.message.chat.id)}')
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=datacenter.schedule(1), parse_mode='html', reply_markup=markup)
		elif call.data == 'schedule/2':
			markup = types.InlineKeyboardMarkup()
			buttonA = types.InlineKeyboardButton(text='Прошлый день', callback_data='schedule/1')
			buttonB = types.InlineKeyboardButton(text='Следующий день', callback_data='schedule/3')
			markup.add(buttonA,buttonB)
			logger.log('W','BOT',f'schedule/2: NAME: {str(call.message.from_user.first_name)} USER-ID: {str(call.message.from_user.id)} CHAT-ID: {str(call.message.chat.id)}')
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=datacenter.schedule(2), parse_mode='html', reply_markup=markup)
		elif call.data == 'schedule/3':
			markup = types.InlineKeyboardMarkup()
			buttonA = types.InlineKeyboardButton(text='Прошлый день', callback_data='schedule/2')
			buttonB = types.InlineKeyboardButton(text='Следующий день', callback_data='schedule/4')
			markup.add(buttonA,buttonB)
			logger.log('W','BOT',f'schedule/3: NAME: {str(call.message.from_user.first_name)} USER-ID: {str(call.message.from_user.id)} CHAT-ID: {str(call.message.chat.id)}')
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=datacenter.schedule(3), parse_mode='html', reply_markup=markup)
		elif call.data == 'schedule/4':
			markup = types.InlineKeyboardMarkup()
			buttonA = types.InlineKeyboardButton(text='Прошлый день', callback_data='schedule/3')
			buttonB = types.InlineKeyboardButton(text='Следующий день', callback_data='schedule/5')
			markup.add(buttonA,buttonB)
			logger.log('W','BOT',f'schedule/4: NAME: {str(call.message.from_user.first_name)} USER-ID: {str(call.message.from_user.id)} CHAT-ID: {str(call.message.chat.id)}')
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=datacenter.schedule(4), parse_mode='html', reply_markup=markup)
		elif call.data == 'schedule/5':
			markup = types.InlineKeyboardMarkup()
			buttonA = types.InlineKeyboardButton(text='Прошлый день', callback_data='schedule/4')
			buttonB = types.InlineKeyboardButton(text='Следующий день', callback_data='schedule/1')
			markup.add(buttonA,buttonB)
			logger.log('W','BOT',f'schedule/5: NAME: {str(call.message.from_user.first_name)} USER-ID: {str(call.message.from_user.id)} CHAT-ID: {str(call.message.chat.id)}')
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=datacenter.schedule(5), parse_mode='html', reply_markup=markup)
		#ADMIN_PANEL
		elif call.data == 'logger':
			markup = types.InlineKeyboardMarkup()
			buttonA = types.InlineKeyboardButton(text='Запросить логи', callback_data='logger/save')
			buttonB = types.InlineKeyboardButton(text='Удалить логи', callback_data='logger/hm')
			markup.add(buttonA)
			markup.add(buttonB)
			logger.log('WS','BOT',f'logger: NAME: {str(call.message.from_user.first_name)} USER-ID: {str(call.message.from_user.id)} CHAT-ID: {str(call.message.chat.id)}')
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='Логирование', parse_mode='html', reply_markup=markup)
		elif call.data == 'stop/hm':
			markup = types.InlineKeyboardMarkup()
			buttonA = types.InlineKeyboardButton(text='Да, точно!', callback_data='stop/yes')
			buttonB = types.InlineKeyboardButton(text='Нет', callback_data='bot_del_mess')
			buttonC = types.InlineKeyboardButton(text='Нет', callback_data='bot_del_mess')
			buttonD = types.InlineKeyboardButton(text='Нет', callback_data='bot_del_mess')
			buttonE = types.InlineKeyboardButton(text='Нет', callback_data='bot_del_mess')
			buttonF = types.InlineKeyboardButton(text='Нет', callback_data='bot_del_mess')
			markup.add(buttonB)
			markup.add(buttonC)
			markup.add(buttonD)
			markup.add(buttonA)
			markup.add(buttonE)
			markup.add(buttonF)
			logger.log('WS','BOT',f'Stop/hm: NAME: {str(call.message.from_user.first_name)} USER-ID: {str(call.message.from_user.id)} CHAT-ID: {str(call.message.chat.id)}')
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='ВЫ ТОЧНО ХОТИТЕ ОСТАНОВИТЬ БОТА?', parse_mode='html', reply_markup=markup)
		elif call.data == 'logger/hm':
			markup = types.InlineKeyboardMarkup()
			buttonA = types.InlineKeyboardButton(text='Да, точно!', callback_data='logger/delete')
			buttonB = types.InlineKeyboardButton(text='Нет', callback_data='bot_del_mess')
			buttonC = types.InlineKeyboardButton(text='Нет', callback_data='bot_del_mess')
			buttonD = types.InlineKeyboardButton(text='Нет', callback_data='bot_del_mess')
			buttonE = types.InlineKeyboardButton(text='Нет', callback_data='bot_del_mess')
			buttonF = types.InlineKeyboardButton(text='Нет', callback_data='bot_del_mess')
			markup.add(buttonB)
			markup.add(buttonC)
			markup.add(buttonD)
			markup.add(buttonA)
			markup.add(buttonE)
			markup.add(buttonF)
			logger.log('WS','BOT',f'logger/hm: NAME: {str(call.message.from_user.first_name)} USER-ID: {str(call.message.from_user.id)} CHAT-ID: {str(call.message.chat.id)}')
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='ВЫ ТОЧНО ХОТИТЕ УДАЛИТЬ ЛОГИ?', parse_mode='html', reply_markup=markup)
		elif call.data == 'bot_del_mess':
			bot.delete_message(call.message.chat.id, call.message.message_id)
			pass
		elif call.data == 'logger/delete':
			open(config.logfile, 'w').close()
			logger.log('WS','BOT',f'logger/delete: CHAT-ID: {str(call.message.chat.id)}')
			bot.delete_message(call.message.chat.id, call.message.message_id)
		elif call.data == 'stop/yes':
			bot.delete_message(call.message.chat.id, call.message.message_id)
			AMOGUSISSUS()
		elif call.data == 'logger/save':
			bot.delete_message(call.message.chat.id, call.message.message_id)
			bot.send_document(call.message.chat.id, open(config.logfile, 'rb'))
			logger.log('WS','BOT',f'logger/save: CHAT-ID: {str(call.message.chat.id)}')
@bot.message_handler(commands=['admin_panel'])
def ADMIN_PANEL(message):
	if message.chat.type == 'private':
		if message.chat.id in config.adminid:
			markup = types.InlineKeyboardMarkup()
			buttonA = types.InlineKeyboardButton(text='Логирование', callback_data='logger')
			buttonB = types.InlineKeyboardButton(text='Остановить бота', callback_data='stop/hm')
			markup.add(buttonA)
			markup.add(buttonB)
			bot.send_message(message.chat.id,'<b>Админка</b>', parse_mode='html',reply_markup=markup)
			logger.log('WS','BOT',f'admin_panel: NAME: {str(message.from_user.first_name)} USER-ID: {str(message.from_user.id)} CHAT-ID: {str(message.chat.id)}')
		else:
			bot.send_message(message.chat.id,f'<b>{str(message.from_user.first_name)}, вы НЕ админ\nваш id: {str(message.from_user.id)}</b>', parse_mode='html')
	else:
		if message.chat.id in config.adminid:
			bot.send_message(message.chat.id,f'<b>{str(message.from_user.first_name)}, вы админ\nНо вы не можете это отправить в группе</b>', parse_mode='html')
		else: 
			bot.send_message(message.chat.id,f'<b>{str(message.from_user.first_name)}, вы НЕ админ\nваш id: {str(message.from_user.id)}</b>', parse_mode='html')

bot.polling(none_stop=True)	