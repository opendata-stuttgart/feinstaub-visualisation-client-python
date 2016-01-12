FROM xblaster/tensorflow-jupyter

ADD . /opt/code
WORKDIR /opt/code

RUN pip install -r /opt/code/requirements.txt
CMD bash start.sh
