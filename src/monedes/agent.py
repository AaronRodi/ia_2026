""" Mòdul que conté l'agent per jugar al joc de les monedes.

Percepcions:
    ClauPercepcio.MONEDES
Solució:
    " XXXC"
"""

from iaLib import agent

SOLUCIO = " XXXC"


class AgentMoneda(agent.Agent):
    def __init__(self):
        super().__init__(long_memoria=0)
        self.__oberts = None
        self.__tancats = None
        self.__accions = None

    def pinta(self, display):
        print(self._posicio_pintar)

    def actua(self, percepcio):

        if self.__accions:
             return self.__accion.pop(0),None

        estado_inicial = Estat(percepcio)
        self.__oberts = [estado_inicial]
        self.__tancats = []

        while self.__oberts:
            estadoOptimo = self.__oberts[0]
            for estado in self.__oberts:
                if estado.notaFinal < estadoOptimo.notaFinal:
                    estadoOptimo = estado
            self.__oberts.remove(estadoOptimo)
            self.__tancats.append(estadoOptimo)

            if "".join(estadoOptimo.tablero) == SOLUCIO:
                break

            pos_buit = estadoOptimo.tablero.index(" ")

            "desplaçament cost 1"
            "A la izquierda"
            if pos_buit > 0: 
                tablero_copia = estadoOptimo.tablero.copy()

                nueva_posicion_buit = pos_buit - 1
                tablero_copia[pos_buit], tablero_copia[pos_buit - 1] = tablero_copia[pos_buit - 1], tablero_copia[pos_buit] 

                nuevo_estado = Estat({"Monedes": tablero_copia}, estadoOptimo.costeA + 1, estadoOptimo, "D")
                self.__oberts.append(nuevo_estado)

            "A la derecha"
            if pos_buit < 4: 
                tablero_copia = estadoOptimo.tablero.copy()

                nueva_posicion_buit = pos_buit + 1
                tablero_copia[pos_buit], tablero_copia[pos_buit + 1] = tablero_copia[pos_buit + 1], tablero_copia[pos_buit] 

                nuevo_estado = Estat({"Monedes": tablero_copia}, estadoOptimo.costeA + 1, estadoOptimo, "D")
                self.__oberts.append(nuevo_estado)


            "Girar moneda"
            for i in range(5):
                if estadoOptimo.tablero[i] != " ":
                    tablero_copia = estadoOptimo.tablero.copy()
                    if tablero_copia[i] == "X":
                        tablero_copia[i] = "C"
                    else:
                        tablero_copia[i] = "X"

                    nuevo_estado = Estat ({"Monedes": tablero_copia}, estadoOptimo.costeA + 2, estadoOptimo, "G") 
                    self.__oberts.append(nuevo_estado)


            "Saltar con la moneda y girarla"

            if pos_buit >= 2:
                tablero_copia= estadoOptimo.tablero.copy()

                nueva_posicion_buit= pos_buit - 2
                tablero_copia[pos_buit], tablero_copia[nueva_posicion_buit] = tablero_copia[nueva_posicion_buit], tablero_copia[pos_buit]

                if tablero_copia[pos_buit] == "X":
                        tablero_copia[pos_buit] = "C"
                else:
                        tablero_copia[pos_buit] = "X"
                
                nuevo_estado = Estat ({"Monedes": tablero_copia}, estadoOptimo.costeA + 2, estadoOptimo, "B")
                self.__oberts.append(nuevo_estado)

            if pos_buit <= 2:
                tablero_copia= estadoOptimo.tablero.copy()

                nueva_posicion_buit= pos_buit + 2
                tablero_copia[pos_buit], tablero_copia[nueva_posicion_buit] = tablero_copia[nueva_posicion_buit], tablero_copia[pos_buit]
                if tablero_copia[pos_buit] == "X":
                        tablero_copia[pos_buit] = "C"
                else:
                        tablero_copia[pos_buit] = "X"              
                
                nuevo_estado = Estat ({"Monedes": tablero_copia}, estadoOptimo.costeA + 2, estadoOptimo, "B")
                self.__oberts.append(nuevo_estado)

        "historial de movimientos"
        lista_movimientos = []
        estado_actual = estadoOptimo
        
        while estado_actual.padre is not None:
            lista_movimientos.append(estado_actual.accion)
            estado_actual = estado_actual.padre
            
        lista_movimientos.reverse()
        self.__accions = lista_movimientos
        
        accion_a_realizar = self.__accions.pop(0)
        return accion_a_realizar, None




