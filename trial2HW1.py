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

L= D+A 
eigenvalues = L.eigenvals()
a=L.eigenvects()
v1= a[0][2]

# assuming that v2 is the second smallest eigenvectot
v2= a[1][2]
print(v2)
partition_ids = [1 if v > 0 else 0 for v in v2]
G = nx.path_graph(10)
# Visualize the graph with color-coded partitions
pos = nx.spring_layout(G)  # You can use a different layout algorithm
nx.draw(G, pos, node_color=partition_ids, with_labels=True, cmap=plt.cm.RdYlBu)
plt.show()
#A random network
#Adjacency matrices
#first, we generate the networks 
#Random Network
N=10
m= 9
E_R= nx.erdos_renyi_graph(N, m)
A1 = nx.adjacency_matrix(E_R).toarray()

#SCALE_FREE NETWORK
barabasi= nx.barabasi_albert_graph(N, m)
A2= nx.adjacency_matrix(barabasi).toarray()

#A SMALL WOLRD NETWORK
k = 1  # Number of nearest neighbors for each node
p = 1/(N-1)  # Probability of rewiring each edge
W_S= nx.watts_strogatz_graph(N, k, p)
A3= nx.adjacency_matrix(W_S).toarray()

#Laplacians and inferring communities
#Random Network
L1 = nx.laplacian_matrix(E_R).toarray()
eigvl, eigvec = np.linalg.eigh(L1)
# Extract the Fiedler vector (second smallest eigenvector)
fiedler_vector1 = eigvec[:, 1]
# Infer communities based on the sign of the Fiedler vector
communities1 = [0 if x >= 0 else 1 for x in fiedler_vector1]
centrality1 = nx.betweenness_centrality(E_R)
avg_path_length1 = nx.average_shortest_path_length(E_R) 
print("Average path length1:", avg_path_length1)
clustering_coefficients1 = nx.clustering(E_R)
for node, cc in clustering_coefficients1.items():
    print(f"Node {node}: Clustering Coefficient = {cc}")
#2
L2 = nx.laplacian_matrix(barabasi).toarray()
eigvl, eigvec = np.linalg.eigh(L2)
fiedler_vector2 = eigvec[:, 1]
communities2 = [0 if x >= 0 else 1 for x in fiedler_vector2]
centrality2 = nx.betweenness_centrality(barabasi)
avg_path_length2 = nx.average_shortest_path_length(barabasi) 
print("Average path length2:", avg_path_length2)
clustering_coefficients2 = nx.clustering(barabasi)
for node, cc in clustering_coefficients2.items():
    print(f"Node {node}: Clustering Coefficient = {cc}")
#L3
L3 = nx.laplacian_matrix(W_S).toarray()
eigvl, eigvec = np.linalg.eigh(L3)
fiedler_vector3 = eigvec[:, 1]
communities3 = [0 if x >= 0 else 1 for x in fiedler_vector3]
centrality3 = nx.betweenness_centrality(W_S)
avg_path_length3 = nx.average_shortest_path_length(W_S) 
print("Average path length3:", avg_path_length3)
clustering_coefficients3 = nx.clustering(W_S)
for node, cc in clustering_coefficients3.items():
    print(f"Node {node}: Clustering Coefficient = {cc}")


