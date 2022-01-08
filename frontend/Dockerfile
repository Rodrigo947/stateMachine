FROM node:14

WORKDIR /code

COPY . .

RUN npm install

RUN chmod +x entrypoint.sh

ENTRYPOINT ["sh", "entrypoint.sh"]