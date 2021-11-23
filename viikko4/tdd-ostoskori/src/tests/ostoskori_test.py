import unittest
from ostoskori import Ostoskori
from tuote import Tuote
from ostos import Ostos

class TestOstoskori(unittest.TestCase):
    def setUp(self):
        self.kori = Ostoskori()

    # Tehtävä 1
    def test_ostoskorin_hinta_ja_tavaroiden_maara_alussa(self):
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(self.kori.tavaroita_korissa(), 0)
    
    # Tehtävä 2 ja 3
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_tavara_ja_hinta_oikein(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 1)
        self.assertEqual(self.kori.hinta(), 3)
      
    # Tehtävä 4 ja 5
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_on_kaksi_tavaraa_ja_hinta_oikein(self):
        maito = Tuote("Maito", 3)
        juusto = Tuote("Juusto", 2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(juusto)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
        self.assertEqual(self.kori.hinta(), 5)
    
    # Tehtävä 6 ja 7
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_on_kaksi_tavaraa_ja_hinta_oikein(self):
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(self.kori.tavaroita_korissa(), 2)
        self.assertEqual(self.kori.hinta(), 6)
    
    # Tehtävä 8
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio(self):
        # testaa että metodin palauttamin listan pituus 1
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        lista = self.kori.ostokset()
        self.assertEqual(len(lista), 1)
    
    # Tehtävä 9 ja 14
    def test_yhden_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
         # testaa täällä, että palautetun listan ensimmäinen ostos on halutunkaltainen.
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(len(self.kori.ostos_oliot_listalla), 1)
        ostos_tuote_nimi = str(self.kori.ostokset()[0].tuote._nimi)
        ostos_tuote_maara = self.kori.ostokset()[0]._lukumaara
        self.assertEqual(ostos_tuote_nimi, "Maito")
        self.assertEqual(ostos_tuote_maara, 1)
        self.kori.poista_tuote(maito)
        self.assertEqual(self.kori.hinta(), 0)
        self.assertEqual(len(self.kori.ostokset()), 0)
    
    # Tehtävä 10 ja 15
    def test_kahden_eri_tuotteen_lisaamisen_jalkeen_korissa_kaksi_ostosoliota_joilla_oikea_tuotteen_nimi_ja_maara(self):
        maito = Tuote("Maito", 3)
        juusto = Tuote("Juusto", 2)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(juusto)
        self.assertEqual(len(self.kori.ostos_oliot_listalla), 2)
        ostos_tuote_nimi = str(self.kori.ostokset()[0].tuote._nimi)
        ostos_tuote_maara = self.kori.ostokset()[0]._lukumaara
        self.assertEqual(ostos_tuote_nimi, "Maito")
        self.assertEqual(ostos_tuote_maara, 1)
        ostos_tuote_nimi = str(self.kori.ostokset()[1].tuote._nimi)
        ostos_tuote_maara = self.kori.ostokset()[1]._lukumaara
        self.assertEqual(ostos_tuote_nimi, "Juusto")
        self.assertEqual(ostos_tuote_maara, 1)
        self.kori.tyhjenna()
        self.assertEqual(len(self.kori.ostokset()), 0)
    
    # Tehtävä 11, 12, 13
    def test_kahden_saman_tuotteen_lisaamisen_jalkeen_korissa_yksi_ostosolio_jolla_oikea_tuotteen_nimi_ja_maara(self):
         # testaa täällä, että palautetun listan ensimmäinen ostos on halutunkaltainen.
        maito = Tuote("Maito", 3)
        self.kori.lisaa_tuote(maito)
        self.kori.lisaa_tuote(maito)
        self.assertEqual(len(self.kori.ostos_oliot_listalla), 1)
        ostos_tuote_nimi = str(self.kori.ostokset()[0].tuote._nimi)
        ostos_tuote_maara = self.kori.ostokset()[0]._lukumaara
        self.assertEqual(ostos_tuote_nimi, "Maito")
        self.assertEqual(ostos_tuote_maara, 2)
        self.kori.poista_tuote(maito)
        ostos_tuote_maara_uusi = self.kori.ostokset()[0]._lukumaara
        self.assertEqual(ostos_tuote_maara_uusi, 1)
