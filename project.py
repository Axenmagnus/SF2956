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
dend = hierarchy.linkage(array_only_votes, 'ward')#,color=np.array(df["Party"].values)) # Creating a Dendrogram
plt.figure()

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
