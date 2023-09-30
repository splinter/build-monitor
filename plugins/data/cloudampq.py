import logging
import time
import pika
from processing.plugins_core import DataPlugin
from processing.plugins_services import PluginServices

logger = logging.getLogger(__name__)

class CloudAMPQPlugin(DataPlugin):

    def __init__(self):
        pass

    def init(self,pluginServices,pluginConfig):
        logger.info("Initializing plugin " + __name__)
        self.pluginConfig = pluginConfig
        self.plugin_services = pluginServices
        return
    def on_message(self,ch,method,properties,body):
        logger.info("Recieved message " + body)
        self.plugin_services.get_queue_service().push_event(body)
    def loop(self):
        print(self.pluginConfig)
        connectionUrl = self.pluginConfig["connectionUrl"]
        queue = self.pluginConfig["queue"]
        print(connectionUrl)
        if queue is None:
            logger.error("Queue name is not defined in configuration")
            pass
        if connectionUrl is None:
            logger.error("Connection url is not deinfed in configuration")
            pass
        params = pika.URLParameters(connectionUrl)
        connection = pika.BlockingConnection(params)
        channel = connection.channel()
        channel.basic_consume(queue=queue,
                              auto_ack=True,
                              on_message_callback=self.on_message)
        channel.start_consuming()
        while True:
            time.sleep(1)
        return