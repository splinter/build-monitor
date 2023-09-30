from  processing.plugins_core import AnalyzerPlugin
import logging


logger =logging.getLogger(__name__)

class BuildStartAnalyzerPlugin(AnalyzerPlugin):
    def init(self, pluginServices,pluginConfig):
        self.pluginServices = pluginServices
        pass

    def analyze(self, event):
        logger.info("Inspecting event " + event)
        return 