class Site:
    name: str
    base_url: str

    def __init__(self, name: str, base_url: str):
        self.name = name
        self.base_url = base_url


def sites_list():
    sites = []
    sites.append(Site("Petz", ""))
    return sites