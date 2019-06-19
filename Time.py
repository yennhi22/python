import time;
import calendar

# bắt thời gian hiện tại
localtime = time.localtime(time.time())
print ("Local current time :", localtime)
#
localtime = time.asctime( time.localtime(time.time()) )
print ("Local current time :", localtime)
# lịch hàng năm và hàng tháng
cal = calendar.month(2008, 1)
print ("Here is the calendar:")
print (cal)
#__________
print ("time.altzone %d " % time.altzone)
