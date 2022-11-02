FROM python:3.10

EXPOSE 5007

RUN mkdir -p /opt/services/bot/ismar_bot
WORKDIR /opt/services/bot/geektech-bot


COPY . /opt/services/bot/ismar_bot/

RUN pip install -r requirements.txt

CMD ["python", "/opt/services/bot/ismar_bot/main.py"]