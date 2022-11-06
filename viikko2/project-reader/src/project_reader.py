from urllib import request

import toml
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")        

        tomlDict = toml.loads(content)["tool"]["poetry"]
        
        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(tomlDict["name"], tomlDict["description"], tomlDict["dependencies"], tomlDict["dev-dependencies"])
