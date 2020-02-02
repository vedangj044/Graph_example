from flask import Flask, redirect, url_for, request
import redis
from flask_cors import CORS, cross_origin
from redisgraph import Graph

app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

r = redis.Redis(host='localhost', port=6379)

redis_graph = Graph('programmer_dataset', r)

@app.route('/', methods=['POST', 'GET'])
@cross_origin()
def process():
    if request.method == 'POST':
        query = str(request.data, "utf-8")
        result = redis_graph.query(query)
        l = result.result_set
        for i in range(len(l)):
            l[i][1] = str(l[i][1])
        return str(l)
    else:
        return "POST REQUEST"

if __name__ == "__main__":
    app.run(debug=True)
