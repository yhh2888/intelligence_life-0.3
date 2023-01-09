Python 3.9.10 (tags/v3.9.10:f2f3f53, Jan 17 2022, 15:14:21) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> import gaussian_kde
Traceback (most recent call last):
  File "<pyshell#0>", line 1, in <module>
    import gaussian_kde
ModuleNotFoundError: No module named 'gaussian_kde'
>>> from sympy import gaussian_kde
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    from sympy import gaussian_kde
ImportError: cannot import name 'gaussian_kde' from 'sympy' (C:\Users\KCDC\AppData\Local\Programs\Python\Python39\lib\site-packages\sympy\__init__.py)
>>> np.random.uniform(-1, 1, size=(11, 11))
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    np.random.uniform(-1, 1, size=(11, 11))
NameError: name 'np' is not defined
>>> import numpy as np
>>> a = np.random.uniform(-1, 1, size=(11, 11))
>>> 
======= RESTART: C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py =======

======= RESTART: C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py =======
layers : [122, 25, 15, 15, 5]
error: 3.99996708012
0.047013282775878906

======= RESTART: C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py =======
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999636161
0.02377796173095703
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 435, in training_view
    self.network.train_once(dat)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 197, in train_once
    self.update(inputs)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 112, in update
    sum = sum + self.activations[k][i] * self.weights[k][i][j]
IndexError: list index out of range
list index out of range
Traceback (most recent call last):

================================ RESTART: Shell ================================
>>> 
======= RESTART: C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py =======
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999858626
0.06736230850219727
>>> n.weights[0,1,2]
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    n.weights[0,1,2]
TypeError: list indices must be integers or slices, not tuple
>>> 0.06736230850219727
0.06736230850219727
>>> n.weights[0][1][2]
0.7108658240484877
>>> n.weights[0]

>>> n.weights[1]

>>> n.weights[1][0]
[0.9631767184068649, 0.0006207974339669242, 0.21074950284822558, 0.7006196648176544, 0.2604793255562895, 0.6305597631758489, 0.6566646565134588, 0.8607090119748352, 0.9243452646744817, 0.575375906784965, 0.9001944574128814, 0.02505436557670815, 0.06157194383635012, 0.8864131182762088, 0.6478754181455367]
>>> e = np.random.uniform(-1, 1, size=(122, 15))
>>> d = np.random.uniform(-1, 1, size=(15, 15))
>>> np.dot(e, d)
array([[-2.08749482,  0.38863632,  1.39864597, ...,  0.83111162,
         0.76402039,  1.6998566 ],
       [-0.20008284,  0.6302038 ,  1.43233255, ...,  2.57758704,
        -1.3230781 ,  0.31639364],
       [ 2.89549449, -1.00782783, -0.81838172, ...,  0.84898988,
         0.55054398, -0.95889209],
       ...,
       [ 0.66911457,  0.50217221, -0.73022219, ..., -1.76260325,
        -1.27191907,  0.30885653],
       [-0.63515318, -0.88684805, -0.59971618, ...,  0.46918807,
         0.15160351, -1.06934082],
       [-1.76040553,  1.38247346,  0.00735954, ..., -0.34457915,
        -2.40954763, -0.32277187]])
>>> def ee(num):
	t =time.time()
	for i in range(num):
		np.dot(e, d)
	print(time.time()-t)

	
>>> ee(100)
0.0
>>> ee(10000)
0.05398130416870117
>>> def as():
	
SyntaxError: invalid syntax
>>> d = np.random.uniform(-1, 1, size=(15, 1))
>>> np.dot(e, d)

>>> len(np.dot(e, d))
122
>>> d = np.random.uniform(-1, 1, size=(1, 15))
>>> len(np.dot(e, d))
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    len(np.dot(e, d))
  File "<__array_function__ internals>", line 180, in dot
ValueError: shapes (122,15) and (1,15) not aligned: 15 (dim 1) != 1 (dim 0)
>>> len(np.dot(e, d)[0])
Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    len(np.dot(e, d)[0])
  File "<__array_function__ internals>", line 180, in dot
ValueError: shapes (122,15) and (1,15) not aligned: 15 (dim 1) != 1 (dim 0)
>>> d = np.random.uniform(-1, 1, size=(15, 1))
>>> len(np.dot(e, d)[0])
1
>>> a = np.array([[1, 3],[2, 4]])
>>> b = np.array([2, 5])
>>> np.dot(a, b)
array([17, 24])
>>> b.shape()
Traceback (most recent call last):
  File "<pyshell#36>", line 1, in <module>
    b.shape()
TypeError: 'tuple' object is not callable
>>> b.shape
(2,)
>>> d = np.random.uniform(-1, 1, size=(15,))
>>> d
array([-0.31794548, -0.16038726, -0.23794208, -0.30741359, -0.02667636,
       -0.39883899, -0.54310392, -0.0841857 , -0.00824148,  0.89773161,
       -0.13466343, -0.27008877, -0.80890675,  0.27433235,  0.70138077])
>>> np.dot(e, d)
array([ 0.76683598, -0.52723871, -0.20193674, -0.07301881,  0.45131805,
        1.19868173,  0.84660359, -0.23856728,  0.33843179, -0.10766473,
       -1.63472994,  2.58305734, -0.35233799,  2.52049415, -0.41915883,
        0.29609016, -1.48404403,  1.29262729,  1.59419243,  2.25212566,
        1.27967708, -0.57436273, -0.12406807,  1.57843129, -1.70392005,
       -1.32102092, -0.44765465,  0.08178548, -1.21663575, -0.85502903,
       -0.07024642, -1.25992816,  0.72679844,  1.65733069, -1.05305133,
        0.51075385,  0.24662144, -0.07310882, -1.13567631, -0.07485671,
        0.09046167,  2.5704406 , -2.48073593,  0.74315648, -0.55573457,
       -0.31285903,  1.91942681, -1.3258775 , -0.87239886, -0.9396673 ,
       -0.74636828,  1.88246993, -0.25211839, -0.68628598,  0.97779674,
        0.08961834, -0.26137885, -0.63072136,  1.15806747,  0.75359172,
       -1.02622494,  1.05473084, -0.3608388 , -1.31601083,  0.49671219,
        0.68726195,  0.58689783,  0.67280675, -0.4610981 ,  1.48496293,
       -0.20039326, -0.39523471,  2.63153164,  0.52685086, -0.37062981,
       -0.28993477,  1.40412153, -0.27920124, -0.06026766, -0.88056274,
       -0.99628189,  0.08128523,  0.18631467,  0.23603987,  0.57494286,
        0.56450341, -0.06807929,  0.59834407,  2.27328939,  2.11349715,
        0.1042144 ,  1.91636651,  0.89373845, -0.6090226 , -0.08894907,
        0.91464917, -0.28490221, -0.18215057, -0.55999842, -0.31497658,
       -0.90408349,  0.25626146, -0.56642325,  0.53728254,  1.16664247,
       -0.51417412, -1.04448688, -0.18241478, -0.54742322, -0.16689394,
        0.60438656, -0.83333589,  0.57729319, -0.33299931, -0.14828584,
       -0.77163773, -0.5807825 ,  0.5090557 ,  0.066021  ,  0.61884888,
       -1.4020423 , -1.17976035])
>>> e = np.random.uniform(-1, 1, size=(15, 122))
>>> d = np.random.uniform(-1, 1, size=(15,))
>>> np.dot(e, d)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    np.dot(e, d)
  File "<__array_function__ internals>", line 180, in dot
ValueError: shapes (15,122) and (15,) not aligned: 122 (dim 1) != 15 (dim 0)
>>> e[1]
array([-0.78105249, -0.12954425, -0.56207888,  0.38304315,  0.09519386,
        0.76887684, -0.12652066, -0.75758101, -0.08810602,  0.62941244,
       -0.21458466,  0.52381506,  0.43607742, -0.75496274,  0.37359492,
        0.02211668,  0.79233144, -0.03357953,  0.80917805, -0.009715  ,
        0.4041001 ,  0.88158647, -0.9189234 , -0.51345985, -0.17887806,
       -0.91548586, -0.05891966, -0.02586144, -0.96159192,  0.76506415,
       -0.53178455,  0.89770276, -0.70887744, -0.85536465, -0.87829089,
       -0.68181418,  0.13333746, -0.46734149,  0.34673418, -0.57778469,
        0.15988786, -0.23744964, -0.61304678,  0.47665544, -0.93167758,
        0.62253749, -0.91980365, -0.99466141,  0.81110366,  0.55877576,
        0.59947666, -0.64697477,  0.11138214, -0.90332722, -0.45036859,
       -0.91805989,  0.98878318, -0.488335  , -0.70215935,  0.6329496 ,
        0.92208026, -0.91984023, -0.00615252, -0.26589247, -0.70851226,
       -0.49341215,  0.12717057, -0.03773915,  0.06252334, -0.19827055,
        0.07326336, -0.64404305,  0.49042788,  0.65940546,  0.92561345,
        0.30232074, -0.77847169, -0.86635093,  0.01214822,  0.15018469,
        0.36872465,  0.99844555,  0.80434557,  0.76791851,  0.21351632,
        0.71293502, -0.16361849, -0.74699014, -0.51992085,  0.7770304 ,
       -0.20175949, -0.21385287, -0.55605215,  0.15881189,  0.21239731,
       -0.2727695 ,  0.52959266, -0.51847096,  0.25156449,  0.59990597,
        0.47651584, -0.3830692 ,  0.70567896, -0.96437441, -0.55008125,
       -0.50707149,  0.34245562, -0.12124628, -0.06450243,  0.15496833,
       -0.36022476, -0.84083785,  0.63279454, -0.12277429, -0.03629358,
        0.64417299,  0.89020427, -0.53203164, -0.83302324, -0.44637111,
        0.06102855, -0.0351265 ])
>>> d = np.random.uniform(-1, 1, size=(122,))
>>> d
array([-0.70175998,  0.37245299,  0.05675171,  0.47050262,  0.28632484,
        0.2924587 ,  0.96752329,  0.86503551,  0.6967232 ,  0.9016225 ,
       -0.67908095, -0.11801209,  0.16489732, -0.97384107, -0.5434326 ,
        0.51508976,  0.84872244,  0.42637734, -0.80961955, -0.15143526,
       -0.97991145, -0.46350046, -0.24092568,  0.1918446 , -0.02783112,
        0.49490377,  0.98738584, -0.59020445, -0.37984496,  0.28346196,
       -0.90762608,  0.99849147,  0.52808629, -0.19168118, -0.45317743,
        0.97265568, -0.64005979,  0.07023143, -0.05924176, -0.41970893,
       -0.38431206, -0.16757581,  0.31529899, -0.10895948, -0.63762016,
       -0.81293285, -0.02705527,  0.59546958, -0.5827767 ,  0.65236725,
        0.78508699,  0.3960492 , -0.23072345, -0.21142103, -0.88029545,
        0.82485793,  0.14514487,  0.07259565, -0.47548989, -0.1314012 ,
       -0.94402155,  0.81923668,  0.54632624, -0.37650515,  0.31699954,
        0.09599396, -0.67932351, -0.67379634, -0.92249169, -0.9965975 ,
        0.96093287,  0.45875355,  0.14202519,  0.63809121,  0.86151084,
        0.96813124, -0.53583859,  0.95900084,  0.56947064,  0.94093839,
       -0.77471016, -0.86765922, -0.78160699, -0.75310208, -0.82798899,
       -0.16879716,  0.6287838 , -0.71842427,  0.83184749,  0.65256634,
       -0.94178111, -0.82522417,  0.77177116,  0.20141992, -0.30565206,
       -0.66595378,  0.50888984,  0.78414799,  0.98009204, -0.50261652,
        0.05496598, -0.34515664, -0.4771048 ,  0.03293117, -0.51461824,
        0.88362054, -0.90333162,  0.04895242, -0.4560054 ,  0.84966885,
       -0.41562268,  0.86445158,  0.98784253,  0.52791815, -0.01550132,
       -0.99977733,  0.16519524, -0.24092032, -0.02796405, -0.08770048,
        0.59993727, -0.40072755])
>>> np.dot(e, d)
array([ 4.54390841, -2.41277073, -3.53510623,  3.38089088,  0.76552762,
        2.14822122,  5.42209025,  4.40894199, -0.27940035, -2.2125017 ,
       -3.92223245,  3.87723967, -4.89557024,  1.15456274, -6.68624827])
>>> ee(100)
0.001026153564453125
>>> ee(1000)
0.0019989013671875
>>> ee(10000)
0.016000986099243164
>>> ee(1000)
0.0019989013671875
>>> ee(3000)
0.006006479263305664
>>> ee(100000)
0.15391850471496582
>>> n.activations[1]
[0.9999997754551908, 0.9999758508600568, 0.9999999997319537, 0.9999999999560845, 0.9999894479517565, 0.9999975826647002, 0.999999878938394, 0.9999999842347659, 0.9999999999944391, 0.9999999991588637, 0.9999999987110575, 0.9999999462835905, 0.9995422154663568, 0.9999999865889847, 0.9998387021151771, 0.99999992965914, 0.9999999999838785, 0.9999980663283298, 0.9999999998639426, 0.9999665828349086, 0.9999999881285205, 0.9999999093572589, 0.9999999999998835, 0.9999980790967534, 0.999999927948957]
>>> n.activations[2]
[0.9999999999977495, 0.9999999867983241, 0.9999999999858024, 0.9999999999995712, 0.9999999999849193, 0.9999999998973721, 0.9999999999925753, 0.9999999999348873, 0.999999999995334, 0.9999999999056594, 0.9999999994685214, 0.9999999832479661, 0.9999999996208894, 0.999999999696752, 0.9999999999994891]
>>> n.weights[1][1]
[0.30510956822660373, 0.4652863158632944, 0.006567311214149663, 0.2786485395209096, 0.9079886315259708, 0.6912256431672036, 0.8874994545649977, 0.20912260899663437, 0.8077387400768566, 0.5980892940156045, 0.928118681289601, 0.2019114920305186, 0.5619923991585031, 0.24757713898727085, 0.9887918565440655]
>>> something = np.array(n.weights[1]0
		     
SyntaxError: invalid syntax
>>> something = np.array(n.weights[1])
>>> something[0]
array([9.63176718e-01, 6.20797434e-04, 2.10749503e-01, 7.00619665e-01,
       2.60479326e-01, 6.30559763e-01, 6.56664657e-01, 8.60709012e-01,
       9.24345265e-01, 5.75375907e-01, 9.00194457e-01, 2.50543656e-02,
       6.15719438e-02, 8.86413118e-01, 6.47875418e-01])
>>> sth = np.array(n.activations[1])
>>> sth
array([0.99999978, 0.99997585, 1.        , 1.        , 0.99998945,
       0.99999758, 0.99999988, 0.99999998, 1.        , 1.        ,
       1.        , 0.99999995, 0.99954222, 0.99999999, 0.9998387 ,
       0.99999993, 1.        , 0.99999807, 1.        , 0.99996658,
       0.99999999, 0.99999991, 1.        , 0.99999808, 0.99999993])
>>> np.set_printoptions(precision=16)
>>> sth
array([0.9999997754551908, 0.9999758508600568, 0.9999999997319537,
       0.9999999999560845, 0.9999894479517565, 0.9999975826647002,
       0.999999878938394 , 0.9999999842347659, 0.9999999999944391,
       0.9999999991588637, 0.9999999987110575, 0.9999999462835905,
       0.9995422154663568, 0.9999999865889847, 0.9998387021151771,
       0.99999992965914  , 0.9999999999838785, 0.9999980663283298,
       0.9999999998639426, 0.9999665828349086, 0.9999999881285205,
       0.9999999093572589, 0.9999999999998835, 0.9999980790967534,
       0.999999927948957 ])
>>> np.dot(something, sth)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    np.dot(something, sth)
  File "<__array_function__ internals>", line 180, in dot
ValueError: shapes (25,15) and (25,) not aligned: 15 (dim 1) != 25 (dim 0)
>>> something = np.array(n.weights[0])
>>> np.dot(something, sth)
array([14.378943074081405, 14.177720395191786, 12.993122031641576,
       13.803067678757044, 13.142243017607528, 12.959266727630201,
       12.736963841243334, 12.753496969137071, 13.763935758655682,
       14.626047045950456, 13.629188272553781, 14.08259111424341 ,
       11.654800491472734, 12.578132936287448, 11.004067605661135,
       13.350602788934607, 13.680017571302889, 14.289354189189812,
       11.781728461102686, 14.136528601864947, 14.91646796184787 ,
       12.165908663855777, 12.118236444178635, 13.769078338704157,
       12.352735184381563, 11.577714875365656, 11.199028738350579,
        9.13466435443453 , 11.520995729405511, 11.418531269938656,
       10.955572873198713, 13.142450722222954, 11.185499304990236,
       12.02921717207236 , 10.485056444372875, 11.990547938667723,
       12.963651431555991, 13.147787660146859, 10.874124228754926,
       11.53249205655549 , 11.367135834768504, 12.0400516093969  ,
       10.47583643791095 , 12.28114094215556 , 13.251676701321628,
       13.123078035760896, 11.99815349474972 , 13.477969635198964,
       11.54170619979604 , 12.551589738802763, 14.473518550637124,
       11.236207301633577, 10.847288101477643, 14.13135255070764 ,
       10.985973287786312, 10.906919513361713, 12.244414494499104,
       13.227079250761724, 13.574956252337369, 15.367300054368924,
       10.5946049943409  , 13.953275652923208, 12.542177558400732,
       13.84593425717617 , 14.358606926210642, 12.407757283016027,
       11.565305076908329, 13.255516240445992, 13.201145403496776,
        9.688844477507503, 13.845601550875909, 14.446990414716755,
       12.062917719401291, 13.744786211212109, 14.608015131911307,
       14.9417424357962  , 13.880752190129687, 12.899516314749032,
       11.316093784126934, 10.467612273714895, 12.712131295841736,
       12.187447096444036, 12.279400659585095, 12.407056678672326,
       14.45306469051404 , 11.793720369121331, 12.453924496947149,
       12.599305379148554,  9.692281961538466, 14.137182680522782,
       13.488394887367454, 11.572771218871084, 14.904239500734102,
       10.918610875100306, 11.836557948584106, 11.907082084069689,
       10.818098313772289, 12.143450132132287, 15.210874229735202,
       13.095572258831632, 11.838363771478775, 14.508016646999044,
       11.344845253498052, 13.173019786273654, 11.216307549908413,
       12.234404163179583, 14.272050634027426, 12.408969948275379,
       13.713975399445326, 12.462086829219333, 11.62295079320369 ,
       11.541881865669817, 10.632927319955893, 14.600467186448903,
       14.895939144539687, 10.74255112871366 , 13.023381693808458,
       12.434505666081229, 14.77164405572829 , 13.036900501777177,
       10.286461479488104, 12.063307352868412])
>>> something.shape
(122, 25)
>>> sth.shape
(25,)
>>> sth = np.array(n.activations[0])
>>> sth.shape
(122,)
>>> something = np.array(n.weights[1])
>>> sth.shape
(122,)
>>> sth = np.array(n.activations[1])
>>> np.dot(something.T, sth)
array([13.756496488422398,  9.418034615056973, 12.835547311197473,
       14.585496890141627, 12.805376007701495, 11.846529151501977,
       13.159675361345181, 12.074024662618486, 13.391929099905026,
       11.888628184700153, 11.024252693402229,  9.298946665188717,
       11.193170068845841, 11.304808746417123, 14.497835626795824])
>>> tanh
<function tanh at 0x0000022E8A3D9EE0>
>>> tanh(np.dot(something.T, sth))
array([0.9999999999977495, 0.9999999867983241, 0.9999999999858024,
       0.9999999999995712, 0.9999999999849193, 0.9999999998973721,
       0.9999999999925753, 0.9999999999348873, 0.999999999995334 ,
       0.9999999999056594, 0.9999999994685214, 0.9999999832479661,
       0.9999999996208894, 0.999999999696752 , 0.9999999999994891])
>>> n.activations[1]
[0.9999997754551908, 0.9999758508600568, 0.9999999997319537, 0.9999999999560845, 0.9999894479517565, 0.9999975826647002, 0.999999878938394, 0.9999999842347659, 0.9999999999944391, 0.9999999991588637, 0.9999999987110575, 0.9999999462835905, 0.9995422154663568, 0.9999999865889847, 0.9998387021151771, 0.99999992965914, 0.9999999999838785, 0.9999980663283298, 0.9999999998639426, 0.9999665828349086, 0.9999999881285205, 0.9999999093572589, 0.9999999999998835, 0.9999980790967534, 0.999999927948957]
>>> n.activations[2]
[0.9999999999977495, 0.9999999867983241, 0.9999999999858024, 0.9999999999995712, 0.9999999999849193, 0.9999999998973721, 0.9999999999925753, 0.9999999999348873, 0.999999999995334, 0.9999999999056594, 0.9999999994685214, 0.9999999832479661, 0.9999999996208894, 0.999999999696752, 0.9999999999994891]
>>> tanh(np.dot(something.T, sth), False)
array([0.9999999999977495, 0.9999999867983241, 0.9999999999858024,
       0.9999999999995712, 0.9999999999849193, 0.9999999998973721,
       0.9999999999925753, 0.9999999999348873, 0.999999999995334 ,
       0.9999999999056594, 0.9999999994685214, 0.9999999832479661,
       0.9999999996208894, 0.999999999696752 , 0.9999999999994891])
>>> list(tanh(np.dot(something.T, sth), False))
[0.9999999999977495, 0.9999999867983241, 0.9999999999858024, 0.9999999999995712, 0.9999999999849193, 0.9999999998973721, 0.9999999999925753, 0.9999999999348873, 0.999999999995334, 0.9999999999056594, 0.9999999994685214, 0.9999999832479661, 0.9999999996208894, 0.999999999696752, 0.9999999999994891]
>>> list(tanh(np.dot(something.T, sth), False))==n.activations[2]
True
>>> for i in range(len(n.activations)-1):
	print(list(tanh(np.dot(n.weights[i].T, n.activations[i]), False))==n.activations[i+1])

	
Traceback (most recent call last):
  File "<pyshell#87>", line 2, in <module>
    print(list(tanh(np.dot(n.weights[i].T, n.activations[i]), False))==n.activations[i+1])
AttributeError: 'list' object has no attribute 'T'
>>> for i in range(len(n.activations)-1):
	weights = np.array(n.weights[i]).T
	act = np.array(n.activations[i])
	print(list(tanh(np.dot(weights, act), False))==n.activations[i+1])

	
True
True
True
True
False
False
>>> for i in range(len(n.activations)-1):
	weights = np.array(n.weights[i]).T
	act = np.array(n.activations[i])
	print(list(tanh(np.dot(weights, act), False))==n.activations[i+1])

	
True
True
True
True
False
False
>>> weights = np.array(n.weights[4]).T
>>> act = np.array(n.activations[4])
>>> print(list(tanh(np.dot(weights, act), False))==n.activations[5])
False
>>> np.dot(weights, act)
array([6.152087540079724, 8.56114436971706 , 6.833690411935751,
       8.479117804441788, 7.531748725005055, 5.634411793880958,
       7.960922555978344, 7.853129218559612, 6.271055314074966,
       7.950421792736598, 9.323887534680713, 4.973243141808784,
       8.503289688106104, 7.322379304663076, 6.549938048911812])
>>> tanh(np.dot(weights, act))
array([0.9999909344807294, 0.9999999267319788, 0.9999976806760207,
       0.9999999136699824, 0.9999994258358791, 0.999974470838523 ,
       0.9999997566336835, 0.9999996980823104, 0.9999928540659015,
       0.9999997514685721, 0.9999999840630878, 0.9999042133272051,
       0.999999917744225 , 0.9999991272457882, 0.9999959090402705])
>>> n.activations[5]
[0.9999909344807321, 0.9999999267319788, 0.9999976806760208, 0.9999999136699824, 0.9999994258358791, 0.9999744708385415, 0.9999997566336835, 0.9999996980823104, 0.9999928540659034, 0.9999997514685721, 0.9999999840630878, 0.9999042133275968, 0.999999917744225, 0.9999991272457883, 0.9999959090402707]
>>> tanh(np.dot(weights, act), False)
array([0.9999909344807294, 0.9999999267319788, 0.9999976806760207,
       0.9999999136699824, 0.9999994258358791, 0.999974470838523 ,
       0.9999997566336835, 0.9999996980823104, 0.9999928540659015,
       0.9999997514685721, 0.9999999840630878, 0.9999042133272051,
       0.999999917744225 , 0.9999991272457882, 0.9999959090402705])
>>> round(weights, 3)
Traceback (most recent call last):
  File "<pyshell#99>", line 1, in <module>
    round(weights, 3)
TypeError: type numpy.ndarray doesn't define __round__ method
>>> for i in range(len(n.activations)-1):
	weights = np.array(n.weights[i]).T
	act = np.array(n.activations[i])
	print(list(tanh(np.dot(weights, act), False))-n.activations[i+1])

	
Traceback (most recent call last):
  File "<pyshell#101>", line 4, in <module>
    print(list(tanh(np.dot(weights, act), False))-n.activations[i+1])
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> for i in range(len(n.activations)-1):
	weights = np.array(n.weights[i]).T
	act = np.array(n.activations[i])
	print(tanh(np.dot(weights, act), False)-np.array(n.activations[i+1]))

	
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.
 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
[0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0. 0.]
[-2.6645352591003757e-15  0.0000000000000000e+00 -1.1102230246251565e-16
  0.0000000000000000e+00  0.0000000000000000e+00 -1.8540724511240114e-14
  0.0000000000000000e+00  0.0000000000000000e+00 -1.8873791418627661e-15
  0.0000000000000000e+00  0.0000000000000000e+00 -3.9168668308775523e-13
  0.0000000000000000e+00 -1.1102230246251565e-16 -2.2204460492503131e-16]
[-2.7977620220553945e-14 -2.8476221380913103e-11 -7.8649309287470714e-12
 -2.6428859101201851e-12 -2.4535928844215960e-14]
>>> def ee(num):
	t = time.time()
	for j in range(num):
		for i in range(len(n.activations)-1):
			weights = np.array(n.weights[i]).T
			act = np.array(n.activations[i])
	print(time.time()-t)

	
>>> ee(100)
0.02699899673461914
>>> 
>>> ee(1000)
0.26984500885009766
>>> def ed(num):
	t = time.time()
	for i in range(n.lengths[0] - 1):
           n.activations[0][i] = inputs[i]

        # 은닉층~출력층의 활성화 함수
        for k in range(len(n.lengths) - 1):
           for j in range(n.lengths[k+1]):
              sum = 0
              for i in range(n.lengths[k]):
                 sum = sum + n.activations[k][i] * n.weights[k][i][j]
              # 시그모이드와 tanh 중에서 활성화 함수 선택
              n.activations[k+1][j] = tanh(sum, False)
              
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> 
>>> def ed(num):
	t = time.time()
	for j in range(num):
		for i in range(n.lengths[0] - 1):
			n.activations[0][i] = inputs[i]

		# 은닉층~출력층의 활성화 함수
		for k in range(len(n.lengths) - 1):
			for j in range(n.lengths[k+1]):
				sum = 0
			for i in range(n.lengths[k]):
				sum = sum + n.activations[k][i] * n.weights[k][i][j]
			# 시그모이드와 tanh 중에서 활성화 함수 선택
			n.activations[k+1][j] = tanh(sum, False)
	print(time.time()-t)

	
>>> ed(1000)
Traceback (most recent call last):
  File "<pyshell#116>", line 1, in <module>
    ed(1000)
  File "<pyshell#115>", line 5, in ed
    n.activations[0][i] = inputs[i]
NameError: name 'inputs' is not defined
>>> def ed(num):
	t = time.time()
	for j in range(num):

		# 은닉층~출력층의 활성화 함수
		for k in range(len(n.lengths) - 1):
			for j in range(n.lengths[k+1]):
				sum = 0
			for i in range(n.lengths[k]):
				sum = sum + n.activations[k][i] * n.weights[k][i][j]
			# 시그모이드와 tanh 중에서 활성화 함수 선택
			n.activations[k+1][j] = tanh(sum, False)
	print(time.time()-t)

	
>>> ed(1000)
0.06596207618713379
>>> ee(1000)
0.2698345184326172
>>> data==0
False
>>> d=0
>>> qq==0
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    qq==0
NameError: name 'qq' is not defined
>>> ee(1000)
0.2788360118865967
>>> def ee(num):
	t = time.time()
	for i in range(num):
		n.train(data)
	print(time.time()-t)

	
>>> ee(1000)
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999574393
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999707129
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999647152
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999422882
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999645358
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999576738
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999707111
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999422851
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999707108
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999576720
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999645329
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999576713
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999634321
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999645319
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999574337
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999704715
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999645308
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999647096
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999576687
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999574319
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999422765
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999704699
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999647076
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999636071
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999645278
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999634273
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999707043
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999858610
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999576645
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999647056
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999422702
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999647052
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999636041
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999574265
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999422672
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999647036
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999422654
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999858605
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999636011
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999645225
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999858603
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999634213
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999704628
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999647005
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999645211
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999576586
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999858601
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999646988
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999645200
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999635986
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999574205
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999574202
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999574198
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999645183
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999706959
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999645176
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999422540
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999645173
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999706943
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999704574
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999634155
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999576528
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999645151
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999858591
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999645140
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999706924
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999634137
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999574144
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999706915
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999645129
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999574133
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999422448
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999422448
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999422436
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999704528
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999422405
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999646892
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999574096
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999704507
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999646875
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999634079
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999646869
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999646865
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999645071
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999704487
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999706851
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999422331
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999646853
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999646843
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999646838
layers : [122, 25, 15, 15, 15, 15, 5]
error: 1.99999704466
layers : [122, 25, 15, 15, 15, 15, 5]
error: 3.99999422295
================================ RESTART: Shell ================================
>>> 
======= RESTART: C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py =======
0.0060122013092041016
>>> ee(1000)
Traceback (most recent call last):
  File "<pyshell#132>", line 1, in <module>
    ee(1000)
NameError: name 'ee' is not defined
>>> def ee(num):
	t = time.time()
	for i in range(num):
		n.train(data)
	print(time.time()-t)

	
>>> ee(1000)
5.007147312164307

>>> def ed(num):
	t = time.time()
	for j in range(num):

		# 은닉층~출력층의 활성화 함수
		for k in range(len(n.lengths) - 1):
			for j in range(n.lengths[k+1]):
				sum = 0
			for i in range(n.lengths[k]):
				sum = sum + n.activations[k][i] * n.weights[k][i][j]
			# 시그모이드와 tanh 중에서 활성화 함수 선택
			n.activations[k+1][j] = tanh(sum, False)
	print(time.time()-t)

	
>>> ed(1000)
0.07295823097229004
>>> def ee(num):
	t = time.time()
	for i in range(num):
		n.backPropagate([0, 0, 0, 0, 0])
	print(time.time()-t)

	
>>> ee(100)
0.374786376953125
>>> def ed(num):
	t = time.time()
	for i in range(num):
		n.update(data)
	print(time.time()-t)

	
>>> ed(100)
Traceback (most recent call last):
  File "<pyshell#148>", line 1, in <module>
    ed(100)
  File "<pyshell#147>", line 4, in ed
    n.update(data)
  File "C:\Users\KCDC\Desktop\intelligence life\base\bp_temp.py", line 105, in update
    self.activations[0][i] = inputs[i]
IndexError: list index out of range
>>> objects = [[j%11-5, j//11-5, np.random.normal()] for j in range(int(self.lengths[0]-1))]
Traceback (most recent call last):
  File "<pyshell#149>", line 1, in <module>
    objects = [[j%11-5, j//11-5, np.random.normal()] for j in range(int(self.lengths[0]-1))]
NameError: name 'self' is not defined
>>> objects = [[j%11-5, j//11-5, np.random.normal()] for j in range(int(n.lengths[0]-1))]
>>> data = [objects[i][2] for i in range(int(self.lengths[0]-1))]
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    data = [objects[i][2] for i in range(int(self.lengths[0]-1))]
NameError: name 'self' is not defined
>>> data = [objects[i][2] for i in range(int(n.lengths[0]-1))]
>>> def ed(num):
	t = time.time()
	for i in range(num):
		n.update(data)
	print(time.time()-t)

	
>>> ed(100)
0.11694502830505371
>>> def ef(num):
	t = time.time()
		for i in range(num):
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
	print(time.time()-t)
	
SyntaxError: unexpected indent
>>> 
>>> def ef(num):
	t = time.time()
	for i in range(num):
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
	print(time.time()-t)

	
>>> ef(100)
Traceback (most recent call last):
  File "<pyshell#163>", line 1, in <module>
    ef(100)
  File "<pyshell#162>", line 4, in ef
    nth_deltas = [[0.0] * self.lengths[-i-1] for i in range(len(self.lengths)-1)]
NameError: name 'self' is not defined
>>> def ef(num):
	self = n
	t = time.time()
	for i in range(num):
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
	print(time.time()-t)

	
>>> ef(100)
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    ef(100)
  File "<pyshell#165>", line 7, in ef
    error = targets[k] - self.activations[-1][k]
NameError: name 'targets' is not defined
>>> def ef(num):
	self = n
	targets =[0, 0, 0, 0, 0]
	t = time.time()
	for i in range(num):
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
	print(time.time()-t)

	
>>> ef(100)
0.004999637603759766
>>> ef(1000)
0.00699615478515625
>>> help(ee)
Help on function ee in module __main__:

ee(num)

>>> ee(100)
0.37579822540283203
>>> ef(10000)
0.02098989486694336
>>> def ef(num):
	self = n
	targets =[0, 0, 0, 0, 0]
	t = time.time()
	for i in range(num):
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
	print(time.time()-t)
	
SyntaxError: inconsistent use of tabs and spaces in indentation
>>> 
>>> def ef(num):
	self = n
	targets =[0, 0, 0, 0, 0]
	t = time.time()
	for i in range(num):
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
	print(time.time()-t)

	
>>> ef(100)
2.499996345729277
>>> ef(100)
2.499996345729277
>>> def ef(num):
	self = n
	targets =[0, 0, 0, 0, 0]
	t = time.time()
	for i in range(num):
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
	print(time.time()-t)

	
>>> ef(100)
0.0049855709075927734
>>> ee(100)
0.3747861385345459
>>> ef(100)
0.003987789154052734
>>> ef(10000)
0.019997835159301758
>>> ef(1000000)
1.6050853729248047
>>> def ef(num):
	self = n
	targets =[0, 0, 0, 0, 0]
	t = time.time()
	for i in range(num):
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
	print(time.time()-t)

	
>>> ef(100)
0.37679409980773926
>>> n.activations[-1]
[0.9999999537587666, 0.9999977827165103, 0.9999993429733011, 0.9999993307362182, 0.9999999355415797]
>>> [0,0,0,0,0]-n.activations[-1]
Traceback (most recent call last):
  File "<pyshell#192>", line 1, in <module>
    [0,0,0,0,0]-n.activations[-1]
TypeError: unsupported operand type(s) for -: 'list' and 'list'
>>> np.array([0,0,0,0,0])-np.array(n.activations[-1])
array([-0.99999995, -0.99999778, -0.99999934, -0.99999933, -0.99999994])
>>> tanh(np.array(n.activations[-1]), True)
array([9.24824647e-08, 4.43456206e-06, 1.31405297e-06, 1.33852712e-06,
       1.28916836e-07])
>>> np.multiply(tanh(np.array(n.activations[-1]), True), np.array([0,0,0,0,0])-np.array(n.activations[-1]))
array([-9.24824604e-08, -4.43455223e-06, -1.31405210e-06, -1.33852622e-06,
       -1.28916828e-07])
>>> nth_deltas = [[0.0] * n.lengths[-i-1] for i in range(len(n.lengths)-1)]
>>> for k in range(n.lengths[-1]):
	error = targets[k] - n.activations[-1][k]
	# 시그모이드와 tanh 중에서 활성화 함수 선택, 미분 적용
	nth_deltas[0][k] = tanh(n.activations[-1][k], True) * error

	
Traceback (most recent call last):
  File "<pyshell#198>", line 2, in <module>
    error = targets[k] - n.activations[-1][k]
NameError: name 'targets' is not defined
>>> for k in range(n.lengths[-1]):
	error = [0,0,0,0,0][k] - n.activations[-1][k]
	# 시그모이드와 tanh 중에서 활성화 함수 선택, 미분 적용
	nth_deltas[0][k] = tanh(n.activations[-1][k], True) * error

	
>>> nth_deltas
[[-9.248246040990207e-08, -4.434552230323608e-06, -1.3140521028491227e-06, -1.3385262199851179e-06, -1.289168281184633e-07], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0], [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]]
>>> def ef(num):
	self = n
	targets =[0, 0, 0, 0, 0]
	t = time.time()
	for i in range(num):
		nth_deltas[0] = np.multiply(tanh(np.array(n.activations[-1]), True),
					    np.array(targets)-np.array(n.activations[-1]))
		# 은닉~입력 노드의 오차 함수
		for i in range(1, len(self.lengths) - 1):
			nth_deltas[i] = np.multiply(tanh(np.array(n.activations[-i-1]), True),
						    np.array(nth_deltas[i-1])-np.array(n.activations[-i-1]))
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
	print(time.time()-t)

	
>>> ef(100)
Traceback (most recent call last):
  File "<pyshell#204>", line 1, in <module>
    ef(100)
  File "<pyshell#203>", line 11, in ef
    np.array(nth_deltas[i-1])-np.array(n.activations[-i-1]))
ValueError: operands could not be broadcast together with shapes (5,) (15,) 
>>> np.multiply(tanh(np.array(n.activations[-1]), True), np.array([0,0,0,0,0])-np.array(n.activations[-1]))
array([-9.24824604e-08, -4.43455223e-06, -1.31405210e-06, -1.33852622e-06,
       -1.28916828e-07])
>>> def ef(num):
	self = n
	targets =[0, 0, 0, 0, 0]
	t = time.time()
	for i in range(num):
		nth_deltas[0] = np.multiply(tanh(np.array(n.activations[-1]), True),
					    np.array(targets)-np.array(n.activations[-1]))
		# 은닉~입력 노드의 오차 함수
		for i in range(1, len(self.lengths) - 1):
			nth_deltas[i] = np.multiply(tanh(np.array(n.activations[-i-1]), True),
						    np.array(nth_deltas[i-1])-np.array(n.activations[-i]))
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
	print(time.time()-t)

	
>>> ef(100)
Traceback (most recent call last):
  File "<pyshell#208>", line 1, in <module>
    ef(100)
  File "<pyshell#207>", line 10, in ef
    nth_deltas[i] = np.multiply(tanh(np.array(n.activations[-i-1]), True),
ValueError: operands could not be broadcast together with shapes (15,) (5,) 
>>> def ef(num):
	self = n
	targets =[0, 0, 0, 0, 0]
	t = time.time()
	for i in range(num):
		nth_deltas[0] = np.multiply(tanh(np.array(n.activations[-1]), True),
					    np.array(targets)-np.array(n.activations[-1]))
		# 은닉~입력 노드의 오차 함수
		for i in range(1, len(self.lengths) - 1):
			nth_deltas[i] = np.multiply(tanh(np.array(n.activations[-i-1]), True),
						    np.array(nth_deltas[i-1])-np.array(n.weights[-i]))
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
	print(time.time()-t)

	
>>> ef(100)
Traceback (most recent call last):
  File "<pyshell#211>", line 1, in <module>
    ef(100)
  File "<pyshell#210>", line 10, in ef
    nth_deltas[i] = np.multiply(tanh(np.array(n.activations[-i-1]), True),
ValueError: operands could not be broadcast together with shapes (15,) (15,5) 
>>> for i in range(1, len(n.lengths) - 1):
			for j in range(n.lengths[-i-1]):
				error = 0.0
				for k in range(n.lengths[-i]):
					error = error + nth_deltas[i-1][k] * self.weights[-i][j][k]
				# 시그모이드와 tanh 중에서 활성화 함수 선택, 미분 적용
				nth_deltas[i][j] = tanh(n.activations[-i-1][j], True) * error

				
Traceback (most recent call last):
  File "<pyshell#213>", line 5, in <module>
    error = error + nth_deltas[i-1][k] * self.weights[-i][j][k]
NameError: name 'self' is not defined
>>> for i in range(1, len(n.lengths) - 1):
			for j in range(n.lengths[-i-1]):
				error = 0.0
				for k in range(n.lengths[-i]):
					error = error + nth_deltas[i-1][k] * n.weights[-i][j][k]
				# 시그모이드와 tanh 중에서 활성화 함수 선택, 미분 적용
				nth_deltas[i][j] = tanh(n.activations[-i-1][j], True) * error

				
>>> nth_deltas[i] = np.multiply(tanh(np.array(n.activations[-i-1]), True),
						    np.array(nth_deltas[i-1])-np.array(n.weights[-i]))
Traceback (most recent call last):
  File "<pyshell#216>", line 1, in <module>
    nth_deltas[i] = np.multiply(tanh(np.array(n.activations[-i-1]), True),
ValueError: operands could not be broadcast together with shapes (25,) (25,15) 
>>> nth_deltas[i] = np.multiply(tanh(np.array(n.activations[-i-1]), True),
						    np.array(nth_deltas[i-1])-np.array(n.weights[-i]))
Traceback (most recent call last):
  File "<pyshell#217>", line 1, in <module>
    nth_deltas[i] = np.multiply(tanh(np.array(n.activations[-i-1]), True),
ValueError: operands could not be broadcast together with shapes (25,) (25,15) 
>>> i=1
>>> nth_deltas[i] = np.multiply(tanh(np.array(n.activations[-i-1]), True),
						    np.array(nth_deltas[i-1])-np.array(n.weights[-i]))
Traceback (most recent call last):
  File "<pyshell#219>", line 1, in <module>
    nth_deltas[i] = np.multiply(tanh(np.array(n.activations[-i-1]), True),
ValueError: operands could not be broadcast together with shapes (15,) (15,5) 
>>> nth_deltas
[array([-9.24824604e-08, -4.43455223e-06, -1.31405210e-06, -1.33852622e-06,
       -1.28916828e-07]), [-5.4280589473668915e-11, -1.951665970380317e-13, -9.591264798830876e-12, -3.7947730946954035e-13, -2.851933167452867e-12, -2.037250404543356e-10, -3.2158290003009987e-12, -2.4771187897173755e-12, -8.084473718016626e-11, -1.5497542239228704e-12, -8.94375714434935e-14, -9.608738124780448e-10, -7.065368486934506e-13, -7.589413403787206e-12, -9.980344227724266e-12], [-2.411468553888652e-16, -8.255407988358204e-17, -9.989940674206956e-15, -1.3585487549664653e-15, -2.7346802124477326e-17, -1.3270102284228079e-16, -1.2464708418758822e-16, -3.4024341574482846e-15, -1.4268971392438448e-18, -2.8881952384746945e-16, -4.618016323434894e-17, -2.5065931543012926e-16, -1.6781808210934285e-16, -1.6626902654642207e-15, -2.7200021050387686e-16], [-4.589267798457969e-21, -1.2273662240732193e-20, -2.1379630911684835e-19, -6.16401384271876e-19, -2.5854275018876328e-20, -2.452223352707927e-19, -1.37574722721419e-19, -2.2000950713594088e-20, -4.795615439800224e-21, -4.156368419725048e-21, -1.2373426555488555e-19, -3.112808373641969e-22, -6.514113392252542e-19, -1.231402404151129e-19, -9.359729338358779e-21], [-1.572536972692169e-20, -8.583471019350444e-21, -5.507446844179132e-23, -5.846426220374484e-23, -6.907633258057299e-21, -1.0928264680302212e-19, -6.629123532005956e-22, -2.1854836409271783e-20, -8.940262890714585e-21, -5.0970191466425666e-21, -1.5907754759234426e-19, -1.1716246414928306e-20, -9.977967255418259e-21, -4.351962459124097e-21, -7.20622320168323e-20], [-3.54606980198412e-19, -7.664769565722062e-22, -6.86514693485861e-26, -4.2227208463863e-24, -1.0079209289597939e-20, -1.2559451154256047e-19, -3.9045298275876236e-21, -2.666733044430948e-23, -2.511141193756482e-19, -4.774530772816935e-21, -2.575582934149825e-20, -8.954226543739894e-20, -2.551125916919689e-21, -1.837771756499797e-19, -3.7551085182098145e-21, -5.511419786428182e-23, -6.766823264250569e-20, -2.060393358365574e-20, -9.736166888378139e-21, -1.779553063941844e-27, -2.2422659976989924e-21, -6.466303998056998e-21, -1.0181506408916745e-22, -6.326408542683458e-23, -9.970775770303297e-21]]
>>> tanh(np.array(n.activations[-2]), True)
array([1.82211658e-05, 1.46958937e-07, 4.64123539e-06, 1.73166303e-07,
       1.15311100e-06, 5.10908025e-05, 4.88127955e-07, 6.04439325e-07,
       1.43218359e-05, 4.97837080e-07, 3.18902194e-08, 1.91785428e-04,
       1.65066675e-07, 1.75498273e-06, 8.20036348e-06])
>>> np.array(nth_deltas[0])-np.array(n.weights[-1])
array([[-0.17700479, -0.26253937, -0.89124965, -0.38796658, -0.83730312],
       [-0.17738547, -0.0399451 , -0.6256927 , -0.21506492, -0.18966943],
       [-0.26421419, -0.15859722, -0.03315265, -0.88238413, -0.88548943],
       [-0.68511537, -0.22863749, -0.37425414, -0.39253017, -0.75211059],
       [-0.87091064, -0.01309879, -0.95533426, -0.76786198, -0.3993334 ],
       [-0.54143016, -0.61466841, -0.26438817, -0.6177235 , -0.29027572],
       [-0.60322367, -0.98430963, -0.95675447, -0.67007697, -0.10245709],
       [-0.74361861, -0.49762023, -0.56072064, -0.75734014, -0.56006665],
       [-0.38807843, -0.91569208, -0.25836493, -0.82601683, -0.80018061],
       [-0.92775622, -0.630974  , -0.08028371, -0.04829725, -0.4573915 ],
       [-0.11589777, -0.51606006, -0.0515058 , -0.31468853, -0.12763843],
       [-0.97847052, -0.77917301, -0.7374349 , -0.29620408, -0.76711385],
       [-0.95490208, -0.73436697, -0.51705847, -0.12185327, -0.72053532],
       [-0.76440471, -0.45902929, -0.94636518, -0.63833588, -0.93263215],
       [-0.59893348, -0.0195873 , -0.21128533, -0.51823194, -0.80304238]])
>>> np.array(nth_deltas[0])-np.array(n.weights[-1])
array([[-0.17700479, -0.26253937, -0.89124965, -0.38796658, -0.83730312],
       [-0.17738547, -0.0399451 , -0.6256927 , -0.21506492, -0.18966943],
       [-0.26421419, -0.15859722, -0.03315265, -0.88238413, -0.88548943],
       [-0.68511537, -0.22863749, -0.37425414, -0.39253017, -0.75211059],
       [-0.87091064, -0.01309879, -0.95533426, -0.76786198, -0.3993334 ],
       [-0.54143016, -0.61466841, -0.26438817, -0.6177235 , -0.29027572],
       [-0.60322367, -0.98430963, -0.95675447, -0.67007697, -0.10245709],
       [-0.74361861, -0.49762023, -0.56072064, -0.75734014, -0.56006665],
       [-0.38807843, -0.91569208, -0.25836493, -0.82601683, -0.80018061],
       [-0.92775622, -0.630974  , -0.08028371, -0.04829725, -0.4573915 ],
       [-0.11589777, -0.51606006, -0.0515058 , -0.31468853, -0.12763843],
       [-0.97847052, -0.77917301, -0.7374349 , -0.29620408, -0.76711385],
       [-0.95490208, -0.73436697, -0.51705847, -0.12185327, -0.72053532],
       [-0.76440471, -0.45902929, -0.94636518, -0.63833588, -0.93263215],
       [-0.59893348, -0.0195873 , -0.21128533, -0.51823194, -0.80304238]])
>>> np.dot(tanh(np.array(n.activations[-2]), True).T, np.array(nth_deltas[0])-np.array(n.weights[-1]))
array([-0.0002341 , -0.00020173, -0.00018062, -0.00011856, -0.00020236])
>>> np.dot(tanh(np.array(n.activations[-2]), True).T, np.array(nth_deltas[0])-np.array(n.weights[-1]))
array([-0.0002341 , -0.00020173, -0.00018062, -0.00011856, -0.00020236])
>>> n.activations[-1]
[0.9999999537587666, 0.9999977827165103, 0.9999993429733011, 0.9999993307362182, 0.9999999355415797]
>>> nth_deltas[1]
[-5.4280589473668915e-11, -1.951665970380317e-13, -9.591264798830876e-12, -3.7947730946954035e-13, -2.851933167452867e-12, -2.037250404543356e-10, -3.2158290003009987e-12, -2.4771187897173755e-12, -8.084473718016626e-11, -1.5497542239228704e-12, -8.94375714434935e-14, -9.608738124780448e-10, -7.065368486934506e-13, -7.589413403787206e-12, -9.980344227724266e-12]
>>> len(nth_deltas[1])
15
>>> len(nth_deltas[1])
15
>>> len(nth_deltas[1])
15
>>> len(nth_deltas[1])
15
>>> 
>>> 
>>> len(nth_deltas[1])
15
>>> nth_deltas[1]
[-5.4280589473668915e-11, -1.951665970380317e-13, -9.591264798830876e-12, -3.7947730946954035e-13, -2.851933167452867e-12, -2.037250404543356e-10, -3.2158290003009987e-12, -2.4771187897173755e-12, -8.084473718016626e-11, -1.5497542239228704e-12, -8.94375714434935e-14, -9.608738124780448e-10, -7.065368486934506e-13, -7.589413403787206e-12, -9.980344227724266e-12]
>>> for i in range(1, len(n.lengths) - 1):
			for j in range(n.lengths[-i-1]):
				error = 0.0
				for k in range(n.lengths[-i]):
					error = error + nth_deltas[i-1][k] * self.weights[-i][j][k]
				# 시그모이드와 tanh 중에서 활성화 함수 선택, 미분 적용
				nth_deltas[i][j] = tanh(n.activations[-i-1][j], True) * error

				
Traceback (most recent call last):
  File "<pyshell#237>", line 5, in <module>
    error = error + nth_deltas[i-1][k] * self.weights[-i][j][k]
NameError: name 'self' is not defined
>>> for i in range(1, len(n.lengths) - 1):
			for j in range(n.lengths[-i-1]):
				error = 0.0
				for k in range(n.lengths[-i]):
					error = error + nth_deltas[i-1][k] * n.weights[-i][j][k]
				# 시그모이드와 tanh 중에서 활성화 함수 선택, 미분 적용
				nth_deltas[i][j] = tanh(n.activations[-i-1][j], True) * error

				
>>> np.dot(tanh(np.array(n.activations[-2]), True).T, np.array(nth_deltas[0])*np.array(n.weights[-1]))
array([-2.16498700e-11, -8.94585374e-10, -2.37337732e-10, -1.58690136e-10,
       -2.60873428e-11])
>>> np.dot(tanh(np.array(n.activations[-2]), True), np.array(nth_deltas[0])*np.array(n.weights[-1]))
array([-2.16498700e-11, -8.94585374e-10, -2.37337732e-10, -1.58690136e-10,
       -2.60873428e-11])
>>> np.dot(tanh(np.array(n.activations[-2]), True), np.array(nth_deltas[0])*np.array(n.weights[-1]))
array([-2.16498700e-11, -8.94585374e-10, -2.37337732e-10, -1.58690136e-10,
       -2.60873428e-11])
>>> np.dot(tanh(np.array(n.activations[-2]), True), np.array(nth_deltas[0])*np.array(n.weights[-1]).T)
Traceback (most recent call last):
  File "<pyshell#243>", line 1, in <module>
    np.dot(tanh(np.array(n.activations[-2]), True), np.array(nth_deltas[0])*np.array(n.weights[-1]).T)
ValueError: operands could not be broadcast together with shapes (5,) (5,15) 
>>> np.dot(tanh(np.array(n.activations[-2]), True).T, np.array(nth_deltas[0])*np.array(n.weights[-1]).T)
Traceback (most recent call last):
  File "<pyshell#244>", line 1, in <module>
    np.dot(tanh(np.array(n.activations[-2]), True).T, np.array(nth_deltas[0])*np.array(n.weights[-1]).T)
ValueError: operands could not be broadcast together with shapes (5,) (5,15) 
>>> np.dot(tanh(np.array(n.activations[-2]), True).T, np.array(nth_deltas[0])*np.array(n.weights[-1]))
array([-2.16498700e-11, -8.94585374e-10, -2.37337732e-10, -1.58690136e-10,
       -2.60873428e-11])
>>> np.dot(
	.T, np.array(nth_deltas[0])*np.array(n.weights[-1]))
SyntaxError: invalid syntax
>>> tanh(np.array(n.activations[-2]), True)
array([1.82211658e-05, 1.46958937e-07, 4.64123539e-06, 1.73166303e-07,
       1.15311100e-06, 5.10908025e-05, 4.88127955e-07, 6.04439325e-07,
       1.43218359e-05, 4.97837080e-07, 3.18902194e-08, 1.91785428e-04,
       1.65066675e-07, 1.75498273e-06, 8.20036348e-06])
>>> np.array(nth_deltas[0])*np.array(n.weights[-1])
array([[-1.63698299e-08, -1.16422486e-06, -1.17114675e-06,
        -5.19301647e-07, -1.07942446e-07],
       [-1.64050365e-08, -1.77118975e-07, -8.22191080e-07,
        -2.87868240e-07, -2.44515644e-08],
       [-2.44351694e-08, -7.03287996e-07, -4.35625801e-08,
        -1.18109250e-06, -1.14154472e-07],
       [-6.33611466e-08, -1.01388521e-06, -4.91787709e-07,
        -5.25410130e-07, -9.69596949e-08],
       [-8.05439501e-08, -5.80676177e-08, -1.25535727e-06,
        -1.02780160e-06, -5.14807786e-08],
       [-5.00727849e-08, -2.72575950e-06, -3.47418104e-07,
        -8.26837316e-07, -3.74214085e-08],
       [-5.57876010e-08, -4.36495280e-06, -1.25722349e-06,
        -8.96913799e-07, -1.32084259e-08],
       [-6.87716705e-08, -2.20670326e-06, -7.36814410e-07,
        -1.01371784e-06, -7.22019999e-08],
       [-3.58904391e-08, -4.06066468e-06, -3.39503251e-07,
        -1.10564339e-06, -1.03156730e-07],
       [-8.58011690e-08, -2.79806747e-06, -1.05495247e-07,
        -6.46453390e-08, -5.89654452e-08],
       [-1.07185024e-08, -2.28847563e-06, -6.76795840e-08,
        -4.21217063e-07, -1.64547252e-08],
       [-9.04913529e-08, -3.45526374e-06, -9.69026157e-07,
        -3.96475133e-07, -9.88938672e-08],
       [-8.83116854e-08, -3.25656902e-06, -6.79440041e-07,
        -1.63102010e-07, -9.28891120e-08],
       [-7.06940201e-08, -2.03556970e-06, -1.24357142e-06,
        -8.54427525e-07, -1.20231962e-07],
       [-5.53908336e-08, -8.68412554e-08, -2.77638203e-07,
        -6.93665249e-07, -1.03525660e-07]])
>>> nth_deltas[0]
array([-9.24824604e-08, -4.43455223e-06, -1.31405210e-06, -1.33852622e-06,
       -1.28916828e-07])
>>> np.dot(tanh(np.array(n.activations[-3]), True).T, np.array(nth_deltas[1])*np.array(n.weights[-2]))
array([-7.74945472e-16, -5.18425389e-18, -2.00585481e-16, -7.30791569e-18,
       -6.23203464e-17, -1.41965638e-15, -7.59284463e-17, -4.16853504e-17,
       -1.64442483e-15, -2.58939112e-17, -9.66124486e-19, -1.35801768e-14,
       -1.12900646e-17, -1.01187522e-16, -9.73610161e-17])
>>> nth_deltas[1]
[-5.4280589473668915e-11, -1.951665970380317e-13, -9.591264798830876e-12, -3.7947730946954035e-13, -2.851933167452867e-12, -2.037250404543356e-10, -3.2158290003009987e-12, -2.4771187897173755e-12, -8.084473718016626e-11, -1.5497542239228704e-12, -8.94375714434935e-14, -9.608738124780448e-10, -7.065368486934506e-13, -7.589413403787206e-12, -9.980344227724266e-12]
>>> np.dot(tanh(np.array(n.activations[-4]), True).T, np.array(nth_deltas[1])*np.array(n.weights[-2]))
array([-7.48641498e-15, -2.20737236e-17, -1.65224333e-15, -6.59802813e-17,
       -3.85165478e-16, -2.81625017e-14, -3.97718282e-16, -5.25532104e-16,
       -7.58962997e-15, -2.35096385e-16, -1.67099768e-17, -1.59013667e-13,
       -1.19422947e-16, -6.99855244e-16, -1.30841888e-15])
>>> np.dot(tanh(np.array(n.activations[-5]), True).T, np.array(nth_deltas[1])*np.array(n.weights[-2]))
array([-6.26884578e-12, -4.44592853e-14, -2.76138251e-12, -8.72351333e-14,
       -5.29100208e-13, -5.62724458e-11, -7.80483660e-13, -6.29848257e-13,
       -1.44007716e-11, -3.15289606e-13, -2.85120698e-14, -1.40849814e-10,
       -1.76770000e-13, -1.39745220e-12, -2.42104948e-12])
>>> np.dot(tanh(np.array(n.activations[-2]), True).T, np.array(nth_deltas[1])*np.array(n.weights[-2]))
array([-1.13203559e-14, -4.26755690e-17, -5.05372803e-16, -9.20201634e-17,
       -4.01872365e-16, -2.71846074e-14, -5.69747838e-16, -1.96251978e-16,
       -1.58094442e-14, -1.92376479e-16, -1.75307925e-17, -3.50907187e-14,
       -1.08717603e-16, -1.54471055e-15, -9.78059207e-16])
>>> np.dot(tanh(np.array(n.activations[-2]), True).T, np.array(nth_deltas[0])*np.array(n.weights[-2]))
Traceback (most recent call last):
  File "<pyshell#255>", line 1, in <module>
    np.dot(tanh(np.array(n.activations[-2]), True).T, np.array(nth_deltas[0])*np.array(n.weights[-2]))
ValueError: operands could not be broadcast together with shapes (5,) (15,15) 
>>> np.dot(tanh(np.array(n.activations[-1]), True).T, np.array(nth_deltas[1])*np.array(n.weights[-2]))
Traceback (most recent call last):
  File "<pyshell#256>", line 1, in <module>
    np.dot(tanh(np.array(n.activations[-1]), True).T, np.array(nth_deltas[1])*np.array(n.weights[-2]))
  File "<__array_function__ internals>", line 180, in dot
ValueError: shapes (5,) and (15,15) not aligned: 5 (dim 0) != 15 (dim 0)
>>> np.dot(tanh(np.array(n.activations[-4]), True).T, np.array(nth_deltas[1])*np.array(n.weights[-2]))
array([-7.48641498e-15, -2.20737236e-17, -1.65224333e-15, -6.59802813e-17,
       -3.85165478e-16, -2.81625017e-14, -3.97718282e-16, -5.25532104e-16,
       -7.58962997e-15, -2.35096385e-16, -1.67099768e-17, -1.59013667e-13,
       -1.19422947e-16, -6.99855244e-16, -1.30841888e-15])
>>> np.dot(tanh(np.array(n.activations[-4]), True).T, np.array(nth_deltas[1])*np.array(n.weights[-2]))
array([-7.48641498e-15, -2.20737236e-17, -1.65224333e-15, -6.59802813e-17,
       -3.85165478e-16, -2.81625017e-14, -3.97718282e-16, -5.25532104e-16,
       -7.58962997e-15, -2.35096385e-16, -1.67099768e-17, -1.59013667e-13,
       -1.19422947e-16, -6.99855244e-16, -1.30841888e-15])
>>> np.dot(tanh(np.array(n.activations[-1]), True).T, np.array(nth_deltas[1])*np.array(n.weights[-2]))
Traceback (most recent call last):
  File "<pyshell#259>", line 1, in <module>
    np.dot(tanh(np.array(n.activations[-1]), True).T, np.array(nth_deltas[1])*np.array(n.weights[-2]))
  File "<__array_function__ internals>", line 180, in dot
ValueError: shapes (5,) and (15,15) not aligned: 5 (dim 0) != 15 (dim 0)
>>> np.dot(tanh(np.array(n.activations[-4]), True).T, np.array(nth_deltas[1])*np.array(n.weights[-2]))
array([-7.48641498e-15, -2.20737236e-17, -1.65224333e-15, -6.59802813e-17,
       -3.85165478e-16, -2.81625017e-14, -3.97718282e-16, -5.25532104e-16,
       -7.58962997e-15, -2.35096385e-16, -1.67099768e-17, -1.59013667e-13,
       -1.19422947e-16, -6.99855244e-16, -1.30841888e-15])
>>> np.dot(tanh(np.array(n.activations[-4]), True).T, np.array(nth_deltas[1])*np.array(n.weights[-2]))
array([-7.48641498e-15, -2.20737236e-17, -1.65224333e-15, -6.59802813e-17,
       -3.85165478e-16, -2.81625017e-14, -3.97718282e-16, -5.25532104e-16,
       -7.58962997e-15, -2.35096385e-16, -1.67099768e-17, -1.59013667e-13,
       -1.19422947e-16, -6.99855244e-16, -1.30841888e-15])
>>> np.dot(tanh(np.array(n.activations[-4]), True).T, np.array(nth_deltas[2])*np.array(n.weights[-2]))
array([-3.32591346e-20, -9.33702779e-21, -1.72092140e-18, -2.36212882e-19,
       -3.69329977e-21, -1.83442976e-20, -1.54157526e-20, -7.21842001e-19,
       -1.33955798e-22, -4.38136738e-20, -8.62802337e-21, -4.14812606e-20,
       -2.83655833e-20, -1.53324432e-19, -3.56591117e-20])
>>> nth_deltas[0]
array([-9.24824604e-08, -4.43455223e-06, -1.31405210e-06, -1.33852622e-06,
       -1.28916828e-07])
>>> nth_deltas[1]
[-5.4280589473668915e-11, -1.951665970380317e-13, -9.591264798830876e-12, -3.7947730946954035e-13, -2.851933167452867e-12, -2.037250404543356e-10, -3.2158290003009987e-12, -2.4771187897173755e-12, -8.084473718016626e-11, -1.5497542239228704e-12, -8.94375714434935e-14, -9.608738124780448e-10, -7.065368486934506e-13, -7.589413403787206e-12, -9.980344227724266e-12]
>>> -1.28916828e-07])
SyntaxError: unmatched ']'
>>> nth_deltas[2]
[-2.411468553888652e-16, -8.255407988358204e-17, -9.989940674206956e-15, -1.3585487549664653e-15, -2.7346802124477326e-17, -1.3270102284228079e-16, -1.2464708418758822e-16, -3.4024341574482846e-15, -1.4268971392438448e-18, -2.8881952384746945e-16, -4.618016323434894e-17, -2.5065931543012926e-16, -1.6781808210934285e-16, -1.6626902654642207e-15, -2.7200021050387686e-16]
>>> np.dot(tanh(np.array(n.activations[-2]), True), np.array(nth_deltas[0])*np.array(n.weights[-2]))
Traceback (most recent call last):
  File "<pyshell#267>", line 1, in <module>
    np.dot(tanh(np.array(n.activations[-2]), True), np.array(nth_deltas[0])*np.array(n.weights[-2]))
ValueError: operands could not be broadcast together with shapes (5,) (15,15) 
>>> np.dot(tanh(np.array(n.activations[-2]), True), np.array(nth_deltas[0])*np.array(n.weights[-1]))
array([-2.16498700e-11, -8.94585374e-10, -2.37337732e-10, -1.58690136e-10,
       -2.60873428e-11])
>>> for i in range(1, len(n.lengths) - 1):
			for j in range(n.lengths[-i-1]):
				error = 0.0
				for k in range(n.lengths[-i]):
					error = error + nth_deltas[i-1][k] * n.weights[-i][j][k]
				# 시그모이드와 tanh 중에서 활성화 함수 선택, 미분 적용
				nth_deltas[i][j] = tanh(n.activations[-i-1][j], True) * error

				
>>> np.dot(tanh(np.array(n.activations[-2]), True), np.array(nth_deltas[0]).T*np.array(n.weights[-1]))
array([-2.16498700e-11, -8.94585374e-10, -2.37337732e-10, -1.58690136e-10,
       -2.60873428e-11])
>>> np.dot(tanh(np.array(n.activations[-2]), True), np.array(nth_deltas[0]).T*np.array(n.weights[-1])T)
SyntaxError: invalid syntax
>>> np.dot(tanh(np.array(n.activations[-2]), True), np.array(nth_deltas[0]).T*np.array(n.weights[-1]).T)
Traceback (most recent call last):
  File "<pyshell#273>", line 1, in <module>
    np.dot(tanh(np.array(n.activations[-2]), True), np.array(nth_deltas[0]).T*np.array(n.weights[-1]).T)
ValueError: operands could not be broadcast together with shapes (5,) (5,15) 
>>> np.dot(tanh(np.array(n.activations[-2]), True).T, np.array(nth_deltas[0]).T*np.array(n.weights[-1]).T)
Traceback (most recent call last):
  File "<pyshell#274>", line 1, in <module>
    np.dot(tanh(np.array(n.activations[-2]), True).T, np.array(nth_deltas[0]).T*np.array(n.weights[-1]).T)
ValueError: operands could not be broadcast together with shapes (5,) (5,15) 
>>> np.dot(tanh(np.array(n.activations[-2]), True).T, np.array(nth_deltas[0])*np.array(n.weights[-1]).T)
Traceback (most recent call last):
  File "<pyshell#275>", line 1, in <module>
    np.dot(tanh(np.array(n.activations[-2]), True).T, np.array(nth_deltas[0])*np.array(n.weights[-1]).T)
ValueError: operands could not be broadcast together with shapes (5,) (5,15) 
>>> np.dot(tanh(np.array(n.activations[-2]), True), np.array(nth_deltas[0])*np.array(n.weights[-1]).T)
Traceback (most recent call last):
  File "<pyshell#276>", line 1, in <module>
    np.dot(tanh(np.array(n.activations[-2]), True), np.array(nth_deltas[0])*np.array(n.weights[-1]).T)
ValueError: operands could not be broadcast together with shapes (5,) (5,15) 
>>> np.dot(tanh(np.array(n.activations[-2]), True), np.array(nth_deltas[0])*np.array(n.weights[-1]))
array([-2.16498700e-11, -8.94585374e-10, -2.37337732e-10, -1.58690136e-10,
       -2.60873428e-11])
>>> np.dot(tanh(np.array(n.activations[-2]), True), np.array(nth_deltas[0]).T*np.array(n.weights[-1]).T)
Traceback (most recent call last):
  File "<pyshell#278>", line 1, in <module>
    np.dot(tanh(np.array(n.activations[-2]), True), np.array(nth_deltas[0]).T*np.array(n.weights[-1]).T)
ValueError: operands could not be broadcast together with shapes (5,) (5,15) 
>>> np.dot(tanh(np.array(n.activations[-2]), True).T, np.array(nth_deltas[0]).T*np.array(n.weights[-1]).T)
Traceback (most recent call last):
  File "<pyshell#279>", line 1, in <module>
    np.dot(tanh(np.array(n.activations[-2]), True).T, np.array(nth_deltas[0]).T*np.array(n.weights[-1]).T)
ValueError: operands could not be broadcast together with shapes (5,) (5,15) 
>>> np.dot(tanh(np.array(n.activations[-2]), True).T, np.array(nth_deltas[0]).T*np.array(n.weights[-1]).)
SyntaxError: invalid syntax
>>> np.dot(tanh(np.array(n.activations[-2]), True).T, np.array(nth_deltas[0]).T*np.array(n.weights[-1]))
array([-2.16498700e-11, -8.94585374e-10, -2.37337732e-10, -1.58690136e-10,
       -2.60873428e-11])
>>> np.array(nth_deltas[0]).T*np.array(n.weights[-1])
array([[-1.63698299e-08, -1.16422486e-06, -1.17114675e-06,
        -5.19301647e-07, -1.07942446e-07],
       [-1.64050365e-08, -1.77118975e-07, -8.22191080e-07,
        -2.87868240e-07, -2.44515644e-08],
       [-2.44351694e-08, -7.03287996e-07, -4.35625801e-08,
        -1.18109250e-06, -1.14154472e-07],
       [-6.33611466e-08, -1.01388521e-06, -4.91787709e-07,
        -5.25410130e-07, -9.69596949e-08],
       [-8.05439501e-08, -5.80676177e-08, -1.25535727e-06,
        -1.02780160e-06, -5.14807786e-08],
       [-5.00727849e-08, -2.72575950e-06, -3.47418104e-07,
        -8.26837316e-07, -3.74214085e-08],
       [-5.57876010e-08, -4.36495280e-06, -1.25722349e-06,
        -8.96913799e-07, -1.32084259e-08],
       [-6.87716705e-08, -2.20670326e-06, -7.36814410e-07,
        -1.01371784e-06, -7.22019999e-08],
       [-3.58904391e-08, -4.06066468e-06, -3.39503251e-07,
        -1.10564339e-06, -1.03156730e-07],
       [-8.58011690e-08, -2.79806747e-06, -1.05495247e-07,
        -6.46453390e-08, -5.89654452e-08],
       [-1.07185024e-08, -2.28847563e-06, -6.76795840e-08,
        -4.21217063e-07, -1.64547252e-08],
       [-9.04913529e-08, -3.45526374e-06, -9.69026157e-07,
        -3.96475133e-07, -9.88938672e-08],
       [-8.83116854e-08, -3.25656902e-06, -6.79440041e-07,
        -1.63102010e-07, -9.28891120e-08],
       [-7.06940201e-08, -2.03556970e-06, -1.24357142e-06,
        -8.54427525e-07, -1.20231962e-07],
       [-5.53908336e-08, -8.68412554e-08, -2.77638203e-07,
        -6.93665249e-07, -1.03525660e-07]])
>>> np.array(nth_deltas[0]).T*np.array(n.weights[-1]).T
Traceback (most recent call last):
  File "<pyshell#283>", line 1, in <module>
    np.array(nth_deltas[0]).T*np.array(n.weights[-1]).T
ValueError: operands could not be broadcast together with shapes (5,) (5,15) 
>>> np.array(nth_deltas[0]).*np.array(n.weights[-1]).T
SyntaxError: invalid syntax
>>> np.array(nth_deltas[0])*np.array(n.weights[-1]).T
Traceback (most recent call last):
  File "<pyshell#285>", line 1, in <module>
    np.array(nth_deltas[0])*np.array(n.weights[-1]).T
ValueError: operands could not be broadcast together with shapes (5,) (5,15) 
>>> np.array(n.weights[-1]).T*np.array(nth_deltas[0])*
SyntaxError: invalid syntax
>>> np.array(n.weights[-1]).T*np.array(nth_deltas[0])
Traceback (most recent call last):
  File "<pyshell#287>", line 1, in <module>
    np.array(n.weights[-1]).T*np.array(nth_deltas[0])
ValueError: operands could not be broadcast together with shapes (5,15) (5,) 
>>> np.array(n.weights[-1])*np.array(nth_deltas[0])
array([[-1.63698299e-08, -1.16422486e-06, -1.17114675e-06,
        -5.19301647e-07, -1.07942446e-07],
       [-1.64050365e-08, -1.77118975e-07, -8.22191080e-07,
        -2.87868240e-07, -2.44515644e-08],
       [-2.44351694e-08, -7.03287996e-07, -4.35625801e-08,
        -1.18109250e-06, -1.14154472e-07],
       [-6.33611466e-08, -1.01388521e-06, -4.91787709e-07,
        -5.25410130e-07, -9.69596949e-08],
       [-8.05439501e-08, -5.80676177e-08, -1.25535727e-06,
        -1.02780160e-06, -5.14807786e-08],
       [-5.00727849e-08, -2.72575950e-06, -3.47418104e-07,
        -8.26837316e-07, -3.74214085e-08],
       [-5.57876010e-08, -4.36495280e-06, -1.25722349e-06,
        -8.96913799e-07, -1.32084259e-08],
       [-6.87716705e-08, -2.20670326e-06, -7.36814410e-07,
        -1.01371784e-06, -7.22019999e-08],
       [-3.58904391e-08, -4.06066468e-06, -3.39503251e-07,
        -1.10564339e-06, -1.03156730e-07],
       [-8.58011690e-08, -2.79806747e-06, -1.05495247e-07,
        -6.46453390e-08, -5.89654452e-08],
       [-1.07185024e-08, -2.28847563e-06, -6.76795840e-08,
        -4.21217063e-07, -1.64547252e-08],
       [-9.04913529e-08, -3.45526374e-06, -9.69026157e-07,
        -3.96475133e-07, -9.88938672e-08],
       [-8.83116854e-08, -3.25656902e-06, -6.79440041e-07,
        -1.63102010e-07, -9.28891120e-08],
       [-7.06940201e-08, -2.03556970e-06, -1.24357142e-06,
        -8.54427525e-07, -1.20231962e-07],
       [-5.53908336e-08, -8.68412554e-08, -2.77638203e-07,
        -6.93665249e-07, -1.03525660e-07]])
>>> np.array(n.weights[-1])*np.array(nth_deltas[0]).T
array([[-1.63698299e-08, -1.16422486e-06, -1.17114675e-06,
        -5.19301647e-07, -1.07942446e-07],
       [-1.64050365e-08, -1.77118975e-07, -8.22191080e-07,
        -2.87868240e-07, -2.44515644e-08],
       [-2.44351694e-08, -7.03287996e-07, -4.35625801e-08,
        -1.18109250e-06, -1.14154472e-07],
       [-6.33611466e-08, -1.01388521e-06, -4.91787709e-07,
        -5.25410130e-07, -9.69596949e-08],
       [-8.05439501e-08, -5.80676177e-08, -1.25535727e-06,
        -1.02780160e-06, -5.14807786e-08],
       [-5.00727849e-08, -2.72575950e-06, -3.47418104e-07,
        -8.26837316e-07, -3.74214085e-08],
       [-5.57876010e-08, -4.36495280e-06, -1.25722349e-06,
        -8.96913799e-07, -1.32084259e-08],
       [-6.87716705e-08, -2.20670326e-06, -7.36814410e-07,
        -1.01371784e-06, -7.22019999e-08],
       [-3.58904391e-08, -4.06066468e-06, -3.39503251e-07,
        -1.10564339e-06, -1.03156730e-07],
       [-8.58011690e-08, -2.79806747e-06, -1.05495247e-07,
        -6.46453390e-08, -5.89654452e-08],
       [-1.07185024e-08, -2.28847563e-06, -6.76795840e-08,
        -4.21217063e-07, -1.64547252e-08],
       [-9.04913529e-08, -3.45526374e-06, -9.69026157e-07,
        -3.96475133e-07, -9.88938672e-08],
       [-8.83116854e-08, -3.25656902e-06, -6.79440041e-07,
        -1.63102010e-07, -9.28891120e-08],
       [-7.06940201e-08, -2.03556970e-06, -1.24357142e-06,
        -8.54427525e-07, -1.20231962e-07],
       [-5.53908336e-08, -8.68412554e-08, -2.77638203e-07,
        -6.93665249e-07, -1.03525660e-07]])
>>> np.dot(np.array(n.weights[-1]),np.array(nth_deltas[0]))
array([-2.97898554e-06, -1.32803490e-06, -2.06653272e-06, -2.19140389e-06,
       -2.47325121e-06, -3.98750911e-06, -6.58808612e-06, -4.09820918e-06,
       -5.64485850e-06, -3.11297468e-06, -2.80454551e-06, -5.01015025e-06,
       -4.28031186e-06, -4.32449463e-06, -1.21706120e-06])
>>> np.dot(np.array(nth_deltas[0]),np.array(n.weights[-1]))
Traceback (most recent call last):
  File "<pyshell#291>", line 1, in <module>
    np.dot(np.array(nth_deltas[0]),np.array(n.weights[-1]))
  File "<__array_function__ internals>", line 180, in dot
ValueError: shapes (5,) and (15,5) not aligned: 5 (dim 0) != 15 (dim 0)
>>> np.dot(tanh(np.array(n.activations[-2]), True).T, np.dot(np.array(n.weights[-1]),np.array(nth_deltas[0])))
-1.338350455524597e-09
>>> np.dot(tanh(np.array(n.activations[-2]), True), np.dot(np.array(n.weights[-1]),np.array(nth_deltas[0])))
-1.338350455524597e-09
>>> tanh(np.array(n.activations[-2]), True)
array([1.82211658e-05, 1.46958937e-07, 4.64123539e-06, 1.73166303e-07,
       1.15311100e-06, 5.10908025e-05, 4.88127955e-07, 6.04439325e-07,
       1.43218359e-05, 4.97837080e-07, 3.18902194e-08, 1.91785428e-04,
       1.65066675e-07, 1.75498273e-06, 8.20036348e-06])
>>> np.multiply(tanh(np.array(n.activations[-2]), True), np.dot(np.array(n.weights[-1]),np.array(nth_deltas[0])))
array([-5.42805895e-11, -1.95166597e-13, -9.59126480e-12, -3.79477309e-13,
       -2.85193317e-12, -2.03725040e-10, -3.21582900e-12, -2.47711879e-12,
       -8.08447372e-11, -1.54975422e-12, -8.94375714e-14, -9.60873812e-10,
       -7.06536849e-13, -7.58941340e-12, -9.98034423e-12])
>>> nth_deltas[1]
[-5.4280589473668915e-11, -1.951665970380317e-13, -9.591264798830876e-12, -3.7947730946954035e-13, -2.851933167452867e-12, -2.037250404543356e-10, -3.2158290003009987e-12, -2.4771187897173755e-12, -8.084473718016626e-11, -1.5497542239228704e-12, -8.94375714434935e-14, -9.608738124780448e-10, -7.065368486934506e-13, -7.589413403787206e-12, -9.980344227724266e-12]
>>> def ef(num):
	self = n
	targets =[0, 0, 0, 0, 0]
	t = time.time()
	for i in range(num):
		nth_deltas[0] = np.multiply(tanh(np.array(n.activations[-1]), True),
					    np.array(targets)-np.array(n.activations[-1]))
		# 은닉~입력 노드의 오차 함수
		for i in range(1, len(self.lengths) - 1):
			nth_deltas[i] = np.multiply(tanh(np.array(n.activations[-i-1]), True), np.dot(np.array(n.weights[-i]),np.array(nth_deltas[i-1])))
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
	print(time.time()-t)

	
>>> ef(100)
0.38578176498413086
>>> def ef(num):
	self = n
	targets =[0, 0, 0, 0, 0]
	t = time.time()
	for i in range(num):
		nth_deltas[0] = np.multiply(tanh(np.array(n.activations[-1]), True),
					    np.array(targets)-np.array(n.activations[-1]))
		# 은닉~입력 노드의 오차 함수
		for i in range(1, len(self.lengths) - 1):
			nth_deltas[i] = np.multiply(tanh(np.array(n.activations[-i-1]), True), np.dot(np.array(n.weights[-i]),np.array(nth_deltas[i-1])))
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
	print(time.time()-t)

	
>>> ef(100)
0.38423943519592285

>>> ef(100)
0.38779163360595703
>>> import torch
Traceback (most recent call last):
  File "<pyshell#304>", line 1, in <module>
    import torch
ModuleNotFoundError: No module named 'torch'
>>> import torch
>>> torch.matmul(np.array(n.weights[-1]),np.array(nth_deltas[0]))
Traceback (most recent call last):
  File "<pyshell#306>", line 1, in <module>
    torch.matmul(np.array(n.weights[-1]),np.array(nth_deltas[0]))
TypeError: matmul(): argument 'input' (position 1) must be Tensor, not numpy.ndarray
>>> torch.tensor(n.weights[-1])
tensor([[0.1770, 0.2624, 0.8912, 0.3879, 0.8373],
        [0.1774, 0.0398, 0.6257, 0.2150, 0.1897],
        [0.2642, 0.1585, 0.0331, 0.8823, 0.8855],
        [0.6851, 0.2285, 0.3742, 0.3925, 0.7521],
        [0.8709, 0.0130, 0.9553, 0.7678, 0.3993],
        [0.5414, 0.6145, 0.2643, 0.6177, 0.2903],
        [0.6032, 0.9842, 0.9567, 0.6700, 0.1025],
        [0.7436, 0.4975, 0.5607, 0.7573, 0.5601],
        [0.3881, 0.9156, 0.2583, 0.8260, 0.8002],
        [0.9278, 0.6308, 0.0802, 0.0483, 0.4574],
        [0.1159, 0.5159, 0.0515, 0.3146, 0.1276],
        [0.9785, 0.7790, 0.7374, 0.2962, 0.7671],
        [0.9549, 0.7342, 0.5170, 0.1218, 0.7205],
        [0.7644, 0.4589, 0.9463, 0.6383, 0.9326],
        [0.5989, 0.0194, 0.2112, 0.5182, 0.8030]], dtype=torch.float64)
>>> torch.tensor(n.weights[-1])
tensor([[0.1770, 0.2624, 0.8912, 0.3879, 0.8373],
        [0.1774, 0.0398, 0.6257, 0.2150, 0.1897],
        [0.2642, 0.1585, 0.0331, 0.8823, 0.8855],
        [0.6851, 0.2285, 0.3742, 0.3925, 0.7521],
        [0.8709, 0.0130, 0.9553, 0.7678, 0.3993],
        [0.5414, 0.6145, 0.2643, 0.6177, 0.2903],
        [0.6032, 0.9842, 0.9567, 0.6700, 0.1025],
        [0.7436, 0.4975, 0.5607, 0.7573, 0.5601],
        [0.3881, 0.9156, 0.2583, 0.8260, 0.8002],
        [0.9278, 0.6308, 0.0802, 0.0483, 0.4574],
        [0.1159, 0.5159, 0.0515, 0.3146, 0.1276],
        [0.9785, 0.7790, 0.7374, 0.2962, 0.7671],
        [0.9549, 0.7342, 0.5170, 0.1218, 0.7205],
        [0.7644, 0.4589, 0.9463, 0.6383, 0.9326],
        [0.5989, 0.0194, 0.2112, 0.5182, 0.8030]], dtype=torch.float64)
>>> torch.set_printoptions(precision=10)
>>> torch.tensor(n.weights[-1])
tensor([[0.1770019226, 0.2624018958, 0.8912089171, 0.3879250856, 0.8372991263],
        [0.1773826068, 0.0398076306, 0.6256519635, 0.2150234237, 0.1896654311],
        [0.2642113185, 0.1584597504, 0.0331119125, 0.8823426374, 0.8854854365],
        [0.6851125038, 0.2285000142, 0.3742134014, 0.3924886736, 0.7521065928],
        [0.8709077713, 0.0129613222, 0.9552935242, 0.7678204810, 0.3993294031],
        [0.5414272945, 0.6145309413, 0.2643474356, 0.6176820112, 0.2902717235],
        [0.6032208075, 0.9841721581, 0.9567137319, 0.6700354733, 0.1024530895],
        [0.7436157477, 0.4974827636, 0.5606799048, 0.7572986442, 0.5600626572],
        [0.3880755588, 0.9155546082, 0.2583241936, 0.8259753348, 0.8001766138],
        [0.9277533498, 0.6308365247, 0.0802429713, 0.0482557521, 0.4573875072],
        [0.1158949037, 0.5159225907, 0.0514650689, 0.3146470406, 0.1276344356],
        [0.9784676566, 0.7790355517, 0.7373941701, 0.2961625877, 0.7671098501],
        [0.9548992149, 0.7342294980, 0.5170177327, 0.1218117790, 0.7205313282],
        [0.7644018466, 0.4588918207, 0.9463244402, 0.6382943885, 0.9326281504],
        [0.5989306164, 0.0194498330, 0.2112445930, 0.5181904469, 0.8030383818]],
       dtype=torch.float64)
>>> torch.matmul(torch.tensor(n.weights[-1]),torch.tensor(nth_deltas[0]))
tensor([-2.9782892830e-06, -1.3273386314e-06, -2.0658364597e-06,
        -2.1907076216e-06, -2.4725549443e-06, -3.9868128658e-06,
        -6.5873898512e-06, -4.0975129136e-06, -5.6441622358e-06,
        -3.1122784113e-06, -2.8038492438e-06, -5.0094540573e-06,
        -4.2796155993e-06, -4.3237983690e-06, -1.2163649401e-06],
       dtype=torch.float64)
>>> def ef(num):
	self = n
	targets =[0, 0, 0, 0, 0]
	t = time.time()
	for i in range(num):
		nth_deltas[0] = np.multiply(tanh(np.array(n.activations[-1]), True),
					    np.array(targets)-np.array(n.activations[-1]))
		# 은닉~입력 노드의 오차 함수
		for i in range(1, len(self.lengths) - 1):
			nth_deltas[i] = torch.multiply(tanh(torch.tensor(n.activations[-i-1]), True), torch.matmul(torch.tensor(n.weights[-1]),torch.tensor(nth_deltas[0])))
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
	print(time.time()-t)

	
>>> torch.multiply(tanh(torch.tensor(n.activations[-2]), True), torch.matmul(torch.tensor(n.weights[-1]),torch.tensor(nth_deltas[0])))
tensor([-5.4267902841e-11, -1.9506427478e-13, -9.5880332796e-12,
        -3.7935673996e-13, -2.8511302978e-12, -2.0368946866e-10,
        -3.2154891343e-12, -2.4766979403e-12, -8.0834765468e-11,
        -1.5494075978e-12, -8.9415367421e-14, -9.6074029193e-10,
        -7.0642191866e-13, -7.5881914730e-12, -9.9746346305e-12],
       dtype=torch.float64)
>>> list(torch.multiply(tanh(torch.tensor(n.activations[-2]), True), torch.matmul(torch.tensor(n.weights[-1]),torch.tensor(nth_deltas[0]))))
[tensor(-5.4267902841e-11, dtype=torch.float64), tensor(-1.9506427478e-13, dtype=torch.float64), tensor(-9.5880332796e-12, dtype=torch.float64), tensor(-3.7935673996e-13, dtype=torch.float64), tensor(-2.8511302978e-12, dtype=torch.float64), tensor(-2.0368946866e-10, dtype=torch.float64), tensor(-3.2154891343e-12, dtype=torch.float64), tensor(-2.4766979403e-12, dtype=torch.float64), tensor(-8.0834765468e-11, dtype=torch.float64), tensor(-1.5494075978e-12, dtype=torch.float64), tensor(-8.9415367421e-14, dtype=torch.float64), tensor(-9.6074029193e-10, dtype=torch.float64), tensor(-7.0642191866e-13, dtype=torch.float64), tensor(-7.5881914730e-12, dtype=torch.float64), tensor(-9.9746346305e-12, dtype=torch.float64)]
>>> np.array(torch.multiply(tanh(torch.tensor(n.activations[-2]), True), torch.matmul(torch.tensor(n.weights[-1]),torch.tensor(nth_deltas[0]))))
array([-5.42679028e-11, -1.95064275e-13, -9.58803328e-12, -3.79356740e-13,
       -2.85113030e-12, -2.03689469e-10, -3.21548913e-12, -2.47669794e-12,
       -8.08347655e-11, -1.54940760e-12, -8.94153674e-14, -9.60740292e-10,
       -7.06421919e-13, -7.58819147e-12, -9.97463463e-12])
>>> def ef(num):
	self = n
	targets =[0, 0, 0, 0, 0]
	t = time.time()
	for i in range(num):
		nth_deltas[0] = np.multiply(tanh(np.array(n.activations[-1]), True),
					    np.array(targets)-np.array(n.activations[-1]))
		# 은닉~입력 노드의 오차 함수
		for i in range(1, len(self.lengths) - 1):
			nth_deltas[i] = list(np.array(torch.multiply(tanh(torch.tensor(n.activations[-i-1]), True), torch.matmul(torch.tensor(n.weights[-1]),torch.tensor(nth_deltas[0])))))
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
	print(time.time()-t)

	
>>> ef(100)
Traceback (most recent call last):
  File "<pyshell#319>", line 1, in <module>
    ef(100)
  File "<pyshell#318>", line 10, in ef
    nth_deltas[i] = list(np.array(torch.multiply(tanh(torch.tensor(n.activations[-i-1]), True), torch.matmul(torch.tensor(n.weights[-1]),torch.tensor(nth_deltas[0])))))
RuntimeError: The size of tensor a (25) must match the size of tensor b (15) at non-singleton dimension 0
>>> def ef(num):
	self = n
	targets =[0, 0, 0, 0, 0]
	t = time.time()
	for i in range(num):
		nth_deltas[0] = np.multiply(tanh(np.array(n.activations[-1]), True),
					    np.array(targets)-np.array(n.activations[-1]))
		# 은닉~입력 노드의 오차 함수
		for i in range(1, len(self.lengths) - 1):
			nth_deltas[i] = list(np.array(torch.multiply(tanh(torch.tensor(n.activations[-i-1]), True), torch.matmul(torch.tensor(n.weights[-i]),torch.tensor(nth_deltas[i-1])))))
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
	print(time.time()-t)

	
>>> ef(100)
0.4047706127166748
>>> def ed(num):
	t = time.time()
	for i in range(num):
		torch.matmul(torch.tensor(np.random.uniform(-1, 1, size=(600, 600))), torch.tensor(np.random.uniform(-1, 1, size=(600, 600))))
	print(time.time()-t)

	
>>> ed(100)
1.6641514301300049

>>> def ed(num):
	t = time.time()
	a = np.random.uniform(-1, 1, size=(600, 600))
	for i in range(num):
		torch.matmul(torch.tensor(a), torch.tensor(a))
	print(time.time()-t)

	
>>> ed(100)
0.7075867652893066
>>> def er(num):
	t = time.time()
	a = np.random.uniform(-1, 1, size=(600, 600))
	for i in range(num):
		np.dot(a, a)
	print(time.time()-t)

	
>>> er(100)
0.4692869186401367
>>> def er(num):
	t = time.time()
	a = np.random.uniform(-1, 1, size=(600, 600))
	for i in range(num):
		np.dot(a, a)
	print(time.time()-t)

	
>>> er(10000)
54.770140647888184
>>> er(1000)
6.841102123260498
>>> ed(1000)
7.475739240646362
>>> torch.random
<module 'torch.random' from 'C:\\Users\\KCDC\\AppData\\Local\\Programs\\Python\\Python39\\lib\\site-packages\\torch\\random.py'>
>>> torch.random.uniform
Traceback (most recent call last):
  File "<pyshell#348>", line 1, in <module>
    torch.random.uniform
AttributeError: module 'torch.random' has no attribute 'uniform'
>>> torch.random.random()
Traceback (most recent call last):
  File "<pyshell#349>", line 1, in <module>
    torch.random.random()
AttributeError: module 'torch.random' has no attribute 'random'
>>> torch.rand()
Traceback (most recent call last):
  File "<pyshell#350>", line 1, in <module>
    torch.rand()
TypeError: rand() received an invalid combination of arguments - got (), but expected one of:
 * (tuple of ints size, *, torch.Generator generator, tuple of names names, torch.dtype dtype, torch.layout layout, torch.device device, bool pin_memory, bool requires_grad)
 * (tuple of ints size, *, torch.Generator generator, Tensor out, torch.dtype dtype, torch.layout layout, torch.device device, bool pin_memory, bool requires_grad)
 * (tuple of ints size, *, Tensor out, torch.dtype dtype, torch.layout layout, torch.device device, bool pin_memory, bool requires_grad)
 * (tuple of ints size, *, tuple of names names, torch.dtype dtype, torch.layout layout, torch.device device, bool pin_memory, bool requires_grad)

>>> torch.rand((100, 100))
tensor([[0.1693654060, 0.3480637670, 0.7817887068,  ..., 0.3384737372,
         0.0296691060, 0.3547458053],
        [0.8648625016, 0.4058845639, 0.2330527902,  ..., 0.2166437507,
         0.1316046715, 0.9615384936],
        [0.1383000016, 0.6112459898, 0.2756816149,  ..., 0.6023052931,
         0.3214700818, 0.5540673733],
        ...,
        [0.7917701602, 0.0061221719, 0.3630200028,  ..., 0.2380336523,
         0.0228750110, 0.4220497608],
        [0.4298754334, 0.5508138537, 0.5556947589,  ..., 0.6033605337,
         0.0025421381, 0.7511394024],
        [0.6787140965, 0.1969000697, 0.4249258637,  ..., 0.4185799956,
         0.9607723355, 0.5776180625]])
>>> def ed(num):
	t = time.time()
	a = torch.rand(600, 600)
	for i in range(num):
		torch.matmul(a, a)
	print(time.time()-t)

	
>>> ed(100)
0.22877788543701172
>>> ed(1000)
1.7440059185028076
>>> 