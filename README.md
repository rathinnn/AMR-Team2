# AMR-Team2
Solution is based around Flask and Dash. The Idea was to first parse the data into a dataframe and then get the required data from the dataframe. When a client sends a request to 
the flask server. the server process the dataframe by selecting over symbol, date and type of graph. 

## Modules

### app.py

Runs the Flask server, serves the index.html page and also contains the dash server.

### parse.py

Parses the dataset into a pandas dataframe

### process.py

Contains Methods to get the dataframe of data requested by client

### info.py (Dropped due to significant overhead in getting info from api)

### plot.py

Contains methods for plot used in Dashboard

### dashapp.py

Contains template, callbacks and logic of the dashboard

Data Structures used are Python dictionaries, and Lists

## Setup and Run

### Developed on Python 3.8

### Make Sure that all dependencies mentioned in requirements.txt is met
### If any package is not installed. Use pip to install it
### run app.py using python run
### The server is now hosted on localhost:5000