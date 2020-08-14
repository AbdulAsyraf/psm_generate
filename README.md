This script generates a year's worth of positional data for training purposes  
Things that can be changed:  
    1.  startDate:  Allows for different periods of time for data  
    2.  timetable:  Can be modified to create different movement patterns over a day  
    3.  currDate.<arg>: The argument can be changed to change the scope? of the period of time for the generated data, by default this is set to the same year as the "startDate" so that a year's worth of data is generated  
    4.  datetime.timedelta(<arg>): This can be changed to adjust the timestep for each data point. By default this is set to 1 hour  

Those are the quick adjustments that should not break the script