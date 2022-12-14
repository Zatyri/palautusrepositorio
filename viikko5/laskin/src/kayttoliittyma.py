from enum import Enum
from tkinter import ttk, constants, StringVar


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4


class Kayttoliittyma:
    def __init__(self, sovellus, root):
        self._sovellus = sovellus
        self._root = root
        self.edellinen_komento = Komento.NOLLAUS

        self._komennot = {
            Komento.SUMMA: Summa(self._sovellus, self._lue_syote),

            Komento.EROTUS: Miinus(self._sovellus, self._lue_syote),

            Komento.NOLLAUS: Nollaa(self._sovellus),

            Komento.KUMOA: Kumoa(self._sovellus)
        }

    def kaynnista(self):
        self._syote_kentta = ttk.Entry(master=self._root)
        self._tulos_var = StringVar()
        self._tulos_var.set(self._sovellus.tulos)

        tulos_teksti = ttk.Label(textvariable=self._tulos_var)

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
            command=lambda: self._suorita_komento(Komento.KUMOA)
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

        komento_olio = self._komennot[komento]

        komento_olio.suorita(self._komennot[self.edellinen_komento])
        self.edellinen_komento = komento 

        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovellus.tulos == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._tulos_var.set(self._sovellus.tulos)

class Summa:
    def __init__(self, sovellus, lue_syote):
        self.lue = lue_syote
        self.sovellus = sovellus
        self.edellinen_arvo = sovellus.tulos

    def suorita(self, olio):        
        arvo = int(self.lue())
        self.edellinen_arvo = self.sovellus.tulos
        self.sovellus.plus(arvo)

    def kumoa(self):
        self.sovellus.aseta_arvo(self.edellinen_arvo)


class Miinus:
    def __init__(self, sovellus, lue_syote):
        self.lue = lue_syote
        self.sovellus = sovellus
        self.edellinen_arvo = sovellus.tulos

    def suorita(self, olio):        
        arvo = int(self.lue())
        self.edellinen_arvo = self.sovellus.tulos
        self.sovellus.miinus(arvo)

    def kumoa(self):
        self.sovellus.aseta_arvo(self.edellinen_arvo)

class Nollaa:
    def __init__(self, sovellus):
        self.sovellus = sovellus
        self.edellinen_arvo = sovellus.tulos

    def suorita(self, olio):  
        self.edellinen_arvo = self.sovellus.tulos    
        self.sovellus.nollaa()

    def kumoa(self):        
        self.sovellus.aseta_arvo(self.edellinen_arvo)

class Kumoa:
    def __init__(self, sovellus):        
        self.sovellus = sovellus

    def suorita(self, olio):        
        olio.kumoa()

    def kumoa(self):
        pass
        
