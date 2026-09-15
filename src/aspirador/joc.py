from iaLib import agent, joc

class Aspirador(joc.JocNoGrafic):

    

    def __init__(self, agents: list[agent.Agent] | None = None):
        self.habitaciones = [True,False] 
        #true=limpio, false=sucio

        self.posicion_robot = 0 
        #izquierda=0, derecha=1
        if agents is None:
            agents = []
        super(Aspirador, self).__init__(agents=agents)


    def _draw(self):

        #Si esta el robot R
        #X si esta limpio
        #O si esta sucio
        #izquierda=0, derecha=1

        if self.habitaciones[0] == True: #habitacion izquierda
            state_izq = "X"
        else:
            state_izq = "O"

        if self.habitaciones[1] == True: #habitacion derecha
            state_der = "X"
        else:
            state_der = "O"

        if self.posicion_robot == 0:
            t_izq = state_izq + "R"
            t_der = state_der + " "
        else:
            t_der = state_der + "R"
            t_izq = state_izq + " "

        print(f"Habitaciones: [{t_izq}] [{t_der}]")
        


    def percepcio(self):

        percepcion = self.posicion_robot,self.habitaciones[self.posicion_robot]
        return percepcion
        


    def _aplica(self, accio, params=None, agent_actual=None):
    
    #acciones posibles en el juego
    # limpiar la habitacion actual = 3
        #cambiamos el estado de la habitacion [0,1]
    # cambiare de habitacion derecha = 4
        #ya esta en la habitacion derecha o cambia
    # cambiare de habitacion izquierda = 2
        #ya esta en la habitacion izquierda o cambia

        if self.accio == 2:
            if self.posicion_robot == 0:
                print("no es posible, limite maximo")
            else:
                self.posicion_robot = 0
                print("se ha cambiado con exito de habitacion")

        if self.accio == 3:
            if self.habitaciones[posicion_robot] == True:
                print("no es posible, la habitacion esta limpia")
            else:
                self.habitaciones[posicion_robot] = True
                print("se ha limpiado con exito la habitacion")

        
        if self.accio == 4:
            if self.posicion_robot == 1:
                print("no es posible, limite maximo")
            else:
                self.posicion_robot = 1
                print("se ha cambiado con exito de habitacion")


        
