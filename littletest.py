Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

=============== RESTART: C:\Users\KDCA\Desktop\IL\base\network.py ==============
Network System stabilized
Successful Network Application, Test start
Epoch 10

Test Error: 
 Accuracy: 81.2%, Avg loss: 0.456068 

0.23525933921337128
Epoch 20

Test Error: 
 Accuracy: 83.6%, Avg loss: 0.415916 

0.16816550493240356
Epoch 30

Test Error: 
 Accuracy: 84.4%, Avg loss: 0.392521 

0.13982732594013214
Traceback (most recent call last):
  File "C:\Users\KDCA\Desktop\IL\base\network.py", line 354, in <module>
    model_fin.roll(150, 10)
  File "C:\Users\KDCA\Desktop\IL\base\network.py", line 162, in roll
    reinforce(epoch, alert, self, DataLoader(self.trd.dataset[first:last+1], batch_size=(last-first)//100), self.ted, self.optim, self.sched)
  File "C:\Users\KDCA\Desktop\IL\base\network.py", line 218, in reinforce
    losses = train_loop(trd, mod, loss_fn, optim)
  File "C:\Users\KDCA\Desktop\IL\base\network.py", line 179, in train_loop
    loss.backward()
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\_tensor.py", line 488, in backward
    torch.autograd.backward(
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\autograd\__init__.py", line 197, in backward
    Variable._execution_engine.run_backward(  # Calls into the C++ engine to run the backward pass
KeyboardInterrupt
model_fin.forward(li68[0][0])
tensor([[ 1.0045,  0.5727,  1.0497,  0.9223, -2.5762, -1.4927]],
       grad_fn=<AddmmBackward0>)
li68[0][0]
tensor([[0.0000e+00, 1.0000e+00, 0.0000e+00, 0.0000e+00, 1.0000e+00, 1.0000e+00,
         0.0000e+00, 2.0000e+00, 2.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         1.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 2.0000e+00, 2.0000e+00,
         2.0000e+00, 2.0000e+00, 2.0000e+00, 2.0000e+00, 2.0000e+00, 2.0000e+00,
         0.0000e+00, 8.7360e-01, 8.7360e-01, 1.0000e-04, 3.5800e-02, 3.5800e-02,
         0.0000e+00, 2.0990e-01, 2.0990e-01, 0.0000e+00, 2.8000e-03, 2.8000e-03,
         3.0000e-08, 9.0800e-06, 9.0800e-06, 0.0000e+00, 2.9050e-05, 2.9050e-05,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 1.0000e-04, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 1.0000e-04, 1.0000e-04, 1.0000e-04,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 3.0000e-04, 2.0000e-04, 1.0000e-04, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 7.0000e-04, 3.0000e-04, 2.0000e-04, 1.0000e-04, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         9.1000e-03, 6.0000e-04, 2.0000e-04, 1.0000e-04, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 5.0000e-02,
         9.0000e-04, 3.0000e-04, 1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 1.0000e-04, 2.0000e-04, 4.0000e-04, 4.8000e-03, 2.0050e-01,
         1.6870e-01, 3.1000e-03, 4.0000e-04, 1.0000e-04, 1.0000e-04, 1.0000e-04,
         1.0000e-04, 3.0000e-04, 5.0000e-04, 8.9000e-03, 4.5170e-01, 4.3140e-01,
         7.7000e-03, 4.0000e-04, 3.0000e-04, 3.0000e-04, 3.0000e-04, 4.0000e-04,
         5.0000e-04, 6.0000e-04, 1.2000e-03, 2.0000e-02, 2.1500e-02, 1.0000e-03,
         3.0000e-04, 9.0000e-04, 9.0000e-04, 9.0000e-04, 9.0000e-04, 3.0000e-03,
         2.7000e-03, 9.0000e-04, 7.0000e-04, 6.0000e-04, 4.0000e-04, 2.0000e-04,
         4.1000e-03, 4.2000e-03, 3.9000e-03, 5.5000e-03, 2.1130e-01, 2.0170e-01,
         4.1000e-03, 6.0000e-04, 3.0000e-04, 2.0000e-04, 1.0000e-04, 2.3430e-01,
         2.1300e-01, 2.2440e-01, 1.2900e-02, 4.0470e-01, 4.3840e-01, 8.9000e-03,
         5.0000e-04, 2.0000e-04, 1.0000e-04, 0.0000e+00, 4.9390e-01, 6.0280e-01,
         6.8650e-01, 1.6900e-02, 1.6400e-02, 1.9000e-02, 1.1000e-03, 3.0000e-04,
         1.0000e-04, 0.0000e+00, 0.0000e+00, 6.5500e-01, 1.0928e+00, 4.8730e-01,
         1.2800e-02, 1.6000e-03, 8.0000e-04, 4.0000e-04, 2.0000e-04, 1.0000e-04,
         0.0000e+00, 0.0000e+00, 1.0655e+00, 1.3774e+00, 5.0400e-02, 2.8000e-03,
         1.1000e-03, 4.0000e-04, 2.0000e-04, 1.0000e-04, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 3.6700e-02, 5.2200e-02, 3.9000e-03, 1.5000e-03, 6.0000e-04,
         2.0000e-04, 1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         1.5000e-03, 1.7000e-03, 1.2000e-03, 7.0000e-04, 3.0000e-04, 1.0000e-04,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 1.0000e-04, 2.0000e-04, 4.0000e-04, 4.8000e-03,
         2.0050e-01, 1.6870e-01, 3.1000e-03, 4.0000e-04, 1.0000e-04, 1.0000e-04,
         1.0000e-04, 1.0000e-04, 3.0000e-04, 5.0000e-04, 8.9000e-03, 4.5170e-01,
         4.3140e-01, 7.7000e-03, 4.0000e-04, 3.0000e-04, 3.0000e-04, 3.0000e-04,
         4.0000e-04, 5.0000e-04, 6.0000e-04, 1.2000e-03, 2.0000e-02, 2.1500e-02,
         1.0000e-03, 3.0000e-04, 9.0000e-04, 9.0000e-04, 9.0000e-04, 9.0000e-04,
         3.0000e-03, 2.7000e-03, 9.0000e-04, 7.0000e-04, 6.0000e-04, 4.0000e-04,
         2.0000e-04, 4.1000e-03, 4.2000e-03, 3.9000e-03, 5.5000e-03, 2.1130e-01,
         2.0170e-01, 4.1000e-03, 6.0000e-04, 3.0000e-04, 2.0000e-04, 1.0000e-04,
         2.3430e-01, 2.1300e-01, 2.2440e-01, 1.2900e-02, 4.0470e-01, 4.3840e-01,
         8.9000e-03, 5.0000e-04, 2.0000e-04, 1.0000e-04, 0.0000e+00, 4.9390e-01,
         6.0280e-01, 6.8650e-01, 1.6900e-02, 1.6400e-02, 1.9000e-02, 1.1000e-03,
         3.0000e-04, 1.0000e-04, 0.0000e+00, 0.0000e+00, 6.5500e-01, 1.0928e+00,
         4.8730e-01, 1.2800e-02, 1.6000e-03, 8.0000e-04, 4.0000e-04, 2.0000e-04,
         1.0000e-04, 0.0000e+00, 0.0000e+00, 1.0655e+00, 1.3774e+00, 5.0400e-02,
         2.8000e-03, 1.1000e-03, 4.0000e-04, 2.0000e-04, 1.0000e-04, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 3.6700e-02, 5.2200e-02, 3.9000e-03, 1.5000e-03,
         6.0000e-04, 2.0000e-04, 1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 1.5000e-03, 1.7000e-03, 1.2000e-03, 7.0000e-04, 3.0000e-04,
         1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00]])
li68[0][0].shape
torch.Size([1, 408])
net.forward(li68[0][0])
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    net.forward(li68[0][0])
NameError: name 'net' is not defined. Did you mean: 'next'?
net = NeuralNetwork(408)
net.forward(li68[0][0])
tensor([[ 0.1765,  0.1876, -0.0458, -0.1803, -0.4229,  0.1518]],
       grad_fn=<AddmmBackward0>)
net = NeuralNetwork(2)
with open('mobs_data.json') as f:
    d = json.load(f)

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    with open('mobs_data.json') as f:
FileNotFoundError: [Errno 2] No such file or directory: 'mobs_data.json'
with open(r'C:\Users\KDCA\Desktop\IL\mobs_data.json') as f:
    d = json.load(f)

d_=[]
for i in range(len(d)-1):
  if len(d[i]) > 1:
    if len(d[i][:-1]) == len(d[i+1][:-1]):
        for j in range(len(d[i][:-1])):
          try:
              d_.append([[d[i][j][0]-d[i][-1][0], d[i][j][1]-d[i][-1][1]], [d[i+1][j][0]-d[i][j][0], d[i+1][j][1]-d[i][j][1]]])
          except Exception as e:
              print(e, d[i+1], d[i])

torch.tensor(d_[0][0])
tensor([-50, -23])
torch.tensor(d_[0][0]).unsqueeze(0)
tensor([[-50, -23]])
net.forward(torch.tensor(d_[0][0]).unsqueeze(0))
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    net.forward(torch.tensor(d_[0][0]).unsqueeze(0))
  File "C:\Users\KDCA\Desktop\IL\base\network.py", line 98, in forward
    processed = self.start(X)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\linear.py", line 114, in forward
    return F.linear(input, self.weight, self.bias)
RuntimeError: mat1 and mat2 must have the same dtype
d_[0][0]
[-50, -23]
torch.tensor(d_[0][0]).unsqueeze(0).shape
torch.Size([1, 2])
net.forward(torch.tensor(d_[0][0]).unsqueeze(0))
Traceback (most recent call last):
  File "<pyshell#19>", line 1, in <module>
    net.forward(torch.tensor(d_[0][0]).unsqueeze(0))
  File "C:\Users\KDCA\Desktop\IL\base\network.py", line 98, in forward
    processed = self.start(X)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\linear.py", line 114, in forward
    return F.linear(input, self.weight, self.bias)
RuntimeError: mat1 and mat2 must have the same dtype
net = NeuralNetwork(2, cellout=1)
net.forward(torch.tensor(d_[0][0]).unsqueeze(0))
Traceback (most recent call last):
  File "<pyshell#21>", line 1, in <module>
    net.forward(torch.tensor(d_[0][0]).unsqueeze(0))
  File "C:\Users\KDCA\Desktop\IL\base\network.py", line 98, in forward
    processed = self.start(X)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\linear.py", line 114, in forward
    return F.linear(input, self.weight, self.bias)
RuntimeError: mat1 and mat2 must have the same dtype
netnet = NeuralNetwork(2, cellout=1, last=1)
net.forward(torch.tensor(d_[0][0]).unsqueeze(0))
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    net.forward(torch.tensor(d_[0][0]).unsqueeze(0))
  File "C:\Users\KDCA\Desktop\IL\base\network.py", line 98, in forward
    processed = self.start(X)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\linear.py", line 114, in forward
    return F.linear(input, self.weight, self.bias)
RuntimeError: mat1 and mat2 must have the same dtype
net.gencode
[[3, 1, 5], [4, 2, 1, 6], [0, 6, 7], [7, 5, 3, 8]]
nn.Flatten()
Flatten(start_dim=1, end_dim=-1)
nn.Flatten()(torch.tensor(d_[0][0]).unsqueeze(0))
tensor([[-50, -23]])
net.start(torch.tensor(d_[0][0]).unsqueeze(0))
Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    net.start(torch.tensor(d_[0][0]).unsqueeze(0))
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\linear.py", line 114, in forward
    return F.linear(input, self.weight, self.bias)
RuntimeError: mat1 and mat2 must have the same dtype
len(torch.tensor(d_[0][0]).unsqueeze(0).shape)
2
torch.tensor(d_[0][0]).unsqueeze(0).squeeze()
tensor([-50, -23])

=============== RESTART: C:\Users\KDCA\Desktop\IL\base\network.py ==============
Network System stabilized

================ RESTART: C:\Users\KDCA\Desktop\IL\mainstart.py ================
pygame 2.1.2 (SDL 2.0.18, Python 3.10.9)
Hello from the pygame community. https://www.pygame.org/contribute.html
Network System stabilized
with open('mobs_data.json') as f:
    d = json.load(f)

    
d_=[]
for i in range(len(d)-1):
  if len(d[i]) > 1:
    if len(d[i][:-1]) == len(d[i+1][:-1]):
        for j in range(len(d[i][:-1])):
          try:
              d_.append([[d[i][j][0]-d[i][-1][0], d[i][j][1]-d[i][-1][1]], [d[i+1][j][0]-d[i][j][0], d[i+1][j][1]-d[i][j][1]]])
          except Exception as e:
              print(e, d[i+1], d[i])

              
>>> net=NeuralNetwork(2)
>>> net(torch.tensor(d_[0][0]).unsqueeze(0))
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    net(torch.tensor(d_[0][0]).unsqueeze(0))
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\Desktop\IL\base\network.py", line 99, in forward
    processed = self.start(X)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\linear.py", line 114, in forward
    return F.linear(input, self.weight, self.bias)
RuntimeError: expected scalar type Long but found Float
>>> net(torch.tensor(d_[0][0], dtype=torch.float32).unsqueeze(0))
Traceback (most recent call last):
  File "<pyshell#37>", line 1, in <module>
    net(torch.tensor(d_[0][0], dtype=torch.float32).unsqueeze(0))
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\Desktop\IL\base\network.py", line 106, in forward
    rnn_out, hidden = self.stack[i](toinput.unsqueeze(1))
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\rnn.py", line 472, in forward
    self.check_forward_args(input, hx, batch_sizes)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\rnn.py", line 234, in check_forward_args
    self.check_input(input, batch_sizes)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\rnn.py", line 210, in check_input
    raise RuntimeError(
RuntimeError: input.size(-1) must be equal to input_size. Expected 18, got 1
