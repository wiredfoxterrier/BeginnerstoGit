import os 
from datetime import *

#BASIC DATE TIME PROGRAMS IN PYTHON


datetime_object = datetime.now()
print(datetime_object)

date_object = date.today()
print(date_object)

a = time(12,34,56,7854)
print("a = ",a)

a = datetime(2017,11,28,23,55,59,342348)
print("a = ",a)


date1 = date(2020,10,17)
date2 = date(2020,12,24)
num_days = date2-date1
print("Number of weeks ",num_days)
