import datetime
import time
import calendar

today = datetime.date.today()
now = datetime.datetime.now()

day = time.strftime("%a")

print("\n\n\t*** Welcome to Canadian National Lottery ***\n")
print("Lottery draw takes place twice per week, on Tuesday and Sunday at 9.30 pm")

sunday = today + datetime.timedelta((calendar.SUNDAY-today.weekday()) % 7 )
tuesday = today + datetime.timedelta((calendar.TUESDAY-today.weekday()) % 7 )


if now.hour <= 21 and now.minute <= 29 and now.second <= 59 and day == 'Tue':
    print ("\n\tYour next Lottery draw is on : ", tuesday, "Tuesday at 9:30 PM")
else :
    print ("\n\tYour next Lottery draw is on : ", sunday, "Sunday at 9:30 PM")
    
print("\n\n\t************************* Wish You Good Luck **********************************\n")


userDate = input("\nEnter the date you want to purchase lottery(YYYY-MM-DD) : ")#format '2013-05-27'
d = datetime.datetime.strptime(userDate, '%Y-%m-%d').date()

userTime = input("\nEnter the Time you want to purchase lottery(HH:MM:SS) : ")
t = datetime.datetime.strptime(userTime,"%H:%M:%S").time()

fixedTime = ("21:30:00")
f = datetime.datetime.strptime(fixedTime,"%H:%M:%S").time()

class lotterDraw:
    def next_weekday(self, d, weekday):
        days_ahead = weekday - d.weekday()
        if days_ahead < 0 and t < f:
            days_ahead += 7
        elif days_ahead == 0:
            if t < f:
                days_ahead = 0
            else:
                days_ahead +=7
       
        return d + datetime.timedelta(days_ahead)


draw = lotterDraw()
next_tuesday = draw.next_weekday(d, 1)
 # 0 = Monday, 1=Tuesday, 2=Wednesday...
print(next_tuesday)
next_sunday = draw.next_weekday(d, 6)
print(next_sunday)

if next_sunday < next_tuesday:
    print("your next lottery Draw is on : ",next_sunday,"9:30 PM")
        #print(" Time", f )
    
else: 
    print("your next lottery Draw is on : ",next_tuesday,"9:30 PM")
    #print(" Time", f )
