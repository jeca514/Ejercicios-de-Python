
class Guerrero:
    def __init__(self, faccion, raza):
        self._faccion = faccion
        self._raza = raza

    faccion_benevola = {
        1: "Ositos",
        2: "Principes",
        3: "Enanos",
        4: "Caris",
        5: "Fulos"
    }

    faccion_malvada = {
        1: "Lolos",
        2: "Fulanos",
        3: "Hoggis",
        4: "Lurcos",
        5: "Trollis"
    }

    victoria_benevola = {
        "Ositos": {"Lolos": 2, "Fulanos": 3, "Hoggis": 5, "Lurcos": 2, "Trollis": 1},
        "Principes": {"Lolos": 0.5, "Fulanos": 0.7, "Hoggis": 0.5, "Lurcos": 1, "Trollis": 0.3},
        "Enanos": {"Lolos": 0.3, "Fulanos": 0.5, "Hoggis": 1, "Lurcos": 0.3, "Trollis": 0.1},
        "Caris": {"Lolos": 2, "Fulanos": 1, "Hoggis": 5, "Lurcos": 2, "Trollis": 3},
        "Fulos": {"Lolos": 1, "Fulanos": 0.5, "Hoggis": 2, "Lurcos": 3, "Trollis": 0.7},
    }
    


