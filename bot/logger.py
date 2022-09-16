#####ИМПОРТ-
import os
import datetime
import config
def work(func,command,message,id):
	logfile=open(config.logfile, 'a', encoding='utf-8')
	date = datetime.datetime.today().strftime("[%d.%m.%Y|%H:%M:%S]")
	#Write
	if 	 func=='W':	#Write
		logfile.write(f'{date}  {command}:  {message}  {id}\n')
		pass
	elif func=='WS':	#Write&SendConsole
		logfile.write(f'{date}  {command}:  {message}  {id}\n')
		print(f'{date}  {command}:  {message}\n')
	else:				#Error
		logfile.write(f'{date}  Logger:  404\n')
		print(f'{date}  Logger:  404\n')
	logfile.close()