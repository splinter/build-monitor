import queue
import logging
import time

class PluginServices:
    def __init__(self):
        self.queueService = QueueService()
        pass
    def get_queue_service(self):
        return self.queueService
    def get_graph_service(self):
        return GraphService()
    def get_persistence_service(self):
        return PersistenceService()

      
class QueueService:
    def __init__(self):
        self.events = queue.Queue()
        self.filteredEvents =queue.Queue()
        self.eventHandlers=[]
        self.filteredEventHandlers = []
        return
    def publish(data,handlers):
        for handler in handlers:
            err = handler(data)
            if err != None:
                return err
        return
    def push_event(self, event):
        self.events.put(event)
        return
    def push_filtered_event(self,event):
        self.filteredEvents.put(event)
        return
    def register_filter_plugin(self,pluginHandler):
        logging.info("Successfully registered filter")
        self.eventHandlers.append(pluginHandler)
        return
    def register_analyzer_plugin(self,plugin):
        return
    def manage_event_queue(self):
        logging.info("Started queue")
        while True:
            logging.info(self.events.qsize())
            try:
                event = self.events.get()
            except queue.Empty as error:
                logging.info("Queue is empty")
            logging.info(event)
            logging.info("Got item")
            for handler in self.eventHandlers:
                try:
                    err = handler(event)
                except:
                    print("Error encountered when handling ")
                if err == True:
                    print("Event been dropped by filter ")
            self.events.task_done()
        time.sleep(1)

class GraphService:
    def upsert_process():
        return
    def upsert_build():
        return
    def upsert_device():
        return
    def query():
        return

class PersistenceService:
    def upsert_build():
        return
    def upsert_event():
        return
    def find_build():
        return
