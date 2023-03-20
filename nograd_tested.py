Python 3.9.6 (tags/v3.9.6:db3ff76, Jun 28 2021, 15:26:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
============= RESTART: C:\Users\hyunhoyang\Desktop\IL\base\temp2.py ============
Done!
Epoch 1

Test Error: 
 Accuracy: 34.0%, Avg loss: 1.642516 

1.6901918649673462
Epoch 31

Test Error: 
 Accuracy: 78.6%, Avg loss: 0.581439 

0.5282168388366699
Epoch 61

Test Error: 
 Accuracy: 79.4%, Avg loss: 0.576417 

0.5898249745368958
Epoch 91

Test Error: 
 Accuracy: 80.6%, Avg loss: 0.538200 

0.6157150864601135
24.894313097000122
real_test: 0.8159090909090909
>>> with torch.no_grad():
	for i in range(len(model_fin.stack[0].weight)):
		for j in range(len(model_fin.stack[0].weight[i])):
			if random.random() < 0.01:
				model_fin.stack[0].weight[i][j] = torch.tensor(random.random()*0.01, requires_grad=True)

				
Traceback (most recent call last):
  File "<pyshell#1>", line 4, in <module>
    if random.random() < 0.01:
NameError: name 'random' is not defined
>>> import random
>>> with torch.no_grad():
	for i in range(len(model_fin.stack[0].weight)):
		for j in range(len(model_fin.stack[0].weight[i])):
			if random.random() < 0.01:
				model_fin.stack[0].weight[i][j] = torch.tensor(random.random()*0.01, requires_grad=True)

				
>>> with torch.no_grad():
	for i in range(len(model_fin.stack[0].weight)):
		for j in range(len(model_fin.stack[0].weight[i])):
			if random.random() < 0.01:
				model_fin.stack[0].weight[i][j] = torch.tensor(random.random()*0.01, requires_grad=True)

				
>>> with torch.no_grad():
	for i in range(len(model_fin.stack[0].weight)):
		for j in range(len(model_fin.stack[0].weight[i])):
			if random.random() < 0.01:
				model_fin.stack[0].weight[i][j] = torch.tensor(random.random()*0.01, requires_grad=True)

				
>>> test_loop(model_fin.ted, model_fin, loss_fn, alert=True)
Test Error: 
 Accuracy: 78.3%, Avg loss: 0.602618 

>>> 
>>> with torch.no_grad():
	for i in range(len(model_fin.stack[0].weight)):
		for j in range(len(model_fin.stack[0].weight[i])):
			if random.random() < 0.01:
				model_fin.stack[0].weight[i][j] = torch.tensor(random.random()*0.01, requires_grad=True)

				
>>> 
>>> test_loop(model_fin.ted, model_fin, loss_fn, alert=True)
Test Error: 
 Accuracy: 78.4%, Avg loss: 0.610462 

>>> with torch.no_grad():
	for i in range(len(model_fin.stack[0].weight)):
		for j in range(len(model_fin.stack[0].weight[i])):
			if random.random() < 0.05:
				model_fin.stack[0].weight[i][j] = torch.tensor(random.random()*0.01, requires_grad=True)

				
>>> test_loop(model_fin.ted, model_fin, loss_fn, alert=True)
Test Error: 
 Accuracy: 79.0%, Avg loss: 0.624431 

>>> with torch.no_grad():
	for i in range(len(model_fin.stack[0].weight)):
		for j in range(len(model_fin.stack[0].weight[i])):
			if random.random() < 0.05:
				model_fin.stack[0].weight[i][j] += torch.tensor(random.random()*0.01, requires_grad=True)

				
>>> model_fin.stack[0].weight.is_leaf
True
>>> test_loop(model_fin.ted, model_fin, loss_fn, alert=True)
Test Error: 
 Accuracy: 78.8%, Avg loss: 0.604984 

>>> with torch.no_grad():
	for i in range(len(model_fin.stack[0].weight)):
		for j in range(len(model_fin.stack[0].weight[i])):
			if random.random() < 0.05:
				model_fin.stack[0].weight[i][j] += torch.tensor(random.random()*0.1, requires_grad=True)

				
>>> test_loop(model_fin.ted, model_fin, loss_fn, alert=True)
Test Error: 
 Accuracy: 78.6%, Avg loss: 0.633554 

>>> with torch.no_grad():
	for i in range(len(model_fin.stack[0].weight)):
		for j in range(len(model_fin.stack[0].weight[i])):
			if random.random() < 0.55:
				model_fin.stack[0].weight[i][j] += torch.tensor(random.random()*0.1, requires_grad=True)

				
>>> test_loop(model_fin.ted, model_fin, loss_fn, alert=True)
Test Error: 
 Accuracy: 57.9%, Avg loss: 1.755294 


>>> model_fin.roll(10)
Epoch 1

Test Error: 
 Accuracy: 72.4%, Avg loss: 0.745933 

0.6934124827384949
2.543689250946045
>>> model_fin.roll(1)
Epoch 1

Test Error: 
 Accuracy: 79.7%, Avg loss: 0.564958 

0.6160382032394409
0.33847618103027344
>>> 