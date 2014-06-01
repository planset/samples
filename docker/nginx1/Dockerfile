FROM ubuntu
MAINTEAINER planset

RUN echo "deb http://archive.ubuntu.com/ubuntu precise main universe" > /etc/apt/sources.list
RUN apt-get update
RUN apt-get install -y inotify-tools nginx openssh-server
RUN echo "daemon off" > /etc/nginx/nginx.conf

EXPOSE 80
CMD ["/usr/sbin/nginx"]

