KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def _luo_lista(self, koko):
        return [0] * koko
    
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatus=None):
        self.kapasiteetti = kapasiteetti
        self.kasvatus = kasvatus or OLETUSKASVATUS
        self.lukujono = self._luo_lista(self.kapasiteetti)
        self.alkioiden_lkm = 0


    def kuuluu(self, n):
        return n in self.lukujono


    def lisaa(self, n):

        if self.kuuluu(n):
            return False

        if self.alkioiden_lkm == self.kapasiteetti:
            self.kasvata_listaa()

        self.lukujono[self.alkioiden_lkm] = n
        self.alkioiden_lkm +=1
        return True
    

    def kasvata_listaa(self):
        vanha_lista = [i for i in self.lukujono]
        self.lukujono = self._luo_lista(self.kapasiteetti + self.kasvatus)
        self.kapasiteetti += self.kasvatus

        self.kopioi_lista(vanha_lista, self.lukujono)


    def lisaa_monta(self, lukulista):
        for luku in lukulista:
            self.lisaa(luku)


    def poista(self, n):
        if not self.kuuluu(n):
            return False
        
        kohta = self.lukujono.index(n)
        self.lukujono.pop(kohta)
        self.alkioiden_lkm -=1
        return True


    def kopioi_lista(self, lahde, kohde):
        for i in range(len(lahde)):
            kohde[i] = lahde[i]


    def mahtavuus(self):
        return self.alkioiden_lkm


    def to_int_list(self):
        return self.lukujono[:self.alkioiden_lkm].copy()
    


    @staticmethod
    def yhdiste(a, b):
        a.lisaa_monta(b.to_int_list())
        return a


    @staticmethod
    def leikkaus(a, b):
        for luku in a.to_int_list():
            if not b.kuuluu(luku):
                a.poista(luku)

        return a


    @staticmethod
    def erotus(a, b):
        for luku in a.to_int_list():
            if b.kuuluu(luku):
                a.poista(luku)

        return a
    

    def __str__(self):
        return str(self.to_int_list()).replace('[', '{').replace(']', '}')