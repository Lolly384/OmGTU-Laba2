import telebot
import requests
from bs4 import BeautifulSoup

bot = telebot.TeleBot("5968418016:AAGt-psd0k9CU5C7sGoWdEt3Bw4-ec0ukM8")

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

@bot.message_handler(commands=['search'])
def handle_search_command(message):
    try:
        medicine_name= message.text.split()[1]
        result = search_medicine(medicine_name)
    except ValueError:
        result = "Введите команду в формате /search название_лекарства"
    bot.send_message(message.chat.id, result)

@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
    bot.send_message(message.chat.id, "Введите команду в формате /search название_лекарства")

bot.polling()