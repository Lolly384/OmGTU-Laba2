import requests
from bs4 import BeautifulSoup

class MedicineSearch:
    def __init__(self):
        self.url = "https://xn----7sbatzcnpe0ae.xn--p1ai"

    def search_medicine(self, medicine_name):
        search_url = f"{self.url}/search?q={medicine_name}"
        response = requests.get(search_url)
        soup = BeautifulSoup(response.content, "html.parser")
        results = []
        for pharmacy in soup.find_all("div", class_="views-field"):
            blockPrice = pharmacy.find('div', class_="col-md-5")
            if blockPrice is not None:
                name = blockPrice.find("a").text.strip()
                price = pharmacy.find("div", class_="price-new").text.strip()
                results.append(f"{name}\n{price}\n")
        if results:
            return "\n".join(results)
        else:
            return f"Аптек, где есть {medicine_name}, не найдено."
