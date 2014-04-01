#!/usr/bin/env python
 
#importamos el modulo socket
import socket
import concurrent.futures
import time, os


#instanciamos un objeto para trabajar con el socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("abre socket")
#Con el metodo bind le indicamos que puerto debe escuchar y de que servidor esperar conexiones
#Es mejor dejarlo en blanco para recibir conexiones externas si es nuestro caso
s.bind(("", 1111))
 
#Aceptamos conexiones entrantes con el metodo listen, y ademas aplicamos como parametro
#El numero de conexiones entrantes que vamos a aceptar
s.listen(5)

def chat():
    print("entra chat")
    soc = cn
    dirc = soc.recv(1024).decode()    
    nombre = "C:/Users/ragm1_000/Downloads/" + dirc
    print(nombre)
    f = open(nombre, "wb")
    soc.send("ok".encode())
    print(" "+nombre)
    while True:
        #Recibimos el mensaje, con el metodo recv recibimos datos y como parametro 
        #la cantidad de bytes para recibir
        recibido = soc.recv(1024)       
        if len(recibido)==1:
            print("==1"+recibido.decode())
            if recibido.decode() == "z":
                print("sale z")
                break
        f.write(recibido)
        #Devolvemos el mensaje al cliente
        soc.send("ok".encode())
        print("dice OK")

    print("salio")
    f.close()    

    #llamar script conv.py
    split = dirc.split(".")
    convert = "/tmp/"+split[0]+".mp4"
    os.system('python conv.py '+nombre+" "+convert)
    print("iniciar envio")

    soc.send(str(split[0]+".mp4").encode())
    fn = open(convert, "rb")
    soc.recv(4).decode()
    for linea in fn:
        soc.send(linea)
        print(soc.recv(4).decode())
    fn.close()
    soc.send("z".encode())
    
    soc.close()
    print("Archivo: " + nombre + " convertido y enviado")
    return "close"
                                                                                   
with concurrent.futures.ThreadPoolExecutor(max_workers=400) as executor:
        while True:
            #Instanciamos un objeto sc (socket cliente) para recibir datos, al recibir datos este 
            #devolvera tambien un objeto que representa una tupla con los datos de conexion: IP y puerto
            cn, addr = s.accept()
            future = executor.submit(chat)

print("Adios.")
 
#Cerramos la instancia del socket cliente y servidor
s.close()

exit()
