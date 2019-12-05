FROM python:3.6.7-alpine3.8
RUN apk add --no-cache openldap-dev
RUN apk add --no-cache git
RUN pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN apk add build-base python-dev py-pip jpeg-dev zlib-dev
ENV LIBRARY_PATH=/lib:/usr/lib
ADD requirements.txt /app/requirements.txt
RUN pip install -r /app/requirements.txt
ADD . /app
EXPOSE 8000
WORKDIR /app
ENV PYTHONUNBUFFERED=1
ENV LDAP_SERVER_URI="ldap://10.10.20.16:389"
ENV LDAP_USER_DN_TEMPLATE="uid=%(user)s,cn=users,dc=pulselogic,dc=lan"
ENV LDAP_GROUP_IS_STAFF='cn=mv_isstaff,cn=groups,dc=pulselogic,dc=lan"
ENV LDAP_GROUP_IS_SUPERUSER='cn=mv_superuser,cn=groups,dc=pulselogic,dc=lan"
ENV LDAP_GROUP_CAN_EDIT='cn=mv_canedit,cn=groups,dc=pulselogic,dc=lan"
ENV LDAP_GROUP_READONLY='cn=mv_readonly,cn=groups,dc=pulselogic,dc=lan"
CMD python manage.py runserver 0.0.0.0:8000
