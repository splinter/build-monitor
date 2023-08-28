from concurrent import futures
import grpc
import event_pb2
import event_pb2_grpc

class EventHandler(event_pb2_grpc.EventLogger):
    def SendEvent(self,request,context):
        print("Recieved request")
        print(request)
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
    serve()