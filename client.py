import grpc
import user_pb2
import user_pb2_grpc

def run():
    channel = grpc.insecure_channel('localhost:50051')
    stub = user_pb2_grpc.UserServiceStub(channel)
    response = stub.GetUser(user_pb2.UserRequest(id=1))
    print(f"Nombre: {response.name}")
    print(f"Correo: {response.email}")

if __name__ == '__main__':
    run()
