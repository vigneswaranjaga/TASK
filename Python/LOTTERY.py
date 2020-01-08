'''
from datetime import datetime
from calendar import calendar

current_date_time = datetime.now()
current_day = datetime.today()
print(current_date_time)
print(current_day)
'''
'''
from datetime import date
today = date.today()
# dd/mm/YY
d1 = today.strftime("%d/%m/%Y")
print("d1 =", d1)
'''
"""
# Python program to Find day of 
# the week for a given date 
import calendar 

print("******************** WELCOME TO LOTTERY**************************")
print(
user_choice = int (input("Do you wish to buy a lottery ticket? if so click 1 : "))
if user_choice ==1:
    
def findDay(date): 
	day, month, year = (int(i) for i in date.split('/'))	 
	dayNumber = calendar.weekday(year, month, day) 
	days =["Monday", "Tuesday", "Wednesday", "Thursday", 
						"Friday", "Saturday", "Sunday"] 
	return (days[dayNumber]) 

# Driver program 
date = '03 02 2019'
print(findDay(date)) 

"""

'''
##
# Python's program to get last and coming Monday
 
import datetime
 
today = datetime.date.today()
last_monday = today - datetime.timedelta(days=today.weekday()+1)
coming_monday = today + datetime.timedelta(days=-today.weekday()+6, weeks=1)
print("Today:", today)
print("Last Monday:", last_monday)
print("Coming Monday:", coming_monday)
'''
"""
from datetime import date

def satandsun(input):
    d = input.toordinal()
    last = d + 6
    sunday = last + (last % 7)
    #saturday = sunday + 6
    print(date.fromordinal(sunday))
    #print(date.fromordinal(saturday))


satandsun(date(2020,1,7))
"""
"""
import datetime
today = datetime.date.today()
today
datetime.date(2013, 8, 13)
idx = (today.weekday() + 1) % 7 # MON = 0, SUN = 6 -> SUN = 0 .. SAT = 6
idx

sun = today + datetime.timedelta(7+idx)
sat = today + datetime.timedelta(7+idx-6)
print("Last Sunday was {:%m/%d/%Y} and last Saturday was {:%m/%d/%Y}".format(sun, sat))
#print(Last Sunday was 08/04/2013 and last Saturday was 08/10/2013)

"""
"""
# Prints current date and time
from datetime import datetime
from calendar import calendar 

date = datetime.today()
print("******************** WELCOME TO LOTTERY**************************")
user_choice = int (input("Do you wish to buy a lottery ticket? if so click 1 : "))
if user_choice == 1:
    print("Today date and time is ",date)
"""
"""
import pendulum

pendulum.now()

#DateTime(2019, 4, 24, 17, 28, 13, 776007, tzinfo=Timezone('America/Los_Angeles'))
pendulum.now().next(pendulum.SATURDAY)
#Out[3]: DateTime(2019, 4, 27, 0, 0, 0, tzinfo=Timezone('America/Los_Angeles'))
pendulum.now().next(pendulum.SATURDAY).strftime('%Y-%m-%d')


"""
import datetime
import calendar
today = datetime.date.today()#reference point.
time = datetime.datetime.now()
sunday = today + datetime.timedelta((calendar.SUNDAY-today.weekday()) % 7 )
tuesday = today + datetime.timedelta((calendar.TUESDAY-today.weekday()) % 7 )
Crt_time = time. strftime("%H:%M:%S")
print("Current Time =",Crt_time)
#print("current date and time ",time)
print ("Next Sunday ",sunday)
print ("Next Tuesday ",tuesday)

#if 
#if Crt_time <= 09:29:59 and 

#saturday.weekday()
#saturday = today + datetime.timedelta((5-today.weekday()) % 7 )




























