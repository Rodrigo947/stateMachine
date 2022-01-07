FROM python:3.9

ARG TYPE_ENV

ENV PYTHONUNBUFFERED 1

WORKDIR /code

COPY . /code

RUN apt update
RUN pip install pipenv

RUN if [ "$TYPE_ENV" = "dev" ]; then \
  pipenv install --dev --system --deploy; \
  else \
  pipenv install --system --deploy; \
  fi

RUN chmod +x entrypoint.sh

ENTRYPOINT ["sh", "entrypoint.sh"]