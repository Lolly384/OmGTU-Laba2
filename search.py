import requests
from bs4 import BeautifulSoup
def search_medicine(medicine_name):
    url = f"https://xn----7sbatzcnpe0ae.xn--p1ai/search?q={medicine_name}"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")
    results = []
    for pharmacy in soup.find_all("div", class_="views-field"):
        blockPrice = pharmacy.find('div', class_="col-md-5")
        if blockPrice != None:
            name = blockPrice.find("a").text.strip()
            price = pharmacy.find("div", class_="price-new").text.strip()
            results.append(f"{name}\n{price}\n")
    if results:
        return "\n".join(results)
    else:
        return f"Аптек, где есть {medicine_name}, не найдено."