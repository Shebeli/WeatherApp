FROM node:21.4.0

WORKDIR /app

COPY package.json package-lock.json /app/

RUN npm cache clean --force
RUN rm -rf node_modules
RUN npm install

COPY . /app/

CMD ["npm", "run", "dev"]