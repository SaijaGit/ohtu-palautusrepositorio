class Ostoskori:
    def __init__(self):
        self._tuotteet = []
    
    def lisaa(self, tuote):
        self._tuotteet.append(tuote)
    
    def poista(self, tuote):
        paikka = -1
        for i, t in enumerate(self._tuotteet):
            if t == tuote:
                paikka = i
                break

        if paikka != -1:
            self._tuotteet.pop(paikka)


    def hinta(self):
        hinnat = map(lambda t: t.hinta, self._tuotteet)

        return sum(hinnat)
