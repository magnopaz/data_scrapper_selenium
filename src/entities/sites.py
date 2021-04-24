from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from chromedriver_py import binary_path


class Site:
    name: str
    base_url: str
    driver: WebDriver
    suffix: list[str]

    def __init__(self, name: str, base_url: str, suffix):
        self.name = name
        self.base_url = base_url
        self.driver = webdriver.Chrome(executable_path=binary_path)
        self.suffix = suffix

    def scrap():
        pass


class Petz(Site):
    def __init__(self) -> None:
        super().__init__("Petz", "https://www.petz.com.br/")

    def scrap(self):
        self.driver.get(self.base_url)
        self.driver.close()


def sites_list():
    sites = []
    sites.append(Petz())
    return sites