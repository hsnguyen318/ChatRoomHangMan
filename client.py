import socket

# Client configuration
host = 'localhost'
port = 15550

# Create a socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
client_socket.connect((host, port))
print(f"Connected to {host}:{port}. Enter 'HANGMAN' to begin playing. Enter '/q' to quit chat.")

while True:
    # Prompt for a message to send
    message = input("Enter input: ")

    # If no data is entered, continue to next loop (user may accidentally hit enter)
    if not message:
        continue

    # Send the message to the server
    client_socket.send(message.encode('utf-8'))

    # Shut down
    if message == '/q':
        print('Shutting down!')
        break

    # Receive data from the server
    data = client_socket.recv(1024).decode('utf-8')

    # Stop chat if message is /q
    if data == '/q':
        print('Server has requested shutdown. Shutdown!')
        break
    print(f"Server: {data}")

# Close the socket
client_socket.close()
