from modelo.modelEstado import Estado


class Semaforo:
    def __init__(self, estado_inicial, calle):
        self.estado = estado_inicial
        self.calle = calle

    def cambiar_estado(self):
        estados = {
            Estado.ROJO: Estado.VERDE,
            Estado.VERDE: Estado.AMARILLO,
            Estado.AMARILLO: Estado.ROJO,
        }

        self.estado = estados.get(self.estado)
