import timetable_db
times = timetable_db.time
tab = timetable_db.table
day = timetable_db.days
print(f"""|------------|  -----------  |   -----------  |   -----------  |   -----------  |   -----------  |   -----------  |   -----------  |   -----------  |   -----------  |
|    Day     |  {times[0]}  |   {times[1]}  |   {times[2]}  |   {times[3]}  |   {times[4]}  |   {times[5]}  |   {times[6]}  |   {times[7]}  |   {times[8]}  |
|------------|  -----------  |   -----------  |   -----------  |   -----------  |   -----------  |   -----------  |   -----------  |   -----------  |   -----------  |
|  Monday    |{tab[day[0]][times[0]]}|{tab[day[0]][times[1]]}|{tab[day[0]][times[2]]}|{tab[day[0]][times[3]]}|{tab[day[0]][times[4]]}|{tab[day[0]][times[5]]}|{tab[day[0]][times[6]]}|{tab[day[0]][times[7]]}|{tab[day[0]][times[8]]}|                      
|------------|  -----------  |   -----------  |   -----------  |   -----------  |   -----------  |   -----------  |   -----------  |   -----------  |   -----------  |
|  Tuesday   |{tab[day[1]][times[0]]}|{tab[day[1]][times[1]]}|{tab[day[1]][times[2]]}|{tab[day[1]][times[3]]}|{tab[day[1]][times[4]]}|{tab[day[1]][times[5]]}|{tab[day[1]][times[6]]}|{tab[day[1]][times[7]]}|{tab[day[1]][times[8]]}|
|------------|  -----------  |   -----------  |   -----------  |   -----------  |   -----------  |   -----------  |   -----------  |   -----------  |   -----------  |
|  Wednesday |{tab[day[2]][times[0]]}|{tab[day[2]][times[1]]}|{tab[day[2]][times[2]]}|{tab[day[2]][times[3]]}|{tab[day[2]][times[4]]}|{tab[day[2]][times[5]]}|{tab[day[2]][times[6]]}|{tab[day[2]][times[7]]}|{tab[day[2]][times[8]]}|
|------------|  -----------  |   -----------  |   -----------  |   -----------  |   -----------  |   -----------  |   -----------  |   -----------  |   -----------  |
|  Thursday  |{tab[day[3]][times[0]]}|{tab[day[3]][times[1]]}|{tab[day[3]][times[2]]}|{tab[day[3]][times[3]]}|{tab[day[3]][times[4]]}|{tab[day[3]][times[5]]}|{tab[day[3]][times[6]]}|{tab[day[3]][times[7]]}|{tab[day[3]][times[8]]}|
|------------|  -----------  |   -----------  |   -----------  |   -----------  |   -----------  |   -----------  |   -----------  |   -----------  |   -----------  |
|  Friday    |{tab[day[4]][times[0]]}|{tab[day[4]][times[1]]}|{tab[day[4]][times[2]]}|{tab[day[4]][times[3]]}|{tab[day[4]][times[4]]}|{tab[day[4]][times[5]]}|{tab[day[4]][times[6]]}|{tab[day[4]][times[7]]}|{tab[day[4]][times[8]]}|
|------------|  -----------  |   -----------  |   -----------  |   -----------  |   -----------  |   -----------  |   -----------  |   -----------  |   -----------  |
|  Saturday  |{tab[day[5]][times[0]]}|{tab[day[5]][times[1]]}|{tab[day[5]][times[2]]}|{tab[day[5]][times[3]]}|{tab[day[5]][times[4]]}|{tab[day[5]][times[5]]}|{tab[day[5]][times[6]]}|{tab[day[5]][times[7]]}|{tab[day[5]][times[8]]}|
|------------|  -----------  |   -----------  |   -----------  |   -----------  |   -----------  |   -----------  |   -----------  |   -----------  |   -----------  |

""")