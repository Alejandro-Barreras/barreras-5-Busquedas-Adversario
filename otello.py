"""

Juego de Otello

El estado se va a representar como una tupla de 64 elementos, 

0  1  2  3  4  5  6  7
8  9  10 11 12 13 14 15
16 17 18 19 20 21 22 23
24 25 26 27 28 29 30 31
32 33 34 35 36 37 38 39
40 41 42 43 44 45 46 47
48 49 50 51 52 53 54 55
56 57 58 59 60 61 62 63

donde cada elemento puede ser 0, 1 o -1. 0 representa una casilla vacía, 1 
representa una ficha del jugador 1 y -1 representa una ficha del jugador 2.

El estado terminal se alcanza cuando no hay más jugadas legales, o cuando
el tablero se llena completamente.

La ganancia es de 1 para el jugador 1 y -1 para el jugador 2. 0 si es 
empate.

"""

import juegos_simplificado as js
import minimax

class Otello(js.JuegoZT2):
    def inicializa(self):
        estado_inicial = [0 for _ in range(64)]
        estado_inicial[27] = -1
        estado_inicial[28] = 1
        estado_inicial[35] = 1
        estado_inicial[36] = -1
        return tuple(estado_inicial)


    def jugadas_legales(self, s, jugador):
        jugadas = []
        for i in range(64):
            if s[i] == 0:
                fila = i // 8
                col = i % 8
                jugada_valida = False
                for dx in [1, 0, -1]:
                    for dy in [1, 0, -1]:
                        if dx == 0 and dy == 0:
                            continue
                        x = col + dx
                        y = fila + dy
                        oponente_encontrado = False
                        while 0 <= x < 8 and 0 <= y < 8:
                            if s[y * 8 + x] == -jugador:
                                oponente_encontrado = True
                                x += dx
                                y += dy
                            elif s[y * 8 + x] == jugador and oponente_encontrado:
                                jugada_valida = True
                                break
                            else:
                                break
                        if jugada_valida:
                            break
                    if jugada_valida:
                        break
                if jugada_valida:
                    jugadas.append(i)
        return jugadas

    def sucesor(self, s, a, jugador):
        nuevo_estado = list(s)
        nuevo_estado[a] = jugador
        return tuple(nuevo_estado)
    
    def ganancia(self, s):
        if s.count(1) > s.count(-1):
            return 1
        elif s.count(1) < s.count(-1):
            return -1
        else:
            return 0

    def terminal(self, s):
        return not self.jugadas_legales(s, 1) and not self.jugadas_legales(s, -1)

class InterfaceOtello:
    def muestra_estado(self, s):
        for i in range(8):
            fila = s[i * 8:(i + 1) * 8]
            print(" | ".join(str(x) for x in fila))
            print("-" * 21)