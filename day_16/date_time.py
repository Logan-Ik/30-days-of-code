from datetime import datetime

#1
now =datetime.now()
print(now)

#2
day = now.day                   # 8
month = now.month               # 7
year = now.year                 # 2021
hour = now.hour                 # 7
minute = now.minute             # 38
second = now.second
print(f'{month}/{day}/{year}, {hour}:{minute}:{second}')

#3
new_year = datetime(2019, 12, 5)

#4
diffrence =now - new_year 
print(diffrence)

#5
long_ago = datetime(1970,1,1)
Eons_pass = now - long_ago
print(Eons_pass)

#6
"""
Ok I thought about it :)
"""