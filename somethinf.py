Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

================ RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ===============
Done!
Epoch 1

Test Error: 
 Accuracy: 79.6%, Avg loss: 0.205241 

0.24136117100715637
Epoch 11

Test Error: 
 Accuracy: 89.7%, Avg loss: 0.106323 

0.08953502029180527
Epoch 21

Test Error: 
 Accuracy: 89.9%, Avg loss: 0.107254 

0.10781226307153702
26.42795729637146
Epoch 1

Test Error: 
 Accuracy: 62.5%, Avg loss: 1.005740 

0.9890037775039673
Epoch 11

Test Error: 
 Accuracy: 74.8%, Avg loss: 0.683018 

0.538800835609436
Epoch 21

Test Error: 
 Accuracy: 75.4%, Avg loss: 0.680063 

0.41347527503967285
Epoch 31

Test Error: 
 Accuracy: 76.0%, Avg loss: 0.678232 

0.47649437189102173
33.5936918258667
Epoch 1

Test Error: 
 Accuracy: 29.6%, Avg loss: 1.691158 

1.7591647505760193
Epoch 31

Test Error: 
 Accuracy: 41.1%, Avg loss: 1.441404 

1.450009286403656
Epoch 61

Test Error: 
 Accuracy: 41.7%, Avg loss: 1.410498 

1.405554473400116
Epoch 91

Test Error: 
 Accuracy: 41.5%, Avg loss: 1.396931 

1.324802279472351
19.65841507911682
for i in range(10):
    print([p[i*11+j][1].item() for j in range(11)])

    
[2, 2, 3, 2, 3, 2, 3, 3, 3, 2, 2]
[2, 2, 3, 3, 3, 2, 2, 2, 0, 0, 2]
[5, 2, 0, 0, 2, 5, 2, 5, 0, 5, 5]
[0, 5, 2, 2, 0, 3, 5, 0, 5, 0, 5]
[5, 5, 0, 2, 0, 5, 5, 5, 5, 5, 0]
[0, 5, 2, 0, 0, 5, 5, 5, 0, 5, 5]
[5, 2, 5, 0, 5, 5, 5, 0, 5, 0, 2]
[5, 5, 5, 2, 3, 3, 2, 2, 2, 2, 2]
[2, 3, 3, 2, 2, 3, 3, 2, 3, 3, 0]
[0, 5, 0, 2, 3, 2, 5, 5, 5, 3, 0]
model_dist(p[i][0])[0], model_dir(p[i][0])[0]
(tensor([0., 0.], grad_fn=<SelectBackward0>), tensor([0.0000, 1.9254, 2.5359, 0.0000], grad_fn=<SelectBackward0>))
((torch.argmax(model_dist(p[i][0])[0])*4)+(torch.argmax(model_dir(p[i][0])[0])+1))
tensor(2)
code = {1:0, 2:2, 3:3, 4:1, 5:1, 6:2, 7:0, 8:3}
code[i]
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    code[i]
KeyError: 9
for i in range(10):
...     es = []
...     for j in range(11):
...         es.append(((torch.argmax(model_dist(p[i][0])[0])*4)+(torch.argmax(model_dir(p[i][0])[0])+1)))
SyntaxError: expected an indented block after 'for' statement on line 1

for i in range(10):
     es = []
     for j in range(11):
         es.append(((torch.argmax(model_dist(p[i][0])[0])*4)+(torch.argmax(model_dir(p[i][0])[0])+1)))

         
for i in range(10):
     es = []
     for j in range(11):
         es.append(((torch.argmax(model_dist(p[i][0])[0])*4)+(torch.argmax(model_dir(p[i][0])[0])+1)))
     print(es)

     
[tensor(3), tensor(3), tensor(4), tensor(3), tensor(3), tensor(3), tensor(3), tensor(1), tensor(4), tensor(3), tensor(4)]
[tensor(3), tensor(3), tensor(3), tensor(3), tensor(3), tensor(3), tensor(3), tensor(4), tensor(4), tensor(1), tensor(1)]
[tensor(3), tensor(4), tensor(3), tensor(4), tensor(3), tensor(3), tensor(3), tensor(3), tensor(3), tensor(3), tensor(1)]
[tensor(4), tensor(3), tensor(3), tensor(3), tensor(1), tensor(4), tensor(3), tensor(4), tensor(3), tensor(4), tensor(3)]
[tensor(3), tensor(4), tensor(3), tensor(3), tensor(4), tensor(4), tensor(1), tensor(3), tensor(4), tensor(3), tensor(3)]
[tensor(4), tensor(3), tensor(4), tensor(3), tensor(3), tensor(3), tensor(1), tensor(4), tensor(4), tensor(4), tensor(4)]
[tensor(4), tensor(4), tensor(3), tensor(3), tensor(3), tensor(3), tensor(3), tensor(4), tensor(4), tensor(3), tensor(3)]
[tensor(3), tensor(3), tensor(3), tensor(3), tensor(3), tensor(3), tensor(3), tensor(3), tensor(3), tensor(3), tensor(3)]
[tensor(3), tensor(3), tensor(3), tensor(3), tensor(4), tensor(3), tensor(3), tensor(3), tensor(4), tensor(1), tensor(3)]
[tensor(3), tensor(2), tensor(2), tensor(3), tensor(2), tensor(3), tensor(3), tensor(3), tensor(2), tensor(2), tensor(3)]
for i in range(10):
     es = []
     for j in range(11):
         es.append(((torch.argmax(model_dist(p[i][0])[0])*4)+(torch.argmax(model_dir(p[i][0])[0])+1)).item())
     print(es)

     
[3, 3, 3, 3, 1, 3, 3, 4, 3, 3, 4]
[3, 3, 4, 3, 4, 4, 3, 3, 3, 4, 3]
[3, 3, 3, 3, 4, 3, 3, 3, 1, 3, 4]
[4, 4, 3, 3, 4, 3, 3, 3, 3, 3, 3]
[3, 1, 3, 1, 3, 3, 4, 4, 4, 3, 1]
[4, 3, 4, 3, 4, 3, 3, 1, 3, 3, 4]
[3, 1, 3, 3, 1, 3, 4, 3, 3, 3, 3]
[3, 3, 4, 3, 3, 3, 3, 3, 3, 3, 3]
[3, 3, 3, 3, 4, 3, 3, 3, 3, 3, 3]
[3, 2, 2, 2, 2, 3, 2, 2, 3, 3, 3]
for i in range(10):
    print([p[i*11+j][1].item() for j in range(11)])

    
[2, 2, 3, 2, 3, 2, 3, 3, 3, 2, 2]
[2, 2, 3, 3, 3, 2, 2, 2, 0, 0, 2]
[5, 2, 0, 0, 2, 5, 2, 5, 0, 5, 5]
[0, 5, 2, 2, 0, 3, 5, 0, 5, 0, 5]
[5, 5, 0, 2, 0, 5, 5, 5, 5, 5, 0]
[0, 5, 2, 0, 0, 5, 5, 5, 0, 5, 5]
[5, 2, 5, 0, 5, 5, 5, 0, 5, 0, 2]
[5, 5, 5, 2, 3, 3, 2, 2, 2, 2, 2]
[2, 3, 3, 2, 2, 3, 3, 2, 3, 3, 0]
[0, 5, 0, 2, 3, 2, 5, 5, 5, 3, 0]
for i in range(10):
     es = []
     for j in range(11):
         es.append(code[((torch.argmax(model_dist(p[i][0])[0])*4)+(torch.argmax(model_dir(p[i][0])[0])+1)).item()])
     print(es)

     
[0, 0, 3, 3, 3, 0, 3, 1, 3, 3, 3]
[1, 3, 3, 3, 3, 3, 1, 3, 3, 3, 3]
[3, 3, 3, 1, 3, 3, 3, 3, 1, 3, 0]
[3, 3, 1, 0, 3, 1, 3, 3, 1, 3, 3]
[1, 3, 0, 3, 3, 3, 3, 3, 3, 1, 1]
[0, 1, 3, 1, 3, 3, 0, 3, 3, 3, 1]
[1, 2, 3, 3, 3, 0, 3, 0, 1, 3, 3]
[3, 1, 1, 3, 0, 3, 3, 3, 0, 1, 0]
[1, 3, 3, 3, 3, 3, 3, 3, 3, 3, 0]
[2, 2, 3, 3, 3, 3, 3, 3, 3, 3, 2]
code = {1:0, 2:2, 3:3, 4:1, 5:1, 6:2, 7:0, 8:3}
\
for i in range(10):
     es = []
     for j in range(11):
         es.append(code[((torch.argmax(model_dist(p[i][0])[0])*4)+(torch.argmax(model_dir(p[i][0])[0])+1)).item()])
     print(es)

     
[3, 3, 1, 3, 3, 3, 0, 3, 3, 1, 0]
[0, 0, 3, 3, 3, 3, 1, 0, 3, 3, 3]
[3, 0, 3, 3, 3, 3, 3, 3, 1, 1, 3]
[3, 3, 3, 3, 3, 1, 3, 3, 3, 3, 3]
[3, 3, 3, 3, 3, 3, 3, 1, 3, 3, 0]
[3, 3, 3, 3, 3, 2, 3, 3, 3, 3, 3]
[3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3]
[3, 3, 3, 1, 0, 1, 0, 3, 3, 3, 0]
[1, 0, 3, 3, 3, 3, 3, 3, 3, 3, 3]
[3, 3, 2, 3, 3, 2, 3, 3, 3, 3, 3]
for i in range(10):
    print([p[i*11+j][1].item() for j in range(11)])for i in range(10):
         es = []
         for j in range(11):
             es.append(((torch.argmax(model_dist(p[i][0])[0])*4)+(torch.argmax(model_dir(p[i][0])[0])+1)).item())
         print(es)
         
SyntaxError: invalid syntax
for i in range(10):
     es = []
     for j in range(11):
         es.append(code[((torch.argmax(model_dist(p[i][0])[0])*4)+(torch.argmax(model_dir(p[i][0])[0])+1)).item()])
     print(es)

     
[3, 3, 1, 1, 3, 3, 3, 1, 3, 1, 0]
[3, 3, 1, 3, 1, 3, 1, 1, 3, 3, 3]
[0, 3, 3, 3, 3, 0, 3, 3, 3, 0, 3]
[3, 3, 3, 3, 1, 3, 3, 1, 2, 3, 1]
[3, 3, 3, 1, 3, 3, 1, 3, 3, 3, 3]
[3, 1, 3, 3, 3, 0, 3, 1, 3, 3, 0]
[0, 3, 1, 3, 0, 1, 1, 1, 3, 3, 0]
[3, 3, 0, 3, 3, 1, 3, 3, 3, 1, 1]
[3, 3, 3, 3, 3, 3, 3, 3, 0, 3, 3]
[3, 3, 2, 3, 3, 3, 2, 2, 3, 3, 2]
>>> code = {1:0, 2:2, 3:3, 4:1, 5:1, 6:2, 7:0, 8:3}
>>> code = {1:0, 2:1, 3:2, 4:3, 5:1, 6:0, 7:3, 8:2}
>>> for i in range(10):
...      es = []
...      for j in range(11):
...          es.append(code[((torch.argmax(model_dist(p[i][0])[0])*4)+(torch.argmax(model_dir(p[i][0])[0])+1)).item()])
...      print(es)
... 
...      
[2, 2, 3, 3, 2, 3, 2, 0, 2, 2, 2]
[0, 3, 0, 2, 3, 3, 2, 2, 0, 2, 2]
[2, 2, 3, 2, 2, 2, 3, 2, 2, 3, 0]
[2, 3, 3, 2, 0, 2, 3, 2, 3, 2, 3]
[3, 2, 2, 2, 2, 2, 2, 3, 2, 2, 3]
[3, 2, 2, 3, 2, 0, 2, 3, 2, 2, 2]
[2, 2, 0, 0, 0, 2, 2, 2, 2, 2, 2]
[2, 2, 0, 2, 0, 2, 2, 2, 2, 2, 0]
[2, 2, 2, 2, 2, 2, 2, 3, 2, 3, 2]
[2, 1, 2, 2, 2, 2, 1, 1, 2, 2, 1]
>>> for i in range(10):
...     print([p[i*11+j][1].item() for j in range(11)])
... 
...     
[2, 2, 3, 2, 3, 2, 3, 3, 3, 2, 2]
[2, 2, 3, 3, 3, 2, 2, 2, 0, 0, 2]
[5, 2, 0, 0, 2, 5, 2, 5, 0, 5, 5]
[0, 5, 2, 2, 0, 3, 5, 0, 5, 0, 5]
[5, 5, 0, 2, 0, 5, 5, 5, 5, 5, 0]
[0, 5, 2, 0, 0, 5, 5, 5, 0, 5, 5]
[5, 2, 5, 0, 5, 5, 5, 0, 5, 0, 2]
[5, 5, 5, 2, 3, 3, 2, 2, 2, 2, 2]
[2, 3, 3, 2, 2, 3, 3, 2, 3, 3, 0]
[0, 5, 0, 2, 3, 2, 5, 5, 5, 3, 0]
>>> se1 = [[p[i*11+j][1].item() for j in range(11)] for i in range(10)]
>>> se2 = [[code[((torch.argmax(model_dist(p[i][0])[0])*4)+(torch.argmax(model_dir(p[i][0])[0])+1)).item()] for j in range(11)] for i in range(10)]
>>> 
se2
[[3, 0, 2, 2, 0, 2, 2, 2, 2, 0, 2], [3, 0, 3, 2, 2, 2, 2, 2, 2, 2, 2], [2, 2, 2, 3, 2, 2, 2, 2, 2, 3, 2], [2, 2, 2, 2, 2, 2, 2, 2, 2, 3, 2], [2, 3, 2, 2, 2, 3, 2, 2, 2, 2, 2], [2, 2, 2, 2, 2, 2, 2, 0, 2, 2, 2], [2, 2, 0, 2, 0, 2, 2, 2, 2, 0, 3], [2, 0, 2, 2, 0, 3, 2, 1, 2, 3, 2], [0, 2, 2, 2, 0, 2, 2, 0, 2, 2, 3], [2, 2, 1, 2, 2, 2, 2, 2, 0, 2, 1]]
torch.tensor(se2)==torch.tensor(se1)
tensor([[False, False, False,  True, False,  True, False, False, False, False,
          True],
        [False, False,  True, False, False,  True,  True,  True, False, False,
          True],
        [False,  True, False, False,  True, False,  True, False, False, False,
         False],
        [False, False,  True,  True, False, False, False, False, False, False,
         False],
        [False, False, False,  True, False, False, False, False, False, False,
         False],
        [False, False,  True, False, False, False, False, False, False, False,
         False],
        [False,  True, False, False, False, False, False, False, False,  True,
         False],
        [False, False, False,  True, False,  True,  True, False,  True, False,
          True],
        [False, False, False,  True, False, False, False, False, False, False,
         False],
        [False, False, False,  True, False,  True, False, False, False, False,
         False]])
22/121
0.18181818181818182
