






# Se abre el archivo con lectura y escritura
# rw indica lectura (read)
file = open("file.txt", "r")

for line in file:
    print(line)

print("hello world")


# Metodo uno de reemplazar QR con I
lista = "RRQRR"
respuesta = []

i = 0
while i < len(lista):
    print(i)
    if i == len(lista) - 1:
        print(respuesta)
    elif lista[i] == "Q" and lista[i+1] == "R":
        respuesta.append("I")
        i = i + 1
    else:
        respuesta.append(lista[i])

    i = i + 1

# Metodo dos de reemplazar QR con I

lista = "RRQRR"
respuesta = []

for i in range(0,len(lista)):
    if lista[i] == "Q" and lista[i+1] == "R":
        x = "T"
    elif lista[i] === "R" and lista[i-1] == "Q":
        x = ""
    else:
        x = lista[i]

    respuesta.append(i)

#Metodo 3 de reemplazar QR con I

lista.replace("QR", "I")
