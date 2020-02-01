import redis
from redisgraph import Node, Edge, Graph, Path

r = redis.Redis(host='localhost', port=6379)

redis_graph = Graph('programmer_dataset', r)

query = """MATCH (p:programmer) WHERE p.name='007lva'
           MATCH (c:skill)
           MATCH (p)-[k]->(c)
		   RETURN p.name, k.weight, c.name"""

result = redis_graph.query(query)

# Print resultset
result.pretty_print()
