Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: C:\Users\hyunhoyang\Desktop\IL\mainstart.py =============
pygame 2.1.0 (SDL 2.0.16, Python 3.9.6)
Hello from the pygame community. https://www.pygame.org/contribute.html
Network System stabilized
>>> with open('mobs_data.json') as f:
    d = json.load(f)

    
>>> d_=[]
>>> for i in range(len(d)-1):
  if len(d[i]) > 1:
    if len(d[i][:-1]) == len(d[i+1][:-1]):
        for j in range(len(d[i][:-1])):
          try:
              d_.append([[d[i][j][0]-d[i][-1][0], d[i][j][1]-d[i][-1][1]], [d[i+1][j][0]-d[i][j][0], d[i+1][j][1]-d[i][j][1]]])
          except Exception as e:
              print(e, d[i+1], d[i])

              
>>> def a(item):
	if item == [1, 0]:
		return 0
	elif item == [0, 1]:
		return 1
	elif item == [-1, 0]:
		return 2
	elif item == [0, -1]:
		return 3
	elif item == [0, 0]:
		return 5

	
>>> deleted = 0
>>> net = NeuralNetwork(2)
>>> for i in range(len(d_)):
	i -= deleted
	if -1<=d_[i][1][0]<=1 and -1<=d_[i][1][1]<=1:
		d_[i][0] = torch.tensor(d_[i][0], dtype=torch.float32)
		d_[i][1] = torch.tensor(a(d_[i][1]))
	else :
		del d_[i]
		deleted += 1

		
>>> net.base_set(d_, call=False)
>>> net.roll(1)
2.536787509918213
>>> set1 = [[net.feature_label[i*11+j][1].item() for j in range(11)] for i in range(-1000, -2)]
>>> set2 = [[torch.argmax(net(torch.tensor([torch.Tensor.tolist(li68[i*11+j][0])]))).item() for j in range(11)] for i in range(-1000, -2)]
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    set2 = [[torch.argmax(net(torch.tensor([torch.Tensor.tolist(li68[i*11+j][0])]))).item() for j in range(11)] for i in range(-1000, -2)]
  File "<pyshell#14>", line 1, in <listcomp>
    set2 = [[torch.argmax(net(torch.tensor([torch.Tensor.tolist(li68[i*11+j][0])]))).item() for j in range(11)] for i in range(-1000, -2)]
  File "<pyshell#14>", line 1, in <listcomp>
    set2 = [[torch.argmax(net(torch.tensor([torch.Tensor.tolist(li68[i*11+j][0])]))).item() for j in range(11)] for i in range(-1000, -2)]
NameError: name 'li68' is not defined
>>> set2 = [[torch.argmax(net(torch.tensor([torch.Tensor.tolist(net[i*11+j][0])]))).item() for j in range(11)] for i in range(-1000, -2)]
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    set2 = [[torch.argmax(net(torch.tensor([torch.Tensor.tolist(net[i*11+j][0])]))).item() for j in range(11)] for i in range(-1000, -2)]
  File "<pyshell#15>", line 1, in <listcomp>
    set2 = [[torch.argmax(net(torch.tensor([torch.Tensor.tolist(net[i*11+j][0])]))).item() for j in range(11)] for i in range(-1000, -2)]
  File "<pyshell#15>", line 1, in <listcomp>
    set2 = [[torch.argmax(net(torch.tensor([torch.Tensor.tolist(net[i*11+j][0])]))).item() for j in range(11)] for i in range(-1000, -2)]
TypeError: 'NeuralNetwork' object is not subscriptable
>>> set2 = [[torch.argmax(net(torch.tensor([torch.Tensor.tolist(d_[i*11+j][0])]))).item() for j in range(11)] for i in range(-1000, -2)]

