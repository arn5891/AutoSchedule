import os
import sys
import numpy as np
import skimage.morphology
#from sklearn.cluster import AgglomerativeClustering
from schedulescan import results
from sklearn.cluster import DBSCAN

class Node:
    def __init__(self, center, content):
        self.group = None
        self.center = center
        self.content = content
    def set_grp(n):
        self.group = n

class Group:

    def __init__(self, nds):
        self.nds = nds
        size = nds.length

nodes = []

for (bbox, text, prob) in results:
    c = [(bbox[0][0]-bbox[1][0])/2 , (bbox[0][1]-bbox[3][1])/2]
    nodes.append(Node(c, text))

#def dist(n1, n2):
#    a = int(n2.x)-int(n1.x)
#    b = int(n2.y)-int(n1.y)
#    return abs((a**2+b**2)**0.5)

dists = 0
t = 0
for i in nodes:
    for j in nodes:
        if j is not i:
#            dists+=(dist(i,j))
            t += 1
avg_dist = dists/t


# Extract their centers as a numpy array
centers = np.array([node.center for node in nodes])

# Run DBSCAN
clustering = DBSCAN(eps=10, min_samples=1).fit(centers)
labels = clustering.labels_  # Each label = group number

# Group nodes by cluster label
groups = {}
for label, node in zip(labels, nodes):
    groups.setdefault(label, []).append(node)

# Example output
for group_id, group_nodes in groups.items():
    print(f"Group {group_id}: {[n.content for n in group_nodes]}")