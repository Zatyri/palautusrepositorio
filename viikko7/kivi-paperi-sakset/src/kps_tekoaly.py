from kps import KiviPaperiSakset
from tuomari import Tuomari
from tekoaly import Tekoaly


class KPSTekoaly(KiviPaperiSakset):
    tekoaly = Tekoaly()

    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        return tokan_siirto