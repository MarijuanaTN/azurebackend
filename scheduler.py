from IntraDay.views import update_forex_data
import time

interval=300
while (True):
    update_forex_data()
    time.sleep(interval)
