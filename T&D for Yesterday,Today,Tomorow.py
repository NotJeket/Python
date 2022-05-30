from datetime import datetime, timedelta

Today=datetime.now()
Yesterday=Today - timedelta(1)
Tomorow=Today + timedelta(1)

print("Yesterday was=", Yesterday.strftime('%d-%m-%Y'))
print("Today is=", Today.strftime('%d-%m-%Y'))
print("Tomorow will be=", Tomorow.strftime('%d-%m-%Y'))