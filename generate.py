import datetime
import csv

startDate = datetime.datetime(2020, 1, 1)

currDate = startDate

# currYear = currDate.year
# currMonth = currDate.month
# currDay = currDate.day

while int(currDate.year) <= 2020:
    filename = f"{currDate.year:04d}" + "-" + f"{currDate.month:02d}" + "-" f"{currDate.day:02d}" + ".csv"
    print(filename)
    # print(f"{currDate.year:04d}" + "-" + f"{currDate.month:02d}" + "-" + f"{currDate.day:02d}" + "  " + f"{currDate.hour:02d}" + ":" + f"{currDate.minute:02d}")
    currDate = currDate + datetime.timedelta(hours=1)
    