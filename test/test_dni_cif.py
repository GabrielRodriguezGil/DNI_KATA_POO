from test.dni_correctos import CASOS_TEST_CORRECTOS
from test.dni_incorrectos import CASOS_TEST_LETRA_PROHIBIDA
from test.dni_formato_incorrecto import CASOS_TEST_FORMATO_INCORRECTO
import pytest
from src.dni_cif import Dni

@pytest.fixture(name="dni")
def inyector():
    return Dni()

def test_constructor_default(dni):
    assert dni.getDni() == ""
    assert not dni.getNumeroSano()
    assert not dni.getLetraSana()

def test_setters_getters(dni):
    dni.setDni("12345678Z")
    assert dni.getDni() == "12345678Z"

@pytest.mark.parametrize("dni_test", CASOS_TEST_CORRECTOS)
def test_check_cif_correcto(dni, dni_test):
    dni.setDni(dni_test)
    assert dni.checkCIF()

@pytest.mark.parametrize("dni_test", CASOS_TEST_LETRA_PROHIBIDA)
def test_check_cif_incorrecto(dni, dni_test):
    dni.setDni(dni_test)
    assert not dni.checkCIF()

@pytest.mark.parametrize("dni_test", CASOS_TEST_CORRECTOS)
def test_check_dni_correcto(dni, dni_test):
    dni.setDni(dni_test)
    assert dni.checkDni()

@pytest.mark.parametrize("dni_test", CASOS_TEST_FORMATO_INCORRECTO)
def test_check_dni_incorrecto(dni, dni_test):
    dni.setDni(dni_test)
    assert not dni.checkDni()

@pytest.mark.parametrize("dni_test", CASOS_TEST_CORRECTOS)
def test_check_letra_correcta(dni, dni_test):
    dni.setDni(dni_test)
    dni.checkDni()  # Necesario para establecer numeroSano
    assert dni.checkLetra()

@pytest.mark.parametrize("dni_test", CASOS_TEST_LETRA_PROHIBIDA)
def test_check_letra_incorrecta(dni, dni_test):
    dni.setDni(dni_test)
    dni.checkDni()  # Necesario para establecer numeroSano
    assert not dni.checkLetra()

@pytest.mark.parametrize("dni_test", CASOS_TEST_FORMATO_INCORRECTO)
def test_check_letra_numero_mal_formateado(dni, dni_test):
    dni.setDni(dni_test)
    dni.checkDni()  # Necesario para establecer numeroSano
    assert not dni.checkLetra()

@pytest.mark.parametrize("dni_test", CASOS_TEST_CORRECTOS)
def test_obtener_letra_correcta(dni, dni_test):
    dni.setDni(dni_test)
    dni.checkDni()  # Necesario para establecer numeroSano
    assert dni.obtenerLetra() == dni_test[-1]

def test_obtener_letra_sin_numero_sano(dni):
    dni.setDni("1234567X")  # DNI con longitud incorrecta
    assert dni.obtenerLetra() is None

def test_parte_alfabetica_dni(dni):
    dni.setDni("12345678Z")
    assert dni.getParteAlfabeticaDni() == "Z"

def test_parte_numerica_dni(dni):
    dni.setDni("12345678Z")
    dni.checkDni()  # Necesario para establecer numeroSano
    assert dni.getParteNumericaDni() == "12345678"

def test_parte_numerica_dni_sin_numero_sano(dni):
    dni.setDni("1234567")  # DNI incompleto
    assert not dni.getParteNumericaDni()