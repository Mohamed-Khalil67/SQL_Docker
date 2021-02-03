FROM mysql:latest

COPY ./bdd.sql /docker-entrypoint-initdb.d

ENV MYSQL_DATABASE classicmodels
ENV MYSQL_USER mohamed
ENV MYSQL_PASSWORD mohamed
ENV MYSQL_ROOT_PASSWORD rootpass

EXPOSE 3306



#FROM mysql:5.7
#RUN chown -R mysql:root /var/lib/mysql/

#ARG MYSQL_DATABASE
#ARG MYSQL_USER
#ARG MYSQL_PASSWORD
#ARG MYSQL_ROOT_PASSWORD

#ENV MYSQL_DATABASE=$MYSQL_DATABASE
#ENV MYSQL_USER=$MYSQL_USER
#ENV MYSQL_PASSWORD=$MYSQL_PASSWORD
#ENV MYSQL_ROOT_PASSWORD=$MYSQL_ROOT_PASSWORD

#ADD bdd.sql /etc/mysql/data.sql
#RUN sed -i 's/MYSQL_DATABASE/'$MYSQL_DATABASE'/g' /etc/mysql/.sql
#RUN cp /etc/mysql/bdd.sql /docker-entrypoint-initdb.d

#EXPOSE 3306