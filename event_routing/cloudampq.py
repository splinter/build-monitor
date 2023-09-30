import pika
import configparser


class CloudAmpqDestination:
    def init(self):
        configs = configparser.ConfigParser()
        configs.read("event_routing.ini")
        c = configs["cloudamqp"]["connectionUrl"]
        print(c)
        self.routingKey=configs["cloudamqp"]["routeKey"]
        params = pika.URLParameters(c)
        self.connection=pika.BlockingConnection(params)
        self.channel = self.connection.channel()
        self.channel.queue_declare("events")
        return
    def publish(self,event):
        self.channel.basic_publish(exchange="",routing_key=self.routingKey, body=str(event))

    
