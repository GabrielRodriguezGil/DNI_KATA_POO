from test.dni_correctos import CASOS_TEST_CORRECTOS
from test.dni_incorrectos import CASOS_TEST_LETRA_PROHIBIDA
import pytest
from src.tabla_asignacion import TablaAsignacion


@pytest.fixture(name="tabla")
def tablaAsignacion():
    return TablaAsignacion()


def test_getTabla(tabla):

    assert tabla.getTabla() == [
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


def test_getLetra(tabla):
    assert tabla.getLetra(0) == "T"
    assert tabla.getLetra(22) == "E"
    assert tabla.getLetra(30) == "Posicion letra fuera de rango"


def test_getModulo(tabla):
    assert tabla.getModulo() == 23


def test_isLetraPermitida(tabla):
    assert tabla.isLetraPermitida("T")
    assert not tabla.isLetraPermitida("I")


@pytest.mark.parametrize("dni", CASOS_TEST_CORRECTOS)
def test_calcularLetra_correcta(tabla, dni):
    numero_dni = dni[:-1]
    letra = dni[-1]
    assert tabla.calcularLetra(numero_dni) == letra


@pytest.mark.parametrize("dni", CASOS_TEST_LETRA_PROHIBIDA)
def test_calcularLetra_incorrecta(tabla, dni):
    numero_dni = dni[:-1]
    letra = dni[-1]
    assert tabla.calcularLetra(numero_dni) != letra