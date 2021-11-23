from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote
        self.ostos_oliot_listalla = []

    def tavaroita_korissa(self):
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 
        tavaroiden_lukumaara_korissa = 0
        for x in self.ostos_oliot_listalla:
            tavaroiden_lukumaara_korissa = tavaroiden_lukumaara_korissa + x._lukumaara

        return tavaroiden_lukumaara_korissa
        
    def hinta(self):
        # kertoo korissa olevien ostosten yhteenlasketun hinnan
        korin_hinta = 0
        
        for ostos in self.ostos_oliot_listalla:
            korin_hinta = korin_hinta + ostos.hinta()
        
        return korin_hinta

    def lisaa_tuote(self, lisattava: Tuote):

        if any(x.tuote == lisattava for x in self.ostos_oliot_listalla):

            indeksi = -1

            # Etsitään indeksi, jossa on ostos, johon kuuluu haluttu tuote
            for x in self.ostos_oliot_listalla:
                indeksi = indeksi + 1
                if x.tuote == lisattava:
                    break

            # Muutetaan kyseisessä indeksissä olevan ostoksen lukumäärää.
            self.ostos_oliot_listalla[indeksi].muuta_lukumaaraa(1)

        else:
            ostos = Ostos(lisattava)
            self.ostos_oliot_listalla.append(ostos)


    def poista_tuote(self, poistettava: Tuote):
        # poistaa tuotteen
        indeksi = -1

        # Etsitään indeksi, jossa poistettava on 
        for x in self.ostos_oliot_listalla:
                indeksi = indeksi + 1
                if x.tuote == poistettava:
                    break

        # Muutetaan kyseisessä indeksissä olevan ostoksen lukumäärää.
        self.ostos_oliot_listalla[indeksi].muuta_lukumaaraa(-1)

        # Poisteaan koko tuote ostoslistalta, jos ei jäljellä.
        if self.ostos_oliot_listalla[indeksi].lukumaara() == 0:
            del self.ostos_oliot_listalla[indeksi]
            
    def tyhjenna(self):
        # tyhjentää ostoskorin
        self.ostos_oliot_listalla.clear()

    def ostokset(self):
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
        if len(self.ostos_oliot_listalla) == 0:
            return []

        else:
            return self.ostos_oliot_listalla