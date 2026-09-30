
class Estat: 

    def __init__(self, percepcio, costeA: int, padre: Estat, accio: str):
        self.tablero = list(percepcio["Monedes"])
        self.costeA = 0
        self.padre = None
        self.__accio = None
        pos_actual = self.tablero.index(" ")
        self.p0 = pos_actual

        listaTemp = []
        listaGanadora = ["X","X","X","C"]
        self.penalizacion = 0
        for moneda in self.tablero:
            if moneda != " ":
                listaTemp.append(moneda)

        for i in range(len(listaTemp)):
            if listaTemp[i] != listaGanadora[i]:
                self.penalizacion = self.penalizacion + 1


        self.heuristica = self.p0 + self.penalizacion
        self.notaFinal = self.heuristica + self.costeA
            
