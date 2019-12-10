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
# LDAP settings
ENV LDAP_SERVER_URI="ldap://10.10.20.16:389"
ENV LDAP_USER_DN_TEMPLATE="uid=%(user)s,cn=users,dc=pulselogic,dc=lan"
ENV LDAP_SEARCH_ROOT="dc=pulselogic,dc=lan"
# The groups below should be the FULL DN of the LDAP group
# IS_STAFF allows users to login to the MakerVentory admin.
ENV LDAP_GROUP_IS_STAFF="cn=mv_isstaff,cn=groups,dc=pulselogic,dc=lan"
# IS_SUPERUSER grants superuser access to the user.
# Adding the user to this group will allow the user to do EVERYTHING.
ENV LDAP_GROUP_IS_SUPERUSER="cn=mv_superuser,cn=groups,dc=pulselogic,dc=lan"
# The groups below should ONLY be the group name of the LDAP group.
# Please create the required groups in the MakerVentory admin first! You can use a local super user to do so.
ENV LDAP_GROUPS_CAN_EDIT="mv_canedit"
ENV LDAP_GROUPS_READONLY="mv_readonly"
CMD python manage.py runserver 0.0.0.0:8000
