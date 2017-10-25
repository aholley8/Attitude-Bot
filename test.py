from datetime import datetime, timedelta
# DATETIME TEST FILE

now = datetime.now()
print(now)

#print(now.strftime("%B %d, %Y"))
print(now.weekday())

#print(str(now.time()).split('.',2)[0])

if (now.weekday()<3) and (now.hour<20):
    print("RAID NIGHT!")
    print('Time until raid: ' + str(datetime(now.year, now.month, now.day, 20) - now).split('.',2)[0])    



#--------------------------------------------------------------------------------
#start = Mon july 10 2017 @ 7.30pm EST
#start = datetime(2017, 7, 10, 19, 30)
#d1 = datetime(2017, 3, 28)
#d2 = datetime.today()
#tuesday1 = (d1 - timedelta(days=d1.weekday()-1))
#tuesday2 = (d2 - timedelta(days=d2.weekday()))
#currentAffix = affixes[floor(((tuesday2 - tuesday1).days / 7) % 12)]
#nextAffix = affixes[floor(((tuesday2 - tuesday1).days / 7) % 12) + 1]

#--------------------------------------------------------------------------------
# Check to see if an invasion is up or not
#loop = True
#enabled = True
#while loop:
#    if enabled:
#        start = start + timedelta(hours=6)
#        if now < start: # Exits loop, invasion is happening
#            loop = False
#            nexttime = start - now
#            print("There is an invasion active now!\nTime left: " + str(nexttime).split('.',2)[0])
#        else:
#            enabled = False
#    else:
#        start = start + timedelta(hours=12, minutes=30)
#        if now < start: # Exits loop, invasion not happening
#            loop = False
#            nexttime = start-now
#            print("There is no invasion active.\nTime until next invasion: " + str(nexttime).split('.',2)[0])
#            
#        else:
#            enabled = True


