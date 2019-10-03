# импортируем нужные компонены. у библиотеки телеграмм есть модуль ext и в нём есть компонент Updater, т.е. это папки и файлики см. github.com python telegram bot. В папке ext есть файл updater.py. В нём есть класс Updater, который соединятеся с платформой телеграм на наличие новых сообщений
# Командхендлер - для обработки команд, если и когда к нам придёт комнада старт мы выполним какую-то функцию
# Мессаджхендлер - обработчик сообщений, Фильтрс - для того чтобы взаимодействовать с текстом
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import logging
import settings

# Настройки прокси
PROXY = {'proxy_url': 'socks5://t2.learn.python.ru:1080', # PROXY - это константа, поэтому написана КАПСОМ, т.е. её менять нельзя! Словарь: строка, скокс 5 это протокол, ссылка на прокси адрес + порт
    'urllib3_proxy_kwargs': {'username': 'learn', 'password': 'python'}} # имя пользователяи и пароль 

# Логи
logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', # asctime- дата/время, name - имя файлав котором что-то произошло, level - уровень важности события, message - сообщение 
                    level=logging.INFO, # уровень инфо уровень ворнинг и уровень эррор. Ворниг - только ворниг и эрор, если эрор то только эррор
                    filename='bot.log'
                    )

def greet_user(bot, update): # функция вызывается на команду /start и отвечает пользователю. bot - экземпляр нашего бота при помощи которого мы сможем им управлять. update - сообщение которое пришло к нам на экран
    text = 'Вызван /start' 
    print(text)
    update.message.reply_text(text)

def talk_to_me(bot, update):
    user_text = "Привет, {}! Ты написал {}".format(update.message.chat.first_name, update.message.text) # имя + то что пришло в мессадж текст
    logging.info('User: %s, Chat id: %, Message: %s, update.message.chat.username, update.message.chat.chat.id, update.message.chat.text')
    update.message.reply_text(user_text) # отправляем п-лю текстом который прислал нам текст, т.е. эхо


# функция которая соединяет с платформой телеграм "тело" нашего бота. mybot (переменная) - Это объект класса Updater. # начни регулярно ходить на платформу телеграм и начни проверять наличие сообщений. mybot будет работать пока мы его не остановим
def main(): 
    mybot = Updater(settings.API_KEY, request_kwargs=settings.PROXY)
    
    dp = mybot.dispatcher # спец объект принимает входящие сообщение и раскидывает по получаетелям, анпримре на команд хендлера
    dp.add_handler(CommandHandler('start', greet_user)) # На команду старт вешают приветственный текст, старт пишем без /. greet_user - это функция которая сработает на /start
    dp.add_handler(MessageHandler(Filters.text, talk_to_me)) # реагировать на текстовые сообщения + функция
    
    mybot.start_polling()
    mybot.idle()

# вызываем функцию
main()