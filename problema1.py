import re

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

lista = "RRQRQ"
respuesta = []

for i in range(0,len(lista)):
    if lista[i] == "Q" and i+1 < len(lista) and lista[i+1] == "R":
        x = "T"
    elif i > 0 and lista[i] == "R" and lista[i-1] == "Q":
        x = ""
    else:
        x = lista[i]

    respuesta.append(x)

reemplazar("QR", "I", lista) # Produce: RRIQ

#Metodo 3 de reemplazar QR con I

lista.replace("QR", "I")

def reemplazar(palabra, reemplazo, lista):
    return lista.replace(palabra, reemplazo)


# Se abre el archivo con lectura y escritura
# rw indica lectura (read)
file = open("file.txt", "r")

def leerReemplazo(actual):
    #leer el reemplazo
    #obtener el resto

    res = re.match(
        '(?P<patron>[A-Z]{3})\s(?P<resto>.*)',
        actual)

    return (
        res.group('patron'),
        res.group('resto'))

def splitLine(linea):
    res = re.match(
        "((?P<cantidad>\d+)\s+(?P<patrones>([A-Z]{3}\s+)+))?(?P<resto>.+)",
        linea)

    return (
        res.group('cantidad'),
        res.group('patrones'),
        res.group('resto'))

def separar(palabra):
    x = []
    for letras in palabra:
        x.append(letras)
    return x

# Función para eleminar elementos de un string
def eliminar(palabra, combinacion):
    palabra = separar(palabra)
    y = separar(combinacion)

    in1 = y[0]
    in2 = y[1]

    x = []
    c = ""

    for i in range(0, len(palabra)):
        if palabra[i] >= in1 and palabra[i] <= in2:
            x.append(c)
        else:
            x.append(palabra[i])

    return "".join(x)

print(eliminar("123456789", "27"))

for line in file:

    (numReemplazos, actual, resto) = splitLine(line)
    reemplazos = []

    for i in range(0, int(numReemplazos)):
        (reemplazo, actual) = leerReemplazo(actual)
        reemplazos.append(reemplazo)

    for rep in reemplazos:
        combinacion = rep[0:2]
        res = rep[2]
        resto = reemplazar(combinacion, res, resto)

    print('linea original:' + line)
    print('resultado:' + resto)

