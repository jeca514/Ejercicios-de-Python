import unittest
from unittest.mock import patch
from BoletasCampinv2 import (
    mostrar_cesta,
    resumen_final,
    obtener_opcion,
    obtener_cantidad_boletas,
    desea_continuar,
    compra_boletas,
)


class TestBoletasCampin(unittest.TestCase):
    def setUp(self):
        self.lista_boletas = {
            "A": {"nombre": "Norte alta", "precio": 15000},
            "B": {"nombre": "Norte baja", "precio": 13000},
            "C": {"nombre": "Oriental alta", "precio": 10000},
            "D": {"nombre": "Occidental alta", "precio": 11000},
            "E": {"nombre": "Exclusivo", "precio": 20000},
        }

    def test_mostrar_cesta(self):
        cesta_de_compra = {
            "Norte alta": {"precio": 15000, "cantidad_boletas": 2},
            "Norte baja": {"precio": 13000, "cantidad_boletas": 1},
        }
        total, total_boletas = mostrar_cesta(cesta_de_compra)
        self.assertEqual(total, 43000)
        self.assertEqual(total_boletas, 3)

    def test_resumen_final(self):
        cesta_de_compra = {
            "Norte alta": {"precio": 15000, "cantidad_boletas": 2},
            "Norte baja": {"precio": 13000, "cantidad_boletas": 1},
        }
        with patch("builtins.print") as mocked_print:
            resumen_final(cesta_de_compra)
            mocked_print.assert_any_call("Total a pagar por 3 boletas: $43000")

    @patch("builtins.input", side_effect=["1", "6"])
    def test_obtener_opcion(self, mock_input):
        opcion = obtener_opcion()
        self.assertEqual(opcion, 1)

    @patch("builtins.input", side_effect=["2"])
    def test_obtener_cantidad_boletas(self, mock_input):
        cantidad_boletas = obtener_cantidad_boletas()
        self.assertEqual(cantidad_boletas, 2)

    @patch("builtins.input", side_effect=["s"])
    def test_desea_continuar_si(self, mock_input):
        continuar = desea_continuar()
        self.assertTrue(continuar)

    @patch("builtins.input", side_effect=["n"])
    def test_desea_continuar_no(self, mock_input):
        continuar = desea_continuar()
        self.assertFalse(continuar)


if __name__ == "__main__":
    unittest.main()
