import pandas as pd
import numpy as np

from ripser import ripser
from persim import plot_diagrams

import numpy as np
import matplotlib.pyplot as plt
from sklearn import datasets
from sklearn.metrics.pairwise import pairwise_distances
from scipy import sparse
import scipy.spatial as spatial

from ripser import ripser
from persim import plot_diagrams
import tadasets

from scipy.cluster import hierarchy
import matplotlib.pyplot as plt

import stablerank.srank as sr




dist = open('PoliticalData/mpdistrict.dat').readlines()
party = open('PoliticalData/mpparty.dat').readlines()
party = party[3:]
sex = open('PoliticalData/mpsex.dat').readlines()
sex = sex[2:]
votes = open('PoliticalData/votes.dat').readline()

dist = list(map(lambda x:x.strip(),dist))
party = list(map(lambda x:x.strip(),party))
sex = list(map(lambda x:x.strip(),sex))

df = pd.DataFrame()
df['District'] = dist
df['Party'] = party
df['Gender'] = sex


votesnp = np.array(list(votes.split(',')))
votenp = np.array_split(votesnp, 31)

dfvote = pd.DataFrame()
i = 0
for vote in votenp:
    df['Vote: ',str(i)] = vote.tolist()
    i = i+1
print(df)

# print(votespd)

# arr = df.sort_values(by="Party", ascending=7) # Ordering by Party
# print(arr)
arr = df.to_numpy() # change from dataframe to array
array_only_votes = arr[0:,3:] # dropping District, Party,Sex


dend = hierarchy.linkage(array_only_votes, 'ward') # Creating a Dendrogram
plt.figure()
dn = hierarchy.dendrogram(dend, labels=list(df['Gender']))
# plt.show()
# Future inmplementation: colorgrade every party


data_dist = [sr.Distance(spatial.distance.pdist(fig, "euclidean")) for fig in arr]


diagrams = ripser(arr, thresh=5)['dgms']
plot_diagrams(diagrams, show=True)



