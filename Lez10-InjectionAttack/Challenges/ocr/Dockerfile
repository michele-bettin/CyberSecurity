FROM python:3.6.12-buster

RUN pip install flask gunicorn pytesseract==0.3.0 flask_recaptcha && \
    apt-get update && apt-get upgrade -y &&\
    apt-get install -y tesseract-ocr &&\
    useradd python-runner

RUN mkdir -p /var/www
COPY www/ /var/www/

WORKDIR /var/www/
RUN chown -R python-runner:python-runner .
USER python-runner
EXPOSE 5000

CMD gunicorn server:app -b 0.0.0.0:5000 --access-logfile - --error-logfile -
