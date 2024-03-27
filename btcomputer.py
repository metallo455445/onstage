import bluetooth

# MAC Address del tuo EV3
mac_address = "00:00:00:00:00:00"  # Sostituisci con il MAC Address Bluetooth del tuo EV3

# Messaggio da inviare
message = "Ciao da computer!"

try:
    # Crea un socket Bluetooth
    sock = bluetooth.BluetoothSocket(bluetooth.RFCOMM)

    # Connetti il socket al dispositivo EV3
    sock.connect((mac_address, 1))

    # Invia il messaggio
    sock.send(message)

    print("Messaggio inviato con successo!")
except bluetooth.btcommon.BluetoothError as e:
    print("Errore durante l'invio del messaggio:", e)

# Chiudi il socket
sock.close()
