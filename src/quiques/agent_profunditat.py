""" Fitxer que conté l'agent barca en profunditat.

S'ha d'implementar el mètode:
    actua()
"""
import abc

from quiques.agent import Barca
from quiques.estat import Estat


class BarcaProfunditat(Barca):
    def __init__(self):
        super(BarcaProfunditat, self).__init__()
        

    @abc.abstractmethod
    def actua(self, percepcio: dict) -> str | tuple[str, (int, int)]:

        EstadoInicial = Estat(percepcio["local_barca"],percepcio["llops_esq"],percepcio["quica_esq"])
        pila = [EstadoInicial]
        visitados = set()

        while pila:
            EstadoActual = pila.pop()
            if EstadoActual.es_meta():
                return EstadoActual.cami[0]

            if(EstadoActual.es_segur() and EstadoActual not in visitados):
                visitados.add(EstadoActual)
                Hijos = EstadoActual.genera_fill()
                for Hijo in Hijos:
                    pila.append(Hijo)
                




