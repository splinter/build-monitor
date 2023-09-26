import queue
from event_routing.cloudampq import CloudAmpqDestination
import threading
import time

q = queue.Queue()

def register_destinations():
    return


def enqueue_data(event):
    q.put(event)
    return


def send_events():
    destinations = []
    destinations.append(CloudAmpqDestination())
    for destination in destinations:
        destination.init()
    while True:
        data = q.get()
        for destination in destinations:
            destination.publish(data)
        q.task_done()

def send_to_destinations():
    t = threading.Thread(target=send_events)
    t.start()

if __name__ == "__main__":
    send_to_destinations()
