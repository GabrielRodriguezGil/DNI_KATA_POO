class TablaAsignacion():
    def __init__(self):
        self.tabla = [
            "T",
            "R",
            "W",
            "A",
            "G",
            "M",
            "Y",
            "F",
            "P",
            "D",
            "X",
            "B",
            "N",
            "J",
            "Z",
            "S",
            "Q",
            "V",
            "H",
            "L",
            "C",
            "K",
            "E",
        ]

    def get_tabla(self):
        return self.tabla
    
    def get_letra(self, indice):
        try:
            return self.get_tabla()[indice]
        except IndexError:
            return "Posicion letra fuera de rango"
    
    def is_letra_permitida(self, letra):
        return letra in self.get_tabla()
    
    def get_letra_dni(self,numeros_dni):
        indice = int(numeros_dni) % 23
        return self.get_letra(indice)
