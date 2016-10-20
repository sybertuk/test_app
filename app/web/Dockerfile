
#FROM ubuntu:latest
FROM tiangolo/uwsgi-nginx-flask:flask
RUN echo 'Creating image.'
RUN  apt-get update -y && \
     apt-get install -y python-pip \
	python-dev \
	build-essential \
	libmysqlclient-dev \
	nano
RUN pip install --upgrade pip
COPY ./app /app
WORKDIR /app
RUN pip install -r /app/requirements.txt
#ENTRYPOINT ["python2"]
#CMD ["main.py"]