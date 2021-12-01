#from _typeshed import Self
from enum import Enum
from tkinter import ttk, constants, StringVar
from sovelluslogiikka import Sovelluslogiikka

#Summa on luokka ja Summa(...) luokan olio. Tuossa self._kommenot = { Komento.SUMMA: Summa(...), ... } oliot laitetaan dictionaryyn
#voit siis tehdä esim. olio = self._komennot[Komento.SUMMA] ja olio.suorita()

#Komennoilla on nyt siis metodi suorita ja ne saavat konstruktorin kautta Sovelluslogiikka-olion ja funktion, 
#jota kutsumalla syötteen voi lukea.


class Komento(Enum):
    SUMMA = 1
    EROTUS = 2
    NOLLAUS = 3
    KUMOA = 4

class Summa:
    def __init__(self, sovelluslogiikka, kayttoliittyma_lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.luku_komento = kayttoliittyma_lue_syote
        self.arvo = 0

    def suorita(self):
        # kutsutaan käyttöliittymän metodia
        self.arvo = self.luku_komento()
        arvo = int(self.arvo)
        #print(arvo)
        # kutsutaan sovelluslogiikan metodia
        tulos = self.sovelluslogiikka.plus(arvo)
        #print(tulos)
    
class Erotus:
    def __init__(self, sovelluslogiikka, kayttoliittyma_lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.luku_komento = kayttoliittyma_lue_syote
        self.arvo = 0

    def suorita(self):
        # kutsutaan käyttöliittymän metodia
        self.arvo = self.luku_komento()
        arvo = int(self.arvo)
        #print(arvo)
        # kutsutaan sovelluslogiikan metodia
        tulos = self.sovelluslogiikka.miinus(arvo)
        #print(tulos)

class Nollaus:
    def __init__(self, sovelluslogiikka, kayttoliittyma_lue_syote):
        self.sovelluslogiikka = sovelluslogiikka
        self.luku_komento = kayttoliittyma_lue_syote
        self.arvo = 0

    def suorita(self):
        # kutsutaan sovelluslogiikan metodia
        self.sovelluslogiikka.nollaa()

class Kayttoliittyma:
    def __init__(self, sovelluslogiikka, root):
        # Sovelluslogiikka-olio
        self._sovelluslogiikka = sovelluslogiikka
        self._root = root

        self.komennot = {
            Komento.SUMMA: Summa(sovelluslogiikka, self._lue_syote),
            Komento.EROTUS: Erotus(sovelluslogiikka, self._lue_syote),
            Komento.NOLLAUS: Nollaus(sovelluslogiikka, self._lue_syote)
            #Komento.KUMOA: Kumoa(sovelluslogiikka, self._lue_syote)
        }

    def _lue_syote(self):
        return self._syote_kentta.get()

    def _suorita_komento(self, komento):
        komento_olio = self.komennot[komento]
        komento_olio.suorita()
        self._kumoa_painike["state"] = constants.NORMAL

        if self._sovelluslogiikka.tulos == 0:
            self._nollaus_painike["state"] = constants.DISABLED
        else:
            self._nollaus_painike["state"] = constants.NORMAL

        self._syote_kentta.delete(0, constants.END)
        self._tulos_var.set(self._sovelluslogiikka.tulos)
    
    def kaynnista(self):
        self._tulos_var = StringVar()
        self._tulos_var.set(self._sovelluslogiikka.tulos)
        self._syote_kentta = ttk.Entry(master=self._root)

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

