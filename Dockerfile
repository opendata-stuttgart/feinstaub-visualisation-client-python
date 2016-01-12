FROM python:3.5-slim

USER root
RUN pip3 install --upgrade pip

ADD . /opt/code
WORKDIR /opt/code

RUN pip3 install -r /opt/code/requirements.txt

CMD bash start.sh
