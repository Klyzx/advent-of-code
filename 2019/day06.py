import networkx as nx
G = nx.Graph()

file = open("inputs/06.in", "r")

for line in file:
    G.add_edge(line[:3], line[4:7])

file.close()

sum = 0
for node in G:
    sum += nx.shortest_path_length(G, node, 'COM')

print(sum)
print(nx.shortest_path_length(G, 'YOU', 'SAN') - 2)
