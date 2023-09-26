import logging
import time
from processing.plugins_core import DataPlugin
from processing.plugins_services import PluginServices

logger = logging.getLogger(__name__)
WAIT_TIME = 10
class ConfluentPlugin(DataPlugin):

    def __init__(self):
        pass

    def init(self,plugin_services):
        logger.info("Initializing the Confluent plugin")
        self.plugin_services = plugin_services
        return

    def loop(self):
        logger.info("Starting plugin in new thread")
        queue_service = self.plugin_services.get_queue_service()
        while True:
            queue_service.push_event(1)
            logger.info("Waiting for a few seconds")
            time.sleep(WAIT_TIME)
        return
