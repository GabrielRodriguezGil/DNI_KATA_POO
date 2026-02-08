from src.tabla_asignacion import TablaAsignacion


class Dni:
    def __init__(self, cadena=""):
        self.dni = cadena
        self.numeroSano = False
        self.letraSana = False
        self.tabla = TablaAsignacion()
    

    def set_dni(self, cadena):
        self.dni = cadena
    
    def get_dni(self):
        return self.dni
    
    def get_numero_sano(self):
        return self.numeroSano
    
    def get_letra_sana(self):
        return self.letraSana
    
    def check_CIF(self):
        return self.check_DNI() and self.check_valid_letter()

    def check_DNI(self):
        if not self._check_lenght():
            return False
        if not self._check_number():
            return False
        self._set_numero_sano(True)
        return True
    
    def calculate_letter(self):
        if self.get_numero_sano():
            return self.tabla.get_letra_dni(self.get_numeric_part())
        return None
    ## Parte Privada ##

    def _set_numero_sano(self, valor):
        self.numeroSano = valor
    
    def _set_letra_sana(self, valor):
        self.letraSana = valor
    
    def _check_lenght(self):
        return len(self.get_dni()) == 9
    
    def _check_number(self):
        return self.get_dni()[:-1].isdigit()
    
    def check_valid_letter(self):
        if self.get_numero_sano():
            return self.get_alphabetic_part() == self.calculate_letter()
        return False
    
    def get_numeric_part(self):
        if self.get_numero_sano():
            return self.get_dni()[:-1]
        else:
            return False
    
    def get_alphabetic_part(self):
        return self.get_dni()[-1]