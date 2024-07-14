FROM node:20
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
RUN npm install -g nodemon
COPY . .
RUN apt-get update && apt-get install -y iputils-ping tcpdump
RUN chmod 777 /tmp
EXPOSE 3001
CMD ["npm", "run", "dev"]
