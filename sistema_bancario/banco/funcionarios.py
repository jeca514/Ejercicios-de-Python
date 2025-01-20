class Trabajadores:
    def __init__(self, empleado, sueldo_base, rendimiento):
        self._empleado = empleado
        self._divisa = "COP$"
        if isinstance(sueldo_base, float):
            self._sueldo_base = sueldo_base
        else:
            print("sueldo no valido se establecera en $1000000")
            self._sueldo_base = 1000000

        if isinstance(rendimiento, int) and 5 >= rendimiento >= 1:
            self._rendimiento = rendimiento
        else:
            print("rendimiento no valido se establcera en 1")
            self._rendimiento = 1

    @property
    def empleado(self):
        return self._empleado

    @property
    def sueldo_base(self):
        return self._sueldo_base

    @sueldo_base.setter
    def sueldo_base(self, sueldo_base):
        if isinstance(sueldo_base, float) and sueldo_base > 0:
            self._sueldo_base = sueldo_base
        else:
            raise ValueError("Suelldo inválido: debe ser un número flotante positivo.")

    @property
    def rendimiento(self):
        return self._rendimiento

    @rendimiento.setter
    def rendimiento(self, rendimiento_nuevo):
        if not isinstance(rendimiento_nuevo, int) or not (1 <= rendimiento_nuevo <= 5):
            raise ValueError("El rendimiento debe ser un número entero entre 1 y 5.")
        self._rendimiento = rendimiento_nuevo

    @property
    def divisa(self):
        return self._divisa

    def sueldo_total(self):
        bono = {1: 1.0, 2: 1.05, 3: 1.1, 4: 1.15, 5: 1.20}
        bono_porcentaje = bono.get(self.rendimiento, 1)
        sueldo_total = self.sueldo_base * bono_porcentaje
        return sueldo_total

    def mostrar_detalles_empleado(self):
        print("\n=== Detalles de la Cuenta ===")
        print(f"empleado: {self.empleado}")
        print(f"nivel de rendimiento: Nivel {self.rendimiento}")
        print(f"Sueldo total: {self.sueldo_total} {self.divisa}")
        print("=============================\n")
