import sys
from socket import *

if __name__ == "__main__":
    # Test validation of command line argument
    arguments = sys.argv[1:]
    # Wrong number of argument
    if len(arguments) != 1:
        print("ERROR: One command line argument required")
        exit(1)
    # Test whether the argument able to convert to int
    try:
        req_code = int(arguments[0])
    except:
        print("ERROR: Argument should be integer")
        exit(1)
    # Receive req_code
    req_code = sys.argv[1]
    
    # TCP Server
    zeroPort = 0
    # Create TCP welcoming socket
    TCPserverSocket = socket(AF_INET,SOCK_STREAM)
    TCPserverSocket.bind(('',zeroPort))
    # Server begins listening for incoming TCP requests
    TCPserverSocket.listen(1)
    # Get TCP host and n_port
    TCPserverHost, n_port = TCPserverSocket.getsockname()
    # Create UDP Socket
    UDPserverSocket = socket(AF_INET, SOCK_DGRAM)
    UDPserverSocket.bind(('',zeroPort))
    # Get UDP host and r_port
    UDPserverHost, r_port = UDPserverSocket.getsockname()
    # Print serverPort number
    print("SERVER_PORT="+str(n_port))
    # Loop forever
    while True:
        # Server waits on accept() for incoming requests, new socket created on 
        # return
        connectionSocket,addr = TCPserverSocket.accept()
        # read bytes from socket (but not address as in UDP)
        sentence = connectionSocket.recv(1024).decode()
        if sentence != str(req_code):
            TCPserverSocket.close()
            print("ERROR: req_code is incorrect")
            exit(1)
        else:
            connectionSocket.send(str(r_port).encode())
            break
    # Close connection to this client (but not welcoming socket)
    connectionSocket.close()
    # Read from UDP socket into message, getting client's address 
    # (client IP and port)
    message,clientAddress = UDPserverSocket.recvfrom(2048)
    # Decode message
    decodedMessage = message.decode()
    # Reverse message
    modifiedMessage = decodedMessage[::-1]
    # Send modified string back to this client
    UDPserverSocket.sendto(modifiedMessage.encode(),clientAddress)
    UDPserverSocket.close()