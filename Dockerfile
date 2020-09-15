ARG version=18.04
FROM ubuntu:${version}
RUN apt update && apt install -y python3 python3-pip
RUN pip3 install requests bs4 pytelegrambotapi schedule prettyconf config
WORKDIR /root
COPY bot.py .
COPY config.py .
CMD ["sleep", "infinity"]
ENTRYPOINT ["python3", "-m", "bot.py"]
