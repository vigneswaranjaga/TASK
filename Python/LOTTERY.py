"""
 1)Takes Users current date and time to say the Next Lottery draw 
 
"""
import datetime
import time
import calendar

today = datetime.date.today()
now = datetime.datetime.now()

day = time.strftime("%a")

print("\n\n******************** Welcome to Canadian National Lottery ********************\n")
print("Lottery draw takes place twice per week, on Tuesday and Sunday at 9.30 pm")

sunday = today + datetime.timedelta((calendar.SUNDAY-today.weekday()) % 7 )
tuesday = today + datetime.timedelta((calendar.TUESDAY-today.weekday()) % 7 )


if now.hour <= 21 and now.minute <= 29 and now.second <= 59 and day == 'Tue':
    print ("\nYour next Lottery draw is on : ", tuesday, "Tuesday at 9:30 PM")
else :
    print ("\nYour next Lottery draw is on : ", sunday, "Sunday at 9:30 PM")
    
print("\n\n******************** Wish You Good Luck ********************\n")


##################################################
"""
2)Get's User input both Date and Time. 
Condition1: Check's for the day (Sunday or Tuesday)
Condition2: If Sunday or Tuesday check's for the time < 9:30 pm
"""

userDate = input("\nEnter the date you want to purchase lottery(YYYY-MM-DD) : ")
d = datetime.datetime.strptime(userDate, '%Y-%m-%d').date()

userTime = input("\nEnter the Time you want to purchase lottery(HH:MM:SS) : ")
t = datetime.datetime.strptime(userTime,"%H:%M:%S").time()

fixedTime = ("21:30:00")
f = datetime.datetime.strptime(fixedTime,"%H:%M:%S").time()

class lotterDraw:
    def next_weekday(self, d, weekday):
        days_ahead = weekday - d.weekday()
        if days_ahead < 0:
            days_ahead += 7
        elif days_ahead == 0 and t < f:
            days_ahead = 0
        elif days_ahead == 0 and t > f:
            days_ahead += 7
        else:
            pass
        return d + datetime.timedelta(days_ahead)


draw = lotterDraw()
next_tuesday = draw.next_weekday(d, 1) # 0 = Monday, 1=Tuesday, 2=Wednesday...
next_sunday = draw.next_weekday(d, 6)


if next_sunday < next_tuesday:
    print("\nYour next lottery Draw is on : ",next_sunday,"9:30 PM")
    
else: 
    print("\nYour next lottery Draw is on : ",next_tuesday,"9:30 PM")
