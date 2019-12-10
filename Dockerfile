# Set the base image to Ubuntu
FROM ubuntu:18.04

# File Author / Maintainer
MAINTAINER Steve Gilissen

# Update the default application repository sources list
RUN apt-get update && apt-get install -y \
    python3-dev \
    python3 \
    python3-pip \
    python3-setuptools \
    build-essential \
    python-ldap \
    libpq-dev \
    libldap2-dev \
    libsasl2-dev \
    git

# Set variables for project name, and where to place files in container.
ENV PROJECT=makerventory
ENV CONTAINER_HOME=/opt
ENV CONTAINER_PROJECT=$CONTAINER_HOME/$PROJECT

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


# Create application subdirectories
WORKDIR $CONTAINER_HOME
RUN mkdir logs

# Copy application source code to $CONTAINER_PROJECT
COPY . $CONTAINER_PROJECT

# Install Python dependencies
RUN pip3 install -r $CONTAINER_PROJECT/requirements.txt
RUN pip3 install gunicorn

# Copy and set entrypoint
WORKDIR $CONTAINER_PROJECT
COPY ./entrypoint.sh /
# ENTRYPOINT ["/entrypoint.sh"]