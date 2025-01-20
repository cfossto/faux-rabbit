import socket
import queues


queue = queues.Queues()



serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serversocket.bind((socket.gethostname(), 8889))
serversocket.listen()
