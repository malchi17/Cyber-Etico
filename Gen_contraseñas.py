import random
import string

def generar_contraseña(longitud=12):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

if __name__ == "__main__":
    longitud = int(input("Introduce la longitud de la contraseña: "))
    print("Contraseña generada:", generar_contraseña(longitud))