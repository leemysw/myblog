FROM python:3.6
LABEL maintainer=leemysw
ENV PYTHONUNBUFFERED 1
RUN mkdir /myweb
WORKDIR /myweb
COPY . /myweb
RUN pip install -r requirements.txt
# RUN pip install  -i  https://pypi.python.org/simple/  -r requirements.txt