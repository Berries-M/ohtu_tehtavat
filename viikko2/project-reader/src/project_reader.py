from urllib import request
from project import Project
import toml
import tomli
import requests

class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")
        #print(content)

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
    

        # TÄMÄ EI TOIMI. MITEN PITÄISI TEHDÄ, JOTTA VOISI KÄYTTÄÄ TIEDOSTOA TALLENTAMATTA SITÄ ENSIN OMALLE KONEELLE?
        # url = "https://raw.githubusercontent.com/ohjelmistotuotanto-hy-avoin/python-kevat-2021/main/koodi/viikko3/web-login-robot/pyproject.toml"
        # tiedosto = requests.get(url, allow_redirects=True)
        # tiedosto2 = toml.load(tiedosto)
        
        # Tiedosto ladattu ja tallennettu ensin projektin kansioon nimellä data.toml
        sisalto = toml.load("data.toml")
        sisalto2 = sisalto["tool"]["poetry"]
        #print(sisalto)

        # Tämä muokattu uusiksi.
        #return Project("Test name", "Test description", [], [])
        
        return Project(sisalto2["name"], sisalto2["description"], sisalto2["dependencies"], sisalto2["dev-dependencies"])
