from entities import sites

sites_list = sites.sites_list()

for s in sites_list:
    s.scrap()
