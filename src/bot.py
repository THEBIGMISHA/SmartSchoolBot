#####IMPORT
import telebot				
import config				
import logger 				
import datacenter			
import os
import time				
from telebot import types
#####SETUP
os.system('cls|clear')
os.system('neofetch')
print('Starting...')
time.sleep(5)
logger.log('WS','BOT','WORKING')
bot = telebot.TeleBot(config.token)
#####CODE
@bot.message_handler(commands=['start', 'restart'])
def START(message):
	sticker=open(f"{config.media}Swelcome.webp", "rb")
	bot.send_sticker(message.chat.id, sticker)
	logger.log('W','BOT',f'start,restart: NAME: {str(message.from_user.first_name)} USER-ID: {str(message.from_user.id)} CHAT-ID: {str(message.chat.id)}')
	bot.send_message(message.chat.id,f'<b>Привет, {str(message.from_user.first_name)}!\n Я бот помощьник 8Б класса\n Все мои функии в кнопке "меню"</b>', parse_mode='html')
	if message.chat.type == 'private':
		bot.send_message(message.chat.id,'<b>↓↓↓↓↓</b>',parse_mode='html')
	bot.delete_message(message.chat.id, message.message_id)
@bot.message_handler(commands=['settings'])
def SETTINGS(message):
	logger.log('W','BOT',f'settings: NAME: {str(message.from_user.first_name)} USER-ID: {str(message.from_user.id)} CHAT-ID: {str(message.chat.id)}')
	bot.send_message(message.chat.id,'<b>СКОРО</b>',parse_mode='html')
	bot.delete_message(message.chat.id, message.message_id)
@bot.message_handler(commands=['qr'])
def QR(message):
	logger.log('W','BOT',f'qr: NAME: {str(message.from_user.first_name)} USER-ID: {str(message.from_user.id)} CHAT-ID: {str(message.chat.id)}')
	photo=open(f"{config.media}Pqr.jpg", "rb")
	bot.send_photo(message.chat.id,photo)
	time.sleep(20)
	bot.delete_message(message.chat.id, message.message_id)
@bot.message_handler(commands=['ping'])
def PING(message):
	logger.log('W','BOT',f'ping, test: NAME: {str(message.from_user.first_name)} USER-ID: {str(message.from_user.id)} CHAT-ID: {str(message.chat.id)}')
	bot.send_message(message.chat.id, '<b>БОТ РАБОТАЕТ!</b>', parse_mode='html')
	bot.delete_message(message.chat.id, message.message_id)
@bot.message_handler(commands=['admin'])
def ADMIN(message):
	photo=open(f"{config.media}Padmin.jpg", "rb")
	bot.send_photo(message.chat.id,photo)
	markup = types.InlineKeyboardMarkup()
	buttonA = types.InlineKeyboardButton(text='Написать', url='https://t.me/thebigmisha/')
	buttonB = types.InlineKeyboardButton(text='GitHub', url='https://GitHub.com/thebigmisha/')
	buttonC = types.InlineKeyboardButton(text='Spotify', url='https://open.spotify.com/user/31c4gv7qnyh5whjq2us5bsqcrpeq?si=EEi5AdIcTZy4DICXE4sNpw&utm_source=copy-link')
	buttonD = types.InlineKeyboardButton(text='Steam', url='https://steamcommunity.com/id/THEBIGMISHA/')
	markup.add(buttonA)
	markup.add(buttonB)
	markup.add(buttonC)
	markup.add(buttonD)
	logger.log('W','BOT',f'admin: NAME: {str(message.from_user.first_name)} USER-ID: {str(message.from_user.id)} CHAT-ID: {str(message.chat.id)}')
	bot.send_message(message.chat.id,'<b>Cот-сети главного админа:</b>',parse_mode='html', reply_markup=markup)
	bot.delete_message(message.chat.id, message.message_id)
@bot.message_handler(commands=['bug_report'])
def BUG_REPORT(m):
	if m.text == '/bug_report':
		bot.send_message(m.chat.id,f'<b>{m.from_user.first_name}, чтобы отправить баг репорт, нужно написать сообщение так\n \n/bug_report Расписание устарело!</b>',parse_mode='html')
	else: 
		bot.send_message(m.chat.id,f'<b>{m.from_user.first_name}, спасибо за репорт бага!</b>',parse_mode='html')
		bot.send_message(1641679319,f'<b>{m.from_user.first_name}, отправил репорт бага!\n \n {m.text}</b>',parse_mode='html')
		logger.log('WS','BOT',f'BUG_REPORT: NAME: {str(m.from_user.first_name)} USER-ID: {str(m.from_user.id)} CHAT-ID: {str(m.chat.id)}\nMESSAGE:\n{m.text}')
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
	bot.delete_message(message.chat.id, message.message_id)
@bot.callback_query_handler(func=lambda call: True)
def CALL(call):
	if call.message:
		#SCHEDULE
		if   call.data == 'schedule/1':
			bot.answer_callback_query(callback_query_id=call.id, show_alert=False,text="ГОТОВО")
			markup = types.InlineKeyboardMarkup()
			buttonA = types.InlineKeyboardButton(text='Прошлый день', callback_data='schedule/5')
			buttonB = types.InlineKeyboardButton(text='Следующий день', callback_data='schedule/2')
			markup.add(buttonA,buttonB)
			logger.log('W','BOT',f'schedule/1: CHAT-ID: {str(call.message.chat.id)}')
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=datacenter.schedule(1), parse_mode='html', reply_markup=markup)
		elif call.data == 'schedule/2':
			bot.answer_callback_query(callback_query_id=call.id, show_alert=False,text="ГОТОВО")			
			markup = types.InlineKeyboardMarkup()
			buttonA = types.InlineKeyboardButton(text='Прошлый день', callback_data='schedule/1')
			buttonB = types.InlineKeyboardButton(text='Следующий день', callback_data='schedule/3')
			markup.add(buttonA,buttonB)
			logger.log('W','BOT',f'schedule/2: CHAT-ID: {str(call.message.chat.id)}')
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=datacenter.schedule(2), parse_mode='html', reply_markup=markup)
		elif call.data == 'schedule/3':
			bot.answer_callback_query(callback_query_id=call.id, show_alert=False,text="ГОТОВО")
			markup = types.InlineKeyboardMarkup()
			buttonA = types.InlineKeyboardButton(text='Прошлый день', callback_data='schedule/2')
			buttonB = types.InlineKeyboardButton(text='Следующий день', callback_data='schedule/4')
			markup.add(buttonA,buttonB)
			logger.log('W','BOT',f'schedule/3: CHAT-ID: {str(call.message.chat.id)}')
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=datacenter.schedule(3), parse_mode='html', reply_markup=markup)
		elif call.data == 'schedule/4':
			bot.answer_callback_query(callback_query_id=call.id, show_alert=False,text="ГОТОВО")
			markup = types.InlineKeyboardMarkup()
			buttonA = types.InlineKeyboardButton(text='Прошлый день', callback_data='schedule/3')
			buttonB = types.InlineKeyboardButton(text='Следующий день', callback_data='schedule/5')
			markup.add(buttonA,buttonB)
			logger.log('W','BOT',f'schedule/4: CHAT-ID: {str(call.message.chat.id)}')
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=datacenter.schedule(4), parse_mode='html', reply_markup=markup)
		elif call.data == 'schedule/5':
			bot.answer_callback_query(callback_query_id=call.id, show_alert=False,text="ГОТОВО")
			markup = types.InlineKeyboardMarkup()
			buttonA = types.InlineKeyboardButton(text='Прошлый день', callback_data='schedule/4')
			buttonB = types.InlineKeyboardButton(text='Следующий день', callback_data='schedule/1')
			markup.add(buttonA,buttonB)
			logger.log('W','BOT',f'schedule/5: CHAT-ID: {str(call.message.chat.id)}')
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=datacenter.schedule(5), parse_mode='html', reply_markup=markup)
		#ADMIN_PANEL
		elif call.from_user.id in config.adminid:
			if call.data == 'logger':
				markup = types.InlineKeyboardMarkup()
				buttonA = types.InlineKeyboardButton(text='Запросить логи', callback_data='logger/save')
				buttonB = types.InlineKeyboardButton(text='Удалить логи', callback_data='logger/hm')
				markup.add(buttonA)
				markup.add(buttonB)
				logger.log('W','BOT',f'logger: CHAT-ID: {str(call.message.chat.id)}')
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
				logger.log('W','BOT',f'stop/hm: CHAT-ID: {str(call.message.chat.id)}')
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
				logger.log('W','BOT',f'logger/hm: CHAT-ID: {str(call.message.chat.id)}')
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='ВЫ ТОЧНО ХОТИТЕ УДАЛИТЬ ЛОГИ?', parse_mode='html', reply_markup=markup)
			elif call.data == 'bot_del_mess':
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False,text="ОТМЕНЕНО")
				bot.delete_message(call.message.chat.id, call.message.message_id)
				pass
			elif call.data == 'logger/delete':
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False,text="ЛОГИ УДАЛЕНЫ")
				open(config.logfile, 'w').close()
				logger.log('W','BOT',f'logger/delete: CHAT-ID: {str(call.message.chat.id)}')
				bot.delete_message(call.message.chat.id, call.message.message_id)
			elif call.data == 'stop/yes':
				logger.log('W','BOT',f'stop/bot: CHAT-ID: {str(call.message.chat.id)}')
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False,text="БОТ ОСТАНОВЛЕН")
				bot.delete_message(call.message.chat.id, call.message.message_id)
				bot.polling(non_stop=False)
			elif call.data == 'logger/save':
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False,text="ЛОГ ФАЙЛ ГОТОВ")
				bot.delete_message(call.message.chat.id, call.message.message_id)
				bot.send_document(call.message.chat.id, open(config.logfile, 'rb'))
				logger.log('W','BOT',f'logger/save: CHAT-ID: {str(call.message.chat.id)}')
		else:
			bot.answer_callback_query(callback_query_id=call.id, show_alert=False,text="ERROR")
@bot.message_handler(commands=['admin_panel'])
def ADMIN_PANEL(message):
	if message.from_user.id in config.adminid:
		markup = types.InlineKeyboardMarkup()
		buttonA = types.InlineKeyboardButton(text='Логирование', callback_data='logger')
		buttonB = types.InlineKeyboardButton(text='Остановить бота', callback_data='stop/hm')
		markup.add(buttonA)
		markup.add(buttonB)
		bot.send_message(message.chat.id,'<b>Админка</b>', parse_mode='html',reply_markup=markup)
		logger.log('WS','BOT',f'admin_panel: NAME: {str(message.from_user.first_name)} USER-ID: {str(message.from_user.id)} CHAT-ID: {str(message.chat.id)}')
	else:
		bot.send_message(message.chat.id,f'<b>{str(message.from_user.first_name)}, вы НЕ админ\nваш id: {str(message.from_user.id)}</b>', parse_mode='html')
	bot.delete_message(message.chat.id, message.message_id)	
@bot.message_handler(commands=['wifi'])
def WIFI(message):
	logger.log('W','BOT',f'wifi: NAME: {str(message.from_user.first_name)} USER-ID: {str(message.from_user.id)} CHAT-ID: {str(message.chat.id)}')
	photo=open(f"{config.media}Pwifi.png", "rb")
	bot.send_photo(message.chat.id,photo)
	bot.send_message(message.chat.id,f'<b>SSID: <i>{config.schoolWlanSSID}</i>\nPASS: {config.schoolWlanPASS}</b>',parse_mode='html')
	time.sleep(20)
	bot.delete_message(message.chat.id, message.message_id)
bot.polling(none_stop=True)	
