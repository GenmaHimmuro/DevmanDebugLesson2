import os

from weather_sdk import get_new_event, SMSServer

token_forecast = os.environ['FORECAST_TOKEN']
town_title = 'Курск'
token_sms = os.environ['SMS_TOKEN']
server = SMSServer(token_sms)
new_event = get_new_event(token_forecast, town_title)
event_date = new_event.get_date()
event_time = new_event.get_time()
event_area = new_event.get_area()
phenomenon_description = new_event.get_phenomenon()

sms_template = '''{1}: {2} {3} {4} ожидается {0}. Будьте внимательны и осторожны.'''

sms_message = sms_template.format(
    phenomenon_description,
    town_title,
    event_time,
    event_date,
    event_area,
)

server.send(sms_message)


# Гипотеза 1: В переменной нет прогноза погоды для Курска
# Способ проверки: Выведу переменную new_event
# Код для проверки: print(new_event)
# Установленный факт: результат команды print(new_event): Регион: Погода: 
# Вывод: не выводит название города

# Гипотеза 2.1: town_title на самом деле пуста
# Способ проверки: выведу town_title
# Код для проверки: print(town_title)
# Установленный факт: результат команды: Курск
# Вывод: town_title не пуста

# Гипотеза 2.2: В town_title не название города
# Способ проверки: выведу town_title
# Код для проверки: print(town_title)
# Установленный факт: результат команды: Курск
# Вывод: в town_title название города

# Гипотеза 3: Переменная token на самом деле пуста
# Способ проверки: выведу token
# Код для проверки: print(token)
# Установленный факт: результат команды: None
# Вывод: token пуста

# Гипотеза 4: Может, `token` всё ещё пуст?
# Способ проверки: выведу token
# Код для проверки: print(token)
# Установленный факт: выводит aGVsbG8gY3J5cHRvIGVudHVzaWFzdCA7KQ==
# Вывод: обе переменные с одинаковым названием token = os.environ['FORECAST_TOKEN']
# token = os.environ['SMS_TOKEN']

# Гипотеза 5: Переменные `event_time`,`event_date`,`event_area`,`phenomenon_description`, пуста/в ней не время,дата,место,описание погодного явления
# Способ проверки: выеду данные переменные
# Код для проверки: print('phenomenon_description',phenomenon_description,'event_time',event_time,"event_date",event_date,'event_area',event_area)
# Установленный факт: результат команды: print('phenomenon_description',phenomenon_description,'event_time',event_time,"event_date",event_date,'event_area',event_area)
# Вывод: переменные пусты, данные соответсвуют их обозначениям

# Гипотеза 6: Опечатка в названиях переменных
# Способ проверки: использование интерфейса Repl
# Код для проверки: -
# Установленный факт: при выделении каждой переменной выделяется её копия в коде
# Вывод: опечатки нет

# Гипотеза 7: ошибка в методе format
# Способ проверки: замена вместо названий переменных на значения индекса
# Код для проверки: sms_template = '''{1}: {2} {3} {4} ожидается {0}. Будьте внимательны и осторожны.'''
# Установленный факт: выполнение через значения индекса переменных корректно
# Вывод: ошибка в методе