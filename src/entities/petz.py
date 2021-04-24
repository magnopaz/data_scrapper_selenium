from entities import sites

class Petz(sites.Site):
    def __init__(self) -> None:
        super().__init__("Petz", "https://www.petz.com.br/")

    def scrap(self):
        self.driver.get(self.base_url)
        self.driver.close()