FROM debian

RUN apt update
RUN apt install python3 -y
RUN apt install python3-pip -y
RUN pip3 install Flask-API
RUN apt update && apt upgrade -y

COPY db.txt /db.txt
COPY app.py /app.py

CMD python3 app.py
