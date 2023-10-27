import datetime
import logging

def add_time(logMessage):
    now = datetime.datetime.now().total_seconds()
    if(logMessage.index("timedata") < 0):
        logMessage += "timedata "
    logMessage +=str(now)
    return logMessage

def debug_time_info(logMessage):
    now = datetime.datetime.now().total_seconds()
    components = logMessage.split("timedata")
    timestamps = components[1].split(" ")
    last = now
    details=""
    lastHop= "current"
    for i in range(len(timestamps),0):
        diff = last - int(timestamps[i].strip())
        details=" hop "+ lastHop +" to hop" +  i + " = " + diff +"s "
        last = int(timestamps[i].strip())
    logging.info(details)