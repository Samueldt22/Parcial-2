import random 
import os
import pygame

filas = 10
columnas = 10
vida = ""
disparo_fallado = ""
player1 = "j1"

for y in range(filas):
    matriz.append
    for y in range(filas):
    matriz[y].append



def vida(x,y,matriz):
    return matriz[y][x] == vida

class jugador
    vida = 3
    pass
    def solicitar_coordenadas(jugador)
    y = none
    x = none
    while True
        letra_fila = input(
            "letra de la fila"
        )
        if len(letra_fila) != 1:
            print "debe ingresar una letra"
            continue
            if (coordenas_rango(0,y)):
                break
            else
                print("fila invalida")
        while True
            try:
                x = int(input("numero columna"))
                if coordenas_rango(x-1,0)
                x = x-1

                return x , y


class turno
    turno = 3
        if turno<=3 
        print("Se han acabo tus turnos")



class disparar 

    def dispararr(x,y,matriz)--> bool:
        if vida(x,y,matriz):
            matriz[y][x] = disparo_fallado
            return False
        elif matriz[y][x == disparo_fallado] or matriz[y][x] == disparo_acertado:
        return False
        elif :
            matriz[y][x] = disparo_acertado
            return True

    def jugar();
        disparos_j1 = disparos_inicial
        disparos_cpu = disparos_inicial
        defensa = 5
        matriz = obtener_vida()

        turno_actual = player1

        while True:
            print "turno de" [turno_actual]
            disparos_j1 = disparon_cpu
            if turno_actual == player1:
                matriz_oponente = matriz_cpu
                imprimir_matriz(matriz_oponente, False, oponente_player1,[turno_actual]) 

                acertado = disparar(x,y[turno_actual])

                if turno_actual == player1:
                    disparos_restantes_j1 -= 1
                else:
                    disparos_restantes_cpu -= 1

                imprimir_matriz(matriz_oponente,False)

                if acertado:
                    print("disparo acertado")
                    indicar_victoria((turno_actual))
                    imprimir_matriz(matriz_j1 , matriz_cpu)
                else disparo_fallado
                    print("disparon fallado")
                    indicar_fracaso(turno_actual)
                    imprimir_matriz(matriz_j1 , matriz_cpu)
                    break
                    turno_actual = oponente_player1(turno_actual)



class defensa

    def (tipo_de_defensa):
        pass

