import socket

#Defining a port of 8888 on any available interfaces ('')
HOST, PORT = '', 8888

#Creating the socket
##Setting the socket to accept IPv4 addresses and allowing for communication between the socket and a client
listen_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
##Setting socket options.
listen_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
##Binding our listener socket to localhost:8888
listen_socket.bind((HOST, PORT))
##Telling our socket to activate and listen for events.
listen_socket.listen(1)
print(f'Serving HTTP on Port: {PORT}...')
while True:
    #Accept connection and return connection (Socket obj) and address of connection.
    client_connection, client_address = listen_socket.accept()
    #Recieve data from socket obj and print.
    request_data = client_connection.recv(1024)
    print(request_data.decode('utf-8'))
    #If connection OK, send HTTP response.
    http_response = b"""/
HTTP/1.1 200 OK 

Hello, world!
"""
    client_connection.sendall(http_response)
    client_connection.close()

