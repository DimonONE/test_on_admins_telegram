import telebot
import time
import config
from mwt import MWT

bot = telebot.TeleBot(config.TOKEN)

# кароткое создание методов
class ADD_PRODUCT:
    def __init__(self):
        data_set = ['categorie', 'name_product', 'color', 'price', 'wight']
        for data in data_set:
            self.data = None

@MWT(timeout=60*60)
def get_admin_ids(bot, chat_id):
    return [admin.user.id for admin in bot.get_chat_administrators(chat_id)]


@bot.message_handler(commands=['create'])
def start_message(message):
    if message.from_user.id in get_admin_ids(bot, message.chat.id):
        bot.send_message(
            message.chat.id, text=" * Создание нового товара: * ", reply_markup=Product.add())
    else:
#       Удаление сообщения  
        bot.delete_message(message.chat.id,
                               message.message_id)
        bot.send_message(
            message.chat.id, text=" * Ви не админ!!!: * ")


if __name__ == '__main__':
    bot.polling(none_stop=True)
