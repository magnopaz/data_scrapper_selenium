from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.keys import Keys
from chromedriver_py import binary_path


class Site:
    name: str
    base_url: str
    driver: WebDriver

    def __init__(self, name: str, base_url: str):
        self.name = name
        self.base_url = base_url
        self.driver = webdriver.Chrome(executable_path=binary_path)

    def scrap():
        pass


def sites_list():
    sites = []
    sites.append(Site("Petz", "https://www.petz.com.br/"))
    return sites