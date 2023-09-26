import queue

q = queue.Queue()


def enqueue_data(event):
    q.put(event)
    return

def send_to_destinations():
    while True:
        data = q.get()

        q.task_done()
