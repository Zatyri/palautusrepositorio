KAPASITEETTI = 5
OLETUSKASVATUS = 5


class IntJoukko:
    def __init__(self, kapasiteetti=KAPASITEETTI, kasvatuskoko=OLETUSKASVATUS):

        if not isinstance(kapasiteetti, int) or kapasiteetti < 0:
            raise Exception("Väärä kapasiteetti") 
        else:
            self.kapasiteetti = kapasiteetti

        if not isinstance(kasvatuskoko, int) or kasvatuskoko < 0:
            raise Exception("Väärä kasvatuskoko")
        else:
            self.kasvatuskoko = kasvatuskoko

        self.lukujono = [0] * self.kapasiteetti

        self.alkioiden_lukumaara = 0

    def kuuluu_lukujonoon(self, luku):
        kuuluu = False

        for i in range(0, self.alkioiden_lukumaara):
            if luku == self.lukujono[i]:
                kuuluu = True
                break

        return kuuluu

    def lisaa(self, lisattava_luku):

        if self.alkioiden_lukumaara == 0:
            self.lukujono[0] = lisattava_luku
            self.alkioiden_lukumaara = self.alkioiden_lukumaara + 1            

        elif not self.kuuluu_lukujonoon(lisattava_luku):            
            self.lukujono[self.alkioiden_lukumaara] = lisattava_luku
            self.alkioiden_lukumaara = self.alkioiden_lukumaara + 1

            if self.alkioiden_lukumaara % len(self.lukujono) == 0:
                taulukko_old = self.lukujono    
                self.lukujono = [0] * (self.alkioiden_lukumaara + self.kasvatuskoko)
                self.kopioi_taulukko(taulukko_old, self.lukujono)

    def poista(self, poistettava_luku):
        for i in range(0, self.alkioiden_lukumaara):
            if poistettava_luku == self.lukujono[i]:
                del self.lukujono[i]
                self.alkioiden_lukumaara = self.alkioiden_lukumaara - 1
                break


    def kopioi_taulukko(self, lahde_taulukko, kohde_taulukko):
        for i in range(0, len(lahde_taulukko)):
            kohde_taulukko[i] = lahde_taulukko[i]

    def hae_alkioiden_lukumaara(self):
        return self.alkioiden_lukumaara

    def to_int_list(self):
        return self.lukujono[0:self.alkioiden_lukumaara]

    @staticmethod
    def yhdiste(eka, toka):
        int_joukko = eka

        for i in range(0, toka.alkioiden_lukumaara):
            int_joukko.lisaa(toka.lukujono[i])

        return int_joukko

    @staticmethod
    def leikkaus(eka, toka):
        int_joukko = IntJoukko()

        for i in range(0, eka.alkioiden_lukumaara):
            for j in range(0, toka.alkioiden_lukumaara):
                if eka.lukujono[i] == toka.lukujono[j]:
                    int_joukko.lisaa(toka.lukujono[j])

        return int_joukko

    @staticmethod
    def erotus(eka, toka):
        int_joukko = eka

        for i in range(0, toka.alkioiden_lukumaara):
            int_joukko.poista(toka.lukujono[i])

        return int_joukko

    def __str__(self):
        if self.alkioiden_lukumaara == 0:
            return "{}"
        elif self.alkioiden_lukumaara == 1:
            return "{" + str(self.lukujono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lukumaara - 1):
                tuotos = tuotos + str(self.lukujono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lukujono[self.alkioiden_lukumaara - 1])
            tuotos = tuotos + "}"
            return tuotos
