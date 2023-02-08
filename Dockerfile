# Dockerfile, Image, Container

FROM python:3.8
RUN pip install python-telegram-bot --upgrade
ADD main.py .
EXPOSE 5000
CMD ["python", "./main.py"]