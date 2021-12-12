from tekoaly import Tekoaly
from kps import KPS

class KPSTekoaly(KPS):
    def __init__(self):
        self.tekoaly = Tekoaly()

    # toteutetaan metodi pelityypin mukaisesti: ihminen ja tekoäly
    def _toisen_siirto(self, ekan_siirto):
        tokan_siirto = self.tekoaly.anna_siirto()

        print(f"Tietokone valitsi: {tokan_siirto}")

        return tokan_siirto
