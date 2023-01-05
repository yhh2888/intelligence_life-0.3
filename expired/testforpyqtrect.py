import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from analysis_functions import *
import numpy as np
import random, time

realmap = np.zeros(shape=(100, 100))
random_mobs = [[random.randint(0, 100), random.randint(0, 100)] for i in range(20)]
protagonist = [random.randint(30, 70), random.randint(30, 70)]

random_code = [[random.randint(0, 4), random.randint(5, 15), random.uniform(0, 0.5)] for i in range(7)]

def map_cal():
    global realmap
    realmap = np.zeros(shape=(100, 100))
    matfull = max([random_code[i][1] for i in range(len(random_code))])
    mat = np.zeros(shape=(matfull*2-1, matfull*2-1))
    for i in range(len(random_code)):
        matsize = random_code[i][1]
        function_selector = random_code[i][0]
        if function_selector == 0:
            matrix = O_matrix(matsize,
                              matsize, matsize,
                              point=random_code[i][2],
                              rotation=random.randint(0, 50))
        elif function_selector == 1:
            matrix = edge3_matrix(matsize, matsize,
                                  matsize,
                                  point=random_code[i][2],
                                  rotation=random.randint(0, 50))
        elif function_selector == 2:
            matrix = edge4_matrix(matsize, matsize,
                                  matsize,
                                  point=random_code[i][2],
                                  rotation=random.randint(0, 50))
        elif function_selector == 3:
            matrix = curve_matrix(matsize, matsize,
                                  matsize,
                                  point=random_code[i][2],
                                  rotation=random.randint(0, 50))
        elif function_selector == 4:
            matrix = reflect_matrix(matsize, matsize,
                                    matsize,
                                    point=random_code[i][2],
                                    rotation=random.randint(0, 50))
        conloc = int(((matfull*2-1)-matrix.shape[0])/2)
        mat += conjunct2([conloc, conloc], matrix, matfull*2-1)
    
    for j in range(1, len(random_mobs)):
        realmap = conjunct_matrix([random_mobs[j][0], random_mobs[j][1]],
                                   mat, realmap)
        
    return realmap

realmap =map_cal()

class MyApp(QMainWindow):

    def __init__(self):
        super().__init__()
        self.image = QImage(QSize(1000, 1000), QImage.Format_RGB32)
        self.image.fill(Qt.white)
        self.drawing = False
        self.brush_size = 5
        self.brush_color = Qt.black
        self.last_point = QPoint()
        self.initUI()

    def initUI(self):
        menubar = self.menuBar()
        menubar.setNativeMenuBar(False)
        filemenu1 = menubar.addMenu('File')
        filemenu2 = menubar.addMenu('Options')

        save_action = QAction('Save', self)
        save_action.setShortcut('Ctrl+S')
        save_action.triggered.connect(self.save)

        clear_action = QAction('Clear', self)
        clear_action.setShortcut('Ctrl+C')
        clear_action.triggered.connect(self.clear)

        filemenu1.addAction(save_action)
        filemenu1.addAction(clear_action)

        geneprint_action = QAction('Genetic information', self)
        geneprint_action.setShortcut('Ctrl+P')
        geneprint_action.triggered.connect(self.gene_print)

        genechange_action = QAction('Change gene random', self)
        genechange_action.setShortcut('Ctrl+R')
        genechange_action.triggered.connect(self.gene_change)

        filemenu2.addAction(genechange_action)
        filemenu2.addAction(geneprint_action)

        self.setWindowTitle('Simple Painter')
        self.setGeometry(300, 300, 1000, 1000)
        self.show()

    def paintEvent(self, e):
        canvas = QPainter()
        canvas.begin(self)
        canvas.drawImage(self.rect(), self.image, self.image.rect())
        
    def mousePressEvent(self, e):
        global realmap
        if e.button() == Qt.LeftButton:
            protagonist = [int(e.x()/10), int(e.y()/10)]
            colornum = 4
            painter = QPainter(self.image)
            
            try:
                
                t = time.time()
                for i in range(realmap.shape[0]):
                    for j in range(realmap.shape[1]):
                        point = realmap[i][j]
                        distance = ((i-protagonist[0])**2+(j-protagonist[1])**2)**0.5
                        point += random.uniform(0, 0.05)+distance/((2**0.5)*15)
                        colorpoint = 255-(point*255)/colornum
                        color_3 = QColor(*[[int(colorpoint) if 0<=colorpoint<=255 else 0][0] for k in range(3)])
                        painter.setBrush(color_3)
                        painter.setPen(Qt.NoPen)
                        painter.drawRect((i-1)*10, (j-1)*10, 10, 10)
                
                painter.setBrush(Qt.red)
                painter.setPen(Qt.NoPen)
                painter.drawRect(protagonist[0]*10, protagonist[1]*10, 10, 10)
                self.update()
                
                for j in range(len(random_mobs)):
                    random_mobs[j][0] += random.randint(-1, 1)
                    random_mobs[j][1] += random.randint(-1, 1)
                
                t = time.time()
                realmap = map_cal()
                
                print(time.time()-t)
                
            except Exception as e:
                print(e)

    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.drawing = False

    def save(self):
        fpath, _ = QFileDialog.getSaveFileName(self, 'Save Image', '', "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")

        if fpath:
            self.image.save(fpath)

    def clear(self):
        self.image.fill(Qt.white)
        self.update()

    def gene_print(self):
        print(random_code)

    def gene_change(self):
        global random_code
        random_code = [[random.randint(0, 4), random.randint(5, 7), random.uniform(0, 0.5)] for i in range(7)]


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())
