import socket

lang = input("Enter language: ")

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(("localhost", 1312))

while True:
    message = input("Enter your message: ")

    if message == "!q":
        client.close()
        break
    else:
        client.send(f"[{lang}]{message}".encode())