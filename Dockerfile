FROM python:3.8

RUN pip install moviepy ffmpeg
WORKDIR /apps
