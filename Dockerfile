FROM python:3
d
RUN pip install youtube-dl

CMD [ "python", "./script.py" ]
