'''datetime'''

from datetime import datetime
now = datetime.now()
print(now)
print(now.strftime('%Y-%m-%d %H:%M:%S'))
print(type(now))