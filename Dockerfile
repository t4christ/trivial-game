FROM python:3.7-alpine

# copy requirements.txt to /requirements.txt in the container
# to avoid reinstalling packages when a container is rebuilt
# it will only reinstall packages when changes has been made to the file
COPY requirements.txt /requirements.txt



#run package installations
RUN apk update && \
    apk add --virtual build-deps gcc python3-dev musl-dev && \
    apk add \
    libffi-dev \
    postgresql-dev \
    libpng \
    git \
    libjpeg-turbo \
    freetype-dev \
    libpng-dev \
    jpeg-dev \
    libjpeg \
    libjpeg-turbo-dev \
    && pip install -r /requirements.txt \
    && pip install -e git+https://github.com/gbozee/django-paystack.git@master#egg=paystack 
    



# set working directory
WORKDIR /var/www/app

RUN chmod +x ./start.sh

