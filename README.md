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
