class kerdesek:
    def __init__(self, sor):
        obliterate = sor.split(";")
        self.pontozas = obliterate[0]
        self.kerdes = obliterate[1]
        self.valaszA = obliterate[2]
        self.valaszB = obliterate[3]
        self.valaszC = obliterate[4]

    def pontszam(self, index):
        if index == 0:
            return int(self.pontozas[0])
        if index == 1:
            return int(self.pontozas[1])
        if index == 2:
            return int(self.pontozas[2])

class szoveg:
    def __init__(self, sor):
        obliterate = sor.split(";")
        self.alsoPont = int(obliterate[0])
        self.felsoPont = int(obliterate[1])
        self.szoveg = obliterate[2]
