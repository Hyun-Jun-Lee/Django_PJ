FROM python:3.9.0

WORKDIR /home/

RUN echo "test45443566"

RUN git clone https://github.com/Hyun-Jun-Lee/Django_PJ

WORKDIR /home/Django_PJ/

RUN pip install -r requirements.txt

RUN pip install gunicorn

RUN pip install mysqlclient

EXPOSE 8000

CMD ["bash", "-c","python manage.py collectstatic --noinput --settings=stay.settings.deploy && python manage.py migrate --settings=stay.settings.deploy && gunicorn stay.wsgi --env DJANGO_SETTINGS_MODULE=stay.settings.deploy --bind 0.0.0.0:8000"]