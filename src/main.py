from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from chromedriver_py import binary_path
from settings import sites

sites_list = sites.sites_list()

for s in sites_list:
    pass


driver = webdriver.Chrome(executable_path=binary_path)
driver.get('http://www.python.org')
assert 'Python' in driver.title
driver.close()
