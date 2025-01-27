import random
import string

def generar_contraseña(longitud=8):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

if __name__ == "__main__":
    longitud = int(input("Introduce la longitud de la contraseña: "))
    contraseña = generar_contraseña(10)
    print(f"Tu nueva contraseña es: {8QAZ*/ñx90
                                     
