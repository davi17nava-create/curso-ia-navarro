mensaje = input("Ingrese el mensaje a revisar: ").lower()
sospechosas = ["gratis", "premio", "urgente", "ganaste", "oferta"]
contador = 0

for palabra in sospechosas:
    if palabra in mensaje:
        contador += 1

print("Cantidad de palabras sospechosas:", contador)
