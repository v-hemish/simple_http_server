import socket

PORT = 6969
HOST = "127.0.0.1"


server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

server_socket.bind((HOST,PORT))

server_socket.listen(5)

print("The HTTP server is active on port {PORT}")


while True: 
    client_conn, client_addr = server_socket.accept()

    request_data = client_conn.recv(1024).decode()
    
    print(request_data)

    headers = request_data.split("\n")

    first_header_components = headers[0].split()

    http_method = first_header_components[0]
    path = first_header_components[1]

    if path == '/':
        fin = open('index.html')
        content = fin.read()
        fin.close()

        response = "HTTP/1.1 200 OK\n\n" + content
        client_conn.sendall(response.encode())


    




        


