from django.core.management.base import BaseCommand
from django.conf import settings
import telebot


# Объявление переменной бота
bot = telebot.TeleBot(settings.TELEGRAM_BOT_API_KEY)


# Название класса обязательно - "Command"
class Command(BaseCommand):
  	# Используется как описание команды обычно
    help = 'Implemented to Django application telegram bot setup command'



    @bot.message_handler(commands=['help', 'start'])
    def send_welcome(message):
        bot.reply_to(message, """\
/start.
/start\
""")

bot.infinity_polling()