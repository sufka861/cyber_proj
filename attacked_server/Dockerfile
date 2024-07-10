FROM node:20
WORKDIR /usr/src/app
COPY package*.json ./
RUN npm install
COPY . .
RUN apt-get update && apt-get install -y iputils-ping tcpdump
RUN chmod 777 /tmp
EXPOSE 3000
CMD ["npm", "start"]
