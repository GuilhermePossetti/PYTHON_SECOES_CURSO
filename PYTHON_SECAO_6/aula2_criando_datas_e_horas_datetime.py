"""
Criando datas com módulos datetime
datetime (ano, mês, dia)
datetime (ano, mês, dia, horas, minutos, segundos)
datetime.strptime ('DATA', 'FORMATO')
datetime.now()
https://pt.wikipedia.org/wiki/Era_unix
datetime.fromtimestamp(Unix Timestamp)
https://docs.python.org/3/library/datetime.html
Para timezones
https://en.wikipedia.org/wiki/List_of_tz_databese_time_zones
Instalano o pytz
pip install pytz types-pytz
"""

from datetime import datetime
from pytz import timezone
# data_str_data = '2026-06-10 10:07:28'
# data_str_fmt = '%Y-%m-%d %H:%M:%S'
data = datetime.now()
print(data.timestamp())
print(datetime.fromtimestamp(1781111869))
# # data = datetime(2026, 6, 10, 10,7,28 )
# data = datetime.strptime(data_str_data, data_str_fmt)
# print(data)
data = datetime(2026, 6, 10, 10,7,28, tzinfo=timezone('Asia/Tokyo'))
# data e hora exata do computador real

# data = datetime.now(timezone('Asia/Tokyo'))
# print(data)
