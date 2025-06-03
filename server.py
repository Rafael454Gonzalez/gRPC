import grpc
from concurrent import futures
import time
import user_pb2
import user_pb2_grpc

class UserService(user_pb2_grpc.UserServiceServicer):
    def GetUser(self, request, context):
        return user_pb2.UserResponse(name="Rafael Gonzalez", email="rafael@gmail.com")

def serve():
    server = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    user_pb2_grpc.add_UserServiceServicer_to_server(UserService(), server)
    server.add_insecure_port('[::]:50051')
    server.start()
    print("Servidor gRPC iniciado en el puerto 50051...")
    server.wait_for_termination()

if __name__ == '__main__':
    serve()
