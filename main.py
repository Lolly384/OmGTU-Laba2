import telebot
import search


bot = telebot.TeleBot("5968418016:AAGt-psd0k9CU5C7sGoWdEt3Bw4-ec0ukM8")

@bot.message_handler(commands=['search'])
def handle_search_command(message):
    try:
        medicine_name = message.text.split()[1]
        result = search.search_medicine(medicine_name)
    except ValueError:
        result = "Введите команду в формате /search название_лекарства"
    bot.send_message(message.chat.id, result)

@bot.message_handler(func=lambda message: True)
def handle_all_message(message):
    bot.send_message(message.chat.id, "Введите команду в формате /search название_лекарства")

if __name__ == "__main__":
    bot.polling()