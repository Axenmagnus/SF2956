import numpy as np
import pandas as pd
import pickle as pickle
import gudhi as gd  
from pylab import *

from scipy.spatial.distance import cdist
import pandas as pd
import numpy as np

from scipy.cluster import hierarchy
import matplotlib.pyplot as plt

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

#arr = df.sort_values(by="Party", ascending=7) # Ordering by Party
arr = df.to_numpy() # change from dataframe to array



array_only_votes = arr[0:,3:] # dropping District, Party,Sex
array_only_votes = array_only_votes.astype(np.float)
from scipy.spatial import distance_matrix
distance=distance_matrix( array_only_votes,array_only_votes)

D=pd.DataFrame(distance)
skeleton_protein = gd.RipsComplex(
    distance_matrix = D.values, 
    max_edge_length = 3
) 



Rips_simplex_tree_protein = skeleton_protein.create_simplex_tree(max_dimension = 1)


Rips_simplex_tree_protein.dimension()
Rips_simplex_tree_protein.num_vertices()
Rips_simplex_tree_protein.num_simplices()
rips_filtration = Rips_simplex_tree_protein.get_filtration()
rips_list = list(rips_filtration)
len(rips_list)

for splx in rips_list[0:600] :
    print(splx)
    