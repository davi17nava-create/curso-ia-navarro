mensaje = input("Escribe tu consulta: ").lower()

if "error" in mensaje or "ayuda" in mensaje or "falla" in mensaje:
    print("Soporte")
elif "precio" in mensaje or "comprar" in mensaje or "catalogo" in mensaje:
    print("Ventas")
else:
    print("Otro")