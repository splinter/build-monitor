import logging
import time
from processing.plugins_core import DataPlugin
from processing.plugins_services import PluginServices

logger = logging.getLogger(__name__)
WAIT_TIME = 10
class RabbitMqPlugin(DataPlugin):

    def __init__(self):
        pass

    def init(self,plugin_services,pluginConfig):
        logger.info("Initializing the RabbitMq plugin")
        self.plugin_services = plugin_services
        self.pluginConfig = pluginConfig
        return

    def loop(self):
        return
