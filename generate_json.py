import datetime
import json
import random
import os.path
import pandas as pd

startDate = datetime.datetime(2020, 1, 1)

currDate = startDate

#   bedroom, bathroom, living room, dining room, kitchen
username = "user1"

timetable = {
    '00:00':[80, 40, 50, 20, 20],    #sleep
    '01:00':[80, 40, 50, 20, 20],
    '02:00':[80, 40, 50, 20, 20],
    '03:00':[80, 40, 50, 20, 20],
    '04:00':[80, 40, 50, 20, 20],
    '05:00':[80, 40, 50, 20, 20],
    '06:00':[40, 80, 60, 40, 40],    #wake up
    '07:00':[20, 30, 70, 90, 80],    #breakfast
    '08:00':[20, 30, 70, 90, 80],
    '09:00':[30, 40, 80, 70, 50],    #lepak
    '10:00':[30, 40, 80, 70, 50],
    '11:00':[30, 40, 80, 70, 50],
    '12:00':[30, 40, 80, 70, 50],
    '13:00':[20, 30, 70, 90, 80],    #lunch
    '14:00':[30, 40, 80, 70, 50],
    '15:00':[30, 40, 80, 70, 50],
    '16:00':[30, 40, 80, 70, 50],
    '17:00':[40, 80, 60, 40, 40],
    '18:00':[20, 30, 70, 90, 80],    #dinner
    '19:00':[30, 40, 80, 70, 50],
    '20:00':[30, 40, 80, 70, 50],
    '21:00':[80, 40, 50, 20, 20],    #sleep
    '22:00':[80, 40, 50, 20, 20],
    '23:00':[80, 40, 50, 20, 20]
}

def gen(currDate):
    data = ["",0,0,0,0,0]
    data[0] = currDate.timestamp() * 1000
    for i in range(5):
        check = random.randint(0,1)
        val = 0
        if check:
            check2 = random.randint(0,1)
            if check2:
                val = val + random.randint(1,10)
            else:
                val = val - random.randint(1,10)
        data[i + 1] = timetable[stamp][i] + val
    row = pd.DataFrame(
        [
            data
        ],
        columns = columns
    )
    return row

while int(currDate.year) <= 2020:
    random.seed()
    filename = "json_data/" + username + "_" + f"{currDate.year:04d}" + "-" + f"{currDate.month:02d}" + "-" f"{currDate.day:02d}" + ".json"
    stamp = f"{currDate.hour:02d}" + ":" + f"{currDate.minute:02d}"
    readings = pd.DataFrame()

    # first import any existing json file
    if os.path.exists(filename):
        readings = pd.read_json(filename,orient='split',convert_dates=['time'])
        columns = readings.columns
        row = gen(currDate)
        readings = readings.append(row,ignore_index=True)
    else:
        columns = ["time","Beacon_1","Beacon_2","Beacon_3","Beacon_4","Beacon_5"]
        row = gen(currDate)
        readings = row
    
    readings.to_json(filename,orient='split')

    currDate = currDate + datetime.timedelta(hours=1)