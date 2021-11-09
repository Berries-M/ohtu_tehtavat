from kauppa import Kauppa

def main():
    #Näitä ei enää tarvita, myös aiemmat importit poistettu
    #viitegeneraattori = Viitegeneraattori()
    #kirjanpito = Kirjanpito()
    #varasto = Varasto(kirjanpito)
    #pankki = Pankki(kirjanpito)
    #kauppa = Kauppa(varasto, pankki, viitegeneraattori)

    # Tämä tullut tilalle
    kauppa = Kauppa()

    # kauppa hoitaa yhden asiakkaan kerrallaan seuraavaan tapaan:
    kauppa.aloita_asiointi()
    kauppa.lisaa_koriin(1)
    kauppa.lisaa_koriin(3)
    kauppa.lisaa_koriin(3)
    kauppa.poista_korista(1)
    kauppa.tilimaksu("Pekka Mikkola", "1234-12345")

    # seuraava asiakas
    kauppa.aloita_asiointi()

    for _ in range(0, 24):
        kauppa.lisaa_koriin(5)

    kauppa.tilimaksu("Arto Vihavainen", "3425-1652")

    # kirjanpito
    # Tätä muokattu, reitti tapahtumiiin korjattu
    for tapahtuma in kauppa._pankki._kirjanpito.tapahtumat:
        print(tapahtuma)


if __name__ == "__main__":
    main()
