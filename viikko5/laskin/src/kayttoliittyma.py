from enum import Enum
from tkinter import ttk, constants, StringVar


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3

class BinaariOperaatio:
    def __init__(self, sovelluslogiikka, lue_syote):
        self._sovellus = sovelluslogiikka
        self._lue_syote = lue_syote
        self.edellinen = None

    def suorita(self):
        return 0
    
    def kumoa(self):
        #print("Kumoa: arvo = ", self._sovellus.arvo(), " self.edellinen = ", self.edellinen)
        self._sovellus.aseta_arvo(self.edellinen)
        self.edellinen = None
        #print("Kumoa: arvo = ", self._sovellus.arvo(), " self.edellinen = ", self.edellinen)

    def aseta_edellinen(self, arvo):
        self.edellinen = arvo


class Summa(BinaariOperaatio):
    def __init__(self, sovelluslogiikka, lue_syote):
        super().__init__(sovelluslogiikka, lue_syote)

    def suorita(self):
        self.aseta_edellinen(self._sovellus.arvo())
        #print("Summa: self.edellinen = ", self.edellinen)
        luku = int(self._lue_syote())
        self._sovellus.plus(luku)
        #print("Summa: arvo = ", self._sovellus.arvo())


class Erotus(BinaariOperaatio):
    def __init__(self, sovelluslogiikka, lue_syote):
        super().__init__(sovelluslogiikka, lue_syote)

    def suorita(self):
        self.aseta_edellinen(self._sovellus.arvo())
        #print("Erotus: self.edellinen = ", self.edellinen)
        luku = int(self._lue_syote())
        self._sovellus.miinus(luku)
        #print("Erotus: arvo = ", self._sovellus.arvo())


class Nollaus(BinaariOperaatio):
    def __init__(self, sovelluslogiikka, lue_syote):
        super().__init__(sovelluslogiikka, lue_syote)

    def suorita(self):
        self.aseta_edellinen(self._sovellus.arvo())
        #print("Nollaus: self.edellinen = ", self.edellinen)
        self._sovellus.nollaa()
        #print("Nollaus: arvo = ", self._sovellus.arvo())


class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        self._sovelluslogiikka = sovelluslogiikka
        self._root = root
        self._viimeinen_komento = None

        self._komennot = {
            Komento.SUMMA: Summa(sovelluslogiikka, self._lue_syote),
            Komento.EROTUS: Erotus(sovelluslogiikka, self._lue_syote),
            Komento.NOLLAUS: Nollaus(sovelluslogiikka, self._lue_syote)
        }

    def kaynnista(self):
        self._arvo_var = StringVar()
        self._arvo_var.set(self._sovelluslogiikka.arvo())
        self._syote_kentta = ttk.Entry(master=self._root)

        tulos_teksti = ttk.Label(textvariable=self._arvo_var)

        summa_painike = ttk.Button(
            master=self._root,
            text="Summa",
            command=lambda: self._suorita_komento(Komento.SUMMA)
        )

        erotus_painike = ttk.Button(
            master=self._root,
            text="Erotus",
            command=lambda: self._suorita_komento(Komento.EROTUS)
        )

        self._nollaus_painike = ttk.Button(
            master=self._root,
            text="Nollaus",
            state=constants.DISABLED,
            command=lambda: self._suorita_komento(Komento.NOLLAUS)
        )

        self._kumoa_painike = ttk.Button(
            master=self._root,
            text="Kumoa",
            state=constants.DISABLED,
            command=lambda: self._kumoa(self._viimeinen_komento)
        )

        tulos_teksti.grid(columnspan=4)
        self._syote_kentta.grid(columnspan=4, sticky=(constants.E, constants.W))
        summa_painike.grid(row=2, column=0)
        erotus_painike.grid(row=2, column=1)
        self._nollaus_painike.grid(row=2, column=2)
        self._kumoa_painike.grid(row=2, column=3)


    def _lue_syote(self):
        return self._syote_kentta.get()

    def _suorita_komento(self, komento):
        #print("_suorita_komento: komento = ", komento)
        komento_olio = self._komennot[komento]
        self._viimeinen_komento = komento_olio
        komento_olio.suorita()
        #print("_suorita_komento: edellinen = ",  komento_olio.edellinen)

        if self._viimeinen_komento == None:
            self._kumoa_painike["state"] = constants.DISABLED
        else:
            self._kumoa_painike["state"] = constants.NORMAL


        if self._sovelluslogiikka.arvo() == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._arvo_var.set(self._sovelluslogiikka.arvo())

    def _kumoa(self, komento):
        #print("_kumoa: komento = ", komento)
        if self._viimeinen_komento is not None:
            self._viimeinen_komento.kumoa()
            self._kumoa_painike["state"] = constants.DISABLED
            self._viimeinen_komento = None


        self._arvo_var.set(self._sovelluslogiikka.arvo())
