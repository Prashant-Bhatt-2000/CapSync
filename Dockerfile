FROM python:3

ENV PYTHONBUFFERED 1
RUN mkdir capsync
WORKDIR /capsync_apis
COPY . /capsync_apis/
RUN pip install -r requirements.txt
