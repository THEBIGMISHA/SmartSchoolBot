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
time.sleep(1)
logger.log('WS','BOT','WORKING')
bot = telebot.TeleBot(config.token)
#####CODE
@bot.message_handler(commands=['start', 'restart'])
def START(message):
	sticker=open(f"{config.media}/Swelcome.webp", "rb")
	bot.send_sticker(message.chat.id, sticker)
	logger.log('W','BOT',f'start,restart: NAME: {str(message.from_user.first_name)} USER-ID: {str(message.from_user.id)} CHAT-ID: {str(message.chat.id)}')
	bot.send_message(message.chat.id,f'<b>Привет, {str(message.from_user.first_name)}!\n Я бот помощьник 8Б класса\n Все мои функии в кнопке "меню"</b>', parse_mode='html')
	if message.chat.type == 'private':
		bot.send_message(message.chat.id,'<b>↓↓↓↓↓</b>',parse_mode='html')
@bot.message_handler(commands=['settings'])
def SETTINGS(message):
	logger.log('W','BOT',f'settings: NAME: {str(message.from_user.first_name)} USER-ID: {str(message.from_user.id)} CHAT-ID: {str(message.chat.id)}')
	bot.send_message(message.chat.id,'<b>СКОРО</b>',parse_mode='html')
	bot.delete_message(message.chat.id, message.message_id)
@bot.message_handler(commands=['qr'])
def QR(message):
	logger.log('W','BOT',f'qr: NAME: {str(message.from_user.first_name)} USER-ID: {str(message.from_user.id)} CHAT-ID: {str(message.chat.id)}')
	photo=open(f"{config.media}/Pqr.jpg", "rb")
	bot.send_photo(message.chat.id,photo)
	bot.delete_message(message.chat.id, message.message_id)
@bot.message_handler(commands=['ping'])
def PING(message):
	logger.log('W','BOT',f'ping, test: NAME: {str(message.from_user.first_name)} USER-ID: {str(message.from_user.id)} CHAT-ID: {str(message.chat.id)}')
	bot.send_message(message.chat.id, '<b>БОТ РАБОТАЕТ!</b>', parse_mode='html')
	bot.delete_message(message.chat.id, message.message_id)
@bot.message_handler(commands=['admin'])
def ADMIN(message):
	markup = types.InlineKeyboardMarkup()
	buttonA = types.InlineKeyboardButton(text='Telegram', url='https://t.me/thebigmisha/')
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
		#WI-FI
		elif call.data == 'wifi/text':	
			markup = types.InlineKeyboardMarkup()
			buttonA = types.InlineKeyboardButton(text='Принять и продолжить', callback_data='wifi/ok')
			markup.add(buttonA)
			bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text=config.schoolWlanTEXT, parse_mode='html', reply_markup=markup)
			bot.answer_callback_query(callback_query_id=call.id, show_alert=False,text='Готово')
		elif call.data == 'wifi/ok':
			logger.log('W','BOT',f'wifi/ok: CHAT-ID: {str(call.message.chat.id)}')			
			bot.delete_message(chat_id=call.message.chat.id, message_id=call.message.message_id)
			bot.answer_callback_query(callback_query_id=call.id, show_alert=True,text=f"WI-FI_1:\n    SSID: {config.schoolWlanSSID}\n    PASS: {config.schoolWlanPASS}")
		#ADMIN_PANEL
		elif call.from_user.id in config.adminid:
			if call.data == 'logger':
				markup = types.InlineKeyboardMarkup()
				buttonA = types.InlineKeyboardButton(text='Download logs', callback_data='logger/save')
				buttonB = types.InlineKeyboardButton(text='Clear logs', callback_data='logger/delete')
				markup.add(buttonA)
				markup.add(buttonB)
				logger.log('W','BOT',f'logger: CHAT-ID: {str(call.message.chat.id)}')
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='Logger', parse_mode='html', reply_markup=markup)
			elif call.data == 'logger/delete':
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False,text="Logs cleared")
				open(config.log, 'w').close()
				logger.log('W','BOT',f'logger/delete: CHAT-ID: {str(call.message.chat.id)}')
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='Logs cleared')
			elif call.data == 'logger/save':
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False,text="done")
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='Logs')
				bot.send_document(call.message.chat.id, open(config.log, 'rb'))
				logger.log('W','BOT',f'logger/save: CHAT-ID: {str(call.message.chat.id)}')
			elif call.data == 'power':
				markup = types.InlineKeyboardMarkup()
				buttonA = types.InlineKeyboardButton(text='Reboot', callback_data='reboot')
				buttonB = types.InlineKeyboardButton(text='PowerOff', callback_data='poweroff')
				buttonC = types.InlineKeyboardButton(text='PowerOff [10 min]', callback_data='powerofft')
				buttonD = types.InlineKeyboardButton(text='MEGAPowerOff', callback_data='halt')				
				markup.add(buttonA)
				markup.add(buttonB)
				markup.add(buttonC)
				markup.add(buttonD)
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='Power:', parse_mode='html', reply_markup=markup)
				logger.log('W','BOT',f'power: CHAT-ID: {str(call.message.chat.id)}')
			elif call.data == 'reboot':
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False,text="Reboot")
				logger.log('W','BOT',f'power/reboot: CHAT-ID: {str(call.message.chat.id)}')
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='Reboot')
				os.system('reboot')
			elif call.data == 'poweroff':
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False,text="PowerOff")
				logger.log('W','BOT',f'power/poweroff: CHAT-ID: {str(call.message.chat.id)}')
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='PowerOff')
				os.system('poweroff')
			elif call.data == 'halt':
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False,text="Halt")
				logger.log('W','BOT',f'power/halt: CHAT-ID: {str(call.message.chat.id)}')
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='Halt')
				os.system('halt')
			elif call.data == 'powerofft':
				bot.answer_callback_query(callback_query_id=call.id, show_alert=False,text="Poweroff: 30min")
				logger.log('W','BOT',f'power/30min: CHAT-ID: {str(call.message.chat.id)}')
				bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,text='Poweroff: 30min')
				os.system('shutdown -h +30')
		else:
			bot.answer_callback_query(callback_query_id=call.id, show_alert=False,text="ERROR")
@bot.message_handler(commands=['admin_panel'])
def ADMIN_PANEL(message):
	if message.from_user.id in config.adminid:
		markup = types.InlineKeyboardMarkup()
		buttonA = types.InlineKeyboardButton(text='Logger', callback_data='logger')
		buttonB = types.InlineKeyboardButton(text='Power', callback_data='power')
		markup.add(buttonA)
		markup.add(buttonB)
		bot.send_message(message.chat.id,'<b>Admin_panel:</b>', parse_mode='html',reply_markup=markup)
		logger.log('WS','BOT',f'admin_panel: NAME: {str(message.from_user.first_name)} USER-ID: {str(message.from_user.id)} CHAT-ID: {str(message.chat.id)}')
	else:
		bot.send_message(message.chat.id,f'<b>{str(message.from_user.first_name)}, вы НЕ админ\nid: </b>{str(message.from_user.id)}', parse_mode='html')
	bot.delete_message(message.chat.id, message.message_id)	
@bot.message_handler(commands=['wifi'])
def WIFI(message):
	markup = types.InlineKeyboardMarkup()
	buttonA = types.InlineKeyboardButton(text='Прочитать', callback_data='wifi/text')
	buttonB = types.InlineKeyboardButton(text='Принять и продолжить', callback_data='wifi/ok')
	markup.add(buttonA)
	markup.add(buttonB)
	bot.send_message(message.chat.id,'Но перед тем как получить пароль вы должны знать что:\n\nПри нажатии кнопки "Принять и продолжить" вы соглашаетесь на пользовательское соглашением', parse_mode='html',reply_markup=markup)
	bot.delete_message(message.chat.id, message.message_id)	
bot.polling(none_stop=True)	
