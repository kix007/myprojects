FROM node:14.19.1
WORKDIR /app
COPY --chown=node:node ["package.json", "package-lock.json", "./"]
RUN npm install
COPY . ./
EXPOSE 3000
CMD ["npm", "start"]