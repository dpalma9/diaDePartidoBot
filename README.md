Telegram bot: diaDePartidoBot
=======================

## Overview
In order to inform when Real Madrid plays, this bot wll send you a daily notification when the day and the hour.

## Pre-requisites
This bot is written in Python3 so you need to install Python3 and pip3:

For Ubuntu:

```
$ apt install -y python3 python3-pip
```

It is been also needed the following pip packages:

```
$ pip install requests bs4 pytelegrambotapi schedule prettyconf
```

## Installation

```
$ echo 'TOKEN = "<token of your dev bot>"' > .env
$ echo 'CHATID = "<chat id>"' > .env
$ python bot.py
```

## Docker

It is also provided a Dockerfile to run the bot into a container.

## pyTelegramBotAPI

We need two things to run this bot:
 - The bot TOKEN.
 - The chat_id where the bot is running.

# TOKEN
You can get your TOKEN ID using @BotFather bot, asking for your bot TOKEN.

# Chat ID

For the chat ID, you can get it using the following URL once you add your bot to one chat group.

Steps: 

- Add the bot to a chat group.
- Go to the URI:
```bash
$ https://api.telegram.org/bot<YourBOTToken>/getUpdates
$ ## For example
$ https://api.telegram.org/bot123456789:jbd78sadvbdy63d37gda37bd8/getUpdates
```
Take the chat_id from the chat object.


This is the official GitHub: https://github.com/eternnoir/pyTelegramBotAPI
