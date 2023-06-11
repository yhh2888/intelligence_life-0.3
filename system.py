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
