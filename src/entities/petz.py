from entities import sites
from sites import Site


class Petz(Site):
    def scrap():
        self.driver.get("http://www.python.org")
        self.driver.close()