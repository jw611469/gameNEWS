FROM ubuntu

RUN apt-get update \
&& apt-get install -y nginx \
&& rm -rf /etc/nginx/sites-enabled/default


COPY source /etc/nginx/conf.d/

EXPOSE 80

CMD ["nginx","-g","daemon off;"]