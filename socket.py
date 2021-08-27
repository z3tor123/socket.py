import socket


print("---------------------")
print("1) scan host")
print("2) scan name_port")
print("3) scan number_port")
print("---------------------")
x = int(input("what you wan't ( 1 - 2 -3 ) : "))
if x == 1:
    hostname = input("Enter the hostname : ")
    ip = socket.gethostbyname(hostname)
    print("---------------------")
    print( hostname + " ip = " + str(ip))
        

if x == 2:
    port_name = input("Enter the port name : ")
    port = socket.getservbyname(port_name)
    print("----------------------")
    print( port_name + " port number : " + str(port))
        
if x == 3:
    port_number = int(input("Enter the port number : "))
    service = socket.getservbyport(port_number)
    print("-----------------------")
    print( str(port_number) + " port name : " + service)
