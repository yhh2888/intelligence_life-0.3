Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> 
======== RESTART: C:\Users\KCDC\Desktop\intelligence life\base\temp2.py ========
Done!
>>> with open(r'C:\Users\KCDC\Desktop\intelligence life\field_data.json') as f:
	p = json.load(f)[0]

	
Traceback (most recent call last):
  File "<pyshell#2>", line 2, in <module>
    p = json.load(f)[0]
NameError: name 'json' is not defined
>>> import json
>>> with open(r'C:\Users\KCDC\Desktop\intelligence life\field_data.json') as f:
	p = json.load(f)[0]

	
>>> for i in range(len(p)):
	p[i][0] = p[i][0][0]

	
>>> p[0][0]
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
>>> len(p[0])
1
>>> p[0]
[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
>>> with open(r'C:\Users\KCDC\Desktop\intelligence life\field_data.json') as f:
	p = json.load(f)[0]

	
>>> for i in range(len(p)):
	p[i] = p[i][0]

	
>>> p[0]
[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0, 0, 0, 0, 0]]
>>> p_ = DataLoader(p)
>>> p_.dataset[0]
[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0, 0, 0, 0, 0]]
>>> len(p_.dataset)
13928
>>> len(train_dataloader.dataset[0])
2
>>> train_dataloader.dataset[0]

>>> train_dataloader.dataset[0][0][0]

>>> train_dataloader.dataset[0][0][0][0]
tensor([0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
        0., 0., 0., 0.])
>>> train_dataloader.dataset
Dataset FashionMNIST
    Number of datapoints: 60000
    Root location: data
    Split: Train
    StandardTransform
Transform: ToTensor()
>>> train_dataloader.dataset[0][0]

>>> len(train_dataloader.dataset)
60000
>>> len(train_dataloader.dataset[0])
2
>>> len(train_dataloader.dataset[0][0])
1
>>> len(train_dataloader.dataset[0][0][0])
28
>>> len(train_dataloader.dataset[0][0][0][0])
28
>>> len(p_.dataset)
13928
>>> len(p_.dataset[0])
2
>>> len(p_.dataset[0][0])
121
>>> len(p_.dataset[0][0][0])
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    len(p_.dataset[0][0][0])
TypeError: object of type 'float' has no len()
>>> with open(r'C:\Users\KCDC\Desktop\intelligence life\field_data.json') as f:
	p = json.load(f)[0]

	
>>> for i in range(len(p)):
	p[i] = [p[i][0]]

	
>>> p_ = DataLoader(p)
>>> len(p_.dataset)
13928
>>> len(p_.dataset[0])
1
>>> len(p_.dataset[0][0])
2
>>> len(p_.dataset[0][0][0])
121
>>> with open(r'C:\Users\KCDC\Desktop\intelligence life\field_data.json') as f:
	p = json.load(f)[0]

	
>>> p_ = DataLoader(p)
>>> len(p_.dataset)
13928
>>> len(p_.dataset[0])
1
>>> len(p_.dataset[0][0])
2
>>> len(p_.dataset[0][0][0])
121
>>> with open(r'C:\Users\KCDC\Desktop\intelligence life\field_data.json') as f:
	p = json.load(f)[0]

	
>>> for i in range(len(p)):
	p[i] = [[p[i][0][0]], p[i][0][1]]

	
>>> p_ = DataLoader(p)
>>> len(p_.dataset)
13928
>>> len(p_.dataset[0])
2
>>> len(p_.dataset[0][0])
1
>>> len(p_.dataset[0][0][0])
121
>>> type(train_dataloader.dataset[0][0][0])
<class 'torch.Tensor'>
>>> type(train_dataloader.dataset[0][0])
<class 'torch.Tensor'>
>>> type(train_dataloader.dataset[0])
<class 'tuple'>
>>> len(train_dataloader.dataset[0])
2
>>> train_dataloader.dataset[0][0][0][0].reshape
<built-in method reshape of Tensor object at 0x00000156EAD21F40>
>>> train_dataloader.dataset[0][0][0][0].reshape(14, 2)
tensor([[0., 0.],
        [0., 0.],
        [0., 0.],
        [0., 0.],
        [0., 0.],
        [0., 0.],
        [0., 0.],
        [0., 0.],
        [0., 0.],
        [0., 0.],
        [0., 0.],
        [0., 0.],
        [0., 0.],
        [0., 0.]])
>>> p[0][0][1]
Traceback (most recent call last):
  File "<pyshell#68>", line 1, in <module>
    p[0][0][1]
IndexError: list index out of range
>>> len(p_.dataset[0][1])
5
>>> len(train_dataloader.dataset)
60000
>>> len(train_dataloader.dataset[0])
2
>>> len(train_dataloader.dataset[0][1])
Traceback (most recent call last):
  File "<pyshell#72>", line 1, in <module>
    len(train_dataloader.dataset[0][1])
TypeError: object of type 'int' has no len()
>>> p[0][1]
[0, 0, 0, 0, 0]
>>> p[1][0]
[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
>>> p[1][0][0]
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
>>> p[1]
[[[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]], [0, 0, 0, 0, 0]]
>>> torch.tensor(p[1])
Traceback (most recent call last):
  File "<pyshell#77>", line 1, in <module>
    torch.tensor(p[1])
ValueError: expected sequence of length 1 at dim 1 (got 5)
>>> torch.tensor(p[1][0])
tensor([[0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
         0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
         0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
         0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
         0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.,
         0.]])
>>> torch.tensor(p[1][0]).reshape
<built-in method reshape of Tensor object at 0x00000156F5B05400>
>>> torch.tensor(p[1][0]).reshape(1)
Traceback (most recent call last):
  File "<pyshell#80>", line 1, in <module>
    torch.tensor(p[1][0]).reshape(1)
RuntimeError: shape '[1]' is invalid for input of size 121
>>> torch.tensor(p[1][0]).reshape(11, 11)
tensor([[0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]])
>>> for i in range(len(p)):
	p[i][0] = torch.tensor(p[i][0]).reshape(11, 11)
	p[i][1] = torch.tensor(p[i][1])

	
>>> p[1][0]
tensor([[0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]])
>>> p[1]
[tensor([[0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]]), tensor([0, 0, 0, 0, 0])]

>>> len(p)
13928
>>> 
>>> for i in range(len(p)):
	p[i] = tuple(p[i])

	
>>> with open(r'C:\Users\KCDC\Desktop\intelligence life\field_data.json') as f:
	p = json.load(f)[0]

	
>>> for i in range(len(p)):
	p[i] = [[p[i][0][0]], p[i][0][1]]
	p[i][0] = torch.tensor(p[i][0]).reshape(11, 11)
	p[i][1] = torch.tensor(p[i][1])
	p[i] = tuple(p[i])

	
>>> p_ = DataLoader(p)
>>> p_.dataset[0]
(tensor([[0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.],
        [0., 0., 0., 0., 0., 0., 0., 0., 0., 0., 0.]]), tensor([0, 0, 0, 0, 0]))
>>> train_dataloader.dataset[0]

>>> len(train_dataloader.dataset[0])
2
>>> len(p_.dataset[0])
2
>>> len(p_.dataset[0][0])
11
>>> len(p_.dataset[0][0][0])
11
>>> len(p_.dataset[0][0][0][0])
Traceback (most recent call last):
  File "<pyshell#105>", line 1, in <module>
    len(p_.dataset[0][0][0][0])
  File "C:\Users\KCDC\AppData\Local\Programs\Python\Python39\lib\site-packages\torch\_tensor.py", line 894, in __len__
    raise TypeError("len() of a 0-d tensor")
TypeError: len() of a 0-d tensor
>>> len(train_dataloader.dataset[0][0])
1
>>> with open(r'C:\Users\KCDC\Desktop\intelligence life\field_data.json') as f:
	p = json.load(f)[0]

	
>>> type(train_dataloader.dataset)
<class 'torchvision.datasets.mnist.FashionMNIST'>
>>> type(train_dataloader.dataset[0])
<class 'tuple'>
>>> type(train_dataloader.dataset[0][0])
<class 'torch.Tensor'>
>>> type(train_dataloader.dataset[0][0][0])
<class 'torch.Tensor'>
>>> type(train_dataloader.dataset[0][0][0][0])
<class 'torch.Tensor'>
>>> type(train_dataloader.dataset[0][0][0][0][0])
<class 'torch.Tensor'>
>>> type(train_dataloader.dataset[0][0][0][0][0][0])
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    type(train_dataloader.dataset[0][0][0][0][0][0])
IndexError: invalid index of a 0-dim tensor. Use `tensor.item()` in Python or `tensor.item<T>()` in C++ to convert a 0-dim tensor to a number
>>> len(train_dataloader.dataset[0])
2
>>> len(train_dataloader.dataset[0][0])
1
>>> len(train_dataloader.dataset[0][0][0])
28
>>> for i in range(len(p)):
	p[i] = [[p[i][0][0]], p[i][0][1]]
	p[i][0] = torch(tensor(torch.tensor(p[i][0]).reshape(11, 11))
	p[i][1] = torch.tensor(p[i][1])
	p[i] = tuple(p[i])
			
SyntaxError: invalid syntax
>>> for i in range(len(p)):
	p[i] = [[p[i][0][0]], p[i][0][1]]
	p[i][0] = torch.tensor(torch.tensor(p[i][0]).reshape(11, 11))
	p[i][1] = torch.tensor(p[i][1])
	p[i] = tuple(p[i])

	

Warning (from warnings module):
  File "<pyshell#123>", line 3
UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).
>>> p_ = DataLoader(p)
>>> len(p_.dataset[0])
2
>>> len(p_.dataset[0][0])
11
>>> with open(r'C:\Users\KCDC\Desktop\intelligence life\field_data.json') as f:
	p = json.load(f)[0]

	
>>> for i in range(len(p)):
	p[i] = [[p[i][0][0]], p[i][0][1]]
	p[i][0] = torch([tensor(torch.tensor(p[i][0]).reshape(11, 11)])
	p[i][1] = torch.tensor(p[i][1])
	p[i] = tuple(p[i])
			
SyntaxError: closing parenthesis ']' does not match opening parenthesis '('
>>> with open(r'C:\Users\KCDC\Desktop\intelligence life\field_data.json') as f:
	p = json.load(f)[0]

	
>>> for i in range(len(p)):
	p[i] = [[p[i][0][0]], p[i][0][1]]
	p[i][0] = torch.tensor([torch.tensor(p[i][0]).reshape(11, 11)])
	p[i][1] = torch.tensor(p[i][1])
	p[i] = tuple(p[i])

	
Traceback (most recent call last):
  File "<pyshell#134>", line 3, in <module>
    p[i][0] = torch.tensor([torch.tensor(p[i][0]).reshape(11, 11)])
ValueError: only one element tensors can be converted to Python scalars
>>> with open(r'C:\Users\KCDC\Desktop\intelligence life\field_data.json') as f:
	p = json.load(f)[0]

	
>>> 