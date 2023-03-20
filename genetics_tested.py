Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

=========== RESTART: C:\Users\KDCA\Desktop\IL\Parameter_Developing.py ==========
pygame 2.1.2 (SDL 2.0.18, Python 3.10.9)
Hello from the pygame community. https://www.pygame.org/contribute.html
Done!

================ RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ===============
Done!
Epoch 1

Test Error: 
 Accuracy: 52.0%, Avg loss: 1.262313 

1.3380906581878662
Epoch 31

Test Error: 
 Accuracy: 79.7%, Avg loss: 0.558268 

0.6439196467399597
Epoch 61

Test Error: 
 Accuracy: 79.3%, Avg loss: 0.544146 

0.6394631266593933
Epoch 91

Test Error: 
 Accuracy: 79.0%, Avg loss: 0.564327 

0.5505417585372925
32.47649693489075
real_test: 0.8145454545454546

=========== RESTART: C:\Users\KDCA\Desktop\IL\Parameter_Developing.py ==========
pygame 2.1.2 (SDL 2.0.18, Python 3.10.9)
Hello from the pygame community. https://www.pygame.org/contribute.html
Done!
rep_test(2)
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    rep_test(2)
  File "C:\Users\KDCA\Desktop\IL\Parameter_Developing.py", line 66, in rep_test
    a.test(10, view_lock = view_lock)
  File "C:\Users\KDCA\Desktop\IL\Parameter_Developing.py", line 18, in test
    score = self.circumstances.run_by_AI(view_lock = view_lock, nn=self.nn)
  File "C:\Users\KDCA\Desktop\IL\Hitting_Frame.py", line 202, in run_by_AI
    sightrange = int((self.nn.lengths[0]-1)**0.5)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1269, in __getattr__
    raise AttributeError("'{}' object has no attribute '{}'".format(
AttributeError: 'NeuralNetwork' object has no attribute 'lengths'

============== RESTART: C:\Users\KDCA\Desktop\IL\Hitting_Frame.py ==============
pygame 2.1.2 (SDL 2.0.18, Python 3.10.9)
Hello from the pygame community. https://www.pygame.org/contribute.html
Done!
Traceback (most recent call last):
  File "C:\Users\KDCA\Desktop\IL\Hitting_Frame.py", line 458, in <module>
    game.run()
  File "C:\Users\KDCA\Desktop\IL\Hitting_Frame.py", line 162, in run
    if vision_print_on and buttoned:
UnboundLocalError: local variable 'vision_print_on' referenced before assignment

=========== RESTART: C:\Users\KDCA\Desktop\IL\Parameter_Developing.py ==========
pygame 2.1.2 (SDL 2.0.18, Python 3.10.9)
Hello from the pygame community. https://www.pygame.org/contribute.html
Done!
rep_test(2)
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    rep_test(2)
  File "C:\Users\KDCA\Desktop\IL\Parameter_Developing.py", line 66, in rep_test
    a.test(10, view_lock = view_lock)
  File "C:\Users\KDCA\Desktop\IL\Parameter_Developing.py", line 18, in test
    score = self.circumstances.run_by_AI(view_lock = view_lock, nn=self.nn)
  File "C:\Users\KDCA\Desktop\IL\Hitting_Frame.py", line 451, in run_by_AI
    self.nn.train_once(data)
AttributeError: 'Game' object has no attribute 'nn'

=========== RESTART: C:\Users\KDCA\Desktop\IL\Parameter_Developing.py ==========
pygame 2.1.2 (SDL 2.0.18, Python 3.10.9)
Hello from the pygame community. https://www.pygame.org/contribute.html
Done!
rep_test(2)

Warning (from warnings module):
  File "C:\Users\KDCA\Desktop\IL\Hitting_Frame.py", line 437
    locals()[n].append(torch.tensor(locals()[n[0:n.index('_')+1]+'now']))
UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    rep_test(2)
  File "C:\Users\KDCA\Desktop\IL\Parameter_Developing.py", line 66, in rep_test
    a.test(10, view_lock = view_lock)
  File "C:\Users\KDCA\Desktop\IL\Parameter_Developing.py", line 18, in test
    score = self.circumstances.run_by_AI(view_lock = view_lock, nn=self.nn)
  File "C:\Users\KDCA\Desktop\IL\Hitting_Frame.py", line 448, in run_by_AI
    netresult = torch.argmax(netmodel(fin_feature))
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\Desktop\IL\base\temp2.py", line 43, in forward
    logits = self.stack(x)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\container.py", line 204, in forward
    input = module(input)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\linear.py", line 114, in forward
    return F.linear(input, self.weight, self.bias)
RuntimeError: mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5)

=========== RESTART: C:\Users\KDCA\Desktop\IL\Parameter_Developing.py ==========
pygame 2.1.2 (SDL 2.0.18, Python 3.10.9)
Hello from the pygame community. https://www.pygame.org/contribute.html
Done!
rep_test(2)

Warning (from warnings module):
  File "C:\Users\KDCA\Desktop\IL\Hitting_Frame.py", line 437
    locals()[n].append(torch.tensor(locals()[n[0:n.index('_')+1]+'now']))
UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    rep_test(2)
  File "C:\Users\KDCA\Desktop\IL\Parameter_Developing.py", line 66, in rep_test
    a.test(10, view_lock = view_lock)
  File "C:\Users\KDCA\Desktop\IL\Parameter_Developing.py", line 18, in test
    score = self.circumstances.run_by_AI(view_lock = view_lock, nn=self.nn)
  File "C:\Users\KDCA\Desktop\IL\Hitting_Frame.py", line 448, in run_by_AI
    netresult = torch.argmax(netmodel(fin_feature))
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\Desktop\IL\base\temp2.py", line 43, in forward
    logits = self.stack(x)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\container.py", line 204, in forward
    input = module(input)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\linear.py", line 114, in forward
    return F.linear(input, self.weight, self.bias)
RuntimeError: mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5)

=========== RESTART: C:\Users\KDCA\Desktop\IL\Parameter_Developing.py ==========
pygame 2.1.2 (SDL 2.0.18, Python 3.10.9)
Hello from the pygame community. https://www.pygame.org/contribute.html
Done!
rep_test(2)

Warning (from warnings module):
  File "C:\Users\KDCA\Desktop\IL\Hitting_Frame.py", line 437
    locals()[n].append(torch.tensor(locals()[n[0:n.index('_')+1]+'now']))
UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
432
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
450
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
528
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5)
=========== RESTART: C:\Users\KDCA\Desktop\IL\Parameter_Developing.py ==========
pygame 2.1.2 (SDL 2.0.18, Python 3.10.9)
Hello from the pygame community. https://www.pygame.org/contribute.html
Done!
rep_test(2)

Warning (from warnings module):
  File "C:\Users\KDCA\Desktop\IL\Hitting_Frame.py", line 437
    locals()[n].append(torch.tensor(locals()[n[0:n.index('_')+1]+'now']))
UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
432
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
450
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
528
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
468
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x5) 420
390
402
528

=========== RESTART: C:\Users\KDCA\Desktop\IL\Parameter_Developing.py ==========
pygame 2.1.2 (SDL 2.0.18, Python 3.10.9)
Hello from the pygame community. https://www.pygame.org/contribute.html
Done!
rep_test(2)

Warning (from warnings module):
  File "C:\Users\KDCA\Desktop\IL\Hitting_Frame.py", line 437
    locals()[n].append(torch.tensor(locals()[n[0:n.index('_')+1]+'now']))
UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
432
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
450
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
528
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420
468

============== RESTART: C:\Users\KDCA\Desktop\IL\Hitting_Frame.py ==============
pygame 2.1.2 (SDL 2.0.18, Python 3.10.9)
Hello from the pygame community. https://www.pygame.org/contribute.html

=========== RESTART: C:\Users\KDCA\Desktop\IL\Parameter_Developing.py ==========
pygame 2.1.2 (SDL 2.0.18, Python 3.10.9)
Hello from the pygame community. https://www.pygame.org/contribute.html
Done!
rep_test(2)

Warning (from warnings module):
  File "C:\Users\KDCA\Desktop\IL\Hitting_Frame.py", line 437
    locals()[n].append(torch.tensor(locals()[n[0:n.index('_')+1]+'now']))
UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    rep_test(2)
  File "C:\Users\KDCA\Desktop\IL\Parameter_Developing.py", line 66, in rep_test
    a.test(10, view_lock = view_lock)
  File "C:\Users\KDCA\Desktop\IL\Parameter_Developing.py", line 18, in test
    score = self.circumstances.run_by_AI(view_lock = view_lock, nn=self.nn)
  File "C:\Users\KDCA\Desktop\IL\Hitting_Frame.py", line 448, in run_by_AI
    netresult = torch.argmax(netmodel(fin_feature))
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\Desktop\IL\base\temp2.py", line 43, in forward
    logits = self.stack(x)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\container.py", line 204, in forward
    input = module(input)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\linear.py", line 114, in forward
    return F.linear(input, self.weight, self.bias)
RuntimeError: mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6)

=========== RESTART: C:\Users\KDCA\Desktop\IL\Parameter_Developing.py ==========
pygame 2.1.2 (SDL 2.0.18, Python 3.10.9)
Hello from the pygame community. https://www.pygame.org/contribute.html
Done!
rep_test(2)

Warning (from warnings module):
  File "C:\Users\KDCA\Desktop\IL\Hitting_Frame.py", line 437
    locals()[n].append(torch.tensor(locals()[n[0:n.index('_')+1]+'now']))
UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).
Traceback (most recent call last):
  File "C:\Users\KDCA\Desktop\IL\Hitting_Frame.py", line 448, in run_by_AI
    netresult = torch.argmax(netmodel(fin_feature))
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\Desktop\IL\base\temp2.py", line 43, in forward
    logits = self.stack(x)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\container.py", line 204, in forward
    input = module(input)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\linear.py", line 114, in forward
    return F.linear(input, self.weight, self.bias)
RuntimeError: mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6)

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    rep_test(2)
  File "C:\Users\KDCA\Desktop\IL\Parameter_Developing.py", line 66, in rep_test
    a.test(10, view_lock = view_lock)
  File "C:\Users\KDCA\Desktop\IL\Parameter_Developing.py", line 18, in test
    score = self.circumstances.run_by_AI(view_lock = view_lock, nn=self.nn)
  File "C:\Users\KDCA\Desktop\IL\Hitting_Frame.py", line 450, in run_by_AI
    print(e, len(fin_feature[0]), len(fin_feature[0][0]), len(fin_feature))
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\_tensor.py", line 894, in __len__
    raise TypeError("len() of a 0-d tensor")
TypeError: len() of a 0-d tensor

=========== RESTART: C:\Users\KDCA\Desktop\IL\Parameter_Developing.py ==========
pygame 2.1.2 (SDL 2.0.18, Python 3.10.9)
Hello from the pygame community. https://www.pygame.org/contribute.html
Done!
rep_test(2)

Warning (from warnings module):
  File "C:\Users\KDCA\Desktop\IL\Hitting_Frame.py", line 437
    locals()[n].append(torch.tensor(locals()[n[0:n.index('_')+1]+'now']))
UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
432
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
450
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
528
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
468
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
390

=========== RESTART: C:\Users\KDCA\Desktop\IL\Parameter_Developing.py ==========
pygame 2.1.2 (SDL 2.0.18, Python 3.10.9)
Hello from the pygame community. https://www.pygame.org/contribute.html
Done!
rep_test(2)

Warning (from warnings module):
  File "C:\Users\KDCA\Desktop\IL\Hitting_Frame.py", line 437
    locals()[n].append(torch.tensor(locals()[n[0:n.index('_')+1]+'now']))
UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
432
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    rep_test(2)
  File "C:\Users\KDCA\Desktop\IL\Parameter_Developing.py", line 66, in rep_test
    a.test(10, view_lock = view_lock)
  File "C:\Users\KDCA\Desktop\IL\Parameter_Developing.py", line 18, in test
    score = self.circumstances.run_by_AI(view_lock = view_lock, nn=self.nn)
  File "C:\Users\KDCA\Desktop\IL\Hitting_Frame.py", line 422, in run_by_AI
    dist_now = [labeler(mat_sight, ['distances', 'maindist'])]
  File "C:\Users\KDCA\Desktop\IL\base\feature_analysis.py", line 57, in labeler
    if tensor[i][j] > min_size:
KeyboardInterrupt
rep_test(2)
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
372
432
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
mat1 and mat2 shapes cannot be multiplied (1x6 and 40x6) 420 1
396

=========== RESTART: C:\Users\KDCA\Desktop\IL\Parameter_Developing.py ==========
pygame 2.1.2 (SDL 2.0.18, Python 3.10.9)
Hello from the pygame community. https://www.pygame.org/contribute.html
Done!
rep_test(2)
438

Warning (from warnings module):
  File "C:\Users\KDCA\Desktop\IL\Hitting_Frame.py", line 438
    locals()[n].append(torch.tensor(locals()[n[0:n.index('_')+1]+'now']))
UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).
0.15951018749
462
516
540
474
480
540
420
468

=========== RESTART: C:\Users\KDCA\Desktop\IL\Parameter_Developing.py ==========
pygame 2.1.2 (SDL 2.0.18, Python 3.10.9)
Hello from the pygame community. https://www.pygame.org/contribute.html
Done!

=========== RESTART: C:\Users\KDCA\Desktop\IL\Parameter_Developing.py ==========
pygame 2.1.2 (SDL 2.0.18, Python 3.10.9)
Hello from the pygame community. https://www.pygame.org/contribute.html
Done!

=========== RESTART: C:\Users\KDCA\Desktop\IL\Parameter_Developing.py ==========
pygame 2.1.2 (SDL 2.0.18, Python 3.10.9)
Hello from the pygame community. https://www.pygame.org/contribute.html
Done!
rep_test(2)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    rep_test(2)
  File "C:\Users\KDCA\Desktop\IL\Parameter_Developing.py", line 70, in rep_test
    a.test(10, view_lock = view_lock)
  File "C:\Users\KDCA\Desktop\IL\Parameter_Developing.py", line 19, in test
    score = self.circumstances.run_by_AI(view_lock = view_lock, nn=self.nn, nn2=nn2)
NameError: name 'nn2' is not defined

=========== RESTART: C:\Users\KDCA\Desktop\IL\Parameter_Developing.py ==========
pygame 2.1.2 (SDL 2.0.18, Python 3.10.9)
Hello from the pygame community. https://www.pygame.org/contribute.html
Done!
rep_test(2)
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    rep_test(2)
  File "C:\Users\KDCA\Desktop\IL\Parameter_Developing.py", line 70, in rep_test
    a.test(10, view_lock = view_lock)
  File "C:\Users\KDCA\Desktop\IL\Parameter_Developing.py", line 19, in test
    score = self.circumstances.run_by_AI(view_lock = view_lock, nn=self.nn, nn2=nn2)
NameError: name 'nn2' is not defined

=========== RESTART: C:\Users\KDCA\Desktop\IL\Parameter_Developing.py ==========
pygame 2.1.2 (SDL 2.0.18, Python 3.10.9)
Hello from the pygame community. https://www.pygame.org/contribute.html
Done!
rep_test(2)
Traceback (most recent call last):
  File "<pyshell#15>", line 1, in <module>
    rep_test(2)
  File "C:\Users\KDCA\Desktop\IL\Parameter_Developing.py", line 71, in rep_test
    a.test(10, view_lock = view_lock)
  File "C:\Users\KDCA\Desktop\IL\Parameter_Developing.py", line 20, in test
    score = self.circumstances.run_by_AI(view_lock = view_lock, nn=self.nn, nn2=self.nn2)
TypeError: Game.run_by_AI() got an unexpected keyword argument 'nn2'

=========== RESTART: C:\Users\KDCA\Desktop\IL\Parameter_Developing.py ==========
pygame 2.1.2 (SDL 2.0.18, Python 3.10.9)
Hello from the pygame community. https://www.pygame.org/contribute.html
Done!
rep_test(2)
438

Warning (from warnings module):
  File "C:\Users\KDCA\Desktop\IL\Hitting_Frame.py", line 438
    locals()[n].append(torch.tensor(locals()[n[0:n.index('_')+1]+'now']))
UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).
0.31131636729
462
0.02399705427
516
582
0.13028987579
0.01419897757
312
426
498
0.04667114849
456
474
450
[438, 512, 566, 582, 412, 426, 498, 506, 474, 450] 486.4
119.1005790233612
432
492
438
492

=========== RESTART: C:\Users\KDCA\Desktop\IL\Parameter_Developing.py ==========
pygame 2.1.2 (SDL 2.0.18, Python 3.10.9)
Hello from the pygame community. https://www.pygame.org/contribute.html
Done!
rep_test(2)

Warning (from warnings module):
  File "C:\Users\KDCA\Desktop\IL\Hitting_Frame.py", line 436
    locals()[n].append(torch.tensor(locals()[n[0:n.index('_')+1]+'now']))
UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).
432
456
564
528
540
474

================ RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ===============
Done!
Epoch 1

Test Error: 
 Accuracy: 46.3%, Avg loss: 1.398431 

1.4457498788833618
Epoch 31

Test Error: 
 Accuracy: 79.8%, Avg loss: 0.539777 

0.5370895862579346
Epoch 61

Test Error: 
 Accuracy: 81.2%, Avg loss: 0.505314 

0.5006411671638489
Epoch 91

Test Error: 
 Accuracy: 80.9%, Avg loss: 0.512069 

0.49476945400238037
25.525272369384766
real_test: 0.8383636363636363
with torch.no_grad():
	for i in range(len(model_fin.stack[0].weight)):
		for j in range(len(model_fin.stack[0].weight[i])):
			if random.random() < 0.01:
				model_fin.stack[0].weight[i][j] = torch.tensor(random.random()*0.01, requires_grad=True)


				
Traceback (most recent call last):
  File "<pyshell#18>", line 4, in <module>
    if random.random() < 0.01:
NameError: name 'random' is not defined
import random
with torch.no_grad():
	for i in range(len(model_fin.stack[0].weight)):
		for j in range(len(model_fin.stack[0].weight[i])):
			if random.random() < 0.01:
				model_fin.stack[0].weight[i][j] = torch.tensor(random.random()*0.01, requires_grad=True)


				
test_loop(model_fin.ted, model_fin, loss_fn, alert=True)

Test Error: 
 Accuracy: 81.2%, Avg loss: 0.510444 

with torch.no_grad():
	for i in range(len(model_fin.stack[0].weight)):
		for j in range(len(model_fin.stack[0].weight[i])):
			if random.random() < 0.05:
				model_fin.stack[0].weight[i][j] = torch.tensor(random.random()*0.1, requires_grad=True)

				
test_loop(model_fin.ted, model_fin, loss_fn, alert=True)
Test Error: 
 Accuracy: 75.3%, Avg loss: 0.732166 

with torch.no_grad():
	for i in range(len(model_fin.stack[0].weight)):
		for j in range(len(model_fin.stack[0].weight[i])):
			if random.random() < 0.05:
				model_fin.stack[0].weight[i][j] = torch.tensor(random.random()*0.1, requires_grad=True)

				
test_loop(model_fin.ted, model_fin, loss_fn, alert=True)
Test Error: 
 Accuracy: 73.6%, Avg loss: 0.769328 

with torch.no_grad():
	for i in range(len(model_fin.stack[0].weight)):
		for j in range(len(model_fin.stack[0].weight[i])):
			if random.random() < 0.05:
				model_fin.stack[0].weight[i][j] = torch.tensor(random.random()*0.1, requires_grad=True)

				
test_loop(model_fin.ted, model_fin, loss_fn, alert=True)
Test Error: 
 Accuracy: 70.6%, Avg loss: 0.884130 

with torch.no_grad():
	for i in range(len(model_fin.stack[0].weight)):
		for j in range(len(model_fin.stack[0].weight[i])):
			if random.random() < 0.05:
				model_fin.stack[0].weight[i][j] = torch.tensor(random.random()*0.1, requires_grad=True)

				
test_loop(model_fin.ted, model_fin, loss_fn, alert=True)
Test Error: 
 Accuracy: 66.8%, Avg loss: 1.047633 

with torch.no_grad():
	for i in range(len(model_fin.stack[0].weight)):
		for j in range(len(model_fin.stack[0].weight[i])):
			if random.random() < 0.01:
				model_fin.stack[0].weight[i][j] = torch.tensor(random.random()*0.05, requires_grad=True)

				
model_fin.roll(10, 2)
Epoch 1

Test Error: 
 Accuracy: 78.6%, Avg loss: 0.593863 

0.5835078954696655
Epoch 3

Test Error: 
 Accuracy: 81.0%, Avg loss: 0.507146 

0.5687434673309326
Epoch 5

Test Error: 
 Accuracy: 81.1%, Avg loss: 0.517591 

0.49947527050971985
Epoch 7

Test Error: 
 Accuracy: 81.1%, Avg loss: 0.493859 

0.5256289839744568
Epoch 9

Test Error: 
 Accuracy: 80.2%, Avg loss: 0.508271 

0.45331066846847534
2.9055449962615967
with torch.no_grad():
	for i in range(len(model_fin.stack[0].weight)):
		for j in range(len(model_fin.stack[0].weight[i])):
			if random.random() < 0.01:
				model_fin.stack[0].weight[i][j] = torch.tensor(random.random()*0.05, requires_grad=True)

				
test_loop(model_fin.ted, model_fin, loss_fn, alert=True)
Test Error: 
 Accuracy: 78.3%, Avg loss: 0.562786 

with torch.no_grad():
	for i in range(len(model_fin.stack[0].weight)):
		for j in range(len(model_fin.stack[0].weight[i])):
			if random.random() < 0.01:
				model_fin.stack[0].weight[i][j] = torch.tensor(random.random()*0.05, requires_grad=True)

				
test_loop(model_fin.ted, model_fin, loss_fn, alert=True)
Test Error: 
 Accuracy: 77.1%, Avg loss: 0.588767 

with torch.no_grad():
	for i in range(len(model_fin.stack[0].weight)):
		for j in range(len(model_fin.stack[0].weight[i])):
			if random.random() < 0.01:
				model_fin.stack[0].weight[i][j] = torch.tensor(random.random()*0.02, requires_grad=True)

				
model_fin.roll(10)
Epoch 1

Test Error: 
 Accuracy: 81.2%, Avg loss: 0.491346 

0.4606601595878601
2.51501202583313

with torch.no_grad():
	for i in range(len(model_fin.stack[0].weight)):
		for j in range(len(model_fin.stack[0].weight[i])):
			if random.random() < 0.01:
				model_fin.stack[0].weight[i][j] = torch.tensor(random.random()*0.02, requires_grad=True)

				
test_loop(model_fin.ted, model_fin, loss_fn, alert=True)
Test Error: 
 Accuracy: 80.9%, Avg loss: 0.504370 


with torch.no_grad():
	for i in range(len(model_fin.stack[0].weight)):
		for j in range(len(model_fin.stack[0].weight[i])):
			if random.random() < 0.01:
				model_fin.stack[0].weight[i][j] = torch.tensor(random.random()*0.02, requires_grad=True)

				
test_loop(model_fin.ted, model_fin, loss_fn, alert=True)
Test Error: 
 Accuracy: 82.1%, Avg loss: 0.472718 

with torch.no_grad():
	for i in range(len(model_fin.stack[0].weight)):
		for j in range(len(model_fin.stack[0].weight[i])):
			if random.random() < 0.01:
				model_fin.stack[0].weight[i][j] = torch.tensor(random.random()*0.02, requires_grad=True)

				
test_loop(model_fin.ted, model_fin, loss_fn, alert=True)
Test Error: 
 Accuracy: 80.5%, Avg loss: 0.520560 

with torch.no_grad():
	for i in range(len(model_fin.stack[0].weight)):
		for j in range(len(model_fin.stack[0].weight[i])):
			if random.random() < 0.01:
				model_fin.stack[0].weight[i][j] = torch.tensor(random.random()*0.02, requires_grad=True)

				
test_loop(model_fin.ted, model_fin, loss_fn, alert=True)
Test Error: 
 Accuracy: 80.1%, Avg loss: 0.540679 

with torch.no_grad():
	for i in range(len(model_fin.stack[0].weight)):
		for j in range(len(model_fin.stack[0].weight[i])):
			if random.random() < 0.01:
				model_fin.stack[0].weight[i][j] = torch.tensor(random.random()*0.02, requires_grad=True)

				
test_loop(model_fin.ted, model_fin, loss_fn, alert=True)
Test Error: 
 Accuracy: 80.1%, Avg loss: 0.524696 

with torch.no_grad():
	for i in range(len(model_fin.stack[0].weight)):
		for j in range(len(model_fin.stack[0].weight[i])):
			if random.random() < 0.01:
				model_fin.stack[0].weight[i][j] = torch.tensor(random.random()*0.02, requires_grad=True)

				
test_loop(model_fin.ted, model_fin, loss_fn, alert=True)
Test Error: 
 Accuracy: 79.4%, Avg loss: 0.542606 

id(test_loop)
2297670395664
ads = test_loop
id(ads)
2297670395664
ads = [1,2,3,4]
id(1)
2297280594160
p[0][0]
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
         [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
          0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
          0.0000e+00],
         [1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
          0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
          0.0000e+00]]])
id(p[0][0])
2295694724688
id(p[0][0][0])
2295910951936
p[0][0][0]
tensor([[0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
        [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
        [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
        [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
        [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
        [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
        [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
        [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
        [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
        [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
        [1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00]])
torch.tensor([p[0][0][0][i] for i in range(len(p[0][0][0]))])
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    torch.tensor([p[0][0][0][i] for i in range(len(p[0][0][0]))])
ValueError: only one element tensors can be converted to Python scalars
torch.tensor([p[0][0][0][i] for i in range(len(p[0][0][0]))])
Traceback (most recent call last):
  File "<pyshell#76>", line 1, in <module>
    torch.tensor([p[0][0][0][i] for i in range(len(p[0][0][0]))])
ValueError: only one element tensors can be converted to Python scalars
[p[0][0][0][i] for i in range(len(p[0][0][0]))]
[tensor([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]), tensor([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]), tensor([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]), tensor([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]), tensor([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]), tensor([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]), tensor([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]), tensor([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]), tensor([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]), tensor([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]), tensor([1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
        0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00])]
torch.tensor([list(p[0][0][0][i]) for i in range(len(p[0][0][0]))])
tensor([[0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
        [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
        [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
        [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
        [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
        [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
        [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
        [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
        [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
        [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
        [1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00]])
id[p[0][0][0]]
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    id[p[0][0][0]]
TypeError: 'builtin_function_or_method' object is not subscriptable
id(p[0][0][0])
2295910877520
for i in range(len(p[0][0][0]))"
SyntaxError: incomplete input
for i in range(len(p[0][0][0])):
    print(id(p[0][0][0][i]))

    
2295910877520
2295910951936
2295910876400
2295910951936
2295910877520
2295910951936
2295910876400
2295910951936
2295910877520
2295910951936
2295910876400
for i in range(len(p[500][0][0])):
    print(id(p[500][0][0][i]))

    
2295921554224
2295910953296
2295921553744
2295910953296
2295921554224
2295910953296
2295921553744
2295910953296
2295921554224
2295910953296
2295921553744
p[500]
(tensor([[[8.7000e-03, 1.1000e-03, 4.0000e-04, 2.0000e-04, 1.0000e-04,
          0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
          0.0000e+00],
         [2.4770e-01, 1.3800e-02, 7.0000e-04, 4.0000e-04, 2.0000e-04,
          1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
          0.0000e+00],
         [3.4980e-01, 1.7000e-02, 1.0000e-03, 6.0000e-04, 3.0000e-04,
          1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
          0.0000e+00],
         [2.4500e-02, 1.2900e-02, 1.0000e-02, 1.2000e-03, 4.0000e-04,
          2.0000e-04, 1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00,
          0.0000e+00],
         [3.3600e-02, 3.4840e-01, 2.5340e-01, 1.3200e-02, 5.0000e-04,
          2.0000e-04, 1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00,
          0.0000e+00],
         [5.5800e-02, 5.1360e-01, 3.2490e-01, 1.4600e-02, 5.0000e-04,
          2.0000e-04, 1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00,
          0.0000e+00],
         [5.0000e-03, 3.5100e-02, 1.9600e-02, 1.3000e-03, 4.0000e-04,
          2.0000e-04, 1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00,
          0.0000e+00],
         [5.0000e-04, 6.0000e-04, 5.0000e-04, 4.0000e-04, 2.0000e-04,
          1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
          0.0000e+00],
         [2.0000e-04, 2.0000e-04, 2.0000e-04, 2.0000e-04, 1.0000e-04,
          0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
          0.0000e+00],
         [1.0000e-04, 1.0000e-04, 1.0000e-04, 1.0000e-04, 0.0000e+00,
          0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
          0.0000e+00],
         [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
          0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
          0.0000e+00]]]), tensor(5))
ads = [1,2,3,4]
id(ads[1])
2297280594192
id(1)
2297280594160
id(ads[0])
2297280594160
p[500][0][0]
tensor([[8.7000e-03, 1.1000e-03, 4.0000e-04, 2.0000e-04, 1.0000e-04, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
        [2.4770e-01, 1.3800e-02, 7.0000e-04, 4.0000e-04, 2.0000e-04, 1.0000e-04,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
        [3.4980e-01, 1.7000e-02, 1.0000e-03, 6.0000e-04, 3.0000e-04, 1.0000e-04,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
        [2.4500e-02, 1.2900e-02, 1.0000e-02, 1.2000e-03, 4.0000e-04, 2.0000e-04,
         1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
        [3.3600e-02, 3.4840e-01, 2.5340e-01, 1.3200e-02, 5.0000e-04, 2.0000e-04,
         1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
        [5.5800e-02, 5.1360e-01, 3.2490e-01, 1.4600e-02, 5.0000e-04, 2.0000e-04,
         1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
        [5.0000e-03, 3.5100e-02, 1.9600e-02, 1.3000e-03, 4.0000e-04, 2.0000e-04,
         1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
        [5.0000e-04, 6.0000e-04, 5.0000e-04, 4.0000e-04, 2.0000e-04, 1.0000e-04,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
        [2.0000e-04, 2.0000e-04, 2.0000e-04, 2.0000e-04, 1.0000e-04, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
        [1.0000e-04, 1.0000e-04, 1.0000e-04, 1.0000e-04, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00],
        [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00]])
p[500][0][0][0]
tensor([8.7000e-03, 1.1000e-03, 4.0000e-04, 2.0000e-04, 1.0000e-04, 0.0000e+00,
        0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00])
def netdata_extract(net):
    extracted_weights = []
    extracted_biases = []
    for n in range(3):
        extracted_weights.append(netmodel.stack[n*3].weight)
        extracted_biases.append(netmodel.stack[n*3].bias)
    return extracted_weights, extracted_biases

adde = netdata_extract(model_fin)
Traceback (most recent call last):
  File "<pyshell#98>", line 1, in <module>
    adde = netdata_extract(model_fin)
  File "<pyshell#97>", line 5, in netdata_extract
    extracted_weights.append(netmodel.stack[n*3].weight)
NameError: name 'netmodel' is not defined
def netdata_extract(net):
    extracted_weights = []
    extracted_biases = []
    for n in range(3):
        extracted_weights.append(net.stack[n*3].weight)
        extracted_biases.append(net.stack[n*3].bias)
    return extracted_weights, extracted_biases

adde = netdata_extract(model_fin)

len(adde[0])
3

adde[0][0][0]

len(adde[0][0][0])
420

len(adde[0][0])
20
adde[0]

adde[0][0]
Parameter containing:
tensor([[ 0.1755,  0.0105,  0.0498,  ..., -0.0191, -0.0653,  0.0554],
        [ 0.0064, -0.0303, -0.0566,  ..., -0.0257, -0.0163,  0.0300],
        [ 0.0911,  0.0062,  0.0479,  ...,  0.0037, -0.0364, -0.0287],
        ...,
        [ 0.1166,  0.0043,  0.0165,  ...,  0.0166,  0.0308, -0.1235],
        [ 0.0329,  0.0102,  0.0147,  ...,  0.0548,  0.0213,  0.0133],
        [ 0.0289, -0.0426, -0.0330,  ..., -0.0242,  0.0115, -0.0174]],
       requires_grad=True)
dff = []
for i in adde[0]:
    dff.append(i)

    
dff[0]
Parameter containing:
tensor([[ 0.1755,  0.0105,  0.0498,  ..., -0.0191, -0.0653,  0.0554],
        [ 0.0064, -0.0303, -0.0566,  ..., -0.0257, -0.0163,  0.0300],
        [ 0.0911,  0.0062,  0.0479,  ...,  0.0037, -0.0364, -0.0287],
        ...,
        [ 0.1166,  0.0043,  0.0165,  ...,  0.0166,  0.0308, -0.1235],
        [ 0.0329,  0.0102,  0.0147,  ...,  0.0548,  0.0213,  0.0133],
        [ 0.0289, -0.0426, -0.0330,  ..., -0.0242,  0.0115, -0.0174]],
       requires_grad=True)
dff[0][0][0]
tensor(0.1755, grad_fn=<SelectBackward0>)
dff[0][0][0]=1
Traceback (most recent call last):
  File "<pyshell#119>", line 1, in <module>
    dff[0][0][0]=1
RuntimeError: a view of a leaf Variable that requires grad is being used in an in-place operation.
a
with torch.no_grad():
    dff[0][0][0]=1

    
dff[0]
Parameter containing:
tensor([[ 1.0000,  0.0105,  0.0498,  ..., -0.0191, -0.0653,  0.0554],
        [ 0.0064, -0.0303, -0.0566,  ..., -0.0257, -0.0163,  0.0300],
        [ 0.0911,  0.0062,  0.0479,  ...,  0.0037, -0.0364, -0.0287],
        ...,
        [ 0.1166,  0.0043,  0.0165,  ...,  0.0166,  0.0308, -0.1235],
        [ 0.0329,  0.0102,  0.0147,  ...,  0.0548,  0.0213,  0.0133],
        [ 0.0289, -0.0426, -0.0330,  ..., -0.0242,  0.0115, -0.0174]],
       requires_grad=True)
adde[0]==dff[0]
False
adde[0]

adde[0][0]
Parameter containing:
tensor([[ 1.0000,  0.0105,  0.0498,  ..., -0.0191, -0.0653,  0.0554],
        [ 0.0064, -0.0303, -0.0566,  ..., -0.0257, -0.0163,  0.0300],
        [ 0.0911,  0.0062,  0.0479,  ...,  0.0037, -0.0364, -0.0287],
        ...,
        [ 0.1166,  0.0043,  0.0165,  ...,  0.0166,  0.0308, -0.1235],
        [ 0.0329,  0.0102,  0.0147,  ...,  0.0548,  0.0213,  0.0133],
        [ 0.0289, -0.0426, -0.0330,  ..., -0.0242,  0.0115, -0.0174]],
       requires_grad=True)
type(dff[0][0][0])
<class 'torch.Tensor'>
type(dff[0][0])
<class 'torch.Tensor'>
type(dff[0])
<class 'torch.nn.parameter.Parameter'>
dff

for i in dff:
    i = torch.tensor(i)

    

Warning (from warnings module):
  File "<pyshell#133>", line 2
UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).
dff[0]
Parameter containing:
tensor([[ 1.0000,  0.0105,  0.0498,  ..., -0.0191, -0.0653,  0.0554],
        [ 0.0064, -0.0303, -0.0566,  ..., -0.0257, -0.0163,  0.0300],
        [ 0.0911,  0.0062,  0.0479,  ...,  0.0037, -0.0364, -0.0287],
        ...,
        [ 0.1166,  0.0043,  0.0165,  ...,  0.0166,  0.0308, -0.1235],
        [ 0.0329,  0.0102,  0.0147,  ...,  0.0548,  0.0213,  0.0133],
        [ 0.0289, -0.0426, -0.0330,  ..., -0.0242,  0.0115, -0.0174]],
       requires_grad=True)
for i in range(len(dff)):
    dff[i] = torch.tensor(dff[i])

    
dff[0]
tensor([[ 1.0000,  0.0105,  0.0498,  ..., -0.0191, -0.0653,  0.0554],
        [ 0.0064, -0.0303, -0.0566,  ..., -0.0257, -0.0163,  0.0300],
        [ 0.0911,  0.0062,  0.0479,  ...,  0.0037, -0.0364, -0.0287],
        ...,
        [ 0.1166,  0.0043,  0.0165,  ...,  0.0166,  0.0308, -0.1235],
        [ 0.0329,  0.0102,  0.0147,  ...,  0.0548,  0.0213,  0.0133],
        [ 0.0289, -0.0426, -0.0330,  ..., -0.0242,  0.0115, -0.0174]])
with torch.no_grad():
    dff[0][0][0]=5

    
adde[0][0]
Parameter containing:
tensor([[ 1.0000,  0.0105,  0.0498,  ..., -0.0191, -0.0653,  0.0554],
        [ 0.0064, -0.0303, -0.0566,  ..., -0.0257, -0.0163,  0.0300],
        [ 0.0911,  0.0062,  0.0479,  ...,  0.0037, -0.0364, -0.0287],
        ...,
        [ 0.1166,  0.0043,  0.0165,  ...,  0.0166,  0.0308, -0.1235],
        [ 0.0329,  0.0102,  0.0147,  ...,  0.0548,  0.0213,  0.0133],
        [ 0.0289, -0.0426, -0.0330,  ..., -0.0242,  0.0115, -0.0174]],
       requires_grad=True)
dff[0]
tensor([[ 5.0000e+00,  1.0527e-02,  4.9790e-02,  ..., -1.9112e-02,
         -6.5263e-02,  5.5393e-02],
        [ 6.4264e-03, -3.0290e-02, -5.6628e-02,  ..., -2.5736e-02,
         -1.6320e-02,  3.0020e-02],
        [ 9.1137e-02,  6.1790e-03,  4.7933e-02,  ...,  3.7003e-03,
         -3.6353e-02, -2.8715e-02],
        ...,
        [ 1.1664e-01,  4.2539e-03,  1.6521e-02,  ...,  1.6624e-02,
          3.0827e-02, -1.2346e-01],
        [ 3.2932e-02,  1.0170e-02,  1.4727e-02,  ...,  5.4820e-02,
          2.1323e-02,  1.3290e-02],
        [ 2.8875e-02, -4.2637e-02, -3.3010e-02,  ..., -2.4164e-02,
          1.1491e-02, -1.7433e-02]])
torch.nn.parameter.Parameter(dff[0])
Parameter containing:
tensor([[ 5.0000e+00,  1.0527e-02,  4.9790e-02,  ..., -1.9112e-02,
         -6.5263e-02,  5.5393e-02],
        [ 6.4264e-03, -3.0290e-02, -5.6628e-02,  ..., -2.5736e-02,
         -1.6320e-02,  3.0020e-02],
        [ 9.1137e-02,  6.1790e-03,  4.7933e-02,  ...,  3.7003e-03,
         -3.6353e-02, -2.8715e-02],
        ...,
        [ 1.1664e-01,  4.2539e-03,  1.6521e-02,  ...,  1.6624e-02,
          3.0827e-02, -1.2346e-01],
        [ 3.2932e-02,  1.0170e-02,  1.4727e-02,  ...,  5.4820e-02,
          2.1323e-02,  1.3290e-02],
        [ 2.8875e-02, -4.2637e-02, -3.3010e-02,  ..., -2.4164e-02,
          1.1491e-02, -1.7433e-02]], requires_grad=True)
torch.nn.parameter.Parameter(dff[0]).is_leaf
True
ered = torch.tensor(model_fin.stack[0].weight)

Warning (from warnings module):
  File "<pyshell#144>", line 1
UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).
ered[0]

ered
tensor([[ 1.0000,  0.0105,  0.0498,  ..., -0.0191, -0.0653,  0.0554],
        [ 0.0064, -0.0303, -0.0566,  ..., -0.0257, -0.0163,  0.0300],
        [ 0.0911,  0.0062,  0.0479,  ...,  0.0037, -0.0364, -0.0287],
        ...,
        [ 0.1166,  0.0043,  0.0165,  ...,  0.0166,  0.0308, -0.1235],
        [ 0.0329,  0.0102,  0.0147,  ...,  0.0548,  0.0213,  0.0133],
        [ 0.0289, -0.0426, -0.0330,  ..., -0.0242,  0.0115, -0.0174]])
id(ered)
2295908537968
id(model_fin.stack[0].weight)
2295910945856
ered.is_leaf
True
model_fin.stack[0].weight = torch.nn.parameter.Parameter(ered)
model_fin.roll(1)
Epoch 1

Test Error: 
 Accuracy: 81.0%, Avg loss: 0.512382 

0.44205695390701294
0.35890913009643555
ered
tensor([[ 1.0000,  0.0105,  0.0498,  ..., -0.0191, -0.0653,  0.0554],
        [ 0.0064, -0.0303, -0.0566,  ..., -0.0257, -0.0163,  0.0300],
        [ 0.0911,  0.0062,  0.0479,  ...,  0.0037, -0.0364, -0.0287],
        ...,
        [ 0.1166,  0.0043,  0.0165,  ...,  0.0166,  0.0308, -0.1235],
        [ 0.0329,  0.0102,  0.0147,  ...,  0.0548,  0.0213,  0.0133],
        [ 0.0289, -0.0426, -0.0330,  ..., -0.0242,  0.0115, -0.0174]])
model_fin.stack[0].weight
Parameter containing:
tensor([[ 1.0000,  0.0105,  0.0498,  ..., -0.0191, -0.0653,  0.0554],
        [ 0.0064, -0.0303, -0.0566,  ..., -0.0257, -0.0163,  0.0300],
        [ 0.0911,  0.0062,  0.0479,  ...,  0.0037, -0.0364, -0.0287],
        ...,
        [ 0.1166,  0.0043,  0.0165,  ...,  0.0166,  0.0308, -0.1235],
        [ 0.0329,  0.0102,  0.0147,  ...,  0.0548,  0.0213,  0.0133],
        [ 0.0289, -0.0426, -0.0330,  ..., -0.0242,  0.0115, -0.0174]],
       requires_grad=True)
model_fin.roll(10)
Epoch 1

Test Error: 
 Accuracy: 80.1%, Avg loss: 0.527446 

0.4575151801109314
2.3631911277770996
model_fin.stack[0].weight
Parameter containing:
tensor([[ 1.0000,  0.0105,  0.0498,  ..., -0.0191, -0.0653,  0.0554],
        [ 0.0064, -0.0303, -0.0566,  ..., -0.0257, -0.0163,  0.0300],
        [ 0.0911,  0.0062,  0.0479,  ...,  0.0037, -0.0364, -0.0287],
        ...,
        [ 0.1166,  0.0043,  0.0165,  ...,  0.0166,  0.0308, -0.1235],
        [ 0.0329,  0.0102,  0.0147,  ...,  0.0548,  0.0213,  0.0133],
        [ 0.0289, -0.0426, -0.0330,  ..., -0.0242,  0.0115, -0.0174]],
       requires_grad=True)
model_fin.stack[0].weight==torch.nn.parameter.Parameter(ered)
tensor([[True, True, True,  ..., True, True, True],
        [True, True, True,  ..., True, True, True],
        [True, True, True,  ..., True, True, True],
        ...,
        [True, True, True,  ..., True, True, True],
        [True, True, True,  ..., True, True, True],
        [True, True, True,  ..., True, True, True]])
for i in (model_fin.stack[0].weight==torch.nn.parameter.Parameter(ered)).flatten():
    if i==False:
        print('yes')
        break

    
model_fin.stack(1)
Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    model_fin.stack(1)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\container.py", line 204, in forward
    input = module(input)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\linear.py", line 114, in forward
    return F.linear(input, self.weight, self.bias)
TypeError: linear(): argument 'input' (position 1) must be Tensor, not int
model_fin.stack(torch.tensor([0]))
Traceback (most recent call last):
  File "<pyshell#164>", line 1, in <module>
    model_fin.stack(torch.tensor([0]))
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\container.py", line 204, in forward
    input = module(input)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\linear.py", line 114, in forward
    return F.linear(input, self.weight, self.bias)
RuntimeError: mat1 and mat2 shapes cannot be multiplied (1x1 and 420x20)
model_fin()
Traceback (most recent call last):
  File "<pyshell#165>", line 1, in <module>
    model_fin()
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
TypeError: NeuralNetwork.forward() missing 1 required positional argument: 'x'
1()
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    1()
TypeError: 'int' object is not callable
nn.Module
<class 'torch.nn.modules.module.Module'>
model_fin.parameters
<bound method Module.parameters of NeuralNetwork(
  (flatten): Flatten(start_dim=1, end_dim=-1)
  (stack): Sequential(
    (0): Linear(in_features=420, out_features=20, bias=True)
    (1): ReLU()
    (2): Dropout(p=0.1, inplace=False)
    (3): Linear(in_features=20, out_features=150, bias=True)
    (4): ReLU()
    (5): Dropout(p=0.1, inplace=False)
    (6): Linear(in_features=150, out_features=6, bias=True)
    (7): ReLU()
    (8): Dropout(p=0.1, inplace=False)
  )
)>
model_fin.parameters.Parameters
Traceback (most recent call last):
  File "<pyshell#169>", line 1, in <module>
    model_fin.parameters.Parameters
AttributeError: 'function' object has no attribute 'Parameters'
model_fin.parameters()
<generator object Module.parameters at 0x00000216F0097E60>

================ RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ===============
Done!
Epoch 1

Test Error: 
 Accuracy: 50.8%, Avg loss: 1.290838 

1.2711433172225952
Epoch 31

Test Error: 
 Accuracy: 79.0%, Avg loss: 0.576580 

0.5166230797767639
Epoch 61

Test Error: 
 Accuracy: 79.9%, Avg loss: 0.546829 

0.6066210865974426
Epoch 91

Test Error: 
 Accuracy: 80.4%, Avg loss: 0.533532 

0.5940296649932861
29.20117998123169
real_test: 0.8185454545454546
def netdata_extract(net):
    extracted_weights = []
    extracted_biases = []
    for n in range(3):
        extracted_weights.append(torch.tensor(net.stack[n*3].weight))
        extracted_biases.append(torch.tensor(net.stack[n*3].bias))
    return extracted_weights, extracted_biases

netdata_extract(model_fin)

Warning (from warnings module):
  File "<pyshell#172>", line 5
UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).

Warning (from warnings module):
  File "<pyshell#172>", line 6
UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).

a = netdata_extract(model_fin)[0]
net_mutate(model_fin)
Traceback (most recent call last):
  File "<pyshell#175>", line 1, in <module>
    net_mutate(model_fin)
NameError: name 'net_mutate' is not defined
def net_mutate(net, prob=0.03, width=0.03)
    with torch.no_grad():
	for i in range(len(net.stack[0].weight)):
	    for j in range(len(net.stack[0].weight[i])):
		    if random.random() < prob:
			net.stack[0].weight[i][j] += torch.tensor(random.random()*width,
                                                                  requires_grad=True)
			
SyntaxError: expected ':'
def net_mutate(net, prob=0.03, width=0.03):
    with torch.no_grad():
	for i in range(len(net.stack[0].weight)):
	    for j in range(len(net.stack[0].weight[i])):
		    if random.random() < prob:
			net.stack[0].weight[i][j] += torch.tensor(random.random()*width,
                                                                  requires_grad=True)
			
SyntaxError: inconsistent use of tabs and spaces in indentation
def net_mutate(net, prob=0.03, width=0.03):
    with torch.no_grad():
        for i in range(len(net.stack[0].weight)):
            for j in range(len(net.stack[0].weight[i])):
		    if random.random() < prob:
			net.stack[0].weight[i][j] += torch.tensor(random.random()*width,
                                                                  requires_grad=True)
			
SyntaxError: inconsistent use of tabs and spaces in indentation
def net_mutate(net, prob=0.03, width=0.03):
    with torch.no_grad():
        for i in range(len(net.stack[0].weight)):
            for j in range(len(net.stack[0].weight[i])):
		if random.random() < prob:
		    net.stack[0].weight[i][j] += torch.tensor(random.random()*width,
                                                                requires_grad=True)
		    
SyntaxError: inconsistent use of tabs and spaces in indentation

def net_mutate(net, prob=0.03, width=0.03):
    with torch.no_grad():
        for i in range(len(net.stack[0].weight)):
            for j in range(len(net.stack[0].weight[i])):
                if random.random() < prob:
                    net.stack[0].weight[i][j] += torch.tensor(random.random()*width,
                                                                requires_grad=True)

                    
net_mutate(model_fin)
Traceback (most recent call last):
  File "<pyshell#183>", line 1, in <module>
    net_mutate(model_fin)
  File "<pyshell#182>", line 5, in net_mutate
    if random.random() < prob:
NameError: name 'random' is not defined
import random
net_mutate(model_fin)
net_mutate(model_fin)
net_mutate(model_fin)
test_loop(model_fin.ted, model_fin, loss_fn, alert=True)

Test Error: 
 Accuracy: 79.0%, Avg loss: 0.570374 

net_mutate(model_fin)
net_mutate(model_fin)
net_mutate(model_fin)
test_loop(model_fin.ted, model_fin, loss_fn, alert=True)
Test Error: 
 Accuracy: 79.2%, Avg loss: 0.590481 

model_fin.stack[0].weight
Parameter containing:
tensor([[ 0.0395,  0.0159, -0.0169,  ...,  0.0198, -0.0478, -0.0119],
        [ 0.0832,  0.0457,  0.0566,  ..., -0.0661,  0.0106, -0.0081],
        [ 0.1226, -0.0192,  0.0455,  ...,  0.0750,  0.0821,  0.0679],
        ...,
        [-0.0086,  0.0609,  0.0181,  ...,  0.0852, -0.0028,  0.0010],
        [ 0.1529,  0.0263, -0.0707,  ..., -0.0756,  0.0260,  0.1057],
        [ 0.0429,  0.0151,  0.0778,  ..., -0.0086, -0.0088,  0.0337]],
       requires_grad=True)
model_fin.stack[0].weight==a
False
model_fin.stack[0].weight==torch.nn.parameter.Parameter(a)
Traceback (most recent call last):
  File "<pyshell#195>", line 1, in <module>
    model_fin.stack[0].weight==torch.nn.parameter.Parameter(a)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\parameter.py", line 39, in __new__
    t = data.detach().requires_grad_(requires_grad)
AttributeError: 'list' object has no attribute 'detach'
model_fin.stack[0].weight==torch.nn.parameter.Parameter(a)
Traceback (most recent call last):
  File "<pyshell#196>", line 1, in <module>
    model_fin.stack[0].weight==torch.nn.parameter.Parameter(a)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\parameter.py", line 39, in __new__
    t = data.detach().requires_grad_(requires_grad)
AttributeError: 'list' object has no attribute 'detach'
a[0]
tensor([[ 0.0395,  0.0159, -0.0169,  ...,  0.0198, -0.0478, -0.0119],
        [ 0.0832,  0.0457,  0.0566,  ..., -0.0661,  0.0106, -0.0081],
        [ 0.1226, -0.0192,  0.0455,  ...,  0.0723,  0.0821,  0.0634],
        ...,
        [-0.0086,  0.0609,  0.0181,  ...,  0.0603, -0.0028,  0.0010],
        [ 0.1529,  0.0263, -0.0707,  ..., -0.0756,  0.0260,  0.1057],
        [ 0.0407,  0.0151,  0.0661,  ..., -0.0318, -0.0088,  0.0337]])
a

len(a)
3
model_fin.stack[0].weight==torch.nn.parameter.Parameter(a[0])
tensor([[ True,  True,  True,  ...,  True,  True,  True],
        [ True,  True,  True,  ...,  True,  True,  True],
        [ True,  True,  True,  ..., False,  True, False],
        ...,
        [ True,  True,  True,  ..., False,  True,  True],
        [ True,  True,  True,  ...,  True,  True,  True],
        [False,  True, False,  ..., False,  True,  True]])
net_mutate(model_fin)
net_mutate(model_fin)
net_mutate(model_fin)
[net_mutate(model_fin) for i in range(100)]
[None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None]
test_loop(model_fin.ted, model_fin, loss_fn, alert=True)
Test Error: 
 Accuracy: 47.9%, Avg loss: 3.459579 

model_fin.roll(2)
Epoch 1

Test Error: 
 Accuracy: 67.0%, Avg loss: 0.942165 

0.8686814904212952
0.7832751274108887
model_fin.roll(2)
Epoch 1

Test Error: 
 Accuracy: 73.1%, Avg loss: 0.748849 

0.7321078777313232
0.7422950267791748
model_fin.roll(2)
Epoch 1

Test Error: 
 Accuracy: 74.1%, Avg loss: 0.716429 

0.7104306221008301
0.7095870971679688
model_fin.roll(10)
Epoch 1

Test Error: 
 Accuracy: 75.8%, Avg loss: 0.661853 

0.7157143950462341
3.0914576053619385
model_fin.roll(10)
Epoch 1

Test Error: 
 Accuracy: 79.7%, Avg loss: 0.555621 

0.6331241130828857
2.8533501625061035
model_fin.roll(2)
Epoch 1

Test Error: 
 Accuracy: 80.4%, Avg loss: 0.545014 

0.5541303753852844
0.5981035232543945
model_fin.stack[0].weight==torch.nn.parameter.Parameter(a[0])
tensor([[False, False, False,  ..., False, False, False],
        [False, False, False,  ..., False, False, False],
        [False, False, False,  ..., False, False, False],
        ...,
        [False, False, False,  ..., False, False, False],
        [False, False, False,  ..., False, False, False],
        [False, False, False,  ..., False, False, False]])
>>> ad = [NeuralNetwork([420, 20, 50, 6]) for i in range(100)]
>>> for i in ad[20:]:
...     net_mutate(i)
... 
...     
>>> a = netdata_extract(ad[25])[0]
>>> for i in ad[20:]:
...     net_mutate(i)
... 
>>> for i in ad[20:]:
...     net_mutate(i)
... 
>>> ad[25].stack[0].weight==torch.nn.parameter.Parameter(ad[25])
Traceback (most recent call last):
  File "<pyshell#222>", line 1, in <module>
    ad[25].stack[0].weight==torch.nn.parameter.Parameter(ad[25])
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\parameter.py", line 39, in __new__
    t = data.detach().requires_grad_(requires_grad)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1269, in __getattr__
    raise AttributeError("'{}' object has no attribute '{}'".format(
AttributeError: 'NeuralNetwork' object has no attribute 'detach'
>>> ad[25].stack[0].weight==torch.nn.parameter.Parameter(a[0])
tensor([[ True,  True,  True,  ...,  True,  True,  True],
        [ True,  True, False,  ...,  True,  True,  True],
        [ True, False,  True,  ...,  True, False,  True],
        ...,
        [ True,  True,  True,  ...,  True,  True,  True],
        [ True,  True,  True,  ...,  True,  True,  True],
        [ True,  True,  True,  ...,  True,  True,  True]])
>>> test_loop(model_fin.ted, ad[25], loss_fn, alert=True)
... 
Test Error: 
 Accuracy: 7.9%, Avg loss: 1.798440 

