from test.dni_correctos import CASOS_TEST_CORRECTOS
from test.dni_incorrectos import CASOS_TEST_LETRA_PROHIBIDA
from test.dni_formato_incorrecto import CASOS_TEST_FORMATO_INCORRECTO
import pytest
from src.dni_cif import Dni


@pytest.fixture(name="dni")
def inyector():
    return Dni()


def test_constructor_default(dni):
    assert dni.get_dni() == ""
    assert not dni.get_numero_sano()
    assert not dni.get_letra_sana()


def test_setters_getters(dni):
    dni.set_dni("12345678Z")
    assert dni.get_dni() == "12345678Z"


@pytest.mark.parametrize("dni_test", CASOS_TEST_CORRECTOS)
def test_check_cif_correcto(dni, dni_test):
    dni.set_dni(dni_test)
    assert dni.check_CIF()


@pytest.mark.parametrize("dni_test", CASOS_TEST_LETRA_PROHIBIDA)
def test_check_cif_incorrecto(dni, dni_test):
    dni.set_dni(dni_test)
    assert not dni.check_CIF()


@pytest.mark.parametrize("dni_test", CASOS_TEST_CORRECTOS)
def test_check_dni_correcto(dni, dni_test):
    dni.set_dni(dni_test)
    assert dni.check_valid_number()


@pytest.mark.parametrize("dni_test", CASOS_TEST_FORMATO_INCORRECTO)
def test_check_dni_incorrecto(dni, dni_test):
    dni.set_dni(dni_test)
    assert not dni.check_valid_number()


@pytest.mark.parametrize("dni_test", CASOS_TEST_CORRECTOS)
def test_check_letra_correcta(dni, dni_test):
    dni.set_dni(dni_test)
    dni.check_valid_number()  # Necesario para establecer numeroSano
    assert dni.check_valid_letter()


@pytest.mark.parametrize("dni_test", CASOS_TEST_LETRA_PROHIBIDA)
def test_check_letra_incorrecta(dni, dni_test):
    dni.set_dni(dni_test)
    dni.check_valid_number()  # Necesario para establecer numeroSano
    assert not dni.check_valid_letter()


@pytest.mark.parametrize("dni_test", CASOS_TEST_FORMATO_INCORRECTO)
def test_check_letra_numero_mal_formateado(dni, dni_test):
    dni.set_dni(dni_test)
    dni.check_valid_number()  # Necesario para establecer numeroSano
    assert not dni.check_valid_letter()


@pytest.mark.parametrize("dni_test", CASOS_TEST_CORRECTOS)
def test_obtener_letra_correcta(dni, dni_test):
    dni.set_dni(dni_test)
    dni.check_valid_number()  # Necesario para establecer numeroSano
    assert dni.get_alphabetic_part() == dni_test[-1]


def test_obtener_letra_sin_numero_sano(dni):
    dni.set_dni("1234567X")  # DNI con longitud incorrecta
    assert dni.calculate_letter() is None


def test_parte_alfabetica_dni(dni):
    dni.set_dni("12345678Z")
    assert dni.get_alphabetic_part() == "Z"


def test_parte_numerica_dni(dni):
    dni.set_dni("12345678Z")
    dni.check_valid_number()  # Necesario para establecer numeroSano
    assert dni.get_numeric_part() == "12345678"


def test_parte_numerica_dni_sin_numero_sano(dni):
    dni.set_dni("1234567")  # DNI incompleto
    assert not dni.get_numeric_part()
