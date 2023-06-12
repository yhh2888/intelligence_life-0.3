from newmap import *
from cells import *
from multinet import *

model = MyNetwork()
dataset = MyDataset()
dataloader = DataLoader(dataset, batch_size=32, shuffle=True)
criterion = torch.nn.MSELoss()


'''
model(dataloader.dataset[0][0].unsqueeze(0))

1. 공간 기본정보와 그것을 모델로 해석한 결과값을 기억하기
2. cells 조합하는 클래스 만들기
2-1. 보상결정, 학습강도, 이동, 공격.
2-2. 에너지, 에너지기울기, 공간적정보, 랜덤포인트.
2-3. 전의특징기억(수치, 기억능력), 신호변환
3. 모델 해석 결과값을 cell조합 클래스에 넣기
4. 1에서 얻은 기억된 데이터를 때때로 학습시키기(보상결정시 학습강도만큼)
'''

class Combiner:
    def __init__(self, gene_data):
        self.gene = gene_data
        self.netc = []
        for i in self.gene[:-1]:
            if i[0] == 0:
                self.netc.append([Reinf_decide(*i[1]), 0, *i[2:]])
            elif i[0] == 1:
                self.netc.append([Movecell(*i[1]), 1, *i[2:]])
            elif i[0] == 2:
                self.netc.append([Convert_neuron(*i[1]), 2, *i[2:]])
            elif i[0] == 3:
                self.netc.append([Variate_neuron(*i[1]), 3, *i[2:]])
            elif i[0] == 4:
                self.netc.append([Sender_neuron(*i[1]), 4, *i[2:]])

        self.from_model = self.gene[-1]
