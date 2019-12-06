import networkx as nx
G = nx.Graph()

file = open("input06.txt", "r")

for line in file:
    line = line[:-1].split(')')
    G.add_edge(line[0], line[1])

sum = 0
for node in G:
    sum += nx.shortest_path_length(G, node, 'COM')

print(sum)
print(nx.shortest_path_length(G, 'YOU', 'SAN') - 2)
