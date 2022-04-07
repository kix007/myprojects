# Backend Server
- To run the server manually, you must do the following:
1. `pip install -r requirements.txt`
2. Edit the `config.ini` file with the correct database and app values
 e.g. 
 [database]
  host = localhost
  port = 5432
  database = ""
  user = "" 
  password = ""
  
  [app]
  host = 0.0.0.0
  port = 8001 
- The app values in the config will startup the server with the current host and port specified.

3. Run `python3 main.py` in your terminal or command prompt window
4. The server should be running on http://localhost:8001
