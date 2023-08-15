import torch, random, math
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader

multiplier = torch.randint(0, 100, size=(11, 11))/1210

def regularize(matrix):
    return torch.sum((torch.randint(-100, 100, size=(20, 20))/100)*matrix)/1210


# 커스텀 데이터셋 클래스 정의
class MyDataset(Dataset):
    def __init__(self, data=None, labels=None):
        if data is None:
            self.data = torch.rand((50, 20, 20))  # 수정: 랜덤한 데이터 생성
        else:
            self.data = data
        if labels is None:
            self.labels = torch.rand((50, 1, 10))  # 수정: 랜덤한 레이블 생성
        else:
            self.labels = labels

    def __len__(self):
        return len(self.data)

    def __getitem__(self, idx):
        return self.data[idx], self.labels[idx]

# 신경망 정의
class MyNetwork(nn.Module):
    def __init__(self, input_size=20):
        super(MyNetwork, self).__init__()
        self.fc1 = nn.Linear(input_size, 20)  # 수정: 입력 크기를 매개변수로 받음
        self.fc2 = nn.Linear(20, 10)
        self.fc3 = nn.Linear(10, 10) 

    def forward(self, x):
        x = self.fc1(x)
        x = self.fc2(x)
        x = self.fc3(x)
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
