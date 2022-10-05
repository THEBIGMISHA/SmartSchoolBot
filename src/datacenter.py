#####IMPORT-
import config
import logger
#####CODE-
def schedule(day):
	if   day ==1 or day=='1':
		return('''
		<b>ПОНЕДЕЛЬНИК
		1 |09:30  -  10:10| *О важном
		2 |10:15  -  10:55| География
		3 |11:00  -  11:40| Русский язык
		4 |11:45  -  12:25| Английский язык
		5 |12:40  -  13:20| Алгебра
		6 |13:35  -  14:15| История
		7 |14:20  -  15:00| Черчение
		8 |00:00  -  00:00| *Захожая.О.В
		9 |00:00  -  00:00| -
		есть ошибка? напиши /bug_report
		</b>''')
	elif day ==2 or day=='2':
		return('''
		<b>ВТОРНИК
		1 |09:30  -  10:10| Литература
		2 |10:15  -  10:55| Биология
		3 |11:00  -  11:40|	Химия
		4 |11:45  -  12:25| Физика
		5 |12:40  -  13:20| Алгебра
		6 |13:35  -  14:15| Физкультура
		7 |14:20  -  15:00| Геометрия
		8 |00:00  -  00:00| -
		9 |00:00  -  00:00| -
		есть ошибка? напиши /bug_report
		</b>''')
	elif day ==3 or day=='3':
		return('''
		<b>СРЕДА
		1 |09:30  -  10:10| Алгебра
		2 |10:15  -  10:55| Информатика
		3 |11:00  -  11:40|	Геометрия
		4 |11:45  -  12:25| Русский язык
		5 |12:40  -  13:20| Английский язык
		6 |13:35  -  14:15| География
		7 |14:20  -  15:00| *Хромнова.С.Ф
		8 |00:00  -  00:00| *Калашникова.Н.Б
		9 |00:00  -  00:00| -
		есть ошибка? напиши /bug_report
		</b>''')
	elif day ==4 or day=='4':
		return('''
		<b>ЧЕТВЕРГ
		1 |09:30  -  10:10| Музыка
		2 |10:15  -  10:55| Биология
		3 |11:00  -  11:40|	Литература
		4 |11:45  -  12:25| Физика
		5 |12:40  -  13:20| Геометрия
		6 |13:35  -  14:15| Обществознание
		7 |14:20  -  15:00| Физкультура
		8 |00:00  -  00:00| *Бащев.А.С
		9 |00:00  -  00:00| *Леонтьева.М.И
		есть ошибка? напиши /bug_report
		</b>''')
	elif day ==5 or day=='5':
		return('''
		<b>ПЯТНИЦА
		1 |09:30  -  10:10| История
		2 |10:15  -  10:55| Химия
		3 |11:00  -  11:40|	Русский язык
		4 |11:45  -  12:25| Физкультура
		5 |12:40  -  13:20| ИЗО
		6 |13:35  -  14:15| ОБЖ
		7 |14:20  -  15:00| Английский язык
		8 |00:00  -  00:00| *Ящерицын.А.Л
		9 |00:00  -  00:00| -
		есть ошибка? напиши /bug_report
		</b>''')
	else:
		logger.log('WS','datacenter/scheldule','404: '+str(day)+' NOT FOUND!')
		return(f'/datacenter/schedule/'+str(day)+' NOT FOUND!')