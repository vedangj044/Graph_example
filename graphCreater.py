import sys

def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    """
    Call in a loop to create terminal progress bar
    @params:
        iteration   - Required  : current iteration (Int)
        total       - Required  : total iterations (Int)
        prefix      - Optional  : prefix string (Str)
        suffix      - Optional  : suffix string (Str)
        decimals    - Optional  : positive number of decimals in percent complete (Int)
        length      - Optional  : character length of bar (Int)
        fill        - Optional  : bar fill character (Str)
        printEnd    - Optional  : end character (e.g. "\r", "\r\n") (Str)
    """
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print('\r%s |%s| %s%% %s' % (prefix, bar, percent, suffix), end = printEnd)
    # Print New Line on Complete
    if iteration == total:
        print()

import redis
from redisgraph import Node, Edge, Graph, Path

r = redis.Redis(host='localhost', port=6379)

csvFIle = open('user-languages.csv', 'r')
csvFIle = csvFIle.readlines()

redis_graph = Graph('programmer_dataset', r)
redis_graph.delete()
redis_graph = Graph('programmer_dataset', r)


for i in csvFIle[1::]:
    node_skills = i.split(',')[0]
    p = Node(label='programmer', properties={'name': node_skills})
    redis_graph.add_node(p)

for i in csvFIle[0].split(',')[1::]:
    s = Node(label='skill', properties={'name': i})
    redis_graph.add_node(s)

redis_graph.commit()

print("Node creation DONE")

c = csvFIle[0].split(',')
k = 0
printProgressBar(0, len(csvFIle[1::]), prefix = 'Progress:', suffix = 'Complete', length = 50)
for i in csvFIle[1::]:
    d = 1
    printProgressBar(k, len(csvFIle[1::]), prefix = 'Progress:', suffix = 'Complete', length = 50)
    for j in i.split(',')[1::]:
        if float(j)==0:
            continue
        else:
            query = """MATCH (p:programmer) WHERE p.name = {0}
                       MATCH (s:skill) WHERE s.name = {1}
                       CREATE (p)-[k:knows {{weight: {2}}}]->(s)""".format("\'"+i.split(',')[0]+"\'", "\'"+c[d]+"\'", j)
            resutl = redis_graph.query(query)
        d=d+1
    k=k+1
