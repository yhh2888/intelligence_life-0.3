import torch, random, math
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

multiplier = torch.randint(0, 100, size=(11, 11))/1210

def regularize(matrix):
    return torch.sum((torch.randint(-100, 100, size=(11, 11))/100)*matrix)/1210


# 커스텀 데이터셋 클래스 정의
class MyDataset(Dataset):
    def __init__(self):
        # 데이터 초기화
        self.data = torch.tensor([[[random.random() for i in range(11)] for j in range(11)] for k in range(5000)])  # 11x11 매트릭스를 수천 개 포함하는 데이터 리스트
        self.labels = torch.tensor([[[regularize(self.data[i]) for i in range(10)]] for j in range(5000)])  # 10x1 벡터를 수천 개 포함하는 라벨 리스트

    def __len__(self):
        # 데이터셋의 총 샘플 수 반환
        return len(self.data)

    def __getitem__(self, idx):
        # 주어진 인덱스에 해당하는 데이터와 라벨 반환
        return self.data[idx], self.labels[idx]

# 신경망 정의
class MyNetwork(nn.Module):
    def __init__(self):
        super(MyNetwork, self).__init__()
        self.fc1 = nn.Linear(11, 10)
        self.fc2 = nn.Linear(11 , 1)

    def forward(self, x):
        x = self.fc1(x).permute(0, 2, 1)
        x = self.fc2(x).permute(0, 2, 1)
        return x

if __name__ == '__main__':         
    # 하이퍼파라미터 설정
    learning_rate = 0.001
    batch_size = 32

    # 데이터셋 및 데이터로더 초기화
    dataset = MyDataset()
    dataloader = DataLoader(dataset, batch_size=batch_size, shuffle=True)

    # 모델 인스턴스 생성
    model = MyNetwork()

    # 손실 함수와 최적화 알고리즘 정의
    criterion = nn.MSELoss()
    optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate)

    def execute(num_epochs=100):
        # 학습 반복
        for epoch in range(num_epochs):
            for data, labels in dataloader:
                # 입력과 라벨을 GPU로 이동 (GPU 사용 시)
                # data = data.to(device)
                # labels = labels.to(device)

                # 순전파
                outputs = model(data)

                # 손실 계산
                loss = criterion(outputs, labels)
                # 역전파 및 가중치 업데이트
                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

            # 현재 에폭의 손실 출력
            print(f"Epoch [{epoch+1}/{num_epochs}], Loss: {loss.item()}")

    execute()
