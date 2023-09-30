import configparser

configs = configparser.ConfigParser()
configs.optionxform  = str
configs.read("engine.ini")


def get_plugin_config(pluginClassName):
    config = {}
    if not configs.has_section(pluginClassName):
        return {}
    items = configs.items(pluginClassName)
    return dict(items)

def is_plugin_enabled(pluginClassName):

    if pluginClassName not in configs:
        print("Plugin " + pluginClassName + " is not enabled")
        return False
    return configs[pluginClassName]["enabled"]