import socket

# Replace with the IP address and port to listen on
listen_ip = '192.168.98.170'  # Listens on all available network interfaces
listen_port = 3000


# Replace with the path where you want to save the received file
output_file_path = 'C:\\Users\\kaspe\\OneDrive\\Documents\\GitHub\\SendFile\\pyut\\login\\logfile.txt'

def receive_file():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((listen_ip, listen_port))
    server.listen(1)
    
    print(f"Listening on {listen_ip}:{listen_port}")

    conn, addr = server.accept()
    print(f"Connection from: {addr[0]}:{addr[1]}")

    with open(output_file_path, 'a', encoding="utf8") as file:
        while True:
            data = conn.recv(1024)
            if not data:
                break
            file.write(data)
    
    conn.close()
    server.close()
    print(f"File received and saved as '{output_file_path}'")

if __name__ == '__main__':
    receive_file()
