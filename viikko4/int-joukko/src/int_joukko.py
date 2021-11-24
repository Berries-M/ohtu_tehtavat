OLETUSKAPASITEETTI = 5
OLETUSKASVATUS = 5

class IntJoukko:
    def __init__(self, kapasiteetti=None, kasvatuskoko=None):
        if kapasiteetti is None or kapasiteetti < 0 or not isinstance(kapasiteetti, int):
            self.kapasiteetti = OLETUSKAPASITEETTI
        else: self.kapasiteetti = kapasiteetti
        if kasvatuskoko is None or kasvatuskoko < 0 or not isinstance(kasvatuskoko, int):
            self.kasvatuskoko = OLETUSKASVATUS
        else: self.kasvatuskoko = kasvatuskoko
        self.lukujono = [0] * self.kapasiteetti
        self.alkioiden_lkm = 0

    def kuuluu(self, etsittava_luku):
        return etsittava_luku in self.lukujono

    def lisaa(self, lisattava_luku):
        if not self.kuuluu(lisattava_luku):
            self.lukujono[self.alkioiden_lkm] = lisattava_luku
            self.alkioiden_lkm += 1
            if self.alkioiden_lkm % len(self.lukujono) == 0:
                self.kopioi_taulukko()

    def poista(self, poistettava_luku):
        if poistettava_luku in self.lukujono: 
            self.lukujono.remove(poistettava_luku)
            self.alkioiden_lkm -=1
                
            if 0 in self.lukujono: self.lukujono.remove(0)
        
    def kopioi_taulukko(self):
        lukujono_vanha = self.lukujono.copy()
        self.lukujono = [0] * (self.alkioiden_lkm + self.kasvatuskoko)

        for i in range(0, len(lukujono_vanha)):
            self.lukujono[i] = lukujono_vanha[i]

    def mahtavuus(self):
        return self.alkioiden_lkm

    def to_int_list(self):
        taulu = [0] * self.alkioiden_lkm

        for i in range(0, len(taulu)):
            taulu[i] = self.lukujono[i]

        return taulu

    @staticmethod
    def yhdiste(alkuperaiset_luvut, lisattavat_luvut):
        yhdistetty_joukko = IntJoukko()
        a_taulu = alkuperaiset_luvut.to_int_list()
        b_taulu = lisattavat_luvut.to_int_list()

        for i in range(0, len(a_taulu)):
            yhdistetty_joukko.lisaa(a_taulu[i])

        for i in range(0, len(b_taulu)):
            yhdistetty_joukko.lisaa(b_taulu[i])

        return yhdistetty_joukko

    @staticmethod
    def leikkaus(ensimmaiset_luvut, toiset_luvut):
        joukkojen_leikkaus = IntJoukko()
        ensimmainen_joukko = ensimmaiset_luvut.to_int_list()
        toinen_joukko = toiset_luvut.to_int_list()

        for i in range(0, len(ensimmainen_joukko)):
            for j in range(0, len(toinen_joukko)):
                if ensimmainen_joukko[i] == toinen_joukko[j]:
                    joukkojen_leikkaus.lisaa(toinen_joukko[j])

        return joukkojen_leikkaus

    @staticmethod
    def erotus(alkuperaiset_luvut, poistettavat_luvut):
        vanhennetty_joukko = IntJoukko()
        alkuperainen_lista = alkuperaiset_luvut.to_int_list()
        poistettavien_lista = poistettavat_luvut.to_int_list()

        for i in range(0, len(alkuperainen_lista)):
            vanhennetty_joukko.lisaa(alkuperainen_lista[i])

        for i in range(0, len(poistettavien_lista)):
            vanhennetty_joukko.poista(poistettavien_lista[i])

        return vanhennetty_joukko

    def __str__(self):
        if self.alkioiden_lkm == 0:
            return "{}"
        elif self.alkioiden_lkm == 1:
            return "{" + str(self.lukujono[0]) + "}"
        else:
            tuotos = "{"
            for i in range(0, self.alkioiden_lkm - 1):
                tuotos = tuotos + str(self.lukujono[i])
                tuotos = tuotos + ", "
            tuotos = tuotos + str(self.lukujono[self.alkioiden_lkm - 1])
            tuotos = tuotos + "}"
            return tuotos
