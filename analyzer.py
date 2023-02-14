import json
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.manifold import TSNE
from sklearn.decomposition import KernelPCA
from sklearn.cluster import KMeans
import warnings

warnings.filterwarnings('ignore')

with open(r'C:\Users\KDCA\Desktop\IL'+'\\'+'field_data.json') as f:
    p = json.load(f)

for i in range(len(p)-1):
    p[0].extend(p[i+1])

p = p[0]

matrices = [np.array(p[i+6000][0][0]).reshape(11, 11) for i in range(6000)]
labels = [np.argmax(p[i+6000][0][1]) if max(p[i+3000][0][1]) != 0 else 4 for i in range(6000)]

flat_matrices = [matrix.flatten() for matrix in matrices]
flat_matrices = np.array(flat_matrices)

colors = ["red", "black", "blue", "green", "white"]
label_colors = [colors[label] if label != 4 else "none" for label in labels]

label_separate = [[colors[label] if label == i else "none" for label in labels] for i in range(4)]

# TSNE 수행
TSNE = TSNE(n_components=3)
TSNE_result = TSNE.fit_transform(flat_matrices)

plotlist = [[0, 1, 2]]*4

kmeans = KMeans(n_clusters=14, random_state=0).fit(TSNE_result)

def pltdraw(plotlist, size=2):
    fig = plt.figure()
    for i in range(size):
        for j in range(size):
            ax = fig.add_subplot(110*size+1+i*size+j, projection='3d')
            ax.scatter(TSNE_result[:, plotlist[i*size+j][0]],
                        TSNE_result[:, plotlist[i*size+j][1]],
                        TSNE_result[:, plotlist[i*size+j][2]],
                        c=label_separate[i*size+j])

            ax.set_xlabel("TSNE 1")
            ax.set_ylabel("TSNE 2")
            ax.set_zlabel("TSNE 3")
    fig2 = plt.figure()
    ax = fig2.add_subplot(111, projection='3d')
    ax.scatter(TSNE_result[:, plotlist[0][0]],
                TSNE_result[:, plotlist[0][1]],
                TSNE_result[:, plotlist[0][2]],
                c=label_colors)
    for i in range(13):
        ax.scatter(kmeans.cluster_centers_[i][0],
                   kmeans.cluster_centers_[i][1],
                   kmeans.cluster_centers_[i][2],
                   c='yellow')
        
pltdraw([[0, 1, 2]]*4, size=2)
plt.show()

es =[[sum([(TSNE_result[k][i]-kmeans.cluster_centers_[l][i])**2 \
          for i in range(3)])**0.5 for k in range(len(TSNE_result))] \
             for l in range(len(kmeans.cluster_centers_))]


bea = []
order = [[] for i in range(len(es))]

for k in range(len(es)):
    bea.append([i for i in es[k]])
    bex = [i for i in es[k]]

    bea[k].sort()

    for i in bea[k]:
        order[k].append(bex.index(i))
        bex[bex.index(i)] = None

ar = []

for ber in bea:
    bero = [ber[i+1]-ber[i] if ber[i+1]-ber[i] != 0 else None for i in range(len(ber)-1)]
    for i in range(len(ber)-1):
        le = [i for i in bero[0:i+1] if i != None]
        if le == []:
            le = [10000]
        if (ber[i+1]-ber[i] > (sum(le)/len(le))*2 and ber[i+1] > 10) or i > 1000:
            ar.append(i+1)
            break

colores = [[] for i in range(len(es))]

for i in range(len(es)):
    for j in range(1, ar[2]):
        colores[i].append(label_colors[order[i].index(j)])

er = [[0,0,0,0,0] for i in range(len(es))]

for k in range(len(es)):
    for i in colores[k]:
        if i != 'none':
            er[k][colors.index(i)] += 1

print(er)
print(kmeans.cluster_centers_)
