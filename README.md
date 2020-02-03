# Redis Graph Console

Redis graph console is a very simple console used to query to redisgraph.
[redisgraph](https://oss.redislabs.com/redisgraph/) used here was a graph created using [Python client](https://github.com/RedisGraph/redisgraph-py)
on the [dataset](https://www.kaggle.com/jaimevalero/developers-and-programming-languages/data).
The redisgraph is exposed to the console via a Flask server. 

#### Snapshot of the dataset

![Selection_001](https://user-images.githubusercontent.com/43697446/73665131-9e358d00-46c6-11ea-83da-c835223ed504.png)

### Features:
- Query the graph with easy to interacte console
- Redisgraph stores the dataset in a spark matrix.

### Installation and demo

#### Creating the graph

`pip install -r requirements.txt`

`python graphCreater.py`

It would take some time.
Then start the server 

#### Starting Flask server

`python server.py`

Open `main.html` page in your browser.

#### [Link to video demo](https://youtu.be/9yMv9rN3mqE)
