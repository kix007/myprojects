# Helium BlockChain 
- A small program written in React framework to showcast how the frontend and backend can communicate with an API endpoint

# Frameworks /Languages used in this project
- React (Front-end)
- Python (Backend)
- Postgresql (Database)

# To get started
1. git clone repository
2. `sudo pip install docker-compose` 
 - See link on how to install using different operating systems https://docs.docker.com/compose/install/
3. Go to the "engineering" folder and run the following command:
  - `docker-compose up -d --build`
4. The build process will create a client frontend, backend and a postgresql database
5. Once the process is completed, launch your app on http://127.0.0.1:3000

# Front-End
**Note** !!! In the `.env file` in the client folder, both the App and API URL is configurable.
- The site shows an example of the following features as follows:
1. Block Chain accounts list
2. Stats
3. Graphs

# Backend (API Endpoints)
- The server runs on the following url: http://127.0.0.1:8001
- Request method is **GET** for all endpoints
1. http://127.0.0.1:8001/accounts_list - shows a list of all the blockchain accounts
2. http://127.0.0.1:8001/stats - shows a list of stats on the blockchain network
3. http://127.0.0.1:8001/rewards - shows a list of rewards for today on the blockchain network

- The database and app values can be configured in the `config.ini` file (see server folder readme)

