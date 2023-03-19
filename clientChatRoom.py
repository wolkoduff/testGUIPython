import socket
import threading

nickname = input("Введи свой никнейм : ").strip()
while not nickname:
    nickname = input("Введён пустой никнейм. Попробуй истчо раз: ").strip()
my_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
HOST = "192.168.1.42"  # 127.0.0.1
PORT = 8000
my_socket.connect((HOST, PORT))


def thread_sending():
    while True:
        message_to_send = input()
        if message_to_send:
            message_with_nickname = nickname + " : " + message_to_send
            my_socket.send(message_with_nickname.encode())


def thread_receiving():
    while True:
        message = my_socket.recv(1024).decode()
        print(message)


thread_send = threading.Thread(target=thread_sending)
thread_receive = threading.Thread(target=thread_receiving)
thread_send.start()
thread_receive.start()
