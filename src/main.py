from entities import sites

sites_list = sites.sites_list()

for s in sites_list:
    pass


assert "Python" in driver.title
driver.close()
