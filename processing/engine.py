import logging
import configparser
import sys
import os
import importlib.util
import inspect
import threading
import time
from processing.plugins_core import DataPlugin,FilterPlugin
from processing.plugins_services import PluginServices


logger = logging.getLogger(__name__)
configs = configparser.ConfigParser()

configs.read("engine.ini")

def plugin_base_path():
    return "plugins"

def data_plugin_path():
    basePath = plugin_base_path()
    return [os.path.join("../",basePath, "data"),basePath+"/data"]

def filter_plugin_path():
    basePath = plugin_base_path()
    return [os.path.join("../",basePath, "filters"),basePath+"/filters"]

def analyzer_plugin_path():
    basePath = plugin_base_path()
    return [os.path.join("../",basePath, "analyzers"),basePath + "/analyzers"]

def load_plugins(pluginPath,relativePluginPath, pluginClass):
    logger.info("Plugins loaded from " + relativePluginPath)
    files = os.listdir(relativePluginPath)
    logger.info("Detected the following plugins:")
    logger.info(files)
    plugins = {}

    for file in files:
        fullNameOfFile = os.path.basename(file)
        if os.path.splitext(file)[1] != ".py":
            continue
        logger.info("Loading {filename}".format(filename = file))
        path = relativePluginPath + "/" + file
        spec = importlib.util.spec_from_file_location(fullNameOfFile, path)
        module = importlib.util.module_from_spec(spec)
        sys.modules[fullNameOfFile] = module
        spec.loader.exec_module(module)

        for cls in inspect.getmembers(module, inspect.isclass):
            className,c = cls
            if issubclass(c,pluginClass) and c is not pluginClass:
                logger.info("Loaded the plugin: " + className)
                plugins[className]=c
    return plugins


def build_plugin_services():
    return PluginServices()

def engine_start():
    logging.basicConfig(level=logging.INFO)

    logger.info("Starting the engine")
    logger.info("Loading data plugins")

    [dataPluginPath,relativeDataPluginPath]= data_plugin_path()
    [filterPluginPath,relativeFilterPluginPath] = filter_plugin_path()
    [analyzerPluginPath, relativeAnalyzerPluginPath] = analyzer_plugin_path()

    dataPlugins = load_plugins(dataPluginPath,relativeDataPluginPath, DataPlugin)
    filterPlugins = load_plugins(filterPluginPath, relativeFilterPluginPath, FilterPlugin)
    analyerPlugins = load_plugins(analyzerPluginPath, relativeAnalyzerPluginPath, FilterPlugin)

    logger.info("Starting data plugins")
    pluginServices = build_plugin_services()

    start_data_plugins(dataPlugins,pluginServices)
    start_filter_plugins(filterPlugins,pluginServices)

    t = threading.Thread(target=pluginServices.get_queue_service().manage_event_queue)
    t.start()
    while True:
        time.sleep(1)



def start_plugins(plugins,pluginServices):
    threads = []
    for plugin in plugins:
        pluginInstance = plugins[plugin]()
        logger.info(f"Initializing plugin: {plugin}")

        pluginInstance.init(pluginServices)
        t = threading.Thread(target=pluginInstance.loop)
        t.start()
    return threads

def start_data_plugins(plugins,pluginServices):
    start_plugins(plugins,pluginServices)
    return

def start_filter_plugins(plugins,pluginServices):
    for plugin in plugins:
        pluginInstance = plugins[plugin]()
        pluginInstance.init(pluginServices)
        pluginServices.get_queue_service().register_filter_plugin(pluginInstance.filter)
    return
