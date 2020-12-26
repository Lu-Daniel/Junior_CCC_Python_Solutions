#J4_Favorite_Times
#2017

hours = 12
minutes = 0
D = int(input())
arith_seq = 0

for i in range(D):
    minutes += 1
    if minutes == 60:
        hours += 1
        minutes = 0
    if hours == 13:
        hours = 0
    minutez = str(minutes)
    hourz = str(hours)
    if hours >= 10:
        if minutes >= 10:
            minutes0 = int(minutez[0])
            minutes1 = int(minutez[1])
            hours0 = int(hourz[0])
            hours1 = int(hourz[1])
            if minutes1 - minutes0 == minutes0 - hours1:
                if minutes0 - hours1 == hours1 - hours0:
                    arith_seq += 1
    elif hours == 0:
        if minutes == 0:
            arith_seq += 1
    else:
        if minutes >= 10:
            minutes0 = int(minutez[0])
            minutes1 = int(minutez[1])
            hours0 = int(hourz[0])            
            if minutes1 - minutes0 == minutes0- hours0:
                arith_seq += 1 
print(arith_seq)