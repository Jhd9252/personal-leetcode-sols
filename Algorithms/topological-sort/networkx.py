import networkx as nx

graph = nx.DiGraph()

graph.add_edges_from([1,2]) # 1 -> 2

order = list(nx.topological_sort(graph))

