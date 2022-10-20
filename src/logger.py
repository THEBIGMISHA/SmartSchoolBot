#####IMPORT
import os
import datetime
import config
#####CODE
def log(func,command,message):
	logfile=open(config.log, 'a', encoding='utf-8')
	date = datetime.datetime.today().strftime("[%d.%m.%Y|%H:%M:%S]")
	#Write
	if 	 func=='W':		#Write
		logfile.write(f'{date}  {command}:  [{message}]\n')
		pass
	elif func=='WS':	#Write&SendConsole
		logfile.write(f'{date}  {command}:  [{message}]\n')
		print(f'{date}  {command}:  [{message}]')
	else:				#Error
		logfile.write(f'{date}  Logger: "W" or "WS" \n')
		print(f'{date}  Logger: "W" or "WS"')
	logfile.close()
