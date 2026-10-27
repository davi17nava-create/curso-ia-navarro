mensaje = ""

while mensaje != "salir":
    mensaje = input("Escribe un mensaje (o escribe salir para terminar): ").lower()
    if mensaje != "salir":
        print("Mensaje recibido:", mensaje)

print("Programa terminado")