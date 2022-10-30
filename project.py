import pandas as pd
import numpy as np

from scipy.cluster import hierarchy
import matplotlib.pyplot as plt
import scipy.spatial as spatial
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

#arr = df.sort_values(by="Party", ascending=7) # Ordering by Party
arr = df.to_numpy() # change from dataframe to array



array_only_votes = arr[0:,3:] # dropping District, Party,Sex
dend = hierarchy.linkage(array_only_votes, 'ward')#,color=np.array(df["Party"].values)) # Creating a Dendrogram
plt.figure()
dist=dend

dn = hierarchy.dendrogram(dend,labels=list(df["Party"].values))
label_colors = {'0': 'r', '1': 'b', '2': 'g', '3': 'b','4': 'm', '5': 'c', '6': 'w', '7': 'y'}
ax = plt.gca()
xlbls = ax.get_xmajorticklabels()
for lbl in xlbls:
    lbl.set_color(label_colors[lbl.get_text()])

plt.show()

#for j in range(len()):
    

dn1 = hierarchy.dendrogram(dend)#,labels=list(df["Party"].values))

#indx=dn1["ivl"]
#for j in range(len(dn['leaves_color_list'])):
#    indx=int(dn["ivl"][j])
#    party=(df.iloc[indx]["Party"])
#    dn1['leaves_color_list'][j]="C"+party

data=dist


#%%




#%%



# Converitng the data into distance objects
data_dist = [sr.Distance(spatial.distance.pdist(fig, "euclidean")) for fig in array_only_votes]
#train_dist = [sr.Distance(spatial.distance.pdist(fig, "euclidean")) for fig in train]
# Converitng the distance objects into H0 stable ranks
clustering_methods = ["single", "complete", "average", "ward"]
data_h0sr = {}
train_h0sr = {}
for cm in clustering_methods:
    data_h0sr[cm] = [d.get_h0sr(clustering_method=cm) for d in data_dist]
    #train_h0sr[cm] = [d.get_h0sr(clustering_method=cm) for d in train_dist]
    
    
    
#%%
plt.figure(figsize=(10,7))
i = 0
for f in data_h0sr["single"]:
    if i <100:
        color = "red"
    else:
        color = "blue"
    f.plot(color=color, linewidth=0.5)
    i += 1
    
    
    
#%%
    
plt.figure(figsize=(10,7))
i = 0
for f in data_h0sr["complete"]:
    if i <100:
        color = "red"
    else:
        color = "blue"
    f.plot(color=color, linewidth=0.5)
    i += 1

#%%    
    
plt.figure(figsize=(10,7))
i = 0
for f in data_h0sr["average"]:
    if i <100:
        color = "red"
    else:
        color = "blue"
    f.plot(color=color, linewidth=0.5)
    i += 1
#%%    
    
plt.figure(figsize=(10,7))
i = 0
for f in data_h0sr["ward"]:
    if i <100:
        color = "red"
    else:
        color = "blue"
    f.plot(color=color, linewidth=0.5)
    i += 1
    
    
    
    
    
    
#%%

import scipy.stats as st

def circle(c, r, s, error=0):
    t = np.random.uniform(high=2 * np.pi, size=s)
    y = np.sin(t) * r + c[1]
    x = np.cos(t) * r + c[0]
    sd = error * 0.635
    pdf = st.norm(loc=[0, 0], scale=(sd, sd))
    return pdf.rvs((s, 2)) + np.vstack([x, y]).transpose()



data = []
i = 0
while i < 100:
    c = circle([0,0], 1, 100, error=0.2)
    data.append(c)
    i += 1  
