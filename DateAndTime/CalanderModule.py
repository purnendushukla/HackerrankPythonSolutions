
# from datetime module being imported

import datetime
dt = raw_input()
month, day, year = (int(x) for x in dt.split(' '))    
ans = datetime.date(year, month, day)
print ans.strftime("%A").upper()

# from calendar module
# calander module is having much simpler approach

#import calendar as ca
#d,m,y = ([int(i) for i in raw_input().split(' ')])
#a = ca.weekday(y,d,m)
#n = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']
#print n[a]
