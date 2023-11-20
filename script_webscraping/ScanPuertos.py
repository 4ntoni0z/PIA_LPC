#Juan Antonio Sena Castillo 
#1973595
#Gpo 062

#Se importa las librerias necesarias 
import sys
import nmap 
import sys 
from socket import *

#Se definde el portscaner de nmap 
escan = nmap.PortScanner()

#Funcion que valida la opcion dada por el usuario 
def evalOpcion():
    #Inicia el ciclo para la evaluacion de la variable opcion
    while True:
        try:
            #Se pide el valor de la variable opcion
            opcion = int(input("Ingresa un número entero: "))
            #Se evalua que este en el rango dado
            if opcion>=1 and opcion<= 5:
                #De ser asi se regresara para que se guarde en la variable resultopcion
                return opcion
            else:
                #Error si no esta en el rango permitido de opciones
                print("El número no está en el rango de opciones permitidas. Inténtalo de nuevo.")
        except ValueError:
            #Se evalua si el valor es del tipo entero 
            print("Por favor, ingresa un número entero válido.")
            
def scan_red(ip):
    escan= nmap.PortScanner()
    escan.scan(hosts=ip, arguments="-sn")

    for host in escan.all_hosts():
        if escan[host]['status']['state'] == 'up':
            print(f"Host {host} está activo")           

def tcp_test(port):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.settimeout(10)
    result=sock.connect_ex((target_ip, port))
    if result ==0:
        print("Opened port: ", port)
        
def escaneosock(host, port):
    udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    try:
        # Establece un tiempo de espera 
        udp_socket.settimeout(5)

    # Intenta conectar al host en el puerto 
        udp_socket.sendto(b'', (host, port))
        data, addr = udp_socket.recvfrom(1024)
    
        print(f"El puerto {port} está abierto en {host}")
    except socket.timeout:
        print(f"El puerto {port} está cerrado en {host}")
    except ConnectionRefusedError:
        print(f"La conexión al puerto {port} fue rechazada en {host}")
    except Exception as e:
        print(f"Ocurrió un error: {str(e)}")
    finally:
        # Cierra el socket
        udp_socket.close()
        
def Scan_Sist_Op(ip):
    scanner = nmap.PortScanner()
    scanner.scan(ip, arguments='-O')
    try:
        Sis_Oper = scanner[ip]['osmatch'][0]['name']
        return Sis_Oper
    except KeyError:
        return "No se pudo obtener información del sistema operativo"


    
    
resultopcion=0

#Se inicia el ciclo para el menu de opciones 
while resultopcion!=5:
    print("Menu de opciones: \n(1)Escaneo UDP \n(2)Escaneo Completo \n(3)Deteccion del sistema Operativo \n(4)Escaneo de red Ping \n(5)Salir ")
    #Variable donde se guarda la opcion despues de la evaluacion dle mimso
    resultopcion=evalOpcion()
    
    #Se inicia el menuo de opciones 
    
    if resultopcion==1:
        print("Opcion 1: Escaneo UDP")
        host = input("Ingresa el host que deseas escanear: ")

        port = int(input("Ingresa el puerto a escanear: "))

        escaneosock(host, port)
        
        

    elif resultopcion==2:
        print("Opcion 2: Escaneo Completo")
        host = input("iNGRESA LA IP A ESCANEAR: ")
        start_port=int( input("Ingresa el puerto de inicio: "))
        end_port= int(input("Ingresa el puerto final: "))
        
        target_ip = gethostbyname(host)
        opened_ports=[]

        for port in range(start_port, end_port):
            sock = socket(AF_INET, SOCK_STREAM) 
            sock.settimeout(10)
            result= sock.connect_ex((target_ip, port))
            if result == 0:
                opened_ports.append(port)
            
        print("Opened ports: ")
        for i in opened_ports:
            print(i)


        
    elif resultopcion==3:
        print("Opcion 3: Deteccion del sistema Operativo")
        ip = input("ingresa la ip que quieres escanear: ")
        Sis_Oper = Scan_Sist_Op(ip)
        print(f"El sistema operativo de la dirección IP {ip} es: {Sis_Oper}")
        
    elif resultopcion==4:
        print("Opcion 3: Escaneo de red Ping")
        if __name__ == "__main__":
            red_rango =input(" Ingresa el la red y el rango, ejemplo de ingreso 192.168.0.1-254: " ) # Cambia esto a tu rango de red
            scan_red(red_rango)
           
        
    else:
        print("Que tenga un buen dia :)")
        
        
