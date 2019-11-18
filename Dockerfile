FROM python:3.7-alpine
ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true
RUN mkdir /src
RUN mkdir /static
WORKDIR /src

# install psycopg2
# RUN apk update \
#     && apk add --virtual build-deps python-imaging libjpeg62 libjpeg62-dev gcc python3-dev musl-dev \
#     jpeg-dev \
#     zlib-dev \
#     freetype-dev \
#     lcms2-dev \
#     openjpeg-dev \
#     tiff-dev \
#     tk-dev \
#     tcl-dev \
#     harfbuzz-dev \
#     fribidi-dev \
#     && apk add postgresql-dev \
#     && pip install psycopg2 \
#     && apk del build-deps
RUN apk update \
    && apk add --virtual build-deps gcc python3-dev musl-dev \
    && apk add postgresql \
    && apk add postgresql-dev \
    && pip install psycopg2 \
    && apk add jpeg-dev zlib-dev libjpeg \
    && pip install Pillow \
    && apk del build-deps

ADD ./src /src
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
WORKDIR /src/src
CMD python manage.py collectstatic --no-input;python manage.py migrate; gunicorn project.wsgi -b 0.0.0.0:8000
