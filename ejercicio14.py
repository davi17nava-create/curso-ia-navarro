palabra = input("Ingresa una palabra: ").lower()
invertida = ""

for letra in palabra:
    invertida = letra + invertida

if palabra == invertida:
    print("Es palindromo")
else:
    print("No es palindromo")