import bluetooth

def main():
    # Impostazione del socket Bluetooth
    server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
    port = 1  # Porta RFCOMM predefinita
    server_socket.bind(("", port))
    server_socket.listen(1)

    print("In attesa di connessione Bluetooth...")

    client_socket, address = server_socket.accept()
    print("Connesso a", address)

    try:
        while True:
            data = client_socket.recv(1024).decode().strip()
            if data == "a":
                print("Messaggio ricevuto:", data)
                # Esegui qui le azioni desiderate quando ricevi "a"
    except KeyboardInterrupt:
        print("Interruzione dell'esecuzione.")

    client_socket.close()
    server_socket.close()

if __name__ == "__main__":
    main()
