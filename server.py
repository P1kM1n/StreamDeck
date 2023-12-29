import subprocess
import socket
import threading

# Function to handle a client's connection
def handle_client(client_socket, client_address):
    try:
        data = client_socket.recv(1024).decode()
        if not data:
            return

        # Interpret the signal received and open the corresponding application
        if data == 'open_1':
            subprocess.run(["C:\\Program Files (x86)\\Steam\\Steam.exe"])
        elif data == 'open_2':
            subprocess.run(["C:\\Program Files (x86)\\Epic Games\\Launcher\\Portal\\Binaries\\Win32\\EpicGamesLauncher.exe"])
        elif data == 'open_3':
            subprocess.run(["C:\\Program Files (x86)\\Razer\\Synapse3\\WPFUI\\Framework\\Razer Synapse 3 Host\\Razer Synapse 3.exe"])
        elif data == 'open_4':
            subprocess.run(["C:\\Users\\tobyo\\AppData\Local\\Programs\\Opera GX\\launcher.exe", "https://www.netflix.com/browse"])
        elif data == 'open_5':
            subprocess.run(["C:\\Users\\tobyo\\AppData\Local\\Programs\\Opera GX\\launcher.exe", "https://www.youtube.com"])
        elif data == 'open_6':
            subprocess.run(["C:\\Users\\tobyo\\AppData\Local\\Programs\\Opera GX\\launcher.exe", "https://web.snapchat.com"])

    except Exception as e:
        print(f"Error handling connection from {client_address}: {e}")

    finally:
        client_socket.close()
        print(f"Connection closed with {client_address}")

# Set up a socket server
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(('0.0.0.0', 5555))  # Choose an appropriate port
server_socket.listen(5)  # Increase the backlog to allow multiple connections

print("Waiting for connections...")

while True:
    client_socket, client_address = server_socket.accept()
    print("Connected to", client_address)

    # Start a new thread to handle the client's connection
    client_thread = threading.Thread(target=handle_client, args=(client_socket, client_address))
    client_thread.start()
