FROM python:3.7-alpine



# copy requirements.txt to /requirements.txt in the container
# to avoid reinstalling packages when a container is rebuilt
# it will only reinstall packages when changes has been made to the file
COPY ./requirements.txt /requirements.txt



#run package installations
RUN apk update && \
    apk add --virtual build-deps gcc python-dev musl-dev && \
    apk add \
    postgresql-dev \
    libpng \
    libjpeg-turbo \
    freetype-dev \
    libpng-dev \
    jpeg-dev \
    libjpeg \
    libjpeg-turbo-dev \
    && pip install -r /requirements.txt



# set working directory
WORKDIR /var/www/app

# copy project root to app folder in the container
COPY . /var/www/app

