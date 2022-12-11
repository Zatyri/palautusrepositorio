from kps import KiviPaperiSakset

class KPSPelaajaVsPelaaja(KiviPaperiSakset):
    def _toisen_siirto(self, _ = None):
        return input("Toisen pelaajan siirto: ")
