FROM ubuntu

WORKDIR /source

COPY source /source/

RUN apt-get update \
&& apt-get install -y python3 \
&& apt-get install -y python3-pip \
&& pip install -r requirements.txt

CMD ["python3","router.py"]