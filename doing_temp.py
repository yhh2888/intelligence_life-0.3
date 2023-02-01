Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

================ RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ===============
Done!
flist = featurecall('distances')
flist1 = feature_change(p, flist)
model_dist = NeuralNetwork([11*11, 128, 128, 128, 2])

ted = trd = DataLoader(p[int(len(flist)//1.2):], batch_size=170)
trd = DataLoader(p[0:int(len(flist)//1.2)], batch_size=170)
optim_dist = torch.optim.Adam(model_dist.parameters(), lr=learning_rate, betas=(0.9, 0.999), eps=1e-10, weight_decay=1e-3,
                             amsgrad=False)
test(30, 10, model_dist, trd, ted, optim_dist)
Epoch 1

Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    test(30, 10, model_dist, trd, ted, optim_dist)
  File "C:\Users\KDCA\Desktop\IL\base\temp2.py", line 160, in test
    train_loop(trd, mod, loss_fn, optim)
  File "C:\Users\KDCA\Desktop\IL\base\temp2.py", line 119, in train_loop
    loss = loss_fn(pred, y)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\loss.py", line 1174, in forward
    return F.cross_entropy(input, target, weight=self.weight,
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\functional.py", line 3026, in cross_entropy
    return torch._C._nn.cross_entropy_loss(input, target, weight, _Reduction.get_enum(reduction), ignore_index, label_smoothing)
IndexError: Target 2 is out of bounds.
ted = DataLoader(flist1[int(len(flist)//1.2):], batch_size=170)
trd = DataLoader(flist[0:int(len(flist)//1.2)], batch_size=170)
trd = DataLoader(flist1[0:int(len(flist)//1.2)], batch_size=170)
optim_dist = torch.optim.Adam(model_dist.parameters(), lr=learning_rate, betas=(0.9, 0.999), eps=1e-10, weight_decay=1e-3,
                             amsgrad=False)

test(30, 10, model_dist, trd, ted, optim_dist)
Epoch 1

loss: 0.265831  [17000/18956]
Test Error: 
 Accuracy: 79.6%, Avg loss: 0.207249 

loss: 0.137641  [17000/18956]
loss: 0.066485  [17000/18956]
loss: 0.089214  [17000/18956]
loss: 0.087702  [17000/18956]
loss: 0.082612  [17000/18956]
loss: 0.115788  [17000/18956]
loss: 0.099078  [17000/18956]
loss: 0.086431  [17000/18956]
loss: 0.081452  [17000/18956]
Epoch 11

loss: 0.081484  [17000/18956]
Test Error: 
 Accuracy: 89.0%, Avg loss: 0.113934 

loss: 0.104953  [17000/18956]
loss: 0.066169  [17000/18956]
loss: 0.064970  [17000/18956]
loss: 0.062651  [17000/18956]
loss: 0.077669  [17000/18956]
loss: 0.076810  [17000/18956]
loss: 0.068463  [17000/18956]
loss: 0.089618  [17000/18956]
loss: 0.108405  [17000/18956]
Epoch 21

loss: 0.077914  [17000/18956]
Test Error: 
 Accuracy: 90.8%, Avg loss: 0.096490 

loss: 0.054016  [17000/18956]
loss: 0.076527  [17000/18956]
loss: 0.087307  [17000/18956]
loss: 0.072400  [17000/18956]
loss: 0.063713  [17000/18956]
loss: 0.065527  [17000/18956]
loss: 0.104385  [17000/18956]
loss: 0.090214  [17000/18956]
loss: 0.076442  [17000/18956]
27.159437656402588
model
NeuralNetwork(
  (flatten): Flatten(start_dim=1, end_dim=-1)
  (stack): Sequential(
    (0): Linear(in_features=121, out_features=128, bias=True)
    (1): ReLU()
    (2): Dropout(p=0.1, inplace=False)
    (3): Linear(in_features=128, out_features=128, bias=True)
    (4): ReLU()
    (5): Dropout(p=0.1, inplace=False)
    (6): Linear(in_features=128, out_features=128, bias=True)
    (7): ReLU()
    (8): Dropout(p=0.1, inplace=False)
    (9): Linear(in_features=128, out_features=4, bias=True)
    (10): ReLU()
    (11): Dropout(p=0.1, inplace=False)
  )
)
test(30, 10, model, train_dataloader, test_dataloader, optim_dist)
Epoch 1

Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    test(30, 10, model, train_dataloader, test_dataloader, optim_dist)
  File "C:\Users\KDCA\Desktop\IL\base\temp2.py", line 160, in test
    train_loop(trd, mod, loss_fn, optim)
  File "C:\Users\KDCA\Desktop\IL\base\temp2.py", line 119, in train_loop
    loss = loss_fn(pred, y)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\loss.py", line 1174, in forward
    return F.cross_entropy(input, target, weight=self.weight,
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\functional.py", line 3026, in cross_entropy
    return torch._C._nn.cross_entropy_loss(input, target, weight, _Reduction.get_enum(reduction), ignore_index, label_smoothing)
IndexError: Target 5 is out of bounds.
>>> test(30, 10, model, train_dataloader, test_dataloader, optimizer)
Epoch 1

Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    test(30, 10, model, train_dataloader, test_dataloader, optimizer)
  File "C:\Users\KDCA\Desktop\IL\base\temp2.py", line 160, in test
    train_loop(trd, mod, loss_fn, optim)
  File "C:\Users\KDCA\Desktop\IL\base\temp2.py", line 119, in train_loop
    loss = loss_fn(pred, y)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\loss.py", line 1174, in forward
    return F.cross_entropy(input, target, weight=self.weight,
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\functional.py", line 3026, in cross_entropy
    return torch._C._nn.cross_entropy_loss(input, target, weight, _Reduction.get_enum(reduction), ignore_index, label_smoothing)
IndexError: Target 5 is out of bounds.
>>> model = NeuralNetwork([11*11, 128, 128, 128, 6])
>>> optimizer = torch.optim.Adam(model.parameters(), lr=learning_rate, betas=(0.9, 0.999), eps=1e-10, weight_decay=1e-3,
...                              amsgrad=False)
>>> test(30, 10, model, train_dataloader, test_dataloader, optimizer)
Epoch 1

loss: 1.575763  [10000/20625]
loss: 1.641011  [20000/20625]
Test Error: 
 Accuracy: 39.2%, Avg loss: 1.631313 

loss: 1.549311  [10000/20625]
loss: 1.606251  [20000/20625]
loss: 1.544470  [10000/20625]
loss: 1.632695  [20000/20625]
loss: 1.538178  [10000/20625]
loss: 1.628896  [20000/20625]
loss: 1.552841  [10000/20625]
loss: 1.646860  [20000/20625]
loss: 1.435078  [10000/20625]
loss: 1.554238  [20000/20625]
loss: 1.404852  [10000/20625]
loss: 1.533168  [20000/20625]
loss: 1.448245  [10000/20625]
loss: 1.532586  [20000/20625]
loss: 1.416053  [10000/20625]
loss: 1.557901  [20000/20625]
loss: 1.389257  [10000/20625]
loss: 1.549612  [20000/20625]
Epoch 11

loss: 1.430456  [10000/20625]
loss: 1.549680  [20000/20625]
Test Error: 
 Accuracy: 39.0%, Avg loss: 1.577146 

loss: 1.401977  [10000/20625]
loss: 1.591099  [20000/20625]
loss: 1.372547  [10000/20625]
loss: 1.496099  [20000/20625]
loss: 1.377670  [10000/20625]
loss: 1.541487  [20000/20625]
loss: 1.366734  [10000/20625]
loss: 1.591537  [20000/20625]
loss: 1.415346  [10000/20625]
loss: 1.489860  [20000/20625]
loss: 1.455697  [10000/20625]
loss: 1.527907  [20000/20625]
loss: 1.399323  [10000/20625]
loss: 1.568652  [20000/20625]
loss: 1.432511  [10000/20625]
loss: 1.551316  [20000/20625]
loss: 1.454455  [10000/20625]
loss: 1.570389  [20000/20625]
Epoch 21

loss: 1.469102  [10000/20625]
loss: 1.602621  [20000/20625]
Test Error: 
 Accuracy: 39.8%, Avg loss: 1.569490 

loss: 1.366814  [10000/20625]
loss: 1.565212  [20000/20625]
loss: 1.374659  [10000/20625]
loss: 1.552596  [20000/20625]
loss: 1.390964  [10000/20625]
loss: 1.611019  [20000/20625]
loss: 1.370618  [10000/20625]
loss: 1.313702  [20000/20625]
loss: 1.398621  [10000/20625]
loss: 1.386081  [20000/20625]
loss: 1.301077  [10000/20625]
loss: 1.384167  [20000/20625]
loss: 1.303696  [10000/20625]
loss: 1.394839  [20000/20625]
loss: 1.363915  [10000/20625]
loss: 1.382864  [20000/20625]
loss: 1.360304  [10000/20625]
loss: 1.406880  [20000/20625]
56.38887405395508
flist = featurecall('directions')
flist2 = feature_change(p, flist)
model_dir = NeuralNetwork([11*11, 128, 128, 128, 4])
optim_dir = torch.optim.Adam(model_dir.parameters(), lr=learning_rate, betas=(0.9, 0.999), eps=1e-10, weight_decay=1e-3,
                             amsgrad=False)
ted1 = DataLoader(flist2[int(len(flist)//1.2):], batch_size=170)
trd1 = DataLoader(flist2[0:int(len(flist)//1.2)], batch_size=170)
test(30, 10, model_dir, trd1, ted1, optim_dir)
Epoch 1

loss: 1.386294  [17000/18956]
Test Error: 
 Accuracy: 45.1%, Avg loss: 1.220765 

loss: 1.387967  [17000/18956]
loss: 1.387614  [17000/18956]
loss: 1.386740  [17000/18956]
loss: 1.386661  [17000/18956]
loss: 1.386425  [17000/18956]
loss: 1.387020  [17000/18956]
loss: 1.386931  [17000/18956]
loss: 1.387175  [17000/18956]
loss: 1.386519  [17000/18956]
Epoch 11

loss: 1.386620  [17000/18956]
Test Error: 
 Accuracy: 44.5%, Avg loss: 1.123517 

loss: 1.106213  [17000/18956]
loss: 0.860207  [17000/18956]
loss: 0.865964  [17000/18956]
loss: 0.830035  [17000/18956]
loss: 0.763171  [17000/18956]
loss: 0.834668  [17000/18956]
loss: 0.758980  [17000/18956]
loss: 0.793374  [17000/18956]
loss: 0.766756  [17000/18956]
Epoch 21

loss: 0.774029  [17000/18956]
Test Error: 
 Accuracy: 67.7%, Avg loss: 0.851211 

loss: 0.730319  [17000/18956]
loss: 0.765682  [17000/18956]
loss: 0.799920  [17000/18956]
loss: 0.780732  [17000/18956]
loss: 0.739119  [17000/18956]
loss: 0.780219  [17000/18956]
loss: 0.765802  [17000/18956]
loss: 0.804617  [17000/18956]
loss: 0.758311  [17000/18956]
24.99962067604065
test(1, 10, model_dir, trd1, ted1, optim_dir)
Epoch 1

loss: 0.777769  [17000/18956]
Test Error: 
 Accuracy: 66.5%, Avg loss: 0.867821 

1.4579370021820068
test(10, 4, model_dir, trd1, ted1, optim_dir)
Epoch 1

loss: 0.773403  [17000/18956]
Test Error: 
 Accuracy: 66.5%, Avg loss: 0.860292 

loss: 0.769692  [17000/18956]
loss: 0.789984  [17000/18956]
loss: 0.760276  [17000/18956]
Epoch 5

loss: 0.725538  [17000/18956]
Test Error: 
 Accuracy: 67.2%, Avg loss: 0.885958 

loss: 0.754616  [17000/18956]
loss: 0.753445  [17000/18956]
loss: 0.794374  [17000/18956]
Epoch 9

loss: 0.724943  [17000/18956]
Test Error: 
 Accuracy: 66.7%, Avg loss: 0.856186 

loss: 0.764642  [17000/18956]
15.278332710266113
test_loop(trd, model_dist, loss_fn, True)
Test Error: 
 Accuracy: 90.0%, Avg loss: 0.105612 

model_dist(trd.dataset[0])
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    model_dist(trd.dataset[0])
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\Desktop\IL\base\temp2.py", line 105, in forward
    x = self.flatten(x)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\flatten.py", line 46, in forward
    return input.flatten(self.start_dim, self.end_dim)
AttributeError: 'tuple' object has no attribute 'flatten'
model_dist(trd.dataset[0][0])
tensor([[4.2373, 0.0000]], grad_fn=<MulBackward0>)
trd.dataset[0][1]
tensor(0)
model_dist(trd.dataset[1231][0])
tensor([[0.0000, 6.1234]], grad_fn=<MulBackward0>)
trd.dataset[1231][1]
tensor(1)
trd.dataset[1231][1]
tensor(1)
model_dist(trd.dataset[1231][0])
tensor([[0.0000, 5.5104]], grad_fn=<MulBackward0>)
model_dist(trd.dataset[1231][0])
tensor([[0.0000, 5.7686]], grad_fn=<MulBackward0>)
model_dist(trd.dataset[1231][0])
tensor([[0.0000, 5.8019]], grad_fn=<MulBackward0>)
model_dist(trd.dataset[1231][0])
tensor([[0.0000, 7.8568]], grad_fn=<MulBackward0>)
model_dist(trd.dataset[1231][0])
tensor([[0.0000, 7.1567]], grad_fn=<MulBackward0>)
model_dist(trd.dataset[1231][0])
tensor([[0.0000, 6.3238]], grad_fn=<MulBackward0>)
model_dist(trd.dataset[1231][0])
tensor([[0.0000, 6.7560]], grad_fn=<MulBackward0>)
model_dist(trd.dataset[1231][0])
tensor([[0.0000, 5.5786]], grad_fn=<MulBackward0>)
model_dist(trd.dataset[1231][0])
tensor([[0., 0.]], grad_fn=<MulBackward0>)
model_dist(trd.dataset[1231][0])
tensor([[0.0000, 6.5135]], grad_fn=<MulBackward0>)
model_dist(trd.dataset[1231][0])
tensor([[0.0000, 5.9843]], grad_fn=<MulBackward0>)

tensor([[0.0000, 5.9843]], grad_fn=<MulBackward0>)
SyntaxError: invalid syntax
model_dist(trd.dataset[0])
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    model_dist(trd.dataset[0])
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\Desktop\IL\base\temp2.py", line 105, in forward
    x = self.flatten(x)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\flatten.py", line 46, in forward
    return input.flatten(self.start_dim, self.end_dim)
AttributeError: 'tuple' object has no attribute 'flatten'
model_dist(trd.dataset[1231][0])
tensor([[0.0000, 6.7248]], grad_fn=<MulBackward0>)
test(10, 4, model_dir, trd1, ted1, optim_dir)
Epoch 1

loss: 0.788546  [17000/18956]
Test Error: 
 Accuracy: 67.1%, Avg loss: 0.863723 

loss: 0.780059  [17000/18956]
loss: 0.816308  [17000/18956]
loss: 0.733943  [17000/18956]
Epoch 5

loss: 0.749211  [17000/18956]
Test Error: 
 Accuracy: 67.3%, Avg loss: 0.864277 

loss: 0.752876  [17000/18956]
loss: 0.761510  [17000/18956]
loss: 0.754119  [17000/18956]
Epoch 9

loss: 0.751209  [17000/18956]
Test Error: 
 Accuracy: 67.2%, Avg loss: 0.853090 

loss: 0.744163  [17000/18956]
15.451980829238892
model
NeuralNetwork(
  (flatten): Flatten(start_dim=1, end_dim=-1)
  (stack): Sequential(
    (0): Linear(in_features=121, out_features=128, bias=True)
    (1): ReLU()
    (2): Dropout(p=0.1, inplace=False)
    (3): Linear(in_features=128, out_features=128, bias=True)
    (4): ReLU()
    (5): Dropout(p=0.1, inplace=False)
    (6): Linear(in_features=128, out_features=128, bias=True)
    (7): ReLU()
    (8): Dropout(p=0.1, inplace=False)
    (9): Linear(in_features=128, out_features=6, bias=True)
    (10): ReLU()
    (11): Dropout(p=0.1, inplace=False)
  )
)
model1 = NeuralNetwork([121, 121])
model1(trd.dataset[0][0])
tensor([[0.0000, 0.0000, 0.0000, 0.0000, 0.0287, 0.0000, 0.0545, 0.0000, 0.0000,
         0.0454, 0.0000, 0.0025, 0.0591, 0.0419, 0.0975, 0.0000, 0.0000, 0.0000,
         0.0077, 0.0000, 0.0000, 0.0000, 0.0194, 0.0000, 0.0000, 0.0000, 0.0596,
         0.0000, 0.0000, 0.0000, 0.0026, 0.0000, 0.0024, 0.0000, 0.0000, 0.0710,
         0.0292, 0.0000, 0.0497, 0.0000, 0.0000, 0.0000, 0.0000, 0.0766, 0.0000,
         0.0000, 0.0892, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0485, 0.0557,
         0.0368, 0.0000, 0.0000, 0.0000, 0.0237, 0.0000, 0.0392, 0.0000, 0.0558,
         0.0000, 0.0000, 0.0000, 0.0407, 0.0025, 0.0000, 0.0000, 0.0198, 0.0000,
         0.0042, 0.0887, 0.0531, 0.0000, 0.0000, 0.0000, 0.0324, 0.0000, 0.0547,
         0.0046, 0.0996, 0.0000, 0.0000, 0.0000, 0.0000, 0.0000, 0.0974, 0.0855,
         0.0391, 0.0000, 0.0000, 0.0373, 0.0290, 0.0000, 0.1035, 0.0642, 0.0000,
         0.0914, 0.0000, 0.0199, 0.0000, 0.0090, 0.0000, 0.0000, 0.0000, 0.0224,
         0.0000, 0.0063, 0.0000, 0.0000, 0.0141, 0.0000, 0.0000, 0.0261, 0.0000,
         0.0000, 0.0000, 0.0789, 0.0277]], grad_fn=<MulBackward0>)
trd.dataset[0][0]
tensor([[[0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
          0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
          0.0000e+00],
         [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
          0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
          0.0000e+00],
         [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
          0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
          0.0000e+00],
         [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
          0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
          0.0000e+00],
         [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
          0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
          0.0000e+00],
         [1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
          0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
          0.0000e+00],
         [1.0000e-04, 1.0000e-04, 1.0000e-04, 0.0000e+00, 0.0000e+00,
          0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
          0.0000e+00],
         [3.0000e-04, 2.0000e-04, 1.0000e-04, 0.0000e+00, 0.0000e+00,
          0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
          0.0000e+00],
         [7.0000e-04, 3.0000e-04, 2.0000e-04, 1.0000e-04, 0.0000e+00,
          0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
          0.0000e+00],
         [9.1000e-03, 6.0000e-04, 2.0000e-04, 1.0000e-04, 0.0000e+00,
          0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
          0.0000e+00],
         [5.0000e-02, 9.0000e-04, 3.0000e-04, 1.0000e-04, 0.0000e+00,
          0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
          0.0000e+00]]])
model(model1(trd.dataset[0][0]))
tensor([[1.3762, 0.3216, 0.0000, 0.3684, 0.0000, 1.2126]],
       grad_fn=<MulBackward0>)
model0.0000e+00],
SyntaxError: unmatched ']'
[1.0000e-04, 1.0000e-04, 1.0000e-04, 0.0000e+00, 0.0000e+00,]
[0.0001, 0.0001, 0.0001, 0.0, 0.0]
models = [NeuralNetwork([121, 121]) for i in range(8)]
models[0]
NeuralNetwork(
  (flatten): Flatten(start_dim=1, end_dim=-1)
  (stack): Sequential(
    (0): Linear(in_features=121, out_features=121, bias=True)
    (1): ReLU()
    (2): Dropout(p=0.1, inplace=False)
  )
)
