# AWS Lambda execution environment is based on Amazon Linux 1
FROM amazonlinux:1

# Install Python 3.6
RUN yum -y install python36 python36-pip

# Install your dependencies
RUN yum -y install python36-devel mysql mysql-devel gcc

# Set the same WORKDIR as default image
RUN mkdir /var/task
WORKDIR /var/task