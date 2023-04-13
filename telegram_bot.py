import telebot
from medicine_search import MedicineSearch

class TelegramBot:
    def __init__(self, token):
        self.bot = telebot.TeleBot(token)
        self.medicine_search = MedicineSearch()

    def start(self):
        @self.bot.message_handler(commands=['search'])
        def handle_search_command(message):
            try:
                medicine_name = message.text.split()[1]
                result = self.medicine_search.search_medicine(medicine_name)
            except IndexError:
                result = "Введите команду в формате /search название_лекарства"
            self.bot.send_message(message.chat.id, result)

        @self.bot.message_handler(func=lambda message: True)
        def handle_all_message(message):
            self.bot.send_message(message.chat.id, "Введите команду в формате /search название_лекарства")

        self.bot.polling()
