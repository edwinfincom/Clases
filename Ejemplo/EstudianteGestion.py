class EstudianteEjemplo:
    def __init__(self,nombre,codigo,promedio):
        self.nombre = nombre
        self.codigo = codigo
        self.promedio = promedio

    def to_json(self):
        return self.__dict__
    
