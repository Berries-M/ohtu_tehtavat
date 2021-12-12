from tuomari import Tuomari

class KPS:
    # Template-metodi
    def pelaa(self):
        tuomari = Tuomari()
        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            tuomari.kirjaa_siirto(ekan_siirto, tokan_siirto)
            print(tuomari)

            ekan_siirto = self._ensimmaisen_siirto()
            tokan_siirto = self._toisen_siirto(ekan_siirto)

        print("Kiitos!")
        print(tuomari)

    # Yhteinen kaikille
    def _ensimmaisen_siirto(self):
      return input("Ensimmäisen pelaajan siirto: ")

    # Yhteinen kaikille
    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
    
    # Oletustoteutus, override aliluokissa
    def _toisen_siirto(self, ekan_siirto):
        return "k"

    