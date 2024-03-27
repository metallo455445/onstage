from bluetooth import *

# Funzione per ricevere messaggi Bluetooth
def receive_message():
    server_sock = BluetoothSocket(RFCOMM)
    server_sock.bind(("", PORT_ANY))
    server_sock.listen(1)

    port = server_sock.getsockname()[1]

    # Inserisci qui il tuo MAC Address Bluetooth
    mac_address = "00:00:00:00:00:00"  # Sostituisci con il tuo MAC Address Bluetooth
    advertise_service(server_sock, "SampleServer", service_id=mac_address)

    print("In attesa di connessione Bluetooth...")

    client_sock, client_info = server_sock.accept()
    print("Connesso a", client_info)

    try:
        while True:
            data = client_sock.recv(1024)
            if len(data) == 0: break
            print("Messaggio ricevuto:", data)
    except IOError:
        pass

    print("Connessione chiusa.")
    client_sock.close()
    server_sock.close()

# Avvia la funzione per ricevere messaggi
receive_message()
