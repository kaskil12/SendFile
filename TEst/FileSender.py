import socket

# Replace with the IP address and port of the receiver
receiver_ip = '192.168.98.170'  # Receiver's IP address
receiver_port = 3000  # Receiver's listening port

# Replace with the path to the file you want to send
file_to_send = 'adadada.txt'

def send_file():
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        client.connect((receiver_ip, receiver_port))
        print(f"Connected to {receiver_ip}:{receiver_port}")
        
        with open(file_to_send, 'rb') as file:
            while True:
                data = file.read(1024)
                if not data:
                    break
                client.send(data)
        
        print(f"File '{file_to_send}' sent successfully.")
    
    except ConnectionRefusedError:
        print(f"Connection to {receiver_ip}:{receiver_port} was refused.")
    
    client.close()

if __name__ == '__main__':
    send_file()
