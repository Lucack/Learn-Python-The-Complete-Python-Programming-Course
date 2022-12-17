import time

    # time.time()
print(time.time())

def numbers(max):
    time1 = time.time()
    for i in range(0,max):
        print(i)
    time2 = time.time()
    print(str(time2-time1))

numbers(100)

    # .asctime()
print(time.asctime()) # current day rigth now
#0 = monday...
tup = (2000,10,15,8,45,12,6,0,0)
print(time.asctime(tup)) # retunr: Sun Oct 15 08:45:12 2000

    # .localtime()
t = time.localtime()
print(t) # time.struct_time(tm_year=2022, tm_mon=12, tm_mday=16, tm_hour=21, tm_min=4, tm_sec=48, tm_wday=4, tm_yday=350, tm_isdst=0)
year = t[0]

day = t[2]
month = t[1]
print(day,"/",month,"/",year) # 16 / 12 / 2022

    # .sleep() 
for i in range(0,5):
    print(i)
    time.sleep(1)


