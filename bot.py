import config
import schedule
import time
import telebot
import requests
from bs4 import BeautifulSoup

# INIT BOT
bot = telebot.TeleBot(config.TOKEN)
chatid = config.chatid

## Send info method
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

## Main
# send the info everyday at 19:00
schedule.every().day.at('19:00').do(sendInfo)

while True:
    schedule.run_pending()
    time.sleep(1)
