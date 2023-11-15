import numpy as np
import matplotlib.pyplot as plt
import sympy as sp
import scipy 
import networkx as nx
from sklearn.cluster import KMeans
#from ABCD_Graph import ABCD_Graph as ABCD

k, m= sp.symbols('k m')
N= 10
D= sp.zeros(N,N)
A= sp.zeros(N,N)

for i in range(N):
    if i == 0:
        A[i, i] = -1 *(k/m)
        D[i, i+1]= 1 *(k/m)
    elif i==N-1:
        A[i , i]= -1 * (k/m)
        D[i, i-1]= 1 * (k/m)
    else:
        A[i , i] = -2 * (k/m)
        D[i, i-1]= 1 * (k/m)
        D[i, i+1]= 1 *(k/m)

L_prime= D + A 
L= - L_prime
print(L)
eigenvalues = L.eigenvals()
a=L.eigenvects()
eigenvector_1= a[0][2]
print(a)
# assuming that v2 is the second smallest eigenvectot
v2= sp.Matrix(a[1][2])
print(v2)
partition_ids = [1 if v > 0 else 0 for v in v2]

# Animate x(t) (dummy example, replace with your own dynamics simulation)
# ...
G = nx.path_graph(10)
# Visualize the graph with color-coded partitions
pos = nx.spring_layout(G)  # You can use a different layout algorithm
nx.draw(G, pos, node_color=partition_ids, with_labels=True, cmap=plt.cm.RdYlBu)
plt.show()

num_nodes=100
def create_scale_free_network(num_nodes):
    G = nx.barabasi_albert_graph(num_nodes, m=1)
    return G
title='trial'
strategy= 'random'
# Plot the network
def plot_network(G, title):
    pos = nx.spring_layout(G)
    nx.draw(G, pos, with_labels=True)
    plt.title(title)
    plt.show()

# Simulate targeted attacks
def targeted_attack(G, strategy):
    original_nodes = set(G.nodes)
    components_sizes = []

    while len(G.nodes) > 0:
        if strategy == "degree":
            node_to_remove = max(G.degree, key=lambda x: x[1])[0]
        elif strategy == "centrality":
            node_to_remove = max(nx.eigenvector_centrality(G), key=nx.eigenvector_centrality(G).get)
        elif strategy == "random":
            node_to_remove = np.random.choice(list(G.nodes))

        G.remove_node(node_to_remove)
        components = list(nx.connected_components(G))
        components_sizes.append([len(comp) for comp in components])

    return original_nodes, components_sizes

# Plot the loss of connectivity
def plot_connectivity_loss(original_nodes, components_sizes, strategy):
    plt.figure(figsize=(10, 6))
    for i, comp_sizes in enumerate(components_sizes):
        plt.plot(range(len(original_nodes) - i), comp_sizes, label=f"Step {i + 1}")

    plt.xlabel("Remaining nodes")
    plt.ylabel("Size of connected components")
    plt.title(f"Loss of Connectivity - Targeted Attack ({strategy} strategy)")
    plt.legend()
    plt.show()

# Main function
def main():
    num_nodes = 100
    G = create_scale_free_network(num_nodes)
    plot_network(G, "Scale-Free Network")

    strategies = ["degree", "centrality", "random"]

    for strategy in strategies:
        original_nodes, components_sizes = targeted_attack(G.copy(), strategy)
        plot_connectivity_loss(original_nodes, components_sizes, strategy)

if __name__ == "__main__":
    main()



          






    

