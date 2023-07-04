FROM node:20.3.0-alpine

MAINTAINER nahkim <nahkim@huray.net>

WORKDIR /app

COPY ./frontend ./

RUN npm install -g npm@9.7.2

RUN npm install

RUN npm install bootstrap

RUN npm install svelte-spa-router

CMD ["npm", "run", "dev", "--", "--host"]
