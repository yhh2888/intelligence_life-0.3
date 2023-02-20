Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

================ RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ===============
Done!
Epoch 1

Test Error: 
 Accuracy: 79.9%, Avg loss: 0.199848 

0.21566447615623474
Epoch 11

Test Error: 
 Accuracy: 91.0%, Avg loss: 0.094170 

0.07106436043977737
Epoch 21

Test Error: 
 Accuracy: 90.0%, Avg loss: 0.101960 

0.059943266212940216
39.15319061279297
Epoch 1

Traceback (most recent call last):
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\utils\data\_utils\collate.py", line 146, in collate
    return elem_type([collate(samples, collate_fn_map=collate_fn_map) for samples in transposed])
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\utils\data\_utils\collate.py", line 146, in <listcomp>
    return elem_type([collate(samples, collate_fn_map=collate_fn_map) for samples in transposed])
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\utils\data\_utils\collate.py", line 138, in collate
    if not all(len(elem) == elem_size for elem in it):
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\utils\data\_utils\collate.py", line 138, in <genexpr>
    if not all(len(elem) == elem_size for elem in it):
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\_tensor.py", line 894, in __len__
    raise TypeError("len() of a 0-d tensor")
TypeError: len() of a 0-d tensor

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "C:\Users\KDCA\Desktop\IL\base\temp2.py", line 195, in <module>
    test(30, 10, model_dist01, trd01, ted01, optim_dist01, sched_dist01)
  File "C:\Users\KDCA\Desktop\IL\base\temp2.py", line 166, in test
    losses = train_loop(trd, mod, loss_fn, optim)
  File "C:\Users\KDCA\Desktop\IL\base\temp2.py", line 121, in train_loop
    for batch, (X, y) in enumerate(dataloader):
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\utils\data\dataloader.py", line 628, in __next__
    data = self._next_data()
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\utils\data\dataloader.py", line 671, in _next_data
    data = self._dataset_fetcher.fetch(index)  # may raise StopIteration
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\utils\data\_utils\fetch.py", line 61, in fetch
    return self.collate_fn(data)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\utils\data\_utils\collate.py", line 265, in default_collate
    return collate(batch, collate_fn_map=default_collate_fn_map)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\utils\data\_utils\collate.py", line 149, in collate
    return [collate(samples, collate_fn_map=collate_fn_map) for samples in transposed]
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\utils\data\_utils\collate.py", line 149, in <listcomp>
    return [collate(samples, collate_fn_map=collate_fn_map) for samples in transposed]
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\utils\data\_utils\collate.py", line 138, in collate
    if not all(len(elem) == elem_size for elem in it):
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\utils\data\_utils\collate.py", line 138, in <genexpr>
    if not all(len(elem) == elem_size for elem in it):
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\_tensor.py", line 894, in __len__
    raise TypeError("len() of a 0-d tensor")
TypeError: len() of a 0-d tensor
flist01[0][0][0]
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
len(flist1)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    len(flist1)
NameError: name 'flist1' is not defined. Did you mean: 'flist'?
len(flist01)
2
len(flistd)
22748

================ RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ===============
Done!
Epoch 1

Test Error: 
 Accuracy: 80.0%, Avg loss: 0.197394 

0.21286246180534363
Epoch 11

Test Error: 
 Accuracy: 88.8%, Avg loss: 0.170817 

0.18333488702774048
Epoch 21

Test Error: 
 Accuracy: 89.9%, Avg loss: 0.161987 

0.17871929705142975
38.362417221069336
Epoch 1

Test Error: 
 Accuracy: 81.2%, Avg loss: 0.157555 

0.20729520916938782
Epoch 11

Test Error: 
 Accuracy: 89.7%, Avg loss: 0.094897 

0.07616132497787476
Epoch 21

Test Error: 
 Accuracy: 90.2%, Avg loss: 0.089121 

0.09290807694196701
39.80654764175415
Epoch 1

Test Error: 
 Accuracy: 81.5%, Avg loss: 0.165130 

0.19834908843040466
Epoch 11

Test Error: 
 Accuracy: 90.4%, Avg loss: 0.087910 

0.06193546578288078
Epoch 21

Test Error: 
 Accuracy: 90.8%, Avg loss: 0.082274 

0.07135182619094849
44.2955048084259
Epoch 1

Test Error: 
 Accuracy: 63.0%, Avg loss: 0.992503 

0.9580702781677246
Epoch 11

Test Error: 
 Accuracy: 73.3%, Avg loss: 0.694211 

0.5728533864021301
Epoch 21

Test Error: 
 Accuracy: 75.4%, Avg loss: 0.681551 

0.42757290601730347
Epoch 31

Test Error: 
 Accuracy: 75.0%, Avg loss: 0.670468 

0.4246719479560852
53.77345037460327
Traceback (most recent call last):
  File "C:\Users\KDCA\Desktop\IL\base\temp2.py", line 219, in <module>
    for i in range(len(flist1)):
NameError: name 'flist1' is not defined. Did you mean: 'flist'?
for i in range(len(flist01)):
    li68.append((torch.tensor([torch.Tensor.tolist((torch.cat((model_dist(flist1[i][0])[0], model_dir(flist1[i][0])[0]))))]), remain_labels[i]))

Traceback (most recent call last):
  File "<pyshell#4>", line 2, in <module>
    li68.append((torch.tensor([torch.Tensor.tolist((torch.cat((model_dist(flist1[i][0])[0], model_dir(flist1[i][0])[0]))))]), remain_labels[i]))
NameError: name 'flist1' is not defined. Did you mean: 'flist'?
for i in range(len(flistd)):
    li68.append((torch.tensor([torch.Tensor.tolist((torch.cat((model_dist(flistd[i][0])[0], model_dir(flistd[i][0])[0]))))]), remain_labels[i]))


================ RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ===============
Done!
Epoch 1

Test Error: 
 Accuracy: 80.0%, Avg loss: 0.205193 

0.22107142210006714
Epoch 11

Test Error: 
 Accuracy: 89.8%, Avg loss: 0.104932 

0.07899346202611923
Epoch 21

Test Error: 
 Accuracy: 90.6%, Avg loss: 0.096118 

0.06027930602431297
38.503040075302124
Epoch 1

Test Error: 
 Accuracy: 81.2%, Avg loss: 0.689621 

0.6931477189064026
Epoch 11

Test Error: 
 Accuracy: 89.8%, Avg loss: 0.093032 

0.11570481956005096
Epoch 21

Test Error: 
 Accuracy: 90.4%, Avg loss: 0.087945 

0.07821127027273178
37.17062282562256
Epoch 1

Test Error: 
 Accuracy: 81.2%, Avg loss: 0.185819 

0.2464628964662552
Epoch 11

Test Error: 
 Accuracy: 90.2%, Avg loss: 0.144135 

0.20166663825511932
Epoch 21

Test Error: 
 Accuracy: 90.5%, Avg loss: 0.142028 

0.1718425750732422
43.79016137123108
Epoch 1

Test Error: 
 Accuracy: 44.7%, Avg loss: 1.222421 

1.386772871017456
Epoch 11

Test Error: 
 Accuracy: 44.4%, Avg loss: 1.053172 

1.06685471534729
Epoch 21

Test Error: 
 Accuracy: 44.7%, Avg loss: 1.043439 

1.0438361167907715
Epoch 31

Test Error: 
 Accuracy: 43.9%, Avg loss: 1.044781 

1.066788673400879
51.41989612579346
Epoch 1

Test Error: 
 Accuracy: 38.0%, Avg loss: 1.616135 

1.6362403631210327
Epoch 31

Test Error: 
 Accuracy: 39.0%, Avg loss: 1.460009 

1.4177952408790588
Epoch 61

Test Error: 
 Accuracy: 39.6%, Avg loss: 1.454117 

1.4716798663139343
Epoch 91

Test Error: 
 Accuracy: 39.8%, Avg loss: 1.451212 

1.3939183354377747
20.115244150161743
li55=[]
for i in range(len(flist01)):
    li55.append((torch.tensor([torch.Tensor.tolist((torch.cat((model_dist(flist01[i][0])[0], model_dir(flist01[i][0])[0]))))]), remain_labels[i]))

    
train_fin = DataLoader(li55[0:int(len(p)//1.2)], batch_size=100)
test_fin = DataLoader(li55[int(len(p)//1.2):], batch_size=100)


test(100, 30, model_fin, train_fin, test_fin, optim_fin, sched_fin)
Epoch 1

Test Error: 
 Accuracy: 40.2%, Avg loss: 1.446472 

1.400347888469696
Epoch 31

Test Error: 
 Accuracy: 39.8%, Avg loss: 1.447162 

1.3036009073257446
Epoch 61

Test Error: 
 Accuracy: 40.8%, Avg loss: 1.430560 

1.4074000120162964
Epoch 91

Test Error: 
 Accuracy: 40.2%, Avg loss: 1.449588 

1.3774367570877075
19.681668281555176
>>> for i in range(len(flist01)):
...     li55.append((torch.tensor([torch.Tensor.tolist((torch.cat((model_dist(flist02[i][0])[0], model_dir(flist02[i][0])[0]))))]), remain_labels[i]))
... 
...     
>>> len(flist01)
22748
>>> len(flist02)
22748
>>> train_fin = DataLoader(li55[0:int(len(p)//1.2)], batch_size=100)
>>> test_fin = DataLoader(li55[int(len(p)//1.2):], batch_size=100)
>>> test(100, 30, model_fin, train_fin, test_fin, optim_fin, sched_fin)
Epoch 1

Test Error: 
 Accuracy: 41.0%, Avg loss: 1.441996 

1.3744767308235168
Epoch 31

Test Error: 
 Accuracy: 41.2%, Avg loss: 1.440687 

1.3867138624191284
Epoch 61

Test Error: 
 Accuracy: 40.7%, Avg loss: 1.444967 

1.397337257862091
Epoch 91

Test Error: 
 Accuracy: 41.2%, Avg loss: 1.439615 

1.3656824827194214
28.376216411590576
>>> 
========== RESTART: C:\Users\KDCA\Desktop\IL\base\feature_analysis.py ==========
