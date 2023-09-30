import logging
from processing.plugins_core import FilterPlugin

logger = logging.getLogger(__name__)

class HtmlFilter(FilterPlugin):
    def init(self,pluginServices,pluginConfig):
        logging.info("Loading HTML filter")
        self.pluginConfig = pluginConfig
        return
    def filter(self,event):
        logger.info("Recieved event " + str(event))
        return True