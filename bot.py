import threading
import config
import schedule
import time
import telebot
import requests
from bs4 import BeautifulSoup

# INIT BOT
bot = telebot.TeleBot(config.TOKEN)
chatid = config.chatid

## Send match info
def sendInfo():
    #GET RM match info
    url= "https://www.realmadrid.com/futbol/partidos/calendario"
    response = requests.get(url)
    html_doc = response.text
    soup = BeautifulSoup(html_doc, 'html.parser')
    elem = soup.findAll("div", {"class": "fecha_container"})
    texto = elem[0].text
    texto = texto.replace('\xa0',u' ')
    texto = texto.splitlines()
    while ("" in texto):
       texto.remove("")

    final = ' '.join(texto)
    bot.send_message(chatid, final)

# Send the info every day at 19:00
def daily_task():
    schedule.every().day.at('19:00').do(sendInfo)

    while True:
        schedule.run_pending()
        time.sleep(1)

# Handle /partido
@bot.message_handler(commands=['partido'])
def send_welcome(message):
    sendInfo()

## Main
# create a thread for the daily message
task = threading.Thread(target=daily_task)
task.start()

# start manage handler
bot.polling()
