class Carro:
    def __init__(self,marca,modelo,serie,color):
        self.marca = marca
        self.modelo = modelo
        self.serie = serie
        self.color = color

    def to_json(self):
        return self.__dict__