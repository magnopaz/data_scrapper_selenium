from entities import base_site as site


class Petz(site.Site):
    def __init__(self) -> None:
        super().__init__("Petz", "https://www.petz.com.br/", "")

    def scrap(self):
        self.driver.get(self.base_url)
        self.driver.close()