class Viitegeneraattori:
    
    def __init__(self):
        self._seuraava = 1

    def uusi(self):
        self._seuraava = self._seuraava + 1

        return self._seuraava

#Lisäys, Nyt muut moduulit voivat käyttää suoraan muuttujaan tallennttua oliota.       
viitegeneraattori = Viitegeneraattori()