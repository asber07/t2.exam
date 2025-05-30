import random
import math

"""DIEGO ASPIROS BERMUDEZ - N00395102"""

def generar_coordenadas(cantidad):
    return [[random.randint(-81, 81), random.randint(-81, 81)] for _ in range(cantidad)]

def distancia(punto):
    return math.sqrt(punto[0]**2 + punto[1]**2)

def combinar(puntos_izq, puntos_der):

    if puntos_izq is None:
        return puntos_der
    if puntos_der is None:
        return puntos_izq
    if distancia(puntos_izq) > distancia(puntos_der):
        return puntos_izq
    else:
        return puntos_der

def divide_y_venceras(puntos):

    if len(puntos) == 0:
        return None
    if len(puntos) == 1:

        if puntos[0][0] > 0 and puntos[0][1] < 0:
            return puntos[0]
        else:
            return None
    medio = len(puntos) // 2
    izquierda = divide_y_venceras(puntos[:medio])
    derecha = divide_y_venceras(puntos[medio:])
    return combinar(izquierda, derecha)

def main():
    cantidad = int(input("¿Cuántos pares de coordenadas desea registrar? "))
    coordenadas = generar_coordenadas(cantidad)

    print("\nCoordenadas generadas:")
    for coord in coordenadas:
        print(coord)

    punto_mas_alejado = divide_y_venceras(coordenadas)

    if punto_mas_alejado:
        print(f"\nLa coordenada más alejada con X positivo e Y negativo es: {punto_mas_alejado} " +
              f"con distancia {distancia(punto_mas_alejado):.4f}")
    else:
        print("\nNo hay coordenadas con X positivo e Y negativo.")

if __name__ == "__main__":
    main()
