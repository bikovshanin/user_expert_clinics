FROM python:3.11


WORKDIR /app

RUN pip install --upgrade pip
RUN pip install gunicorn
ADD ./requirements.txt /app/
RUN pip install -r requirements.txt

ADD ./backend /app/backend
ADD ./docker /app/docker

RUN chmod +x /app/docker/backend/server-entrypoint.sh
