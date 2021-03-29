from datetime import datetime
from datetime import timedelta

tomorrow = (datetime.now() + timedelta(days=1) ).strftime('%Y-%m-%d')
yesterday = (datetime.now() + timedelta(days=-1) ).strftime('%Y-%m-%d')

print('<<[[' + yesterday + ']]|[[' + tomorrow + ']]>>')

