import sys
from socket import *

if __name__ == "__main__":
    # Test validation of command line argument
    arguments = sys.argv[1:]
    # Wrong number of argument
    if len(arguments) != 4:
        print("ERROR: Four command line arguments required")
        exit(1)
    # Test whether the argument able to convert to int
    try:
        server_address = str(arguments[0])
        n_port = int(arguments[1])
        req_code = int(arguments[2])
        message = str(arguments[3])
    except:
        print("ERROR: Argument has wrong format")
        exit(1)
    if not(server_address and n_port and req_code and message):
        print("ERROR: Empty string occurs")
        exit(1)
    
    # TCP Client
    # Create TCP socket for server
    TCPclientSocket = socket(AF_INET,SOCK_STREAM)
    TCPclientSocket.connect((server_address,n_port))
    # No need to attach server name, port
    TCPclientSocket.send(str(req_code).encode())
    r_port = TCPclientSocket.recv(1024)
    if (str(r_port) == ""):
        print("ERROR: Received unexpected r_port")
        exit(1)
    TCPclientSocket.close()
    # Create UDP socket for server
    UDPclientSocket = socket(AF_INET, SOCK_DGRAM)
    # Attach server name, port to message; send into socket
    UDPclientSocket.sendto(message.encode(),(server_address,int(r_port)))
    # Read reply characters from socket into string
    modifiedMessage, serverAddress = UDPclientSocket.recvfrom(2048)
    # Print out received string and close socket
    print(modifiedMessage.decode())
    UDPclientSocket.close()