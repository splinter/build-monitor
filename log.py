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
    lastHop= len(timestamps)
    lastTime=None
    for i in range(len(timestamps)-2,0,-1):
        time = datetime.datetime.fromtimestamp(float(timestamps[i]))
        diff = (datetime.datetime.fromtimestamp(last) - time).total_seconds()
        details = details + " hop "+ str(lastHop) +" to hop " +  str(i) + " = " + str(diff) +"s "
        last = time
        lastHop=i
        lastTime = last
    time = datetime.datetime.fromtimestamp((float(timestamps[0])))
    diff = ( lastTime - time).total_seconds()
    i=0
    details = details + " |  hop " + str(lastHop) + " to hop 0"+ str(i) + " = " + str(diff) + "s"
    logging.info(details)