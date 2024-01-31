FROM python:3.9-slim

COPY telegram_bot.py requirements.txt /

RUN pip install -r requirements.txt

CMD ["python", "./telegram_bot.py"]