from test.dni_correctos import CASOS_TEST_CORRECTOS
from test.dni_incorrectos import CASOS_TEST_LETRA_PROHIBIDA
import pytest
from src.tabla_asignacion import TablaAsignacion


@pytest.fixture(name="tabla")
def tablaAsignacion():
    return TablaAsignacion()


def test_get_tabla(tabla):

    assert tabla.get_tabla() == [
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


def test_get_letra(tabla):
    assert tabla.get_letra(0) == "T"
    assert tabla.get_letra(22) == "E"
    assert tabla.get_letra(30) == "Posicion letra fuera de rango"


def test_is_letra_permitida(tabla):
    assert tabla.is_letra_permitida("T")
    assert not tabla.is_letra_permitida("I")


@pytest.mark.parametrize("dni", CASOS_TEST_CORRECTOS)
def test_calcular_letra_correcta(tabla, dni):
    numero_dni = dni[:-1]
    letra = dni[-1]
    assert tabla.get_letra_dni(numero_dni) == letra


@pytest.mark.parametrize("dni", CASOS_TEST_LETRA_PROHIBIDA)
def test_calcular_letra_incorrecta(tabla, dni):
    numero_dni = dni[:-1]
    letra = dni[-1]
    assert tabla.get_letra_dni(numero_dni) != letra