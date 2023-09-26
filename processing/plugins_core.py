from processing.core import Event

class DataPlugin:
    def loop(self):
        return

class FilterPlugin:
    def init(self, pluginServices):
        self.pluginServices = pluginServices
        
    def filter(self,event):
        return

class AnalyzerPlugin:
    def init(self, pluginServices):
        self.pluginServices = pluginServices

    def analyze(self,event):
        return

