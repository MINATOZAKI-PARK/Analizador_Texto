import string as str


def contador_palabras(txt):
    caracteres = str.punctuation  # caracteres
    for carac in caracteres:  # recorre 'caracteres' para remplazarlos de txt
        if carac in txt:
            limpiador = txt.replace(carac, '')
    palabras = limpiador.split()  # divide limpiador en palabras
    contador = len(palabras)  # cuenta las palabras en txt

    print(f'El texto tiene {contador} palabras')


def contador_palabras_frecuentes(txt):
    caracteres = str.punctuation  # caracteres
    for carac in caracteres:  # recorre 'caracteres' para remplazarlos de txt
        txt = txt.replace(carac, '')  # Reemplaza los caracteres especiales en el texto

    palabras = txt.lower().split()  # Convierte todo a minúsculas y divide en palabras

    palabras_frecuentes = {}  # crea un diccionario
    for palabra in palabras:  # recorre las palabras en txt con txt
        if palabra in palabras_frecuentes:  # revisa si palabra esta en palabras_frecuentes
            palabras_frecuentes[palabra] += 1  # suma la palabra si ya esta en palabras_frecuentes
        else:
            palabras_frecuentes[palabra] = 1  # agrega la palabra a palabras_frecuentes

    for palabra, frecuencia in palabras_frecuentes.items():  # muestra la palabra, frecuencia en el diccionario de palabras frecuentes
        if frecuencia >= 15:  # si palabra aparece mas de 15 o 15 veces muestra la palabra y frecuencia
            print(f'La palabra "{palabra}" aparece un total de {frecuencia} veces')  # arroja esto


def longitud_palabras(txt):  # longitud promedio de las palabras

    # Divide la oración en palabras
    palabras = txt.split()
    longitud = len(palabras)

    if len(palabras) == 0:  # si no hay palabras arroja esto
        print("La oración no contiene palabras.")
        return

    # Calcula la longitud total de las palabras

    # longitud_total = 0

    # for palabra in palabras:
    #    longitud_total += len(palabra)

    longitud_total = sum(len(palabra) for palabra in
                         palabras)  # recorre la variable palabras con un for para tomar la longitud de palabra, y sumarlo

    # Calcula la longitud promedio
    longitud_promedio = longitud_total / longitud

    print(f"La longitud promedio de las palabras en la oración es: {longitud_promedio:.2f}")


with open('Noches blancas.txt', 'r') as txt:
    texto = txt.read()

contador_palabras_frecuentes(texto)
contador_palabras(texto)
longitud_palabras(texto)
