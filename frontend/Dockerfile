# build stage
FROM node:21.4.0 as build-stage

WORKDIR /app

COPY package.json package-lock.json /app/

RUN npm install

COPY . /app/

RUN npm run build


# production stage

FROM nginx:1.13.12-alpine as production-stage
    
WORKDIR /usr/share/nginx/html

RUN rm -rf ./*

COPY --from=build-stage /app/dist .

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]