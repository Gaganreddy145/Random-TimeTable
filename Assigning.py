import timetable_db
import random
def random_time():
    return random.choice(timetable_db.time)
def random_day():
    return random.choice(timetable_db.days)
def random_time_lab():
    while(True):
        randtime = random_time()
        if randtime == "03.00-04.00" or randtime == "04.00-05.00" or randtime == "11.00-11.15" or randtime == "01.15-02.00":
            randtime = random_time()
        else:
            break
    return randtime
def digit_func(digit):
    if digit == 1.15:
        digit = 2.00
    elif digit == 11.00:
        digit = 11.15
    return digit
def check_digit_start(digit):
    if digit == 9.00 or digit == 1.15 or digit == 2.00 or digit == 3.00 or digit == 4.00 or digit == 5.00:
        return "0"+str(digit)
    return digit
def check_last_time(randtime):
    if randtime[4:5] == '-' and len(randtime[5:]) == 4:
        slicetime = randtime[:4]
        slicetime+="0"
        slicetime = slicetime + "-" + randtime[5:] + "0"
        return slicetime
    if randtime[4:5] == '-':
        slicetime = randtime[:5]
        slicetime += "0"
        return slicetime
    if len(randtime[5:]) == 4:
        slicetime = randtime[5:]+"0"
        randtime = randtime[:6] + slicetime
        return randtime
    return randtime
def check_empty_slot(randday,randtime):
    while (True):
        if timetable_db.table[randday][randtime] != "":
            randtime = random_time()
            randday = random_day()
        else:
            break
    return (randtime,randday)
def check_empty_slot_count(table):
    count=0
    for i in table:
        for j in table[i]:
            if table[i][j] == "":
                count += 1
    return count
removeday=[]
for i in timetable_db.labs:          # Assigning labs
    randtime = random_time_lab()
    randday = random_day()
    while(True):
        if timetable_db.table[randday][randtime] != "":
            randtime = random_time_lab()
            randday = random_day()
        else:
            break
    while(True):
        if randday in removeday:
            randday = random_day()
        else:
            break
    removeday.append(randday)
    print("****   "+i+"   ****")
    timetable_db.table[randday][randtime] = i
    print(randday,randtime)
    digit = float(randtime[6:])
    digit = digit_func(digit)
    if digit == 12.15:
        digit2 = 1.15
    else:
        digit2 = digit + 1
    digit = check_digit_start(digit)
    digit2 = check_digit_start(digit2)
    randtime = str(digit)+"-"+str(digit2)
    randtime = check_last_time(randtime)
    timetable_db.table[randday][randtime] = i
    print(randday, randtime)
    digit2 = digit_func(float(digit2))
    if float(digit2) == 12.15:
        digit3 = 1.15
    else:
        digit3 = float(digit2) + 1
    digit2 = check_digit_start(digit2)
    digit3 = check_digit_start(digit3)
    randtime = str(digit2)+"-"+str(digit3)
    randtime = check_last_time(randtime)
    timetable_db.table[randday][randtime] = i
    print(randday, randtime)
for sub in timetable_db.subjects:          # Assigning subjects
    print("****   "+sub+"  ****")
    for i in range(4):
        randday = random_day()
        randtime = random_time()
        tup = check_empty_slot(randday,randtime)
        randtime = tup[0]
        randday = tup[1]
        print(randday,randtime)
        timetable_db.table[randday][randtime] = sub
for other in timetable_db.other_activities:       # Assigning other activities
    print("****   "+other+"   ****")
    randday = random_day()
    randtime = random_time()
    tup = check_empty_slot(randday,randtime)
    randtime = tup[0]
    randday = tup[1]
    print(randday,randtime)
    timetable_db.table[randday][randtime] = other




