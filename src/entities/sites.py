from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from chromedriver_py import binary_path


class Site:
    name: str
    base_url: str
    driver = driver = webdriver.Chrome(executable_path=binary_path)

    def __init__(self, name: str, base_url: str):
        self.name = name
        self.base_url = base_url


def sites_list():
    sites = []
    sites.append(Site("Petz", "https://www.petz.com.br/"))
    return sites