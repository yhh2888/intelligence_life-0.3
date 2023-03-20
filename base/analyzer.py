import json
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.tree import DecisionTreeClassifier
import warnings

warnings.filterwarnings('ignore')

with open(r'C:\Users\KDCA\Desktop\IL'+'\\'+'field_data.json') as f:
    p = json.load(f)

for i in range(len(p)-1):
    p[0].extend(p[i+1])

p = p[0]

matrices = [np.array(p[i+18000][0][0]).reshape(11, 11) for i in range(6000)]
labels = [np.argmax(p[i+18000][0][1]) if max(p[i+18000][0][1]) != 0 else 4 for i in range(6000)]

model = DecisionTreeClassifier()

for i in range(int(len(matrices)/11.01)):
    model.fit(np.array(matrices[i*11:i*11+11]).reshape(11, 11*11), np.array(labels[i*11:i*11+11]))
    print(labels[i*11:i*11+11])
