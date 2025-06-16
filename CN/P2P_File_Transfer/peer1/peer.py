import os
import socket
import threading
import time

# Directory to sync
SYNC_DIR = 'sync_folder'
HOST = 'localhost'
PORT = 12346

# List of peers (other clients)
peers = []

def handle_client(conn, addr):
    print(f"Connected by {addr}")
    while True:
        # Read the length of the file name first
        file_name_length_bytes = conn.recv(4)
        if not file_name_length_bytes:
            break
        file_name_length = int.from_bytes(file_name_length_bytes, 'big')
        
        # Now read the file name
        file_name = conn.recv(file_name_length).decode('utf-8')
        
        # Read the file data
        file_data = bytearray()
        while True:
            chunk = conn.recv(4096)
            if not chunk:
                break
            file_data.extend(chunk)
        
        sync_files({file_name: file_data})
    conn.close()

def sync_files(files):
    existing_files = set(os.listdir(SYNC_DIR))

    # Check for new files to add
    for file_name, file_data in files.items():
        if file_name not in existing_files:
            with open(os.path.join(SYNC_DIR, file_name), 'wb') as f:
                f.write(file_data)
            print(f"Added: {file_name}")

def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen()
    print(f"Peer listening on {HOST}:{PORT}")

    while True:
        conn, addr = server.accept()
        threading.Thread(target=handle_client, args=(conn, addr)).start()

def sync_file_with_peer(peer, file_name, file_data):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((peer['host'], peer['port']))
            # Send file name length followed by the file name and then the file data
            s.sendall(len(file_name).to_bytes(4, 'big'))  # Send length of file name
            s.sendall(file_name.encode('utf-8'))  # Send file name
            s.sendall(file_data)  # Send raw file data
            print(f"Sent {file_name} to {peer['host']}:{peer['port']}")
    except ConnectionRefusedError:
        print(f"Connection refused by {peer['host']}:{peer['port']}")
    except Exception as e:
        print(f"Error sending {file_name} to {peer['host']}:{peer['port']} - {e}")

def sync_with_peers():
    files = {}
    for filename in os.listdir(SYNC_DIR):
        with open(os.path.join(SYNC_DIR, filename), 'rb') as f:
            files[filename] = f.read()

    threads = []
    for peer in peers:
        for file_name, file_data in files.items():
            thread = threading.Thread(target=sync_file_with_peer, args=(peer, file_name, file_data))
            threads.append(thread)
            thread.start()

    # Wait for all threads to complete
    for thread in threads:
        thread.join()

def discover_peers():
    # Example: manually adding peers
    peers.append({'host': 'localhost', 'port': 12345})  # Adjust as necessary

def start_client():
    while True:
        sync_with_peers()
        time.sleep(5)  # Sync every 10 seconds

if __name__ == "__main__":
    os.makedirs(SYNC_DIR, exist_ok=True)
    discover_peers()  # Discover or add peers here
    threading.Thread(target=start_server, daemon=True).start()
    start_client()