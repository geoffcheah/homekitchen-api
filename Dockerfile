FROM python:3.7

RUN mkdir /code
WORKDIR /code
ADD Pipfile /code/
ADD Pipfile.lock /code/
RUN pip install --upgrade pip
RUN pip install pipenv
RUN pipenv install --dev
ADD . /code/

EXPOSE 8000

CMD ["./start.sh"]
