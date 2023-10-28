import datetime
import logging

def get_current_timestamp():
    return datetime.datetime.timestamp(datetime.datetime.now())

def add_time(logMessage):
    now = get_current_timestamp()
    try:
        logMessage.index("timedata")
    except Exception:
        logMessage+=" timedata "
    logMessage += str(now) + " "
    return logMessage

def debug_time_info(logMessage):
    now = get_current_timestamp()
    components = logMessage.split("timedata")
    print(components)
    timestamps = components[1].strip().split(" ")
    last = now
    details=""
    lastHop= "current"
    
    for i in range(len(timestamps),1,-1):
        print(i)
        time = datetime.datetime.fromtimestamp(timestamps[i])
        diff = last - time
        details=" hop "+ lastHop +" to hop" +  i + " = " + diff +"s "
        last = time
        lastHop=i
    logging.info(details)