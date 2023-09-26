from concurrent import futures
from event_routing.event_queue import send_to_destinations,enqueue_data
import grpc
import event_pb2
import event_pb2_grpc
import logging
import time
import threading


class EventHandler(event_pb2_grpc.EventLogger):
    def SendEvent(self,request,context):
        logging.info("Recieved")
        enqueue_data(request)
        return event_pb2.EventReply(ok=True)
    
def serve():
    port="50061"
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    event_pb2_grpc.add_EventLoggerServicer_to_server(EventHandler(), server)
    server.add_insecure_port("[::]:"+port)
    server.start()
    print("Server started")
    server.wait_for_termination()

if __name__ == "__main__":
    send_to_destinations()
    serve()

    while True:
        enqueue_data("Test")
        time.sleep(5)