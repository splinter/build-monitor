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
    def register_analyzer_plugin(self,pluginHandler):
        self.filteredEventHandlers.append(pluginHandler)
        return
    def manage_event_queue(self):
        while True:
            event = self.events.get()
            for handler in self.eventHandlers:
                filtered = handler(event)
                if filtered:
                    self.filteredEvents.put(event)
            self.events.task_done()
        time.sleep(1)
    def manage_filtered_event_queue(self):
        while True:
            event = self.filteredEvents.get()
            for handler in self.filteredEventHandlers:
                handler(event)
            self.filteredEvents.task_done()
        time.sleep(1)
        return

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
