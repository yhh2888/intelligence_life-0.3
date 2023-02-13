import json
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.manifold import Isomap

with open(r'C:\Users\hyunhoyang\Desktop\IL'+'\\'+'field_data.json') as f:
    p = json.load(f)

for i in range(len(p)-1):
    p[0].extend(p[i+1])

p = p[0]

matrices = [np.array(p[i][0][0]).reshape(11, 11) for i in range(3000)]
labels = [np.argmax(p[i][0][1]) if max(p[i][0][1]) != 0 else 4 for i in range(3000)]

flat_matrices = [matrix.flatten() for matrix in matrices]
flat_matrices = np.array(flat_matrices)

colors = ["red", "green", "blue", "yellow", "white"]
label_colors = [colors[label] if label != 4 else "none" for label in labels]

# Isomap 수행
isomap = Isomap(n_components=6)
isomap_result = isomap.fit_transform(flat_matrices)

from sklearn import svm
from sklearn.model_selection import train_test_split

# 데이터를 훈련 데이터와 테스트 데이터로 분할
X_train, X_test, y_train, y_test = train_test_split(flat_matrices, labels, test_size=0.2, random_state=0)

# SVM 분류 모델을 훈련
clf = svm.SVC(kernel='linear')
clf.fit(X_train, y_train)

# 테스트 데이터에 대한 정확도 평가
accuracy = clf.score(X_test, y_test)
print("SVM Accuracy: ", accuracy)

# 테스트 데이터의 라벨을 예측
y_pred = clf.predict(X_test)
print("Predicted Labels: ", y_pred)


plotlist = [[0, 1, 2], [0, 2, 4], [1, 3, 4], [1, 3, 5]]
# 3D 산점도 그리기
fig = plt.figure()
for i in range(2):
    for j in range(2):
        ax = fig.add_subplot(221+i*2+j, projection='3d')
        ax.scatter(isomap_result[:, plotlist[i*2+j][0]],
                    isomap_result[:, plotlist[i*2+j][1]],
                    isomap_result[:, plotlist[i*2+j][2]],
                    c=label_colors)

        ax.set_xlabel("Isomap 1")
        ax.set_ylabel("Isomap 2")
        ax.set_zlabel("Isomap 3")

plt.show()
