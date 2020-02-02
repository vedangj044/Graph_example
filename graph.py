import redis
from redisgraph import Node, Edge, Graph, Path

r = redis.Redis(host='localhost', port=6379)

redis_graph = Graph('programmer_dataset', r)

query = """MATCH (p:programmer) WHERE p.name='007lva'
           MATCH (c:skill)
           MATCH (p)-[k]->(c)
		   RETURN (c)"""

query = """MATCH (p:programmer) WHERE p.name='007lva' MATCH (s:skill) MATCH (p)-[k]->(s) WHERE k.weight>0.05 RETURN p.name, k.weight, s.name"""
query = """MATCH (p:programmer) WHERE p.name = '007lva' MATCH (s:skill) WHERE s.name = 'python' MATCH (p)-[k]->(s) RETURN p.name, k.weight, s.name"""

result = redis_graph.query(query)

# Print resultset
print(result.result_set)
