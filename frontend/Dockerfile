FROM node:21.4.0

WORKDIR /app

COPY package.json package-lock.json /app/
RUN npm install

COPY . /app/

CMD ["npm", "run", "dev"]