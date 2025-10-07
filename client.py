import socket

HOST = '127.0.0.1'  
PORT = 65432

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((HOST, PORT))

print(f"Terhubung ke server {HOST}:{PORT}")
print("Ketik 'exit' untuk keluar.\n")

while True:
    pesan = input("Kirim ke server: ")
    if pesan.lower() == 'exit':
        break
    client_socket.sendall(pesan.encode('utf-8'))
    data = client_socket.recv(1024).decode('utf-8')
    print(f"Balasan dari server: {data}\n")

client_socket.close()
print("Koneksi ditutup.")
