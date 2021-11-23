from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self.ostokset = []

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 
        return len(self.ostokset)
        
    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        korin_hinta = 0
        
        for ostos in self.ostokset:
            korin_hinta = korin_hinta + ostos.hinta()
        
        return korin_hinta

    def lisaa_tuote(self, lisattava: Tuote):
        ostos = Ostos(lisattava)

        if ostos not in self.ostokset:
            self.ostokset.append(ostos)
        else:
            ostos.muuta_lukumaara(1)


    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        pass

    def tyhjenna(self):
        pass
        # tyhjentää ostoskorin

    def ostokset(self):
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
        lista = []
        if len(self.ostokset) == 0:
            return lista

        else:
            return self.ostokset