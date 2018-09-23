FROM python:3
d
RUN pip install youtube-dl feedparser

CMD [ "python", "./script.py" ]
