import socket
import threading

my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
PORT = 8000
ADDRESS = "192.168.1.42"
broadcast_list = []
my_socket.bind((ADDRESS, PORT))


def accept_loop():
    while True:
        my_socket.listen()
        client, client_address = my_socket.accept()
        broadcast_list.append(client)
        start_listening_thread(client)


def start_listening_thread(client):
    client_thread = threading.Thread(
        target=listen_thread,
        args=(client,)
    )
    client_thread.start()


def listen_thread(client):
    while True:
        message = client.recv(1024).decode()
        if message:
            print("Полученное сообщение : {0}".format(message))
            broadcast(message)
        else:
            print("Клиент {0} отвалился!".format(client))
            return


def broadcast(message):
    for client in broadcast_list:
        try:
            client.send(message.encode())
        except Exception as e:
            print(e)
            broadcast_list.remove(client)
            print("Клиент {0} удалён".format(client))


accept_loop()
