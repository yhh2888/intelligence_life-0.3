import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import axes3d
from time import perf_counter as perfc
import traceback
from datetime import datetime

import os.path
from pathlib import Path
import sys, random, json, time, os
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QPainter, QColor, QFont, QPen, QBrush, QPainterPath, QPalette
from PyQt5.QtCore import Qt, QTimer

random.seed(777)

if __name__ == '__main__':
    path = str(Path(os.getcwd()).parent)
    
else :
    tobe_append = []
    
    try:
        tobe_append.extend(os.listdir(sys.path[0]))
    except FileNotFoundError:
        pass

    for i in tobe_append:
        sys.path.append(sys.path[0]+'\\'+i)
    
    for i in sys.path:
        try:
            if 'test.json' in os.listdir(i):
                path = i
        except Exception:
            pass

def distrib_analyze(points):
    rdlum = [0]*5
    for i in points:
        if abs(i[0])+abs(i[1]) < 4:
            rdlum[4] += i[2]
        elif i[0]>0 and abs(i[1])<=abs(i[0]):
            rdlum[0] += i[2]
        elif i[0]<0 and abs(i[1])<=abs(i[0]):
            rdlum[2] += i[2]
        elif i[1]>0 and abs(i[1])>=abs(i[0]):
            rdlum[1] += i[2]
        elif i[1]<0 and abs(i[1])>=abs(i[0]):
            rdlum[3] += i[2]
    dirs = np.argmax(rdlum)
    rdlum = [0]*5
    rdlum[dirs] =+ 1
    return rdlum
    
# 입력값 및 타겟값 XOR문제
data = [[[random.random() for i in range(49)], [random.random()]] for j in range(5)]


# 활성화 함수 - 2. tanh
# tanh 함수의 미분은 1 - (활성화 함수 출력의 제곱)
def tanh(x, derivative=False):
    if (derivative == True):
        return 1 - x ** 2
    return np.tanh(x)

# 가중치 배열 만드는 함수
def makeMatrix(i, j, fill=0.0):
    mat = []
    for i in range(i):
        mat.append([fill] * j)
    return mat

# 신경망의 실행
class NeuralNetwork:

    # 초깃값의 지정
    def __init__(self, layer=[2, 2, 1], bias=1, iterations=5000, lr=0.12, mo=0.22):

        self.iterations=iterations
        self.lr=lr
        self.mo=mo
        self.received_data = []
        self.real_data = None
        
        # 입력값(num_x), 은닉층 초깃값(num_yh), 출력층 초깃값(num_yo), 바이어스
        self.lengths = [0]*len(layer)
        self.lengths[0] = layer[0]+bias # 바이어스는 1로 지정(본문 참조)
        for i in range(1, len(layer)):
            self.lengths[i] = layer[i]

        # 활성화 함수 초깃값
        self.activations = [[1.0] * i for i in self.lengths]

        # 가중치 입력~출력 초깃값
        self.weights = [makeMatrix(self.lengths[i], self.lengths[i+1])
                        for i in range(len(self.lengths)-1)]
        for k in range(len(self.lengths)-1):
           for i in range(self.lengths[k]):
               for j in range(self.lengths[k+1]):
                  self.weights[k][i][j] = random.random()

        # 모멘텀 SGD를 위한 이전 가중치 초깃값
        self.gradients = [makeMatrix(self.lengths[i], self.lengths[i+1])
                          for i in range(len(self.lengths)-1)]

    # 업데이트 함수
    def update(self, inputs):

        # 입력 레이어의 활성화 함수
        for i in range(self.lengths[0] - 1):
           self.activations[0][i] = inputs[i]

        # 은닉층~출력층의 활성화 함수
        for k in range(len(self.lengths) - 1):
           for j in range(self.lengths[k+1]):
              sum = 0
              for i in range(self.lengths[k]):
                 sum = sum + self.activations[k][i] * self.weights[k][i][j]
              # 시그모이드와 tanh 중에서 활성화 함수 선택
              self.activations[k+1][j] = tanh(sum, False)

        return self.activations[-1][:]
    
    # 역전파의 실행
    def backPropagate(self, targets):

        # 델타 출력 계산
        nth_deltas = [[0.0] * self.lengths[-i-1] for i in range(len(self.lengths)-1)]
        for k in range(self.lengths[-1]):
            error = targets[k] - self.activations[-1][k]
            # 시그모이드와 tanh 중에서 활성화 함수 선택, 미분 적용
            nth_deltas[0][k] = tanh(self.activations[-1][k], True) * error

        # 은닉~입력 노드의 오차 함수
        for i in range(1, len(self.lengths) - 1):
           for j in range(self.lengths[-i-1]):
              error = 0.0
              for k in range(self.lengths[-i]):
                 error = error + nth_deltas[i-1][k] * self.weights[-i][j][k]
              # 시그모이드와 tanh 중에서 활성화 함수 선택, 미분 적용
              nth_deltas[i][j] = tanh(self.activations[-i-1][j], True) * error

        # 출력~입력 가중치 업데이트
        for i in range(1, len(self.lengths)):
           for j in range(self.lengths[-i-1]):
               for k in range(self.lengths[-i]):
                   gradient = nth_deltas[i-1][k] * self.activations[-i-1][j]
                   v = self.mo * self.gradients[-i][j][k] - self.lr * gradient
                   self.weights[-i][j][k] += v
                   self.gradients[-i][j][k] = gradient

        # 오차의 계산(최소 제곱법)
        error = 0.0
        for k in range(len(targets)):
            error = error + 0.5 * (targets[k] - self.activations[-1][k]) ** 2
        return error

    # 학습 실행
    def train(self, patterns, real_data = False):
        self.real_data = real_data
        if self.real_data == True:
            path1 = path + '\\' + 'field_data.json'
            with open(path1) as f:
                realdata = json.load(f)[0]
        
        #print("layers : " + str(self.lengths))
        errorlist = []
        #t = perfc()
        self.trace = [None]*5
        for i in range(self.iterations):
            
            error = 0.0
            objects = [[j%11-5, j//11-5, np.random.normal()] for j in range(int(self.lengths[0]-1))]
            obj_ = distrib_analyze(objects)
            self.trace[obj_.index(1)] = [self.weights, self.activations]
            patterns = [[[objects[i][2] for i in range(int(self.lengths[0]-1))], obj_] for j in range(1)]
            if self.real_data == True:
                patterns = realdata[i]
                
            #obj_ = [1, 0, 0, 0, 0]
            #patterns = [[[np.random.normal() for i in range(int(self.lengths[0]-1))], obj_] for j in range(1)]
            for p in patterns:
                inputs = p[0]
                targets = p[1]
                self.update(inputs)
                error = error + self.backPropagate(targets)
            #print(error)
            errorlist.append(error)
            if i % 1000 == 0:
                #print('error: %-.11f' % (sum(errorlist)/len(errorlist)))
                errorlist=[]
                
                #print(variety_test)
            '''if ([sum(errorlist) if errorlist != [] else 1][0]/[len(errorlist) if errorlist != [] else 1][0]) < 0.1**11:
                print(error)
                break'''

    def train_once(self, patterns):
        self.error = 0.0
        for p in patterns:
            inputs = p[0]
            targets = p[1]
            self.update(inputs)
            self.error = self.error + self.backPropagate(targets)
            
    def save(self, filename):
        neuron_data = [{
            'date' : str(datetime.now().year)+'-'+str(datetime.now().month)+'-'+str(datetime.now().day)+' '+str(datetime.now().hour)+':'+str(datetime.now().minute)+':'+str(datetime.now().second),
            'layers' : self.lengths,
            'weights' : self.weights
            }]
        
        filename = path + '\\' + filename + '.json'
        with open(filename, 'w') as f:
            json.dump(neuron_data, f, indent=2)

    def load(self, filename):
        filename = path + '\\' + filename + '.json'
        with open(filename) as f:
            neuron_data = json.load(f)
        self.lengths = neuron_data[-1]['layers']
        self.weights = neuron_data[-1]['weights']

    def view(self, father=None):
        if father == None:
            app = QApplication(sys.argv)
            ex = NeuronViewer(self)
            sys.exit(app.exec_())
        
   
class NeuronViewer(QWidget):
    def __init__(self, networks):
        super().__init__()
        self.network = networks
        self.initUI()
        
    def initUI(self):
        self.setGeometry(200, 200, 1000, 670)
        self.setWindowTitle('Neuron Network Viewer')
        pal = QPalette()
        pal.setColor(QPalette.Background,QColor(60,60,64))
        self.setAutoFillBackground(True)
        self.setPalette(pal)
        self.objects = [[0 for i in range(int(self.network.lengths[0]-1))] for j in range(int(self.network.lengths[0]-1))]

        if self.network.real_data == True:
            path1 = path + '\\' + 'field_data.json'
            with open(path1) as f:
                self.realdata = json.load(f)[0]
        self.realdata_num = 0

        self.show()

        #--------------------------------- Labels --------------------------------
        
        label1 = QLabel('Right : ', self)
        label2 = QLabel('Down : ', self)
        label3 = QLabel('Left : ', self)
        label4 = QLabel('Up : ', self)
        label5 = QLabel('Center : ', self)

        self.labels = [label1, label2, label3, label4, label5, *[QLabel('0', self) for i in range(5)]]

        label_ys = 190
        for i in self.labels[0:5]:
            i.move(260, label_ys)
            i.resize(100, 38)
            i.setFont(QFont('Arial', 17))
            i.setStyleSheet("color: white")
            i.show()
            label_ys += 38
                       
        label_ys = 195
        for i in self.labels[5:10]:
            i.move(380, label_ys)
            i.resize(200, 38)
            i.setFont(QFont('Arial', 17))
            i.setStyleSheet("color: white")
            i.show()
            label_ys += 38

        #--------------------------------- Funcs ---------------------------------

        self.btn1 = QPushButton('Stop Training', self)
        self.btn1.clicked.connect(self.stop_resume)
        self.btn1.resize(120, 30)
        self.btn1.move(250, 386)
        self.btn1.setStyleSheet("color : #54DFE3; background-color : #333335")
        self.btn1.show()

        self.btn2 = QPushButton('Save Current Data', self)
        self.btn2.clicked.connect(self.data_save)
        self.btn2.resize(120, 30)
        self.btn2.move(380, 386)
        self.btn2.setStyleSheet("color : #54DFE3; background-color : #333335")
        self.btn2.show()

        self.btn3 = QPushButton('Load', self)
        self.btn3.clicked.connect(self.data_load)
        self.btn3.resize(50, 20)
        self.btn3.move(925, 430)
        self.btn3.setStyleSheet("color : #DDDD22; background-color : #333335")
        self.btn3.show()

        self.dtlabel = QLabel('Data', self)
        self.dtlabel.move(20, 415)
        self.dtlabel.resize(100, 40)
        self.dtlabel.setFont(QFont('Arial', 15))
        self.dtlabel.setStyleSheet("color : white")
        self.dtlabel.show()

        self.treev = QTreeWidget(self)
        self.treev.setColumnCount(3)
        self.treev.header().setVisible(False)
        self.treev.setColumnWidth(0, 50)
        self.treev.setColumnWidth(1, 150)
        self.treev.show()
        self.treev.setStyleSheet("color : #FFFFFF; background-color : #111111")
        self.treev.resize(960, 200)
        self.treev.move(20, 450)
        self.data_preload('test')
        
        self.timer = QTimer(self)
        self.timer.start(1)
        self.timer.timeout.connect(self.timeout)
        
    def paintEvent(self, event):
        try:
           qp = QPainter()
           qp.begin(self)
           n_loc = []
           
           rooter = int((len(self.network.activations[0])-1)**0.5)
           midsetter = rooter*15
           n_stage = []
           spac = 6
           self.length = int((self.network.lengths[0]-1)**0.5)
           self.locset = 45+10*self.network.lengths[1]
           for j in range(len(self.network.activations[0])-1):
               xys = [j%rooter, j//rooter]
               minus_weight = abs(self.network.activations[0][j])-self.network.activations[0][j]
               self.colorsettings(qp, [50+180*(self.network.activations[0][j]-minus_weight), 50+180*(self.network.activations[0][j]-minus_weight), 50+130*(self.network.activations[0][j]-minus_weight)])
               n_stage.append([10+xys[0]*spac+xys[1]*spac*(rooter+1), 10])
               self.drawNeurons(qp, 10+xys[0]*spac+xys[1]*spac*(rooter+1), 10)
               
               qp.drawRect(20+xys[0]*20, self.locset+xys[1]*20, 20, 20)
               

           n_loc.append(n_stage)
               
           for i in range(1, len(self.network.activations)):
              n_stage = []
              lennode = len(self.network.activations[i])
              pre_lennode = len(self.network.activations[i-1])
              for j in range(lennode):
                 minus_weight = abs(self.network.activations[0][j])-self.network.activations[0][j]
                 self.colorsettings(qp, [50+180*(self.network.activations[i][j]-minus_weight), 50+180*(self.network.activations[i][j]-minus_weight), 50+130*(self.network.activations[i][j]-minus_weight)])
                 benchmark = n_loc[-1][-1]
                 
                 if i%2 != 0:
                     flipper = [-1 if i%4==1 and i>4 else 1][0]
                     flipper_truth = (flipper-1)/-2
                     n_stage.append([benchmark[0]+10,
                                     benchmark[1]+15+j*10*flipper-flipper_truth*30])
                     self.drawNeurons(qp, benchmark[0]+10,
                                      benchmark[1]+15+j*10*flipper-flipper_truth*30)
                 elif i%2 == 0:
                     isfour_0 = [-1 if i%4==0 else 1][0]
                     if i>4 and i%4 == 2:
                         benchmark = n_loc[-1][0]
                     n_stage.append([benchmark[0]+j*spac+9,
                                     benchmark[1]+5-(pre_lennode*5)+(10+pre_lennode*5)*isfour_0])
                     self.drawNeurons(qp, benchmark[0]+j*spac+9,
                                      benchmark[1]+5-(pre_lennode*5)+(10+pre_lennode*5)*isfour_0)
                     
              n_loc.append(n_stage)

           for j in range(len(self.network.weights[0])-1):
               for k in range(len(self.network.weights[0][j])):
                    rpoint = 200*(abs(self.network.weights[0][j][k]) - self.network.weights[0][j][k])
                    bpoint = [200*self.network.weights[0][j][k] if self.network.weights[0][j][k] >= 0 else 0][0]
                    self.colorsettings(qp, [rpoint, 0, bpoint], max_=[245,245,245])
                    self.drawNeurons(qp, n_loc[0][j][0], n_loc[0][j][1]+(k+1.5)*10)

            
           for i in range(1, len(self.network.weights)):
              for j in range(len(self.network.weights[i])):
                 for k in range(len(self.network.weights[i][j])):
                    rpoint = 150*(abs(self.network.weights[i][j][k]) - self.network.weights[i][j][k])
                    bpoint = [150*self.network.weights[i][j][k] if self.network.weights[i][j][k] >= 0 else 0][0]
                    self.colorsettings(qp, [rpoint, 0, bpoint], max_=[245,245,245])
                    if i%2 != 0:
                        self.drawNeurons(qp, n_loc[i][j][0]+(k+1.5)*6, n_loc[i][j][1])
                    elif i%2 == 0:
                        self.drawNeurons(qp, n_loc[i][j][0], n_loc[i][j][1]+(k+1.5)*10*[-1 if i%4==0 else 1][0])

           ys = 0
           for i in range(len(self.network.activations[-1])):
               minus_weight = abs(self.network.activations[-1][i])-self.network.activations[-1][i]
               self.colorsettings(qp, [50+180*(self.network.activations[-1][i]-minus_weight),
                                       50+180*(self.network.activations[-1][i]-minus_weight),
                                       50+130*(self.network.activations[-1][i]-minus_weight)])
               
               qp.drawRect(520, ys+190, 38, 38)
               
               ys += 40
           qp.end()
           
        except Exception as e:
           print(e)
           traceback.print_exc()
        
    def drawNeurons(self, qp, x_loc, y_loc):
        try:
           qp.drawRect(int(x_loc), int(y_loc), 4, 8)
        except Exception as e:
           print(e)

    def colorsettings(self, field, value, max_=[255, 255, 255], min_=[0,0,0]):
        R_ = max(min_[0], min(max_[0], value[0]))
        G_ = max(min_[1], min(max_[1], value[1]))
        B_ = max(min_[2], min(max_[2], value[2]))
        color = QColor(int(R_), int(G_), int(B_))
        field.setBrush(QBrush(color, 1))
        field.setPen(QPen(QColor(int(100+R_*0.3), int(100+G_*0.3), int(100+B_*0.3))))

    def training_view(self, data=None, times=100):
        try:
            self.network.iterations = 1
            '''objects = [[j%11-5, j//11-5, np.random.normal()] for j in range(int(self.network.lengths[0]-1))]
            obj_ = distrib_analyze(objects)
            dat = [[[objects[i][2] for i in range(int(self.network.lengths[0]-1))], obj_] for j in range(1)]'''
            if data == None:
                dat = [[j%11-5, j//11-5, self.objects[j//11][j%11]] for j in range(int(self.network.lengths[0]-1))]
                obj_ = distrib_analyze(dat)
                dat = [[[dat[i][2] for i in range(int(self.network.lengths[0]-1))], obj_] for j in range(1)]
            else :
                dat = data
        
            for i in range(times):
                self.network.train_once(dat)
                
            l1str = str(round(self.network.activations[-1][0], 7))
            l2str = str(round(self.network.activations[-1][1], 7))
            l3str = str(round(self.network.activations[-1][2], 7))
            l4str = str(round(self.network.activations[-1][3], 7))
            l5str = str(round(self.network.activations[-1][4], 7))

            self.label_ = [l1str, l2str, l3str, l4str, l5str]

            for i in range(5, len(self.labels)):
                self.labels[i].setText(self.label_[i-5])
                if self.network.activations[-1][i-5] < 0:
                    self.labels[i].move(372, 190+(i-5)*38)
                    self.labels[i].setStyleSheet("color: red")
                else :
                    self.labels[i].move(380, 190+(i-5)*38)
                    self.labels[i].setStyleSheet("color: blue")
                self.labels[np.argmax(self.network.activations[-1])+5].setStyleSheet("color: yellow")
            self.update()
        except Exception as e:
            print(e)
            traceback.print_exc()
        

    def mousePressEvent(self, e):
        try:
            if e.button() == Qt.LeftButton:
                if 20<e.x()<20+20*self.length and self.locset<e.y()<int(self.locset+20*self.length):
                    self.objects[int((e.y()-self.locset)/20)][int((e.x()-20)/20)] += 0.2
                    self.objects[int((e.y()-self.locset)/20)][int((e.x()-20)/20)] = max(0, min(1.5, self.objects[int((e.y()-self.locset)/20)][int((e.x()-20)/20)]))
                    self.training_view(times = 1)
            if e.button() == Qt.RightButton:
                if 20<e.x()<20+20*self.length and self.locset<e.y()<int(self.locset+20*self.length):
                    self.objects[int((e.y()-self.locset)/20)][int((e.x()-20)/20)] -= 0.2
                    self.objects[int((e.y()-self.locset)/20)][int((e.x()-20)/20)] = max(0, min(1.5, self.objects[int((e.y()-self.locset)/20)][int((e.x()-20)/20)]))
                    self.training_view(times = 1)
        except Exception as ev:
            print(ev)
            traceback.print_exc()

    '''def wheelEvent(self, e):
        direction = int(abs(e.angleDelta().y())/e.angleDelta().y())
        changer = self.network.trace[np.argmax(n.activations[-1])+direction]
        if changer != None:
            self.network.weights, self.network.activations = changer
            print(np.argmax(n.activations[-1])+direction)
            self.update()'''

    def timeout(self):
        try:
            objects = [[j%11-5, j//11-5, np.random.normal()] for j in range(int(self.network.lengths[0]-1))]
            obj_ = distrib_analyze(objects)
            dat = [[[objects[i][2] for i in range(int(self.network.lengths[0]-1))], obj_] for j in range(1)]
            if self.network.real_data == True:
                sights = np.array(self.realdata[self.realdata_num][0][0])
                sights = [round(i, 8) for i in list((sights-min(sights))/[max(sights) if max(sights)!=0.0 else 1][0])]
                dat = [[sights, self.realdata[self.realdata_num][0][1]]]
            self.training_view(dat, 1)
            self.realdata_num += 1
        except Exception as e:
            print(e)
            traceback.print_exc()

    def stop_resume(self):
        if self.timer == None:
            self.btn1.setText('Stop Training')
            self.timer = QTimer(self)
            self.timer.start(1)
            self.timer.timeout.connect(self.timeout)
        else :
            self.btn1.setText('Resume Training')
            self.timer.stop()
            self.timer = None

    def data_preload(self, filename):
        self.items = []
        self.filename = path + '\\' + filename + '.json'
        with open(self.filename) as f:
            self.nndata = json.load(f)
        number = 1
        for i in self.nndata:
            item = QTreeWidgetItem(self.treev, [str(number), str(i['date']), str(i['layers'])])
            self.items.append([item, i])
            number += 1

    def data_load(self):
        try:
            self.network.weights = self.items[int(self.treev.selectedItems()[0].data(0, 0))-1][1]['weights']
            self.network.layers = self.treev.selectedItems()[0].data(1, 0)
        except Exception as e:
            print(e)
            traceback.print_exc()

    def data_save(self):
        try:
            network_data = [i[1] for i in self.items]
            new_data = {
                'date' : str(datetime.now().year)+'-'+str(datetime.now().month)+'-'+str(datetime.now().day)+' '+str(datetime.now().hour)+':'+str(datetime.now().minute)+':'+str(datetime.now().second),
                'layers' : self.network.lengths,
                'weights' : self.network.weights
                }
                
            network_data.append(new_data)
            with open(self.filename, 'w') as f:
                json.dump(network_data, f, indent=2)
            item = QTreeWidgetItem(self.treev, [str(int(self.items[-1][0].data(0, 0))+1),
                                                str(new_data['date']),
                                                str(new_data['layers'])])
            self.items.append([item, new_data])
        except Exception as e:
            print(e)
            traceback.print_exc()
    

def all_neurons(dat, iter_=5000):
    for i in range(6, 10):
        for j in range(5, 10):
            for k in range(5, 15):
                print([4,i,j,k,1])
                n = NeuralNetwork(layer=[4, i, j, k, 1], iterations=iter_)
                n.train(dat)
                print('done')
   

if __name__ == '__main__':

    #all_neurons(data)
    t = time.time()
    n = NeuralNetwork(layer=[15**2, 20, 15, 15, 5], iterations=1)
    #n.load('test')
    # 학습 실행
    n.train(data)
    print(time.time()-t)

    # 결괏값 출력
    n.view()


