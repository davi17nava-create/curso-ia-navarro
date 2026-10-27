texto = input("Escribe una opinion: ").lower()
positivas = ["bueno", "excelente", "genial", "feliz", "bien"]
negativas = ["malo", "pesimo", "horrible", "triste", "error"]
puntaje = 0

for palabra in positivas:
    if palabra in texto:
        puntaje += 1

for palabra in negativas:
    if palabra in texto:
        puntaje = puntaje - 1

print("Puntaje:", puntaje)

if puntaje > 0:
    print("Positivo")
elif puntaje < 0:
    print("Negativo")
else:
    print("Neutral")