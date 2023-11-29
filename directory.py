#!/usr/bin/env python3
import base64
import socket
import json
import crypty

keypair1 = crypty.gen_rsa_keypair()
keypair2 = crypty.gen_rsa_keypair()
keypair3 = crypty.gen_rsa_keypair()

RELAY_NODES = {
    'localhost:5001' : list(crypty.get_pem_format(keypair1[0], keypair1[1])),
    'localhost:5002' : list(crypty.get_pem_format(keypair2[0], keypair2[1])),
    'localhost:5003' : list(crypty.get_pem_format(keypair3[0], keypair3[1]))
}
RELAY_NODES['localhost:5001'] = [base64.b64encode(RELAY_NODES['localhost:5001'][0]).decode('ascii'), base64.b64encode(RELAY_NODES['localhost:5001'][1]).decode('ascii')]
RELAY_NODES['localhost:5002'] = [base64.b64encode(RELAY_NODES['localhost:5002'][0]).decode('ascii'), base64.b64encode(RELAY_NODES['localhost:5002'][1]).decode('ascii')]
RELAY_NODES['localhost:5003'] = [base64.b64encode(RELAY_NODES['localhost:5003'][0]).decode('ascii'), base64.b64encode(RELAY_NODES['localhost:5003'][1]).decode('ascii')]

def main():
    listen()

def listen():
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(('localhost', 3001))
    serversocket.listen(5)
    while True:
        clientsocket, address = serversocket.accept()
        payload = json.dumps(RELAY_NODES) 
        print ('Payload: ', payload)
        clientsocket.send(payload.encode())
    clientsocket.close()
    return

def get_private_key(): #delete later
  return RELAY_NODES


if __name__ == '__main__':
    main()
