import logging
from processing.plugins_core import FilterPlugin

logger = logging.getLogger(__name__)

class NodeFilter(FilterPlugin):
    def init(self,pluginServices,pluginConfig):
        logging.info("Loading Node filter")
        self.pluginConfig = pluginConfig
        self.pluginServices = pluginServices
        return
    def filter(self,event):
        logger.info("Recieved event " + str(event))
        return True