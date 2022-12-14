from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    

    def __init__(self):
        self.lista = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        return len(self.lista)
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        summa = 0
        for tuote in self.lista:
            summa = summa + tuote.hinta()
        return summa
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):       
        loytyi = False
        for ostos in self.lista:            
            if ostos.tuotteen_nimi() == lisattava.nimi():
                ostos.muuta_lukumaaraa(1)
                loytyi = True
                break
        if not loytyi:
            self.lista.append(Ostos(lisattava))
        

    def poista_tuote(self, poistettava: Tuote):
        for ostos in self.lista:            
            if ostos.tuotteen_nimi() == poistettava.nimi():
                ostos.muuta_lukumaaraa(-1)
                if ostos.lukumaara() == 0:
                    self.lista.remove(ostos)  
                break    

    def tyhjenna(self):
        self.lista = []
        # tyhjentää ostoskorin

    def ostokset(self):
        return self.lista
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
