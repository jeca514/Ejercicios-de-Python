from abc import ABC, abstractmethod


class Cliente:
    def __init__(self):
        self._nombre = ""

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
