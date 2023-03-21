Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.

================ RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ===============
Done!
Epoch 1

Test Error: 
 Accuracy: 52.0%, Avg loss: 1.265673 

1.3325974941253662
Epoch 31

Test Error: 
 Accuracy: 80.2%, Avg loss: 0.532267 

0.5499602556228638
Epoch 61

Test Error: 
 Accuracy: 81.1%, Avg loss: 0.521206 

0.3929717540740967
Epoch 91

Test Error: 
 Accuracy: 81.0%, Avg loss: 0.522485 

0.522723913192749
34.17606449127197
real_test: 0.8342727272727273
model_fin.train
<bound method Module.train of NeuralNetwork(
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
model_fin.train(ted.dataset[0])
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    model_fin.train(ted.dataset[0])
NameError: name 'ted' is not defined
model_fin.train(model_fin.ted.dataset[0])
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    model_fin.train(model_fin.ted.dataset[0])
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1908, in train
    raise ValueError("training mode is expected to be boolean")
ValueError: training mode is expected to be boolean
model_fin.train()
NeuralNetwork(
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
)
model_fin.train(True)
NeuralNetwork(
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
)
train_loop(model_fin.ted.dataset[0], model_fin, loss_fn, optimizer)
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    train_loop(model_fin.ted.dataset[0], model_fin, loss_fn, optimizer)
  File "C:\Users\KDCA\Desktop\IL\base\temp2.py", line 92, in train_loop
    size = len(dataloader.dataset)
AttributeError: 'tuple' object has no attribute 'dataset'
train_loop(model_fin.trd.dataset[0], model_fin, loss_fn, optimizer)
Traceback (most recent call last):
  File "<pyshell#6>", line 1, in <module>
    train_loop(model_fin.trd.dataset[0], model_fin, loss_fn, optimizer)
  File "C:\Users\KDCA\Desktop\IL\base\temp2.py", line 92, in train_loop
    size = len(dataloader.dataset)
AttributeError: 'tuple' object has no attribute 'dataset'
model_fin.trd
<torch.utils.data.dataloader.DataLoader object at 0x000002204E6198A0>
model_fin.trd.dataset
Traceback (most recent call last):
  File "<pyshell#8>", line 1, in <module>
    model_fin.trd.dataset
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\idlelib\rpc.py", line 620, in displayhook
    text = repr(value)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\_tensor.py", line 427, in __repr__
    return torch._tensor_str._str(self, tensor_contents=tensor_contents)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\_tensor_str.py", line 637, in _str
    return _str_intern(self, tensor_contents=tensor_contents)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\_tensor_str.py", line 568, in _str_intern
    tensor_str = _tensor_str(self, indent)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\_tensor_str.py", line 328, in _tensor_str
    formatter = _Formatter(get_summarized_data(self) if summarize else self)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\_tensor_str.py", line 158, in __init__
    for value in nonzero_finite_vals:
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\_tensor.py", line 926, in __iter__
    return iter(self.unbind(0))
KeyboardInterrupt
model_fin.trd.dataset[0]

train_loop(model_fin.trd, model_fin, loss_fn, optimizer)
[0.4979112148284912]
train_loop(model_fin.trd, model_fin, loss_fn, optimizer)
[0.43562349677085876]
train_loop(model_fin.trd, model_fin, loss_fn, optimizer)
[0.4558136761188507]
train_loop(model_fin.trd, model_fin, loss_fn, optimizer)
[0.42758601903915405]
train_loop(model_fin.trd, model_fin, loss_fn, optimizer)
[0.4411815404891968]
train_loop(model_fin.trd, model_fin, loss_fn, optimizer)
[0.5050907731056213]
train_loop(model_fin.trd, model_fin, loss_fn, optimizer)
[0.4751107096672058]
train_loop(DataLoader(model_fin.trd.dataset[0]), model_fin, loss_fn, optimizer)
Traceback (most recent call last):
  File "<pyshell#17>", line 1, in <module>
    train_loop(DataLoader(model_fin.trd.dataset[0]), model_fin, loss_fn, optimizer)
  File "C:\Users\KDCA\Desktop\IL\base\temp2.py", line 93, in train_loop
    for batch, (X, y) in enumerate(dataloader):
ValueError: not enough values to unpack (expected 2, got 1)
train_loop(DataLoader(model_fin.trd.dataset[0:2]), model_fin, loss_fn, optimizer)
[]
train_loop(DataLoader(model_fin.trd.dataset[0:50]), model_fin, loss_fn, optimizer)
[]
train_loop(DataLoader(model_fin.trd.dataset[0:]), model_fin, loss_fn, optimizer)
[0.00012087091454304755, 2.90866428258596e-05, 8.761498611420393e-05, 0.03530846908688545, 1.9993438720703125, 0.0011978124966844916, 0.003920251969248056, 2.249911308288574, 0.004780885763466358, 0.10232743620872498, 0.09408842772245407, 0.007048503030091524, 0.0034261594992130995, 0.13022169470787048, 4.154986381530762, 0.01660432666540146, 0.0005141366855241358, 1.7917594909667969, 0.0003051292151212692, 0.0003090619284193963, 0.0008023141999728978, 0.016308236867189407, 0.13375066220760345, 0.005657731089740992, 0.07391440123319626, 0.017603352665901184, 0.56789630651474, 0.0007665794692002237, 2.777537883957848e-05, 0.0625554621219635, 0.0021206289529800415, 0.3342479467391968, 0.00012230125139467418, 2.3189687728881836, 0.47257858514785767, 0.0752323791384697, 0.020705386996269226, 0.04057072848081589, 0.05535399168729782, 1.7917594909667969, 2.3019487857818604, 0.0008168459753505886, 2.95544695854187, 0.00031192204914987087, 1.7917594909667969, 0.10148768872022629, 0.0004477690381463617, 1.7917594909667969, 0.002202943665906787, 0.16147485375404358, 1.7917594909667969, 0.0002112165529979393, 0.0537957139313221, 0.001023364719003439, 0.00022313489171210676, 0.00016616393986623734, 0.014254885725677013, 0.0006709231529384851, 0.043738801032304764, 1.7917594909667969, 0.04356728494167328, 2.729921579360962, 0.016028951853513718, 2.7894584491150454e-05, 4.446407547220588e-05, 0.00016735584358684719, 4.303362584323622e-05, 0.0024188091047108173, 1.7917594909667969, 2.446315050125122, 0.0013465156080201268, 2.308169364929199, 0.026382071897387505, 1.8489303588867188, 5.757642793469131e-05, 0.08726784586906433, 0.0874188095331192, 2.1849706172943115, 0.0036334467586129904, 0.38906630873680115, 0.0012048374628648162, 3.298312187194824, 0.44610345363616943, 0.014540422707796097, 0.007275041658431292, 1.7917594909667969, 8.976056415122002e-05, 1.7917594909667969, 0.0045209103263914585, 2.1457441107486375e-05, 0.15690772235393524, 0.5209257006645203, 0.07270365208387375, 2.788149833679199, 1.7917594909667969, 0.7017014026641846, 3.957670196541585e-05, 1.7917594909667969, 1.7917594909667969, 0.09604296088218689, 0.004659153055399656, 0.022891780361533165, 2.291400909423828, 0.0003305127320345491, 1.7917594909667969, 0.08522260934114456, 0.00011932138295378536, 0.015000167302787304, 0.39916089177131653, 1.1673203706741333, 0.00024256148026324809, 0.003369727171957493, 0.05731348693370819, 0.0683562159538269, 0.4760964512825012, 6.01988795096986e-05, 0.1029406487941742, 0.005368815269321203, 0.2782782018184662, 1.7917594909667969, 1.9113408327102661, 0.0006032554083503783, 0.0016381428577005863, 0.0038294093683362007, 3.576214658096433e-05, 0.0007489498239010572, 0.4865171015262604, 0.020113088190555573, 0.00013159839727450162, 0.1389947533607483, 0.005569298751652241, 0.0003003622987307608, 0.00426217308267951, 0.00015984688070602715, 0.0956360250711441, 0.00027640812913887203, 1.7416396141052246, 0.0064018648117780685, 0.007191604934632778, 0.6429038047790527, 0.207660511136055, 0.0004076126788277179, 0.00018070495571009815, 0.6384696364402771, 0.445487916469574, 0.10371480137109756, 0.0031630981247872114, 0.012679790146648884, 0.0016473069554194808, 1.624092698097229, 0.0013765154872089624, 0.08000026643276215, 0.16718052327632904, 1.9341905117034912, 7.86750388215296e-05, 0.13808724284172058, 0.02175176702439785, 0.00025686301523819566, 0.0006500753224827349, 1.2338039875030518, 0.08739171922206879, 0.028920743614435196, 0.00010322991875000298, 1.9307725429534912, 0.00019047829846385866, 0.0001774868869688362, 0.3834928274154663, 0.02090328559279442, 0.0009459549910388887, 0.011123784817755222, 0.00014578233822248876, 1.3761194944381714, 0.001029080944135785, 0.016247717663645744, 0.05067751929163933, 0.000433112756581977, 2.0652902126312256, 0.00234352913685143, 0.0004737447015941143, 0.24591711163520813, 2.4716618061065674, 3.8265450712060556e-05, 2.477053165435791, 0.32897162437438965, 0.00025018901214934886, 0.00028606137493625283, 0.13670164346694946, 0.0636976808309555, 0.00013422065239865333]

train_loop(DataLoader(model_fin.trd.dataset[0:]), model_fin, loss_fn, optimizer)

train_loop(DataLoader(model_fin.trd), model_fin, loss_fn, optimizer)
Traceback (most recent call last):
  File "<pyshell#22>", line 1, in <module>
    train_loop(DataLoader(model_fin.trd), model_fin, loss_fn, optimizer)
  File "C:\Users\KDCA\Desktop\IL\base\temp2.py", line 93, in train_loop
    for batch, (X, y) in enumerate(dataloader):
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\utils\data\dataloader.py", line 628, in __next__
    data = self._next_data()
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\utils\data\dataloader.py", line 671, in _next_data
    data = self._dataset_fetcher.fetch(index)  # may raise StopIteration
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\utils\data\_utils\fetch.py", line 58, in fetch
    data = [self.dataset[idx] for idx in possibly_batched_index]
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\utils\data\_utils\fetch.py", line 58, in <listcomp>
    data = [self.dataset[idx] for idx in possibly_batched_index]
TypeError: 'DataLoader' object is not subscriptable
train_loop(DataLoader(model_fin.trd.dataset), model_fin, loss_fn, optimizer)
Traceback (most recent call last):
  File "<pyshell#23>", line 1, in <module>
    train_loop(DataLoader(model_fin.trd.dataset), model_fin, loss_fn, optimizer)
  File "C:\Users\KDCA\Desktop\IL\base\temp2.py", line 100, in train_loop
    loss.backward()
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\_tensor.py", line 488, in backward
    torch.autograd.backward(
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\autograd\__init__.py", line 197, in backward
    Variable._execution_engine.run_backward(  # Calls into the C++ engine to run the backward pass
KeyboardInterrupt
train_loop(DataLoader(model_fin.trd.dataset), model_fin, loss_fn, optimizer)
Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    train_loop(DataLoader(model_fin.trd.dataset), model_fin, loss_fn, optimizer)
  File "C:\Users\KDCA\Desktop\IL\base\temp2.py", line 100, in train_loop
    loss.backward()
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\_tensor.py", line 488, in backward
    torch.autograd.backward(
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\autograd\__init__.py", line 197, in backward
    Variable._execution_engine.run_backward(  # Calls into the C++ engine to run the backward pass
KeyboardInterrupt
type(model_fin.trd)
<class 'torch.utils.data.dataloader.DataLoader'>
type(model_fin.trd.dataset)
<class 'list'>
type(DataLoader(model_fin.trd.dataset))
<class 'torch.utils.data.dataloader.DataLoader'>
len(DataLoader(model_fin.trd.dataset).dataset))
  
SyntaxError: unmatched ')'
len(DataLoader(model_fin.trd.dataset).dataset)
  
18956
len(model_fin.trd.dataset)
  
18956
DataLoader(model_fin.trd.dataset).dataset[0]
  
(tensor([[0.0000e+00, 1.0000e+00, 1.0000e+00, 2.0000e+00, 2.0000e+00, 2.0000e+00,
         0.0000e+00, 1.0000e+00, 0.0000e+00, 0.0000e+00, 8.7360e-01, 8.7360e-01,
         1.0000e-04, 3.5800e-02, 3.5800e-02, 0.0000e+00, 8.0510e-01, 8.0510e-01,
         9.0000e-04, 4.6920e-01, 4.6920e-01, 0.0000e+00, 2.0990e-01, 2.0990e-01,
         0.0000e+00, 2.8000e-03, 2.8000e-03, 1.2000e-03, 4.7670e-01, 4.7670e-01,
         6.3000e-02, 4.9310e+00, 4.9310e+00, 4.0000e-04, 4.3089e+00, 4.3089e+00,
         0.0000e+00, 1.7486e+00, 1.7486e+00, 1.0000e-08, 8.0680e-05, 8.0680e-05,
         3.0000e-08, 9.0800e-06, 9.0800e-06, 3.0000e-08, 9.0800e-06, 9.0800e-06,
         0.0000e+00, 2.9050e-05, 2.9050e-05, 1.0000e+00, 0.0000e+00, 0.0000e+00,
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
         1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00]]), tensor(3))
model_fin.trd.dataset[0]
  
(tensor([[0.0000e+00, 1.0000e+00, 1.0000e+00, 2.0000e+00, 2.0000e+00, 2.0000e+00,
         0.0000e+00, 1.0000e+00, 0.0000e+00, 0.0000e+00, 8.7360e-01, 8.7360e-01,
         1.0000e-04, 3.5800e-02, 3.5800e-02, 0.0000e+00, 8.0510e-01, 8.0510e-01,
         9.0000e-04, 4.6920e-01, 4.6920e-01, 0.0000e+00, 2.0990e-01, 2.0990e-01,
         0.0000e+00, 2.8000e-03, 2.8000e-03, 1.2000e-03, 4.7670e-01, 4.7670e-01,
         6.3000e-02, 4.9310e+00, 4.9310e+00, 4.0000e-04, 4.3089e+00, 4.3089e+00,
         0.0000e+00, 1.7486e+00, 1.7486e+00, 1.0000e-08, 8.0680e-05, 8.0680e-05,
         3.0000e-08, 9.0800e-06, 9.0800e-06, 3.0000e-08, 9.0800e-06, 9.0800e-06,
         0.0000e+00, 2.9050e-05, 2.9050e-05, 1.0000e+00, 0.0000e+00, 0.0000e+00,
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
         1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00]]), tensor(3))
DataLoader(model_fin.trd.dataset).dataset[0]
  

train_loop(DataLoader(model_fin.trd.dataset, batch_size=100), model_fin, loss_fn, optimizer)
  
[0.2777791917324066]
train_loop(DataLoader(model_fin.trd.dataset[0:100]), model_fin, loss_fn, optimizer)
  
[]
train_loop(DataLoader(model_fin.trd.dataset[0:120]), model_fin, loss_fn, optimizer)
  
[0.002621073741465807]
train_loop(DataLoader(model_fin.trd.dataset[0:101]), model_fin, loss_fn, optimizer)
  
[1.7917594909667969]
def train_loop(dataloader, model, loss_fn, optimizer):
    losses_list = []
    size = len(dataloader.dataset)
    for batch, (X, y) in enumerate(dataloader):
        # 예측(prediction)과 손실(loss) 계산
        pred = model.forward(X)
        loss = loss_fn(pred, y)

        # 역전파
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        if batch % 1 == 0 and batch != 0:
            loss, current = loss.item(), batch * len(X)
            '''print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")'''
            losses_list.append(loss)
    return losses_list

train_loop(DataLoader(model_fin.trd.dataset[0:1]), model_fin, loss_fn, optimizer)
[]
train_loop(DataLoader(model_fin.trd.dataset[0:2]), model_fin, loss_fn, optimizer)
[2.1288321018218994]
def train_loop(dataloader, model, loss_fn, optimizer):
    losses_list = []
    size = len(dataloader.dataset)
    for batch, (X, y) in enumerate(dataloader):
        # 예측(prediction)과 손실(loss) 계산
        pred = model.forward(X)
        loss = loss_fn(pred, y)

        # 역전파
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if batch != 0:
            loss, current = loss.item(), batch * len(X)
            '''print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")'''
            losses_list.append(loss)
    return losses_list

train_loop(DataLoader(model_fin.trd.dataset[0:1]), model_fin, loss_fn, optimizer)
[]
def train_loop(dataloader, model, loss_fn, optimizer):
    losses_list = []
    size = len(dataloader.dataset)
    for batch, (X, y) in enumerate(dataloader):
        # 예측(prediction)과 손실(loss) 계산
        pred = model.forward(X)
        loss = loss_fn(pred, y)

        # 역전파
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if batch == 0:
            loss, current = loss.item(), batch * len(X)
            '''print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")'''
            losses_list.append(loss)
    return losses_list

train_loop(DataLoader(model_fin.trd.dataset[0:1]), model_fin, loss_fn, optimizer)
[1.9694790840148926]
train_loop(DataLoader(model_fin.trd.dataset[0]), model_fin, loss_fn, optimizer)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    train_loop(DataLoader(model_fin.trd.dataset[0]), model_fin, loss_fn, optimizer)
  File "<pyshell#47>", line 4, in train_loop
    for batch, (X, y) in enumerate(dataloader):
ValueError: not enough values to unpack (expected 2, got 1)
train_loop(DataLoader(model_fin.trd.dataset[0:]), model_fin, loss_fn, optimizer)
Traceback (most recent call last):
  File "<pyshell#50>", line 1, in <module>
    train_loop(DataLoader(model_fin.trd.dataset[0:]), model_fin, loss_fn, optimizer)
  File "<pyshell#47>", line 11, in train_loop
    loss.backward()
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\_tensor.py", line 488, in backward
    torch.autograd.backward(
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\autograd\__init__.py", line 197, in backward
    Variable._execution_engine.run_backward(  # Calls into the C++ engine to run the backward pass
KeyboardInterrupt
train_loop(DataLoader(model_fin.trd.dataset[0]), model_fin, loss_fn, optimizer)
Traceback (most recent call last):
  File "<pyshell#51>", line 1, in <module>
    train_loop(DataLoader(model_fin.trd.dataset[0]), model_fin, loss_fn, optimizer)
  File "<pyshell#47>", line 4, in train_loop
    for batch, (X, y) in enumerate(dataloader):
ValueError: not enough values to unpack (expected 2, got 1)
model_fin.trd.dataset[0:1]
[(tensor([[0.0000e+00, 1.0000e+00, 1.0000e+00, 2.0000e+00, 2.0000e+00, 2.0000e+00,
         0.0000e+00, 1.0000e+00, 0.0000e+00, 0.0000e+00, 8.7360e-01, 8.7360e-01,
         1.0000e-04, 3.5800e-02, 3.5800e-02, 0.0000e+00, 8.0510e-01, 8.0510e-01,
         9.0000e-04, 4.6920e-01, 4.6920e-01, 0.0000e+00, 2.0990e-01, 2.0990e-01,
         0.0000e+00, 2.8000e-03, 2.8000e-03, 1.2000e-03, 4.7670e-01, 4.7670e-01,
         6.3000e-02, 4.9310e+00, 4.9310e+00, 4.0000e-04, 4.3089e+00, 4.3089e+00,
         0.0000e+00, 1.7486e+00, 1.7486e+00, 1.0000e-08, 8.0680e-05, 8.0680e-05,
         3.0000e-08, 9.0800e-06, 9.0800e-06, 3.0000e-08, 9.0800e-06, 9.0800e-06,
         0.0000e+00, 2.9050e-05, 2.9050e-05, 1.0000e+00, 0.0000e+00, 0.0000e+00,
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
         1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00]]), tensor(3))]
train_loop(DataLoader(model_fin.trd.dataset[0:1]), model_fin, loss_fn, optimizer)
[1.9987361431121826]
def train_loop(dataloader, model, loss_fn, optimizer):
    losses_list = []
    size = len(dataloader.dataset)
    for batch, (X, y) in enumerate(dataloader):
        # 예측(prediction)과 손실(loss) 계산
        pred = model.forward(X)
        loss = loss_fn(pred, y)

        # 역전파
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        if batch % 10 == 0 and batch != 0:
            loss, current = loss.item(), batch * len(X)
            '''print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")'''
            losses_list.append(loss)
    return losses_list


train_loop(DataLoader(model_fin.trd.dataset[0:15]), model_fin, loss_fn, optimizer)
[0.20367658138275146]
train_loop(DataLoader(model_fin.trd.dataset[150:170]), model_fin, loss_fn, optimizer)
[0.556979775428772]
train_loop(DataLoader(model_fin.trd.dataset[130:170]), model_fin, loss_fn, optimizer)
[1.9325554370880127, 0.16649052500724792, 1.9803632497787476]
train_loop(DataLoader(model_fin.trd.dataset[100:170]), model_fin, loss_fn, optimizer)
[0.0003302744007669389, 2.897210121154785, 0.0003719830128829926, 1.9389021396636963, 0.17874199151992798, 1.8178038597106934]
set1[9]
[2, 5, 5, 0, 0, 5, 5, 5, 0, 5, 0]
set2[9]
[2, 5, 5, 0, 0, 5, 5, 0, 0, 5, 0]
set1[11]
[0, 3, 3, 0, 0, 0, 3, 3, 5, 5, 2]
set2[11]
[0, 2, 2, 0, 0, 0, 0, 2, 5, 5, 0]
set1[10]
[5, 2, 5, 2, 5, 0, 5, 0, 0, 0, 0]
set2[10]
[5, 2, 5, 2, 5, 0, 0, 0, 0, 0, 2]
set1[12]
[2, 2, 1, 1, 3, 0, 0, 0, 3, 2, 1]
set2[12]
[2, 2, 0, 0, 0, 0, 0, 2, 1, 1, 2]
set1[13]
[1, 3, 3, 2, 1, 1, 0, 0, 0, 0, 3]
set2[13]
[1, 1, 2, 2, 2, 1, 1, 0, 0, 1, 0]
set1[14]
[5, 5, 2, 5, 1, 5, 0, 2, 1, 1, 2]
set2[14]
[5, 5, 2, 5, 2, 5, 2, 2, 2, 1, 2]
1_s
SyntaxError: invalid decimal literal
s_1 = 0
s_3 = 0
a = [0,0,0,0]
a = [0,0,0,0,0,0]
for i in set1:
    for j in i:
        a[j] += 1

        
a
[2782, 488, 2616, 476, 0, 4638]
b = [0,0,0,0,0,0]
for i in set2:
    for j in i:
        a[j] += 1

        
b
[0, 0, 0, 0, 0, 0]
a=[2782, 488, 2616, 476, 0, 4638]
for i in set2:
    for j in i:
        b[j] += 1
a
SyntaxError: incomplete input
b
[0, 0, 0, 0, 0, 0]
for i in set2:
    for j in i:
        b[j] += 1

b
[3537, 488, 2781, 0, 0, 4194]

================ RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ===============
Done!
Epoch 1

Test Error: 
 Accuracy: 45.8%, Avg loss: 1.344511 

1.3846977949142456
Epoch 31

Test Error: 
 Accuracy: 79.5%, Avg loss: 0.567088 

0.6652083396911621
Epoch 61

Test Error: 
 Accuracy: 81.2%, Avg loss: 0.521070 

0.5277361869812012
Epoch 91

Test Error: 
 Accuracy: 80.8%, Avg loss: 0.523600 

0.5482639074325562
31.070286750793457
real_test: 0.8151818181818182
b = [0,0,0,0,0,0]
a = [0,0,0,0,0,0]
for i in set2:
    for j in i:
        b[j] += 1
a
SyntaxError: incomplete input
for i in set2:
    for j in i:
        b[j] += 1

for i in set1:
    for j in i:
        a[j] += 1

a
[2782, 488, 2616, 476, 0, 4638]
b
[3906, 0, 2914, 0, 0, 4180]
model_fin.roll(150, 30)
Epoch 1

Test Error: 
 Accuracy: 80.0%, Avg loss: 0.538462 

0.5746549963951111
Epoch 31

Test Error: 
 Accuracy: 79.4%, Avg loss: 0.540706 

0.5996428728103638
Epoch 61

Test Error: 
 Accuracy: 80.5%, Avg loss: 0.532875 

0.6182023286819458
Epoch 91

Test Error: 
 Accuracy: 80.4%, Avg loss: 0.532509 

0.5174999237060547
Epoch 121

Test Error: 
 Accuracy: 80.2%, Avg loss: 0.544289 

0.5297898650169373
48.270386695861816
set2 = [[torch.argmax(model_fin(li68[i*11+j][0])).item() for j in range(11)] for i in range(0, 1000)]


b = [0,0,0,0,0,0]
for i in set2:
    for j in i:
        b[j] += 1

b
[4129, 0, 2652, 0, 0, 4219]
model_fin = NeuralNetwork([len(li68[0][0][0]), 20, 150, 6])
model_fin.base_set(li68, call = False)
model_fin.roll(100, 30)
Epoch 1

Test Error: 
 Accuracy: 41.6%, Avg loss: 1.516891 

1.6718593835830688
Epoch 31

Test Error: 
 Accuracy: 79.1%, Avg loss: 0.590734 

0.5763957500457764
Epoch 61

Test Error: 
 Accuracy: 79.2%, Avg loss: 0.565504 

0.5957813262939453
Epoch 91

Test Error: 
 Accuracy: 80.1%, Avg loss: 0.556203 

0.545163094997406
37.556809425354004
set2 = [[torch.argmax(model_fin(li68[i*11+j][0])).item() for j in range(11)] for i in range(0, 1000)]
a = [0,0,0,0,0,0]
b = [0,0,0,0,0,0]
for i in set2:
    for j in i:
        b[j] += 1

b
[3875, 0, 2872, 0, 0, 4253]
def train_loop(dataloader, model, loss_fn, optimizer):
    losses_list = []
    size = len(dataloader.dataset)
    for batch, (X, y) in enumerate(dataloader):
        # 예측(prediction)과 손실(loss) 계산
        pred = model.forward(X)
        loss = loss_fn(pred, y)

        # 역전파
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
        if batch % 1 == 0 and batch != 0:
            loss, current = loss.item(), batch * len(X)
            '''print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")'''
            losses_list.append(loss)
    return losses_list

model_fin.trd.dataset[0]
(tensor([[0.0000e+00, 1.0000e+00, 1.0000e+00, 2.0000e+00, 2.0000e+00, 2.0000e+00,
         0.0000e+00, 1.0000e+00, 0.0000e+00, 0.0000e+00, 8.7360e-01, 8.7360e-01,
         1.0000e-04, 3.5800e-02, 3.5800e-02, 0.0000e+00, 8.0510e-01, 8.0510e-01,
         9.0000e-04, 4.6920e-01, 4.6920e-01, 0.0000e+00, 2.0990e-01, 2.0990e-01,
         0.0000e+00, 2.8000e-03, 2.8000e-03, 1.2000e-03, 4.7670e-01, 4.7670e-01,
         6.3000e-02, 4.9310e+00, 4.9310e+00, 4.0000e-04, 4.3089e+00, 4.3089e+00,
         0.0000e+00, 1.7486e+00, 1.7486e+00, 1.0000e-08, 8.0680e-05, 8.0680e-05,
         3.0000e-08, 9.0800e-06, 9.0800e-06, 3.0000e-08, 9.0800e-06, 9.0800e-06,
         0.0000e+00, 2.9050e-05, 2.9050e-05, 1.0000e+00, 0.0000e+00, 0.0000e+00,
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
         1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00]]), tensor(3))
train_loop(DataLoader(model_fin.trd.dataset[0:1]), model_fin, loss_fn, optimizer)
[]
train_loop(DataLoader(model_fin.trd.dataset[0:1]), model_fin, loss_fn, optimizer)
[]
def train_loop(dataloader, model, loss_fn, optimizer):
    losses_list = []
    size = len(dataloader.dataset)
    for batch, (X, y) in enumerate(dataloader):
        # 예측(prediction)과 손실(loss) 계산
        pred = model.forward(X)
        loss = loss_fn(pred, y)

        # 역전파
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if batch == 0:
            loss, current = loss.item(), batch * len(X)
            '''print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")'''
            losses_list.append(loss)
    return losses_list

train_loop(DataLoader(model_fin.trd.dataset[0:1]), model_fin, loss_fn, optimizer)
[1.8117648363113403]
for i in range(500):
    train_loop(DataLoader(model_fin.trd.dataset[0:1]), model_fin, loss_fn, optimizer)

    
[1.8051884174346924]
[1.8857636451721191]
[1.8442624807357788]
[1.8410615921020508]
[2.637153387069702]
[1.8350130319595337]
[1.832594633102417]
[1.7917594909667969]
[1.8388434648513794]
[1.8156307935714722]
[1.7988821268081665]
[1.7927526235580444]
[2.3924660682678223]
[1.7917594909667969]
[1.8377909660339355]
[1.7917594909667969]
[1.7964630126953125]
[1.7917594909667969]
[1.8199412822723389]
[1.8562629222869873]
[1.7917594909667969]
[2.502399444580078]
[1.830580472946167]
[1.8963452577590942]
[1.7917594909667969]
[1.7917594909667969]
[1.8602283000946045]
[1.8068653345108032]
[1.843686580657959]
[1.8256336450576782]
[1.8224918842315674]
[1.8328720331192017]
[1.8079396486282349]
[1.8137866258621216]
[1.8133585453033447]
[1.811584711074829]
[1.8001245260238647]
[1.7917594909667969]
[1.797873854637146]
[1.8634161949157715]
[1.7917594909667969]
[1.7917594909667969]
[1.838201880455017]
[1.8333117961883545]
[1.8434337377548218]
[1.7917594909667969]
[1.8128212690353394]
[2.2725348472595215]
[1.820044755935669]
[1.7917594909667969]
[1.8711977005004883]
[1.8401297330856323]
[1.7917594909667969]
[1.821998953819275]
[1.7963014841079712]
[1.8059329986572266]
[1.7917594909667969]
[1.85558021068573]
[1.8174123764038086]
[1.887317419052124]
[1.8115628957748413]
[1.7951804399490356]
[1.8226302862167358]
[1.8094453811645508]
[2.4140701293945312]
[1.8358087539672852]
[1.8331454992294312]
[1.8749537467956543]
[1.8150131702423096]
[2.2326149940490723]
[1.8669496774673462]
[1.7917594909667969]
[1.8318700790405273]
[1.8445661067962646]
[1.7917594909667969]
[1.864776611328125]
[1.8080631494522095]
[1.8449710607528687]
[1.8199634552001953]
[1.809471845626831]
[1.861293077468872]
[1.7917594909667969]
[1.8512595891952515]
[1.8663535118103027]
[1.8059074878692627]
[1.7917594909667969]
[1.8521305322647095]
[1.8643722534179688]
[2.6912801265716553]
[1.8506841659545898]
[1.867868423461914]
[1.8779358863830566]
[1.7917594909667969]
[1.8274686336517334]
[1.7917594909667969]Traceback (most recent call last):
  File "<pyshell#128>", line 2, in <module>
    train_loop(DataLoader(model_fin.trd.dataset[0:1]), model_fin, loss_fn, optimizer)
KeyboardInterrupt
for i in range(500):
    g=train_loop(DataLoader(model_fin.trd.dataset[0:1]), model_fin, loss_fn, optimizer)

    
g
[1.8260042667388916]
for i in range(5000):
    g=train_loop(DataLoader(model_fin.trd.dataset[0:1]), model_fin, loss_fn, optimizer)

    
g
[1.8335070610046387]
set1[50]
[5, 5, 5, 0, 5, 5, 5, 0, 0, 2, 2]
set1[58]
[0, 2, 2, 0, 0, 2, 2, 5, 0, 5, 5]
set1[92]
[2, 5, 5, 2, 1, 0, 5, 2, 2, 5, 2]
set[108]
set[108]
set2[108]
[0, 0, 0, 0, 0, 2, 2, 5, 5, 5, 5]
set2[502]
[0, 5, 5, 5, 2, 2, 2, 0, 2, 0, 2]
set2[592]
[5, 5, 0, 2, 5, 0, 0, 0, 0, 2, 0]
set1[892]
[5, 2, 5, 0, 5, 5, 0, 5, 2, 2, 0]
set1[592]
[5, 5, 2, 2, 5, 0, 2, 5, 2, 2, 0]
set1[58]
[0, 2, 2, 0, 0, 2, 2, 5, 0, 5, 5]
set1[502]
[0, 5, 5, 5, 2, 2, 3, 3, 3, 2, 3]
set1[503]
[3, 2, 3, 3, 5, 2, 2, 0, 5, 0, 2]
503*11
5533
p_.dataset[5533]
(tensor([[[6.0000e-04, 7.0000e-04, 1.0000e-03, 5.0000e-04, 3.0000e-04,
          1.0000e-04, 1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00,
          0.0000e+00],
         [7.0000e-04, 1.3700e-02, 4.9600e-02, 5.9000e-03, 4.0000e-04,
          2.0000e-04, 1.0000e-04, 1.0000e-04, 1.0000e-04, 1.0000e-04,
          1.0000e-04],
         [2.0000e-03, 1.6070e-01, 5.3260e-01, 5.0600e-02, 7.0000e-04,
          3.0000e-04, 2.0000e-04, 3.0000e-04, 3.0000e-04, 2.0000e-04,
          1.0000e-04],
         [2.2000e-03, 1.6540e-01, 4.8330e-01, 4.0600e-02, 6.0000e-04,
          4.0000e-04, 4.0000e-04, 6.0000e-04, 1.0000e-03, 5.0000e-04,
          3.0000e-04],
         [7.0000e-04, 1.4900e-02, 3.7300e-02, 3.3000e-03, 5.0000e-04,
          4.0000e-04, 7.0000e-04, 1.8100e-02, 5.3400e-02, 5.2000e-03,
          4.0000e-04],
         [3.0000e-04, 6.0000e-04, 8.0000e-04, 5.0000e-04, 3.0000e-04,
          4.0000e-04, 2.7000e-03, 1.9800e-01, 5.2810e-01, 4.0500e-02,
          6.0000e-04],
         [2.0000e-04, 3.0000e-04, 3.0000e-04, 2.0000e-04, 2.0000e-04,
          4.0000e-04, 2.9000e-03, 1.8780e-01, 4.4150e-01, 3.0000e-02,
          5.0000e-04],
         [1.0000e-04, 1.0000e-04, 1.0000e-04, 1.0000e-04, 1.0000e-04,
          3.0000e-04, 7.0000e-04, 1.5500e-02, 3.1500e-02, 2.4000e-03,
          4.0000e-04],
         [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 1.0000e-04,
          2.0000e-04, 3.0000e-04, 6.0000e-04, 7.0000e-04, 4.0000e-04,
          2.0000e-04],
         [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
          1.0000e-04, 2.0000e-04, 3.0000e-04, 3.0000e-04, 2.0000e-04,
          1.0000e-04],
         [0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
          0.0000e+00, 1.0000e-04, 1.0000e-04, 1.0000e-04, 1.0000e-04,
          1.0000e-04]]]), tensor(2))
p_.dataset[5534][1]
tensor(5)
p_.dataset[5535][1]
tensor(5)
p_.dataset[5536][1]
tensor(5)
p_.dataset[5537][1]
tensor(5)
model_fin.trd.dataset[5537][1]
tensor(5)
model_fin.trd.dataset[5538][1]
tensor(2)
model_fin.trd.dataset[5539][1]
tensor(2)
model_fin.trd.dataset[5530][1]
tensor(3)
model_fin.trd.dataset[5531][1]
tensor(2)
model_fin.trd.dataset[5532][1]
tensor(3)
model_fin.trd.dataset[5534][1]
tensor(2)
model_fin.trd.dataset[5535][1]
tensor(3)
model_fin.trd.dataset[5536][1]
tensor(3)
set1[504]
[2, 0, 0, 0, 0, 5, 2, 2, 0, 5, 5]

set1[505]
[0, 5, 3, 2, 2, 0, 5, 5, 0, 3, 3]
set1[501]
[0, 5, 5, 5, 5, 5, 5, 5, 0, 0, 5]
model_fin.trd.dataset[5525:5540][1]
(tensor([[1.0000e+00, 1.0000e+00, 1.0000e+00, 1.0000e+00, 1.0000e+00, 1.0000e+00,
         0.0000e+00, 1.0000e+00, 1.0000e+00, 1.2000e-03, 1.2000e-03, 1.2000e-03,
         3.7100e-02, 3.7100e-02, 3.7100e-02, 2.8700e-02, 2.8700e-02, 2.8700e-02,
         9.0000e-04, 9.0000e-04, 9.0000e-04, 1.0000e-04, 1.0000e-04, 1.0000e-04,
         7.0000e-04, 7.0000e-04, 7.0000e-04, 1.4000e-03, 1.4000e-03, 1.4000e-03,
         6.1720e-01, 6.1720e-01, 6.1720e-01, 1.3435e+00, 1.3435e+00, 1.3435e+00,
         2.2000e-03, 2.2000e-03, 2.2000e-03, 6.5890e-05, 6.5890e-05, 6.5890e-05,
         7.3000e-07, 7.3000e-07, 7.3000e-07, 7.3000e-07, 7.3000e-07, 7.3000e-07,
         3.5960e-05, 3.5960e-05, 3.5960e-05, 1.0000e+00, 1.0000e+00, 1.0000e+00,
         5.0000e+00, 5.0000e+00, 5.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 1.0000e-04, 1.0000e-04, 1.0000e-04, 1.0000e-04,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 2.0000e-04, 2.0000e-04, 2.0000e-04, 2.0000e-04, 1.0000e-04,
         1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         4.0000e-04, 5.0000e-04, 5.0000e-04, 4.0000e-04, 2.0000e-04, 1.0000e-04,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 1.3000e-03,
         1.2900e-02, 1.5100e-02, 1.8000e-03, 4.0000e-04, 2.0000e-04, 1.0000e-04,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 2.0100e-02, 3.2500e-01,
         3.5860e-01, 2.6800e-02, 7.0000e-04, 3.0000e-04, 1.0000e-04, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 3.0600e-02, 4.6550e-01, 4.7790e-01,
         3.3000e-02, 7.0000e-04, 3.0000e-04, 1.0000e-04, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 3.2000e-03, 3.6400e-02, 3.4800e-02, 2.8000e-03,
         5.0000e-04, 2.0000e-04, 1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 5.0000e-04, 7.0000e-04, 7.0000e-04, 4.0000e-04, 3.0000e-04,
         1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         2.0000e-04, 3.0000e-04, 3.0000e-04, 2.0000e-04, 1.0000e-04, 1.0000e-04,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 1.0000e-04,
         1.0000e-04, 1.0000e-04, 1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 1.0000e-04, 1.0000e-04, 1.0000e-04,
         1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 2.0000e-04, 2.0000e-04, 2.0000e-04, 2.0000e-04,
         1.0000e-04, 1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 4.0000e-04, 5.0000e-04, 5.0000e-04, 4.0000e-04, 2.0000e-04,
         1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         1.3000e-03, 1.2900e-02, 1.5100e-02, 1.8000e-03, 4.0000e-04, 2.0000e-04,
         1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 2.0100e-02,
         3.2500e-01, 3.5860e-01, 2.6800e-02, 7.0000e-04, 3.0000e-04, 1.0000e-04,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 3.0600e-02, 4.6550e-01,
         4.7790e-01, 3.3000e-02, 7.0000e-04, 3.0000e-04, 1.0000e-04, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 3.2000e-03, 3.6400e-02, 3.4800e-02,
         2.8000e-03, 5.0000e-04, 2.0000e-04, 1.0000e-04, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 5.0000e-04, 7.0000e-04, 7.0000e-04, 4.0000e-04,
         3.0000e-04, 1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 2.0000e-04, 3.0000e-04, 3.0000e-04, 2.0000e-04, 1.0000e-04,
         1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         1.0000e-04, 1.0000e-04, 1.0000e-04, 1.0000e-04, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 1.0000e-04, 1.0000e-04,
         1.0000e-04, 1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 2.0000e-04, 2.0000e-04, 2.0000e-04,
         2.0000e-04, 1.0000e-04, 1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 4.0000e-04, 5.0000e-04, 5.0000e-04, 4.0000e-04,
         2.0000e-04, 1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 1.3000e-03, 1.2900e-02, 1.5100e-02, 1.8000e-03, 4.0000e-04,
         2.0000e-04, 1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         2.0100e-02, 3.2500e-01, 3.5860e-01, 2.6800e-02, 7.0000e-04, 3.0000e-04,
         1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 3.0600e-02,
         4.6550e-01, 4.7790e-01, 3.3000e-02, 7.0000e-04, 3.0000e-04, 1.0000e-04,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 3.2000e-03, 3.6400e-02,
         3.4800e-02, 2.8000e-03, 5.0000e-04, 2.0000e-04, 1.0000e-04, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 5.0000e-04, 7.0000e-04, 7.0000e-04,
         4.0000e-04, 3.0000e-04, 1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 2.0000e-04, 3.0000e-04, 3.0000e-04, 2.0000e-04,
         1.0000e-04, 1.0000e-04, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00,
         0.0000e+00, 1.0000e-04, 1.0000e-04, 1.0000e-04, 1.0000e-04, 0.0000e+00,
         0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00, 0.0000e+00]]), tensor(2))
train_loop(DataLoader(model_fin.trd.dataset[5525:5540]), model_fin, loss_fn, optimizer)
[0.00017855956684798002]
train_loop(DataLoader(model_fin.trd.dataset[5525:5540]), model_fin, loss_fn, optimizer)
[0.0001245659514097497]
train_loop(DataLoader(model_fin.trd.dataset[5525:5540]), model_fin, loss_fn, optimizer)
[0.0006993946735747159]
train_loop(DataLoader(model_fin.trd.dataset[5525:5540]), model_fin, loss_fn, optimizer)
[0.0014405598631128669]
train_loop(DataLoader(model_fin.trd.dataset[5525:5540]), model_fin, loss_fn, optimizer)
[0.00016962042718660086]
train_loop(DataLoader(model_fin.trd.dataset[5525:5540]), model_fin, loss_fn, optimizer)
[6.389413465512916e-05]
train_loop(DataLoader(model_fin.trd.dataset[5525:5540]), model_fin, loss_fn, optimizer)
[0.0021992563270032406]
train_loop(DataLoader(model_fin.trd.dataset[5525:5540]), model_fin, loss_fn, optimizer)
[6.186770770000294e-05]
train_loop(DataLoader(model_fin.trd.dataset[5525:5540]), model_fin, loss_fn, optimizer)
[6.460934673668817e-05]

train_loop(DataLoader(model_fin.trd.dataset[5525:5540]), model_fin, loss_fn, optimizer)
[0.00043084874050691724]
for i in range(5000):
    g = train_loop(DataLoader(model_fin.trd.dataset[5525:5540]), model_fin, loss_fn, optimizer)

    


g
[0.00082601752365008]
KeyboardInterrupt
set2 = [[torch.argmax(model_fin(li68[i*11+j][0])).item() for j in range(11)] for i in range(0, 1000)]


b = [0,0,0,0,0,0]
for i in set2:
    for j in i:
        b[j] += 1
        
SyntaxError: multiple statements found while compiling a single statement
b = [0,0,0,0,0,0]
for i in set2:
    for j in i:
        b[j] += 1

        
b
[3884, 0, 2868, 0, 0, 4248]
b
[3884, 0, 2868, 0, 0, 4248]

=============== RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ==============
Done!
Epoch 1

Test Error: 
 Accuracy: 51.2%, Avg loss: 1.279879 

1.3223366737365723
Epoch 31

Test Error: 
 Accuracy: 80.2%, Avg loss: 0.528297 

0.5365430116653442
Epoch 61

Test Error: 
 Accuracy: 81.1%, Avg loss: 0.514760 

0.5821343660354614
Epoch 91

Test Error: 
 Accuracy: 80.9%, Avg loss: 0.511998 

0.4206385016441345
27.980325937271118
real_test: 0.832
b = [0,0,0,0,0,0]
for i in set2:
    for j in i:
        b[j] += 1

        
b
[3451, 508, 2797, 0, 0, 4244]
model_fin.roll(100, 30)
Epoch 1

Test Error: 
 Accuracy: 80.9%, Avg loss: 0.515862 

0.4876598119735718
Epoch 31

Test Error: 
 Accuracy: 80.4%, Avg loss: 0.514878 

0.4751618206501007
Epoch 61

Test Error: 
 Accuracy: 80.9%, Avg loss: 0.504075 

0.3992583751678467
Epoch 91

Test Error: 
 Accuracy: 80.5%, Avg loss: 0.513625 

0.4710402190685272
27.168273210525513
b = [0,0,0,0,0,0]
for i in set2:
    for j in i:
        b[j] += 1

        
b
[3451, 508, 2797, 0, 0, 4244]
b = [0,0,0,0,0,0]
set2 = [[torch.argmax(model_fin(li68[i*11+j][0])).item() for j in range(11)] for i in range(0, 1000)]


for i in set2:
    for j in i:
        b[j] += 1

        
b
[3586, 508, 2681, 0, 0, 4225]

=============== RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ==============
Done!
Epoch 1

Test Error: 
 Accuracy: 49.9%, Avg loss: 1.339909 

1.5689789056777954
Epoch 31

Test Error: 
 Accuracy: 80.0%, Avg loss: 0.564461 

0.5805555582046509
Epoch 61

Test Error: 
 Accuracy: 81.0%, Avg loss: 0.516816 

0.5422630310058594
Epoch 91

Test Error: 
 Accuracy: 80.9%, Avg loss: 0.521637 

0.5252808332443237
29.13643479347229
real_test: 0.8285454545454546
b = [0,0,0,0,0,0]
for i in set2:
    for j in i:
        b[j] += 1

        
b
[3583, 572, 2684, 0, 0, 4161]

=============== RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ==============
Done!
Epoch 1

Test Error: 
 Accuracy: 55.7%, Avg loss: 1.242177 

1.2420722246170044
Epoch 31

Test Error: 
 Accuracy: 81.1%, Avg loss: 0.534968 

0.4824691414833069
Epoch 61

Test Error: 
 Accuracy: 80.1%, Avg loss: 0.533967 

0.5496441125869751
Epoch 91

Test Error: 
 Accuracy: 80.6%, Avg loss: 0.522118 

0.47606927156448364
28.837543725967407
real_test: 0.8358181818181818
b = [0,0,0,0,0,0]
for i in set2:
    for j in i:
        b[j] += 1

        
b
[3519, 486, 2753, 0, 0, 4242]

=============== RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ==============
Done!
Epoch 1

Test Error: 
 Accuracy: 56.5%, Avg loss: 1.227356 

1.3148432970046997
Epoch 31

Test Error: 
 Accuracy: 81.2%, Avg loss: 0.491931 

0.5486739873886108
Epoch 61

Test Error: 
 Accuracy: 82.0%, Avg loss: 0.476855 

0.4352037012577057
Epoch 91

Test Error: 
 Accuracy: 80.9%, Avg loss: 0.486909 

0.42783451080322266
27.90315842628479
real_test: 0.8430909090909091
b = [0,0,0,0,0,0]
for i in set2:
    for j in i:
        b[j] += 1

b
[3211, 500, 2596, 518, 0, 4175]

=============== RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ==============
Done!
Epoch 1

Test Error: 
 Accuracy: 51.3%, Avg loss: 1.323591 

1.3287519216537476
Epoch 31

Test Error: 
 Accuracy: 80.8%, Avg loss: 0.523849 

0.6251732110977173
Epoch 61

Test Error: 
 Accuracy: 80.5%, Avg loss: 0.529955 

0.4425261914730072
Epoch 91

Test Error: 
 Accuracy: 80.6%, Avg loss: 0.515729 

0.587931215763092
28.549078702926636
real_test: 0.8286363636363636
b = [0,0,0,0,0,0]
for i in set2:
    for j in i:
        b[j] += 1

b
[3602, 0, 2764, 459, 0, 4175]
model_fin.roll(10)
Epoch 1

Test Error: 
 Accuracy: 81.2%, Avg loss: 0.515267 

0.5752508044242859
2.6497786045074463
set2 = [[torch.argmax(model_fin(li68[i*11+j][0])).item() for j in range(11)] for i in range(0, 1000)]


set2 = [[torch.argmax(model_fin(li68[i*11+j][0])).item() for j in range(11)] for i in range(0, 1000)]

b = [0,0,0,0,0,0]
for i in set2:
    for j in i:
        b[j] += 1

b
[3592, 0, 2678, 507, 0, 4223]
model_fin = NeuralNetwork([len(li68[0][0][0]), 20, 150, 6])model_fin = NeuralNetwork([len(li68[0][0][0]), 20, 150, 6])model_fin = NeuralNetwork([len(li68[0][0][0]), 20, 150, 6])model_fin = NeuralNetwork([len(li68[0][0][0]), 20, 150, 6])model_fin = NeuralNetwork([len(li68[0][0][0]), 20, 150, 6])model_fin = NeuralNetwork([len(li68[0][0][0]), 20, 150, 6])model_fin = NeuralNetwork([len(li68[0][0][0]), 20, 150, 6])model_fin = NeuralNetwork([len(li68[0][0][0]), 20, 150, 6])model_fin = NeuralNetwork([len(li68[0][0][0]), 20, 150, 6])model_fin = NeuralNetwork([len(li68[0][0][0]), 20, 150, 6])model_fin = NeuralNetwork([len(li68[0][0][0]), 20, 150, 6])model_fin = NeuralNetwork([len(li68[0][0][0]), 20, 150, 6])
SyntaxError: invalid syntax
model_fin = NeuralNetwork([len(li68[0][0][0]), 20, 150, 6])
model_fin.base_set(li68, call = False)
model_fin.roll(100, 30)
Epoch 1

Test Error: 
 Accuracy: 50.7%, Avg loss: 1.255821 

1.3150218725204468
Epoch 31

Test Error: 
 Accuracy: 80.3%, Avg loss: 0.540117 

0.518284797668457
Epoch 61

Test Error: 
 Accuracy: 81.2%, Avg loss: 0.505290 

0.467023104429245
Epoch 91

Test Error: 
 Accuracy: 81.8%, Avg loss: 0.483922 

0.3999961316585541
25.15818762779236
set2 = [[torch.argmax(model_fin(li68[i*11+j][0])).item() for j in range(11)] for i in range(0, 1000)]

b = [0,0,0,0,0,0]

for i in set2:
    for j in i:
        b[j] += 1

b
[3176, 548, 2684, 423, 0, 4169]
for i in (np.array(set1)==np.array(set2)).flatten()
SyntaxError: incomplete input
for i in (np.array(set1)==np.array(set2)).flatten():
    if i == True:
        b[4] += 1

b
[3176, 548, 2684, 423, 9280, 4169]
9280/11000
0.8436363636363636

=============== RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ==============
Done!
Epoch 1

Test Error: 
 Accuracy: 53.8%, Avg loss: 1.237491 

1.3547289371490479
Epoch 31

Test Error: 
 Accuracy: 79.6%, Avg loss: 0.577346 

0.5702206492424011
Epoch 61

Test Error: 
 Accuracy: 80.0%, Avg loss: 0.549960 

0.6160880923271179
Epoch 91

Test Error: 
 Accuracy: 78.9%, Avg loss: 0.574334 

0.5311505794525146
34.44093346595764
real_test: 0.8187272727272727
b = [0,0,0,0,0,0]
for i in set2:
    for j in i:
        b[j] += 1

b
[3814, 0, 2971, 0, 0, 4215]

=============== RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ==============
Done!
Epoch 1

Test Error: 
 Accuracy: 48.1%, Avg loss: 1.326627 

1.3563640117645264
Epoch 31

Test Error: 
 Accuracy: 79.2%, Avg loss: 0.571146 

0.6399325132369995
Epoch 61

Test Error: 
 Accuracy: 78.8%, Avg loss: 0.571900 

0.6471798419952393
Epoch 91

Test Error: 
 Accuracy: 79.4%, Avg loss: 0.554234 

0.5369731783866882
33.96733903884888
real_test: 0.8139090909090909

=============== RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ==============
Done!
Epoch 1

Test Error: 
 Accuracy: 47.4%, Avg loss: 1.429474 

1.443002700805664
Epoch 31

Test Error: 
 Accuracy: 79.3%, Avg loss: 0.542228 

0.5483793616294861
Epoch 61

Test Error: 
 Accuracy: 81.1%, Avg loss: 0.511881 

0.5300065279006958
Epoch 91

Test Error: 
 Accuracy: 80.6%, Avg loss: 0.514828 

0.43103718757629395
25.584637880325317
real_test: 0.8212727272727273
b = [0,0,0,0,0,0]

for i in set2:
    for j in i:
        b[j] += 1

b
[3403, 0, 2855, 533, 0, 4209]

=============== RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ==============
Done!
Epoch 1

Test Error: 
 Accuracy: 31.7%, Avg loss: 1.603282 

1.6878719329833984
Epoch 31

Test Error: 
 Accuracy: 79.7%, Avg loss: 0.566874 

0.5707327127456665
Epoch 61

Test Error: 
 Accuracy: 79.6%, Avg loss: 0.560604 

0.5707429051399231
Epoch 91

Test Error: 
 Accuracy: 79.6%, Avg loss: 0.564986 

0.5950617790222168
44.051270961761475

=============== RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ==============
Done!
Epoch 1

Test Error: 
 Accuracy: 49.2%, Avg loss: 1.298779 

1.3877798318862915
Epoch 31

Test Error: 
 Accuracy: 80.1%, Avg loss: 0.517446 

0.384086549282074
Epoch 61

Test Error: 
 Accuracy: 81.3%, Avg loss: 0.498212 

0.4198816120624542
Epoch 91

Test Error: 
 Accuracy: 79.9%, Avg loss: 0.517116 

0.34111931920051575
38.12311840057373
real_test: 0.8578181818181818
b = [0,0,0,0,0,0]
for i in set2:
    for j in i:
        b[j] += 1

b
[3249, 442, 2653, 485, 0, 4171]
model_fin
NeuralNetwork(
  (flatten): Flatten(start_dim=1, end_dim=-1)
  (stack): Sequential(
    (0): Linear(in_features=626, out_features=20, bias=True)
    (1): ReLU()
    (2): Dropout(p=0.1, inplace=False)
    (3): Linear(in_features=20, out_features=150, bias=True)
    (4): ReLU()
    (5): Dropout(p=0.1, inplace=False)
    (6): Linear(in_features=150, out_features=6, bias=True)
    (7): ReLU()
    (8): Dropout(p=0.1, inplace=False)
  )
)

=============== RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ==============
Done!
Epoch 1

Test Error: 
 Accuracy: 30.7%, Avg loss: 1.706987 

1.744864821434021
Epoch 31

Test Error: 
 Accuracy: 79.9%, Avg loss: 0.542435 

0.4916496276855469
Epoch 61

Test Error: 
 Accuracy: 79.2%, Avg loss: 0.527724 

0.48344308137893677
Epoch 91

Test Error: 
 Accuracy: 79.9%, Avg loss: 0.514155 

0.4385996162891388
36.28677439689636
real_test: 0.8392727272727273

=============== RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ==============
Done!
Epoch 1

Test Error: 
 Accuracy: 41.4%, Avg loss: 1.457741 

1.4101037979125977
Epoch 31

Test Error: 
 Accuracy: 79.1%, Avg loss: 0.842647 

0.7952086329460144
Epoch 61

Test Error: 
 Accuracy: 79.6%, Avg loss: 0.587669 

0.6169618964195251
Epoch 91

Test Error: 
 Accuracy: 79.4%, Avg loss: 0.579649 

0.5157179832458496
31.27270770072937
real_test: 0.8188181818181818

=============== RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ==============
Done!
Epoch 1

Test Error: 
 Accuracy: 40.0%, Avg loss: 1.456804 

1.4418830871582031
Epoch 31

Test Error: 
 Accuracy: 78.3%, Avg loss: 0.568721 

0.5845046639442444
Epoch 61

Test Error: 
 Accuracy: 79.5%, Avg loss: 0.557831 

0.5164670944213867
Epoch 91

Test Error: 
 Accuracy: 79.0%, Avg loss: 0.553352 

0.4872235953807831
40.23544239997864
real_test: 0.8188181818181818
b = [0,0,0,0,0,0]
n
Traceback (most recent call last):
  File "<pyshell#258>", line 1, in <module>
    n
NameError: name 'n' is not defined. Did you mean: 'nn'?

for i in set2:
    for j in i:
        b[j] += 1

b
[3703, 0, 2619, 456, 0, 4222]

=============== RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ==============
Done!
Epoch 1

Test Error: 
 Accuracy: 46.3%, Avg loss: 1.433495 

1.4322954416275024
Epoch 31

Test Error: 
 Accuracy: 60.3%, Avg loss: 0.887755 

0.993193507194519
Epoch 61

Test Error: 
 Accuracy: 79.8%, Avg loss: 0.574461 

0.5350534319877625
Epoch 91

Test Error: 
 Accuracy: 78.9%, Avg loss: 0.578296 

0.5560105443000793
60.41619682312012
real_test: 0.8104545454545454

=============== RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ==============
Done!
Epoch 1

Test Error: 
 Accuracy: 46.8%, Avg loss: 1.344942 

1.2331137657165527
Epoch 31

Test Error: 
 Accuracy: 78.9%, Avg loss: 0.554806 

0.5595985651016235
Epoch 61

Test Error: 
 Accuracy: 80.6%, Avg loss: 0.519027 

0.5380938649177551
Epoch 91

Test Error: 
 Accuracy: 80.4%, Avg loss: 0.524898 

0.5038856863975525
29.687236070632935
real_test: 0.8246363636363636

=============== RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ==============
Done!
Epoch 1

Test Error: 
 Accuracy: 50.2%, Avg loss: 1.361295 

1.4217844009399414
Epoch 31

Test Error: 
 Accuracy: 79.9%, Avg loss: 0.560207 

0.6701918840408325
Epoch 61

Test Error: 
 Accuracy: 79.7%, Avg loss: 0.538949 

0.6430018544197083
Epoch 91

Test Error: 
 Accuracy: 80.6%, Avg loss: 0.537120 

0.5344333052635193
25.7641339302063
real_test: 0.8133636363636364

=============== RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ==============
Done!
Epoch 1

Test Error: 
 Accuracy: 54.6%, Avg loss: 1.216441 

1.270928978919983
Epoch 31

Test Error: 
 Accuracy: 80.0%, Avg loss: 0.542619 

0.5222755670547485
Epoch 61

Test Error: 
 Accuracy: 81.0%, Avg loss: 0.515672 

0.6000409722328186
Epoch 91

Test Error: 
 Accuracy: 81.2%, Avg loss: 0.519475 

0.4887496829032898
26.02341079711914
real_test: 0.8264545454545454

=============== RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ==============
Done!
Epoch 1

Test Error: 
 Accuracy: 51.6%, Avg loss: 1.285865 

1.3000236749649048
Epoch 31

Test Error: 
 Accuracy: 79.7%, Avg loss: 0.536330 

0.550285816192627
Epoch 61

Test Error: 
 Accuracy: 79.8%, Avg loss: 0.535848 

0.5576332807540894
Epoch 91

Test Error: 
 Accuracy: 80.4%, Avg loss: 0.530751 

0.44577816128730774
38.90853810310364
real_test: 0.8348181818181818
b = [0]*6
for i in set2:
    for j in i:
        b[j] += 1

b
[3444, 506, 2838, 0, 0, 4212]

=============== RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ==============
Done!
Epoch 1

Test Error: 
 Accuracy: 45.5%, Avg loss: 1.307468 

1.404494047164917
Epoch 31

Test Error: 
 Accuracy: 81.4%, Avg loss: 0.490903 

0.48286622762680054
Epoch 61

Test Error: 
 Accuracy: 81.7%, Avg loss: 0.478048 

0.4607168436050415
Epoch 91

Test Error: 
 Accuracy: 82.0%, Avg loss: 0.483152 

0.4505271017551422
26.51829171180725
real_test: 0.8417272727272728
b = [0]*6
for i in set2:
    for j in i:
        b[j] += 1

b
[3194, 502, 2667, 466, 0, 4171]

=============== RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ==============
Done!
Epoch 1

Test Error: 
 Accuracy: 61.6%, Avg loss: 1.056142 

1.1425477266311646
Epoch 31

Test Error: 
 Accuracy: 79.6%, Avg loss: 0.564997 

0.548116147518158
Epoch 61

Test Error: 
 Accuracy: 81.5%, Avg loss: 0.500235 

0.5286715626716614
Epoch 91

Test Error: 
 Accuracy: 80.6%, Avg loss: 0.525414 

0.36043936014175415
47.519307136535645
real_test: 0.8255454545454546
b = [0]*6
for i in set2:
    for j in i:
        b[j] += 1

b
[2992, 501, 2785, 565, 0, 4157]

=============== RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ==============
Done!
Epoch 1

Test Error: 
 Accuracy: 60.1%, Avg loss: 1.131778 

1.2051323652267456
Epoch 31

Test Error: 
 Accuracy: 80.5%, Avg loss: 0.530446 

0.5085684657096863
Epoch 61

Test Error: 
 Accuracy: 80.6%, Avg loss: 0.510343 

0.47000619769096375
Epoch 91

Test Error: 
 Accuracy: 81.1%, Avg loss: 0.500498 

0.44207701086997986
36.956528186798096
real_test: 0.8356363636363636


b = [0]*6

for i in set2:
    for j in i:
        b[j] += 1

b
[3491, 0, 2759, 516, 0, 4234]
model_fin.roll(30)
Epoch 1

Test Error: 
 Accuracy: 80.7%, Avg loss: 0.508184 

0.423052042722702
Epoch 11

Test Error: 
 Accuracy: 80.7%, Avg loss: 0.501791 

0.4996977746486664
Epoch 21

Test Error: 
 Accuracy: 81.2%, Avg loss: 0.502273 

0.47747838497161865
13.712827682495117
set2 = [[torch.argmax(model_fin(li68[i*11+j][0])).item() for j in range(11)] for i in range(0, 1000)]

b = [0]*6
for i in set2:
    for j in i:
        b[j] += 1

b
[3652, 0, 2660, 506, 0, 4182]
def net_mutate(net, prob=0.03, width=0.03):
    with torch.no_grad():
        for i in range(len(net.stack[0].weight)):
            for j in range(len(net.stack[0].weight[i])):
                if random.random() < prob:
                    net.stack[0].weight[i][j] += torch.tensor(random.random()*width,
                                                                  requires_grad=True)


net_mutate(model_fin, prob=0.50)
Traceback (most recent call last):
  File "<pyshell#290>", line 1, in <module>
    net_mutate(model_fin, prob=0.50)
  File "<pyshell#288>", line 5, in net_mutate
    if random.random() < prob:
NameError: name 'random' is not defined
import random
def net_mutate(net, prob=0.03, width=0.03):
    with torch.no_grad():
        for i in range(len(net.stack[0].weight)):
            for j in range(len(net.stack[0].weight[i])):
                if random.random() < prob:
                    net.stack[0].weight[i][j] += torch.tensor(random.random()*width,
                                                                  requires_grad=True)

                    
net_mutate(model_fin, prob=0.50)
model_fin.roll(50)
Epoch 1

Test Error: 
 Accuracy: 81.5%, Avg loss: 0.501339 

0.46288707852363586
Epoch 11

Test Error: 
 Accuracy: 81.9%, Avg loss: 0.502877 

0.4607977867126465
Epoch 21

Test Error: 
 Accuracy: 81.3%, Avg loss: 0.505179 

0.47789859771728516
Epoch 31

Test Error: 
 Accuracy: 81.2%, Avg loss: 0.507880 

0.4160846471786499
Epoch 41

Test Error: 
 Accuracy: 81.3%, Avg loss: 0.503429 

0.48954248428344727
16.977165937423706
set2 = [[torch.argmax(model_fin(li68[i*11+j][0])).item() for j in range(11)] for i in range(0, 1000)]

b = [0]*6
for i in set2:
    for j in i:
        b[j] += 1

        
b
[3672, 0, 2615, 483, 0, 4230]
def net_mutate(net, prob=0.03, width=0.53):
    with torch.no_grad():
        for i in range(len(net.stack[0].weight)):
            for j in range(len(net.stack[0].weight[i])):
                if random.random() < prob:
                    net.stack[0].weight[i][j] += torch.tensor(random.random()*width,
                                                                  requires_grad=True)

                    
def net_mutate(net, prob=0.03, width=0.03):
    with torch.no_grad():
        for i in range(len(net.stack[0].weight)):
            for j in range(len(net.stack[0].weight[i])):
                if random.random() < prob:
                    net.stack[0].weight[i][j] += torch.tensor(random.random()*width,
                                                                  requires_grad=True)

                    
net_mutate(model_fin, prob=0.50, width=0.50)
model_fin.roll(50, 20)
Epoch 1

Test Error: 
 Accuracy: 45.6%, Avg loss: 1.595790 

1.6115690469741821
Epoch 21

Test Error: 
 Accuracy: 64.6%, Avg loss: 0.906829 

0.8781090378761292
Epoch 41

Test Error: 
 Accuracy: 71.4%, Avg loss: 0.738603 

0.6710022687911987
14.846737384796143
model_fin.roll(50, 20)
Epoch 1

Test Error: 
 Accuracy: 73.3%, Avg loss: 0.683991 

0.6312193870544434
Epoch 21

Test Error: 
 Accuracy: 76.1%, Avg loss: 0.628933 

0.5666101574897766
Epoch 41

Test Error: 
 Accuracy: 77.5%, Avg loss: 0.600129 

0.6335368156433105
15.311562299728394
model_fin.roll(50, 20)
Epoch 1

Test Error: 
 Accuracy: 76.9%, Avg loss: 0.626123 

0.660438597202301
Epoch 21

Test Error: 
 Accuracy: 77.5%, Avg loss: 0.600864 

0.5864384174346924
Epoch 41

Test Error: 
 Accuracy: 78.2%, Avg loss: 0.577593 

0.542616605758667
15.6689932346344

=============== RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ==============
Done!
Epoch 1

Test Error: 
 Accuracy: 59.5%, Avg loss: 1.123263 

1.2001196146011353
Epoch 31

Test Error: 
 Accuracy: 79.8%, Avg loss: 0.550921 

0.4349178969860077
Epoch 61

Test Error: 
 Accuracy: 80.9%, Avg loss: 0.522729 

0.45164310932159424
Epoch 91

Test Error: 
 Accuracy: 80.3%, Avg loss: 0.516734 

0.5009472966194153
26.290719509124756
real_test: 0.834
b = [0]*6
for i in set2:
    for j in i:
        b[j] += 1

        
b
[3399, 582, 2807, 0, 0, 4212]

=============== RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ==============
Done!
Epoch 1

Test Error: 
 Accuracy: 49.5%, Avg loss: 1.276920 

1.350225806236267
Epoch 31

Test Error: 
 Accuracy: 60.4%, Avg loss: 0.877794 

0.9128907322883606
Epoch 61

Test Error: 
 Accuracy: 59.8%, Avg loss: 0.877415 

0.8220580816268921

=============== RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ==============
Done!
Epoch 1

Test Error: 
 Accuracy: 60.1%, Avg loss: 1.124255 

1.198274850845337
Epoch 31

Test Error: 
 Accuracy: 81.2%, Avg loss: 0.492727 

0.4245511293411255
Epoch 61

Test Error: 
 Accuracy: 80.9%, Avg loss: 0.493556 

0.42328521609306335
Epoch 91

Test Error: 
 Accuracy: 82.1%, Avg loss: 0.480079 

0.3571627140045166
25.33991575241089
real_test: 0.8607272727272727
b = [0]*6
for i in set2:
    for j in i:
        b[j] += 1

        
b
[3171, 498, 2632, 504, 0, 4195]

=============== RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ==============
Done!

=============== RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ==============
Done!
Epoch 1

Test Error: 
 Accuracy: 67.4%, Avg loss: 0.894513 

0.9088493585586548
Epoch 31

Test Error: 
 Accuracy: 80.5%, Avg loss: 0.529003 

0.4860894978046417
Epoch 61

Test Error: 
 Accuracy: 81.8%, Avg loss: 0.495035 

0.4300551116466522
Epoch 91

Test Error: 
 Accuracy: 81.5%, Avg loss: 0.514208 

0.40931186079978943
85.02234268188477
real_test: 0.8534545454545455

=============== RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ==============
Done!
Epoch 1

Test Error: 
 Accuracy: 64.5%, Avg loss: 1.112828 

1.2541089057922363
Epoch 31

Test Error: 
 Accuracy: 79.4%, Avg loss: 0.576649 

0.5283844470977783
Epoch 61

Test Error: 
 Accuracy: 80.2%, Avg loss: 0.560605 

0.5712255835533142
Epoch 91

Test Error: 
 Accuracy: 80.2%, Avg loss: 0.549338 

0.5444105863571167
62.82624316215515
real_test: 0.8244545454545454

\=============== RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ==============
Done!
Epoch 1

Test Error: 
 Accuracy: 46.8%, Avg loss: 1.324602 

1.358182430267334
Epoch 31

Test Error: 
 Accuracy: 81.0%, Avg loss: 0.511256 

0.4902173578739166
Epoch 61

Test Error: 
 Accuracy: 81.1%, Avg loss: 0.497215 

0.40063175559043884
Epoch 91

Test Error: 
 Accuracy: 82.8%, Avg loss: 0.462867 

0.4203924834728241
38.88505554199219
real_test: 0.8493636363636363
b = [0]*6
for i in set2:
    for j in i:
        b[j] += 1

        
b
[3251, 452, 2642, 493, 0, 4162]
params = []
for i in model_fin.parameters():
    params.append(i)

    
for i in range(len(params)):
    params[i]=torch.Tensor.tolist(params[i][0:])

    
with open('modelparam_data.json', 'w') as f:
    json.dump(params, f)

    
model_fin
NeuralNetwork(
  (flatten): Flatten(start_dim=1, end_dim=-1)
  (stack): Sequential(
    (0): Linear(in_features=380, out_features=50, bias=True)
    (1): ReLU()
    (2): Dropout(p=0.1, inplace=False)
    (3): Linear(in_features=50, out_features=30, bias=True)
    (4): ReLU()
    (5): Dropout(p=0.1, inplace=False)
    (6): Linear(in_features=30, out_features=6, bias=True)
    (7): ReLU()
    (8): Dropout(p=0.1, inplace=False)
  )
)

with open('modelparam_data.json', 'w') as f:
    json.dump(params, f)============= RESTART: C:\Users\KDCA\Desktop\IL\Hitting_Frame.py =============
pygame 2.1.2 (SDL 2.0.18, Python 3.10.9)
Hello from the pygame community. https://www.pygame.org/contribute.html

========== RESTART: C:\Users\KDCA\Desktop\IL\Parameter_Developing.py =========
pygame 2.1.2 (SDL 2.0.18, Python 3.10.9)
Hello from the pygame community. https://www.pygame.org/contribute.html
Done!
rep_test(2)

Warning (from warnings module):
  File "C:\Users\KDCA\Desktop\IL\Parameter_Developing.py", line 103
    extracted_weights.append(torch.tensor(net.stack[n*(length-1)].weight))
UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).

Warning (from warnings module):
  File "C:\Users\KDCA\Desktop\IL\Parameter_Developing.py", line 104
    extracted_biases.append(torch.tensor(net.stack[n*(length-1)].bias))
UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).

Warning (from warnings module):
  File "C:\Users\KDCA\Desktop\IL\Hitting_Frame.py", line 414
    locals()[n].append(torch.tensor(locals()[n[0:n.index('_')+1]+'now']))
UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).
Traceback (most recent call last):
  File "<pyshell#329>", line 1, in <module>
    rep_test(2)
  File "C:\Users\KDCA\Desktop\IL\Parameter_Developing.py", line 81, in rep_test
    a.test(5, view_lock = view_lock)
  File "C:\Users\KDCA\Desktop\IL\Parameter_Developing.py", line 29, in test
    score = self.circumstances.run_by_AI(view_lock = view_lock, net=self.paramgens[i])
  File "C:\Users\KDCA\Desktop\IL\Hitting_Frame.py", line 423, in run_by_AI
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
RuntimeError: mat1 and mat2 shapes cannot be multiplied (1x378 and 380x50)

========== RESTART: C:\Users\KDCA\Desktop\IL\Parameter_Developing.py =========
pygame 2.1.2 (SDL 2.0.18, Python 3.10.9)
Hello from the pygame community. https://www.pygame.org/contribute.html
Done!
rep_test(2)

Warning (from warnings module):
  File "C:\Users\KDCA\Desktop\IL\Parameter_Developing.py", line 103
    extracted_weights.append(torch.tensor(net.stack[n*(length-1)].weight))
UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).

Warning (from warnings module):
  File "C:\Users\KDCA\Desktop\IL\Parameter_Developing.py", line 104
    extracted_biases.append(torch.tensor(net.stack[n*(length-1)].bias))
UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).

Warning (from warnings module):
  File "C:\Users\KDCA\Desktop\IL\Hitting_Frame.py", line 414
    locals()[n].append(torch.tensor(locals()[n[0:n.index('_')+1]+'now']))
UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).
534 500
450 50
528 500
570 100
528 400
552 500
384 100
498 0
582 0
360 50
408 50
564 0
546 0
354 100
522 0
504 50
438 100
390 0
582 500
654 200
[1034, 500, 1028, 670, 928, 1052, 484, 498, 582, 410, 458, 564, 546, 454, 522, 554, 538, 390, 1082, 854] 657.4
222.47276329994202
366 100
564 200
522 200
618 200
510 150
486 100
600 300
546 0
450 100
504 0
492 0
396 0
462 0
384 0
612 100
540 300
528 50
414 0
540 150
408 50
[466, 764, 722, 818, 660, 586, 900, 546, 550, 504, 492, 396, 462, 384, 712, 840, 578, 414, 690, 458] 597.1
237.37634563446045

========== RESTART: C:\Users\KDCA\Desktop\IL\Parameter_Developing.py =========
pygame 2.1.2 (SDL 2.0.18, Python 3.10.9)
Hello from the pygame community. https://www.pygame.org/contribute.html
Done!
rep_test(2)

Warning (from warnings module):
  File "C:\Users\KDCA\Desktop\IL\Parameter_Developing.py", line 104
    extracted_weights.append(torch.tensor(net.stack[n*(length-1)].weight))
UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).

Warning (from warnings module):
  File "C:\Users\KDCA\Desktop\IL\Parameter_Developing.py", line 105
    extracted_biases.append(torch.tensor(net.stack[n*(length-1)].bias))
UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).

Warning (from warnings module):
  File "C:\Users\KDCA\Desktop\IL\Hitting_Frame.py", line 414
    locals()[n].append(torch.tensor(locals()[n[0:n.index('_')+1]+'now']))
UserWarning: To copy construct from a tensor, it is recommended to use sourceTensor.clone().detach() or sourceTensor.clone().detach().requires_grad_(True), rather than torch.tensor(sourceTensor).
504 300
564 0
432 50
564 0
588 300
570 400
474 150
456 0
534 200
438 50
558 0
594 0
504 100
546 400
480 0
420 50
444 0
450 0
468 0
618 50
[804, 564, 482, 564, 888, 970, 624, 456, 734, 488, 558, 594, 604, 946, 480, 470, 444, 450, 468, 668] 612.8
221.41185450553894
414 100
480 0
Traceback (most recent call last):
  File "<pyshell#331>", line 1, in <module>
    rep_test(2)
  File "C:\Users\KDCA\Desktop\IL\Parameter_Developing.py", line 82, in rep_test
    a.test(5, view_lock = view_lock)
  File "C:\Users\KDCA\Desktop\IL\Parameter_Developing.py", line 30, in test
    score = self.circumstances.run_by_AI(view_lock = view_lock, net=self.paramgens[i])
  File "C:\Users\KDCA\Desktop\IL\Hitting_Frame.py", line 390, in run_by_AI
    mapkde.Z = mapkde.kde_distribution(*kdeval, 0.03, 30) + mapkde.kde_distribution(*kdeval, 0.1, 0.5)
  File "C:\Users\KDCA\Desktop\IL\base\kde_temp.py", line 175, in kde_distribution
    Z = np.reshape(self.kernel(positions).T, self.Xmg.shape)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\scipy\stats\_kde.py", line 268, in evaluate
    result = gaussian_kernel_estimate[spec](
KeyboardInterrupt

=============== RESTART: C:\Users\KDCA\Desktop\IL\base\temp2.py ==============
Done!
Epoch 1

Test Error: 
 Accuracy: 45.2%, Avg loss: 1.456196 

1.4815863370895386
Epoch 31

Test Error: 
 Accuracy: 79.8%, Avg loss: 0.559087 

0.5537684559822083
Epoch 61

Test Error: 
 Accuracy: 80.8%, Avg loss: 0.521424 

0.49801892042160034
Epoch 91

Test Error: 
 Accuracy: 81.0%, Avg loss: 0.524950 

0.5380710959434509
43.67730259895325
real_test: 0.8374545454545455
def train_loop(dataloader, model, loss_fn, optimizer):
    losses_list = []
    size = len(dataloader.dataset)
    for batch, (X, y) in enumerate(dataloader):
        # 예측(prediction)과 손실(loss) 계산
        pred = model.forward(X)
        loss = loss_fn(pred, y)

        # 역전파
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        if batch == 0:
            loss, current = loss.item(), batch * len(X)
            '''print(f"loss: {loss:>7f}  [{current:>5d}/{size:>5d}]")'''
            losses_list.append(loss)
    return losses_list

for i in range(500):
    g=train_loop(DataLoader(model_fin.trd.dataset[0:1]), model_fin, loss_fn, optimizer)

    
test_loop(model_fin.ted, model_fin, loss_fn, True)
Test Error: 
 Accuracy: 81.0%, Avg loss: 0.504583 

for i in range(1000):
    g=train_loop(DataLoader(model_fin.trd.dataset[500:551]), model_fin, loss_fn, optimizer)

    
test_loop(model_fin.ted, model_fin, loss_fn, True)
Test Error: 
 Accuracy: 81.6%, Avg loss: 0.502643 

test_loop(model_fin.ted, model_fin, loss_fn, True)
Test Error: 
 Accuracy: 81.1%, Avg loss: 0.513521 

test_loop(model_fin.ted, model_fin, loss_fn, True)
Test Error: 
 Accuracy: 81.7%, Avg loss: 0.502616 

model_fin = NeuralNetwork([len(li68[0][0][0]), 40, 40, 6])
model_fin.base_set(li68, call = False)
for i in range(1000):
    g=train_loop(DataLoader(model_fin.trd.dataset[500:551]), model_fin, loss_fn, optimizer)

    
test_loop(model_fin.ted, model_fin, loss_fn, True)
Test Error: 
 Accuracy: 23.0%, Avg loss: 1.779795 

model_fin.roll(1)
Epoch 1

Test Error: 
 Accuracy: 55.3%, Avg loss: 1.227600 

1.7784268856048584
0.3433797359466553
test_loop(model_fin.ted, model_fin, loss_fn, True)
Test Error: 
 Accuracy: 54.9%, Avg loss: 1.254022 

for i in range(100):
    g=train_loop(DataLoader(model_fin.trd.dataset[500:1551]), model_fin, loss_fn, optimizer)

    
test_loop(model_fin.ted, model_fin, loss_fn, True)
Test Error: 
 Accuracy: 55.3%, Avg loss: 1.234377 

test_loop(model_fin.ted, model_fin, loss_fn, True)
Test Error: 
 Accuracy: 55.0%, Avg loss: 1.236642 

reinforce(1, alert=1, mod = model_fin, trd = DataLoader(model_fin.trd.dataset[500:1551]), ted = model_fin.ted, optim = optimizer, scheduler=scheduler)
Epoch 1

Test Error: 
 Accuracy: 55.3%, Avg loss: 1.234170 

1.4594159126281738
0.6245601177215576
reinforce(1, alert=1, mod = model_fin, trd = DataLoader(model_fin.trd.dataset[500:1551]), ted = model_fin.ted, optim = optimizer, scheduler=scheduler)
Epoch 1

Test Error: 
 Accuracy: 55.1%, Avg loss: 1.236844 

1.3229118585586548
0.6246457099914551
reinforce(1, alert=1, mod = model_fin, trd = DataLoader(model_fin.trd.dataset[500:5551]), ted = model_fin.ted, optim = optimizer, scheduler=scheduler)
Epoch 1

Test Error: 
 Accuracy: 55.1%, Avg loss: 1.235436 

1.3346033096313477
2.515005588531494

reinforce(1, alert=1, mod = model_fin, trd = DataLoader(model_fin.trd.dataset[0:15551]), ted = model_fin.ted, optim = optimizer, scheduler=scheduler)
Epoch 1

Test Error: 
 Accuracy: 54.9%, Avg loss: 1.228179 

2.8716914653778076
7.60757040977478
reinforce(1, alert=1, mod = model_fin, trd = DataLoader(model_fin.trd.dataset[i:i+1]), ted = model_fin.ted, optim = optimizer, scheduler=scheduler)
Epoch 1

Test Error: 
 Accuracy: 55.8%, Avg loss: 1.236011 

1.8092045783996582
0.10905766487121582
i
99
reinforce(1, alert=2, mod = model_fin, trd = DataLoader(model_fin.trd.dataset[i:i+1]), ted = model_fin.ted, optim = optimizer, scheduler=scheduler)
Epoch 1

Test Error: 
 Accuracy: 55.0%, Avg loss: 1.239602 

1.7367899417877197
0.06248950958251953
def reinforce(epochs, alert=1, mod = model, trd = train_dataloader, ted = test_dataloader, optim = optimizer, scheduler=scheduler):
        times = time.time()
        ale = False
        for t in range(epochs):
            if t % alert == alert-1:
                print(f"Epoch {t+1}\n")
                ale = True
            losses = train_loop(trd, mod, loss_fn, optim)
            scheduler.step()
            test_loop(ted, mod, loss_fn, ale)
            if ale == True and len(losses) != 0:
                print(sum(losses)/len(losses))
            elif ale == True and len(losses) == 0:
                print(sum(losses))
            ale = False

        print(time.time()-times)

        
reinforce(1, alert=2, mod = model_fin, trd = DataLoader(model_fin.trd.dataset[i:i+1]), ted = model_fin.ted, optim = optimizer, scheduler=scheduler)
0.03098011016845703
def reinforce(epochs, alert=1, mod = model, trd = train_dataloader, ted = test_dataloader, optim = optimizer, scheduler=scheduler):
        times = time.time()
        ale = False
        for t in range(epochs):
            if t % alert == alert-1:
                print(f"Epoch {t+1}\n")
                ale = True
            losses = train_loop(trd, mod, loss_fn, optim)
            scheduler.step()
            test_loop(ted, mod, loss_fn, ale)
            if ale == True and len(losses) != 0:
                print(sum(losses)/len(losses))
            elif ale == True and len(losses) == 0:
                print(sum(losses))
            ale = False

        #print(time.time()-times)

            
reinforce(1, alert=2, mod = model_fin, trd = DataLoader(model_fin.trd.dataset[i:i+1]), ted = model_fin.ted, optim = optimizer, scheduler=scheduler)
for i in range(100):
    reinforce(1, alert=2, mod = model_fin, trd = DataLoader(model_fin.trd.dataset[i:i+1]), ted = model_fin.ted, optim = optimizer, scheduler=scheduler)

    
for i in range(100, 3000):
    reinforce(1, alert=2, mod = model_fin, trd = DataLoader(model_fin.trd.dataset[i:i+1]), ted = model_fin.ted, optim = optimizer, scheduler=scheduler)

    
reinforce(1, alert=1, mod = model_fin, trd = DataLoader(model_fin.trd.dataset[i:i+1]), ted = model_fin.ted, optim = optimizer, scheduler=scheduler)
Epoch 1

Test Error: 
 Accuracy: 54.6%, Avg loss: 1.231474 

1.3079560995101929
reinforce(1, alert=1, mod = model_fin, trd = DataLoader(model_fin.trd.dataset[i:i+1]), ted = model_fin.ted, optim = optimizer, scheduler=scheduler)
Epoch 1

Test Error: 
 Accuracy: 56.1%, Avg loss: 1.212789 

1.697115182876587
reinforce(1, alert=1, mod = model_fin, trd = DataLoader(model_fin.trd.dataset[i:i+1]), ted = model_fin.ted, optim = optimizer, scheduler=scheduler)
Epoch 1

Test Error: 
 Accuracy: 54.7%, Avg loss: 1.225400 

1.5325394868850708
reinforce(1, alert=1, mod = model_fin, trd = DataLoader(model_fin.trd.dataset[i:5000]), ted = model_fin.ted, optim = optimizer, scheduler=scheduler)
Epoch 1

Test Error: 
 Accuracy: 55.7%, Avg loss: 1.224629 

1.8229020833969116
reinforce(1, alert=1, mod = model_fin, trd = DataLoader(model_fin.trd.dataset[i:5000]), ted = model_fin.ted, optim = optimizer, scheduler=scheduler)
Epoch 1

Test Error: 
 Accuracy: 54.9%, Avg loss: 1.223968 

2.7260167598724365
reinforce(1, alert=1, mod = model_fin, trd = DataLoader(model_fin.trd.dataset[i:i+1]), ted = model_fin.ted, optim = optimizer, scheduler=scheduler)
Epoch 1

Test Error: 
 Accuracy: 55.3%, Avg loss: 1.232461 

1.1196374893188477
for i in range(8000, 10000):
    reinforce(1, alert=1, mod = model_fin, trd = DataLoader(model_fin.trd.dataset[i:i+1]), ted = model_fin.ted, optim = optimizer, scheduler=scheduler)

    
Epoch 1

Test Error: 
 Accuracy: 55.0%, Avg loss: 1.232262 

1.5456347465515137
Epoch 1

Test Error: 
 Accuracy: 55.5%, Avg loss: 1.237148 

1.4853200912475586
Epoch 1

Test Error: 
 Accuracy: 55.3%, Avg loss: 1.229156 

1.6563644409179688
Epoch 1

Test Error: 
 Accuracy: 55.2%, Avg loss: 1.237061 

1.4418413639068604
Epoch 1

Test Error: 
 Accuracy: 55.7%, Avg loss: 1.228148 

2.3092775344848633
Epoch 1

Test Error: 
 Accuracy: 55.4%, Avg loss: 1.235606 

2.333247184753418
Epoch 1

Test Error: 
 Accuracy: 54.6%, Avg loss: 1.238414 

1.384661078453064
Epoch 1

Test Error: 
 Accuracy: 54.9%, Avg loss: 1.223072 

0.8378539681434631
Epoch 1

Test Error: 
 Accuracy: 54.5%, Avg loss: 1.241262 

1.220729947090149
Epoch 1

Test Error: 
 Accuracy: 54.8%, Avg loss: 1.215255 

0.6761060357093811
Epoch 1

Test Error: 
 Accuracy: 55.4%, Avg loss: 1.232651 

0.6820112466812134
Epoch 1

Test Error: 
 Accuracy: 55.6%, Avg loss: 1.219177 

2.6986074447631836
Epoch 1

Test Error: 
 Accuracy: 55.2%, Avg loss: 1.230298 

2.6770670413970947
Epoch 1

Test Error: 
 Accuracy: 54.9%, Avg loss: 1.237388 

1.5240569114685059
Epoch 1

Test Error: 
 Accuracy: 55.3%, Avg loss: 1.230734 

2.606424570083618
Epoch 1

Test Error: 
 Accuracy: 55.7%, Avg loss: 1.220957 

1.4246245622634888
Epoch 1

Test Error: 
 Accuracy: 54.4%, Avg loss: 1.238986 

0.38318073749542236
Epoch 1

Test Error: 
 Accuracy: 55.3%, Avg loss: 1.230720 

0.9208998680114746
Epoch 1

Test Error: 
 Accuracy: 55.3%, Avg loss: 1.241337 

0.6411141753196716
Epoch 1

Test Error: 
 Accuracy: 53.8%, Avg loss: 1.250541 

1.1597460508346558
Epoch 1

Test Error: 
 Accuracy: 55.4%, Avg loss: 1.237522 

0.5752781629562378
Epoch 1

Test Error: 
 Accuracy: 55.1%, Avg loss: 1.241270 

0.8801811337471008
Epoch 1

Test Error: 
 Accuracy: 54.3%, Avg loss: 1.239453 

1.3347562551498413
Epoch 1

Test Error: 
 Accuracy: 55.0%, Avg loss: 1.236302 
Traceback (most recent call last):
  File "<pyshell#378>", line 2, in <module>
    reinforce(1, alert=1, mod = model_fin, trd = DataLoader(model_fin.trd.dataset[i:i+1]), ted = model_fin.ted, optim = optimizer, scheduler=scheduler)
  File "<pyshell#364>", line 10, in reinforce
    test_loop(ted, mod, loss_fn, ale)
  File "C:\Users\KDCA\Desktop\IL\base\temp2.py", line 123, in test_loop
    print(f"Test Error: \n Accuracy: {(100*correct):>0.1f}%, Avg loss: {test_loss:>8f} \n")
KeyboardInterrupt
for i in range(8000, 10000):
    reinforce(1, alert=2, mod = model_fin, trd = DataLoader(model_fin.trd.dataset[i:i+1]), ted = model_fin.ted, optim = optimizer, scheduler=scheduler)

    
test_loop(model_fin.ted, model_fin, loss_fn, True)
Test Error: 
 Accuracy: 54.7%, Avg loss: 1.228018 

for i in range(8000, 10000):
    reinforce(1, alert=2, mod = model_fin, trd = model_fin.trd, ted = model_fin.ted, optim = optimizer, scheduler=scheduler)

    
Traceback (most recent call last):
  File "<pyshell#383>", line 2, in <module>
    reinforce(1, alert=2, mod = model_fin, trd = model_fin.trd, ted = model_fin.ted, optim = optimizer, scheduler=scheduler)
  File "<pyshell#364>", line 8, in reinforce
    losses = train_loop(trd, mod, loss_fn, optim)
  File "<pyshell#333>", line 4, in train_loop
    for batch, (X, y) in enumerate(dataloader):
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\utils\data\dataloader.py", line 624, in __next__
    with torch.autograd.profiler.record_function(self._profile_name):
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\autograd\profiler.py", line 488, in __enter__
    self.handle = torch.ops.profiler._record_function_enter(self.name, self.args)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\_ops.py", line 442, in __call__
    return self._op(*args, **kwargs or {})
KeyboardInterrupt
test_loop(model_fin.ted, model_fin, loss_fn, True)
Test Error: 
 Accuracy: 55.2%, Avg loss: 1.224381 

reinforce(1, alert=2, mod = model_fin, trd = model_fin.trd, ted = model_fin.ted, optim = optimizer, scheduler=scheduler)
test_loop(model_fin.ted, model_fin, loss_fn, True)
Test Error: 
 Accuracy: 54.5%, Avg loss: 1.239268 

i=5000
model_fin.trd = DataLoader(model_fin.trd.dataset[i:i+1])
model_fin.roll(1)
model_fin.roll(150)
Epoch 10

Test Error: 
 Accuracy: 32.4%, Avg loss: 1.497965 

0.16983366012573242
Epoch 20

Test Error: 
 Accuracy: 29.0%, Avg loss: 2.006469 

0.0526321679353714
Epoch 30

Test Error: 
 Accuracy: 28.4%, Avg loss: 2.413759 

2.2001793384552
Epoch 40

Test Error: 
 Accuracy: 28.1%, Avg loss: 2.704519 

2.024595260620117
Epoch 50

Test Error: 
 Accuracy: 28.7%, Avg loss: 2.801744 

0.005951895844191313
Epoch 60

Test Error: 
 Accuracy: 28.1%, Avg loss: 2.882260 

0.005725768860429525
Epoch 70

Test Error: 
 Accuracy: 28.6%, Avg loss: 2.913850 

0.0020601970609277487
Epoch 80

Test Error: 
 Accuracy: 28.0%, Avg loss: 2.976798 

0.004492428619414568
Traceback (most recent call last):
  File "<pyshell#390>", line 1, in <module>
    model_fin.roll(150)
  File "C:\Users\KDCA\Desktop\IL\base\temp2.py", line 82, in roll
    reinforce(epoch, alert, self, self.trd, self.ted, self.optim, self.sched)
  File "<pyshell#364>", line 10, in reinforce
    test_loop(ted, mod, loss_fn, ale)
  File "C:\Users\KDCA\Desktop\IL\base\temp2.py", line 116, in test_loop
    pred = model(X)
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
KeyboardInterrupt
>>> model_fin.trd = DataLoader(model_fin.trd.dataset[i:5000])
>>> model_fin.trd = DataLoader(model_fin.trd.dataset[i:10000])
>>> model_fin.roll(1)
>>> model_fin.roll(100)
Epoch 10

Test Error: 
 Accuracy: 28.5%, Avg loss: 2.995335 

0
Epoch 20

Test Error: 
 Accuracy: 28.5%, Avg loss: 3.016479 

0
Epoch 30

Test Error: 
 Accuracy: 28.2%, Avg loss: 3.006205 

0
Epoch 40

Test Error: 
 Accuracy: 28.6%, Avg loss: 2.996658 

0
Epoch 50

Test Error: 
 Accuracy: 28.7%, Avg loss: 2.995603 

0
Epoch 60

Test Error: 
 Accuracy: 28.6%, Avg loss: 2.983961 

0
Epoch 70

Test Error: 
 Accuracy: 28.0%, Avg loss: 3.040148 

0
Epoch 80

Test Error: 
 Accuracy: 28.6%, Avg loss: 2.993120 

0
Epoch 90

Test Error: 
 Accuracy: 28.2%, Avg loss: 3.016319 

0
Epoch 100

Test Error: 
 Accuracy: 28.4%, Avg loss: 3.020375 

0
model_fin.trd = DataLoader(model_fin.trd.dataset[0:10000])
model_fin.roll(100, 98)
Epoch 98

Test Error: 
 Accuracy: 27.6%, Avg loss: 3.048245 

0
model_fin.roll(100, 98)
Epoch 98

Test Error: 
 Accuracy: 28.2%, Avg loss: 3.013636 

0
