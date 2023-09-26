import logging
import threading
import time
import grpc
import event_pb2_grpc
import event_pb2
import queue

q = queue.Queue()
def log_event(event):
    q.put(event)  
    return

def loop():
    logging.info("Started sending events")
    with grpc.insecure_channel("localhost:50061") as channel:
        stub = event_pb2_grpc.EventLoggerStub(channel)
        print("Start")
        while True:
            item = q.get()
            logging.debug("Sending events")
            response = stub.SendEvent(event_pb2.EventRequest(eventName=item))
            q.task_done()
    

def start_client():
    format="%(message)s"
    logging.basicConfig(format=format, level=logging.INFO)
    l = threading.Thread(target=loop)
    l.start()
    logging.info("Started client")
    return

if __name__ == "__main__":
    print("w")
    logging.info("Event client")
    start_client()

    while True:
        log_event("aa")
        print("Added")
        time.sleep(10)

