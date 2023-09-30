from processing.core import Event

class DataPlugin:
    def init(self, pluginServices, pluginConfig):
        self.pluginConfig = pluginConfig
        self.pluginServices = pluginServices
    def loop(self):
        return

class FilterPlugin:
    def init(self, pluginServices,pluginConfig):
        self.pluginConfig = pluginConfig
        self.pluginServices = pluginServices
    def filter(self,event):
        return

class AnalyzerPlugin:
    def init(self, pluginServices,pluginConfig):
        self.pluginServices = pluginServices

    def analyze(self,event):
        return

