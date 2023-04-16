Python 3.10.9 (tags/v3.10.9:1dd9be6, Dec  6 2022, 20:01:21) [MSC v.1934 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import torch
import torch as nn
class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(RNN, self).__init__()

        
Traceback (most recent call last):
  File "<pyshell#5>", line 1, in <module>
    class RNN(nn.Module):
AttributeError: module 'torch' has no attribute 'Module'
class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(RNN, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.rnn = nn.RNN(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)

        
Traceback (most recent call last):
  File "<pyshell#11>", line 1, in <module>
    class RNN(nn.Module):
AttributeError: module 'torch' has no attribute 'Module'
class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(RNN, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.rnn = nn.RNN(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
    def forward(self, x):
        hO = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        out, _ = self.rnn(x, hO)
        out = self.fc(out[:, -1, :])
        return out

    
Traceback (most recent call last):
  File "<pyshell#18>", line 1, in <module>
    class RNN(nn.Module):
AttributeError: module 'torch' has no attribute 'Module'
import torch
import torch.nn as nn
class RNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(RNN, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.rnn = nn.RNN(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
    def forward(self, x):
        hO = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        out, _ = self.rnn(x, hO)
        out = self.fc(out[:, -1, :])
        return out

    
batch_size=4
seq_len=10
input_size=20
hidden_size=50
num_layers=2
output_size=1
model=RNN(input_size, hidden_size)
Traceback (most recent call last):
  File "<pyshell#29>", line 1, in <module>
    model=RNN(input_size, hidden_size)
TypeError: RNN.__init__() missing 2 required positional arguments: 'num_layers' and 'output_size'
model=RNN(input_size, hidden_size, num_layers, output_size)
inputs = torch.randn(batch_size, seq_len, input_size)
outputs = model(inputs)
print(outputs.size())
torch.Size([4, 1])
outputs
tensor([[-0.1059],
        [-0.3580],
        [-0.2088],
        [ 0.2058]], grad_fn=<AddmmBackward0>)
inputs
tensor([[[-0.6469, -0.6137, -0.8805,  0.4569, -0.9163, -0.0879, -0.6967,
           1.0499, -0.1082,  0.7818, -0.5288, -0.1021, -0.3882,  2.5187,
           0.5123,  1.9301,  1.0408, -1.6547, -0.8252, -0.5667],
         [ 1.2205, -0.0991, -1.2081,  0.0337, -0.4588,  0.4188, -0.5316,
          -2.3966,  0.7693,  1.0584, -1.1218, -1.0050, -0.6990,  1.0199,
           0.1725, -0.2113,  0.6300, -0.8422, -0.4340,  0.7001],
         [-0.1183, -0.5992, -0.6397, -0.0651, -0.6456,  0.5433,  1.5534,
          -0.8232, -2.2801,  0.3298, -0.8825,  0.2258,  1.4216, -0.4661,
          -0.2926, -0.0064,  0.8861,  0.2387,  0.6155,  1.0579],
         [-0.2991,  1.3904, -1.4507,  0.8872,  0.4281,  0.0870,  2.1480,
          -1.2235,  0.1195,  0.6037, -1.3754,  1.2834,  1.5780,  0.6762,
           0.6623, -1.0490, -1.6886,  1.9064, -0.1121, -0.6243],
         [-0.6982,  1.0134, -0.5366, -0.3773, -0.3446, -0.2066,  0.2905,
          -1.8194,  0.4765, -0.2872,  0.1149,  0.5095,  0.5972,  0.2085,
          -1.6389, -2.2156, -1.4857, -0.9652,  0.1592,  0.7002],
         [ 0.3484, -0.4666, -0.3200,  0.9416, -0.7533,  0.2700,  0.0037,
           0.3359, -0.2658,  0.3107, -0.3645, -2.1133, -0.5394, -1.0436,
          -0.8768, -1.2207,  0.4084, -0.8723,  1.4699, -0.1005],
         [-0.3929, -0.3157, -1.1751,  0.3770, -0.5374, -0.7542, -0.5225,
          -1.2983, -0.6248, -0.4904,  0.9140,  1.1537, -0.3567,  0.6933,
           1.0024, -1.6627, -0.0211, -0.0568, -0.5586,  0.4526],
         [-0.1434, -0.6142,  1.3701,  0.1566,  0.2782, -0.5518, -0.1592,
          -1.3457,  0.7925,  1.4351,  0.5190,  0.4321, -1.8259, -1.2045,
          -1.6807, -0.8376, -0.5863,  2.0465, -0.1803,  1.1342],
         [-1.9697,  1.1820,  0.4331,  0.5828, -0.1686,  0.9170,  0.7301,
           0.7779,  1.0420, -0.9678, -0.8791,  1.0909,  1.4381, -1.9214,
           1.0473, -0.0145, -0.9517,  1.7477, -1.4352, -2.0058],
         [ 1.0437,  1.7824, -1.2141,  1.8186,  0.1673, -0.4611,  1.2434,
          -0.8481,  0.2254,  0.4989, -0.4065, -0.2058, -0.5063,  1.3411,
          -0.4036, -1.3478, -0.0554, -0.1149, -0.9930,  1.0881]],

        [[ 0.8987, -0.1309,  0.2524, -2.4537,  0.9052, -0.7629, -0.2818,
           1.2909,  0.1811, -0.1973, -0.3149, -0.0373,  1.1155, -0.5001,
           1.4905, -1.7436, -0.2031,  0.0681, -0.9315,  0.0983],
         [ 1.2250, -0.9201, -1.2256, -0.0384,  0.3769,  1.1971,  1.7107,
          -0.3923,  0.8552,  0.1968,  0.3616,  1.5383,  0.3185, -0.4219,
           0.7048,  1.4993,  1.6552,  0.3642,  1.2916,  0.4003],
         [-1.1412, -1.8360,  0.5251,  0.1868,  0.6929, -1.0695, -1.2581,
          -0.4802, -0.1137,  0.3765, -0.3834, -0.2915,  1.8573, -0.4335,
          -0.7020, -0.9566,  0.2697, -0.6106,  0.2770, -1.3631],
         [ 1.0984,  0.5295, -0.0723,  0.2849, -1.5768,  1.2418, -0.8345,
           1.4599, -0.5646, -0.2925, -0.4371,  1.5965,  0.6484,  0.3377,
           0.3693,  1.3852, -1.4409,  0.3311, -0.7233,  0.2090],
         [-2.0716,  1.1571,  0.0821,  0.3492, -0.3292,  1.2859, -1.0450,
           0.4896, -0.9759, -0.1052,  0.1754,  2.0206,  1.1614, -0.5227,
          -1.0814,  1.0268, -2.1760,  0.9461,  0.0357,  1.1827],
         [-2.5295, -0.1726, -0.7022,  0.2518, -0.4683, -0.6524, -0.1398,
          -0.7953,  0.3842, -1.6775,  1.6664,  0.9478,  2.4650, -1.3227,
          -0.7790,  0.2002, -0.5015, -1.0129, -0.4471, -0.0612],
         [ 0.7688,  0.9110,  0.9894,  0.0291,  1.0699,  1.2394, -0.5011,
          -0.3820,  0.7526, -0.7526,  0.1917, -1.3163, -1.3927,  0.5075,
           0.6881, -0.4635,  1.7487, -0.9990,  1.4655, -1.0587],
         [ 2.1116,  1.4838, -0.3019, -0.1527, -2.6511, -0.6577,  0.3419,
          -0.4427, -1.1661, -0.7731, -1.0871,  0.9924, -2.9771, -0.3055,
          -2.3005,  0.0676, -0.7173, -0.8665,  0.3163,  1.3369],
         [-0.8292, -0.4171,  0.2287, -0.0245,  0.1676,  1.2914, -1.4310,
          -1.8488, -0.0923,  0.0946,  0.4077,  0.6957, -0.5767,  0.6328,
          -1.5296,  1.0664,  0.0893, -0.1291, -0.4318,  0.1260],
         [ 1.0357,  1.5198,  0.2548,  0.0417,  0.4352,  0.0620, -0.1637,
          -0.3994,  1.4705,  0.0788,  0.9436, -1.2832, -0.6035,  0.4645,
          -0.2239,  0.4159,  0.6468,  1.0375, -0.4851,  1.1776]],

        [[ 0.3315,  0.8731,  0.0847,  0.4728, -0.9616, -1.8955, -0.4956,
           0.3727, -0.3107, -0.2026,  0.9915, -1.2217, -2.1992,  0.5445,
          -0.7997,  1.4994,  0.1217, -0.3241,  0.7063, -0.2027],
         [ 0.2355, -0.5440, -2.0614,  0.1699, -0.8787, -1.0853, -1.3565,
           0.0881,  1.8442, -0.5630,  0.6450,  0.1380,  0.5847, -0.5879,
          -0.4366,  0.0824,  0.4971,  0.8195,  0.2456,  0.4408],
         [-1.7475,  0.0922, -0.1243, -1.8817, -0.4202, -1.2658,  1.4802,
          -1.8689, -2.2364, -1.1220, -0.8686,  0.5376, -0.5687, -0.4858,
          -1.2306, -0.4379,  0.8966,  1.7699, -0.7777,  0.1856],
         [ 0.4782,  1.0188, -0.0503, -0.2164,  0.1772,  1.0668, -0.9152,
           2.0104, -0.9817,  1.3657, -0.1656,  0.4455,  0.7184, -0.5457,
          -0.1483,  1.1771,  1.6149, -0.3046,  1.1686,  0.4387],
         [ 0.5563, -2.0057, -0.3263,  0.9143,  1.1034,  0.5405, -0.0201,
           1.6113, -0.8249, -0.1580,  0.7641, -0.1081, -0.9403,  1.7840,
          -0.2047,  0.1705, -0.3056,  1.1345, -2.0110, -0.6321],
         [-0.5367, -0.9728, -1.1524, -0.1924, -0.3512, -0.7980,  0.4623,
           1.5891,  1.1978,  0.6304,  0.2953, -0.3055,  1.1387, -0.9105,
          -0.7215,  1.7649, -1.9810,  0.7875, -0.5242, -1.4802],
         [ 1.4318, -0.8700, -0.4824,  1.8892,  0.8046, -1.6896, -1.4205,
          -0.8672,  0.6260, -0.8977,  0.6302,  0.3766, -0.0690, -0.2531,
          -1.6147, -0.3007,  0.6710,  1.3584, -0.2108,  0.4051],
         [-0.7618, -0.7317,  0.3685,  0.6136, -1.7014,  0.4149,  0.4553,
           2.7064, -0.3545,  1.0258, -0.7858,  0.6354, -0.6033, -0.7624,
          -0.5681, -0.1476,  2.2990,  0.7168, -1.5145, -1.6154],
         [ 0.0778, -1.2114,  1.0329, -1.0894,  0.8885,  1.4655, -1.1734,
           0.8349, -1.5795,  0.0258,  0.4350,  0.4812,  1.6636,  0.8784,
          -1.8479,  1.0396, -0.8803,  0.3494, -1.2882,  0.2929],
         [-1.2517, -0.1028,  0.1206, -0.1360,  0.5617,  1.5444,  0.7313,
          -0.3552,  2.5998,  1.1569, -0.8457,  0.8497,  0.1911,  0.1431,
          -2.2066,  1.1078, -1.6007,  0.3924, -0.8596,  1.4012]],

        [[ 0.7791, -1.4363, -0.3170, -0.2647,  0.7059, -0.4824, -0.2435,
           1.4958,  2.8395,  2.0258,  1.3662, -0.0564,  0.4728,  0.3497,
          -0.4701,  1.0693, -2.2388, -0.2721, -0.6303, -0.1185],
         [ 1.6850, -0.9827,  1.5038,  1.0821,  1.8015, -0.7930,  0.0408,
           0.1498,  0.7709,  0.4399,  1.2982,  1.3955,  0.7971, -1.2176,
           0.1876, -0.0602, -0.5287,  0.6802,  0.8210,  0.5462],
         [-1.8115, -0.9458,  0.5228, -1.5668,  0.9167,  1.2615,  0.3108,
           0.2883, -1.9938,  0.1429, -0.3074, -0.0889, -0.3617, -1.2854,
          -2.5080, -0.2745,  0.7252,  0.5520, -0.2277,  1.3536],
         [-0.5420, -0.9397, -1.1302, -1.3969,  0.5704,  0.3347,  0.6905,
           0.3421, -0.4317, -1.1829, -1.5380, -0.2934, -1.8247, -0.6256,
           1.1189,  0.2436, -0.8385, -1.1066,  1.9405, -0.7086],
         [ 0.5324, -1.8138,  0.5168,  0.8252,  1.0022,  2.1821, -1.6674,
          -0.6804, -0.4048,  0.1847, -0.4020,  1.1249,  2.1585,  0.1598,
          -0.2848, -0.9076,  0.3626, -1.3445, -0.3172,  0.0411],
         [ 0.7981, -0.0241, -0.6323,  0.2055,  0.8292, -2.3140, -1.0324,
           1.1629,  1.7645, -0.5018,  0.5348,  1.2490,  0.6096,  0.2363,
          -0.0857, -0.4722,  1.0928, -1.7871, -0.0576, -0.4892],
         [-1.7883,  0.3834, -2.4874,  0.7833, -0.8296,  0.3980, -1.1301,
           0.0845, -2.2410, -1.2816, -1.2275,  0.2840,  0.4844, -0.0858,
          -1.4258, -0.7304,  0.0376, -0.6901, -0.9249,  0.1444],
         [-2.0298,  0.4953, -0.1355, -1.3905, -2.4790,  0.5270, -1.8691,
          -0.9837, -0.9385,  0.9598, -1.4750,  0.0893,  0.5676,  0.0565,
           0.9602, -0.6582, -1.1719, -0.1657, -0.3038,  0.1792],
         [-0.1594,  0.6372, -0.0334,  1.0876,  0.0666,  0.5352,  0.6645,
          -0.0766,  1.0573,  0.0635, -0.0660,  0.0266, -1.1399, -0.3609,
          -0.5048, -0.2553,  1.4730, -0.3849, -0.4600,  1.3315],
         [-0.3809,  0.4982,  1.5053,  0.9217,  1.8013,  0.1986,  0.1798,
          -0.4768,  1.6256,  0.0317, -1.5942,  0.7043,  1.3084, -0.8652,
           0.7658, -1.4532,  0.5592,  0.7976,  0.6506, -0.4631]]])
outputs = model(inputs)
outputs
tensor([[-0.1059],
        [-0.3580],
        [-0.2088],
        [ 0.2058]], grad_fn=<AddmmBackward0>)
outputs = model(inputs)
outputs
tensor([[-0.1059],
        [-0.3580],
        [-0.2088],
        [ 0.2058]], grad_fn=<AddmmBackward0>)
print(inputs.size())
torch.Size([4, 10, 20])
model
RNN(
  (rnn): RNN(20, 50, num_layers=2, batch_first=True)
  (fc): Linear(in_features=50, out_features=1, bias=True)
)
inputs = torch.randn(1, 50, 500)
outputs = model(inputs)
Traceback (most recent call last):
  File "<pyshell#43>", line 1, in <module>
    outputs = model(inputs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "<pyshell#22>", line 10, in forward
    out, _ = self.rnn(x, hO)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\rnn.py", line 472, in forward
    self.check_forward_args(input, hx, batch_sizes)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\rnn.py", line 234, in check_forward_args
    self.check_input(input, batch_sizes)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\rnn.py", line 210, in check_input
    raise RuntimeError(
RuntimeError: input.size(-1) must be equal to input_size. Expected 20, got 500
model=RNN(500, hidden_size, num_layers, output_size)
outputs = model(inputs)
outputs
tensor([[0.0121]], grad_fn=<AddmmBackward0>)
inputs = torch.randn(5, 15, 2)

model=RNN(2, hidden_size, num_layers, output_size)
outputs = model(inputs)
outputs
tensor([[-0.0126],
        [-0.0941],
        [-0.0339],
        [ 0.0496],
        [ 0.0491]], grad_fn=<AddmmBackward0>)
inputs
tensor([[[-1.4475e+00,  1.3553e+00],
         [ 1.2171e+00,  7.3388e-01],
         [-6.0688e-01,  7.7668e-01],
         [-3.7107e-01, -1.8990e+00],
         [-1.0673e+00, -2.7027e-01],
         [-1.3637e+00,  7.4425e-01],
         [-1.6839e+00,  2.5446e-01],
         [-5.0761e-01,  1.7664e-01],
         [-4.1866e-01,  2.4534e-01],
         [-1.0286e-01,  3.4190e-01],
         [-6.1205e-01, -1.0883e+00],
         [ 5.7082e-01, -2.8970e-01],
         [ 1.2437e+00,  5.5907e-01],
         [-7.6035e-01,  1.9441e-02],
         [ 7.7514e-01,  4.0291e-01]],

        [[ 5.9050e-01, -2.7976e+00],
         [ 5.3773e-01, -9.3368e-01],
         [-2.1136e-01,  1.8768e+00],
         [-1.4462e+00,  1.0041e+00],
         [-9.0109e-01,  2.2956e-01],
         [ 1.4362e-01, -1.9794e+00],
         [-2.1423e-01,  1.5210e-01],
         [-6.5917e-01,  1.0760e+00],
         [-1.0854e+00,  4.6844e-01],
         [-3.3539e-01, -3.7498e-01],
         [-5.9978e-01,  7.0830e-01],
         [-1.1594e-01, -5.5916e-02],
         [ 1.3799e+00, -1.9360e+00],
         [-8.1015e-02,  6.1486e-01],
         [-9.7374e-01,  1.4932e+00]],

        [[-9.4624e-01,  4.0760e-01],
         [ 1.2327e+00, -6.1088e-01],
         [ 4.7903e-02, -9.1784e-01],
         [-1.4998e+00,  2.8782e-01],
         [-6.5562e-01, -5.4681e-01],
         [ 1.5212e+00, -2.4126e+00],
         [-4.8817e-01, -1.1358e+00],
         [-3.8306e-01, -1.6222e+00],
         [ 9.2194e-01,  5.9663e-01],
         [-4.1421e-01,  5.5451e-02],
         [-6.0787e-01,  5.7554e-01],
         [ 9.5946e-01, -2.3835e+00],
         [ 8.5069e-01, -3.9951e-02],
         [-1.4857e+00, -1.2926e-01],
         [ 1.7638e-01, -2.8390e-01]],

        [[-1.4506e-03, -8.2724e-01],
         [ 1.6426e+00,  1.3501e+00],
         [-4.4506e-01, -1.6592e+00],
         [ 3.3447e-01,  3.4101e+00],
         [-8.3859e-01,  2.6552e-01],
         [ 1.2240e+00,  1.0687e+00],
         [ 1.6378e+00, -3.8466e-01],
         [ 4.5848e-01,  3.7649e-01],
         [-5.0275e-02,  7.7763e-03],
         [-3.4279e-01,  3.5672e-01],
         [ 3.2601e-01, -8.8878e-01],
         [-2.5179e-01, -9.6033e-01],
         [ 6.4678e-01, -3.6247e-01],
         [-1.0926e+00,  2.8411e-01],
         [-7.2613e-01, -9.3239e-01]],

        [[ 3.0054e-01,  1.5840e-01],
         [ 6.0473e-01, -3.9451e-01],
         [-1.1609e+00,  1.3570e+00],
         [-3.4541e-01, -1.2346e+00],
         [ 2.6773e-02, -1.9065e+00],
         [-4.5832e-01,  6.5758e-01],
         [-7.9729e-01, -4.6017e-01],
         [ 1.2776e+00, -1.1476e-01],
         [-1.2252e+00, -5.2133e-01],
         [-1.0236e+00, -2.1992e-01],
         [-1.0143e+00,  4.4596e-01],
         [-4.9188e-01, -1.6673e-01],
         [-6.6770e-01, -2.0825e+00],
         [ 2.2099e-01,  2.3116e-01],
         [ 7.1432e-01, -2.1626e-01]]])
inputs = torch.randn(1, 15, 2)
inputs
tensor([[[ 0.5292, -1.2654],
         [ 0.7111, -1.4124],
         [-2.4075,  1.1628],
         [-0.3586,  1.2732],
         [-0.6272,  1.2893],
         [ 0.8396, -0.4039],
         [-0.4989, -1.0699],
         [ 0.1614, -0.4640],
         [ 0.5178,  0.3888],
         [ 1.5184,  1.1330],
         [-0.7590,  0.6515],
         [-0.1199,  1.4429],
         [-0.5991, -0.2419],
         [-1.4697,  0.7405],
         [-0.4014, -0.0946]]])
outputs = model(inputs)
outputs
tensor([[-0.0171]], grad_fn=<AddmmBackward0>)
inputs = torch.randn(1, 15, 2)
outputs = model(inputs)
outputs
tensor([[0.0692]], grad_fn=<AddmmBackward0>)
model=Linear(2, hidden_size, num_layers, output_size)
Traceback (most recent call last):
  File "<pyshell#60>", line 1, in <module>
    model=Linear(2, hidden_size, num_layers, output_size)
NameError: name 'Linear' is not defined
model=nn.Linear(2, hidden_size, num_layers, output_size)
Traceback (most recent call last):
  File "<pyshell#61>", line 1, in <module>
    model=nn.Linear(2, hidden_size, num_layers, output_size)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\linear.py", line 96, in __init__
    self.weight = Parameter(torch.empty((out_features, in_features), **factory_kwargs))
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\cuda\__init__.py", line 221, in _lazy_init
    raise AssertionError("Torch not compiled with CUDA enabled")
AssertionError: Torch not compiled with CUDA enabled
model=nn.Linear(2, hidden_size, num_layers, output_size)
Traceback (most recent call last):
  File "<pyshell#62>", line 1, in <module>
    model=nn.Linear(2, hidden_size, num_layers, output_size)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\linear.py", line 96, in __init__
    self.weight = Parameter(torch.empty((out_features, in_features), **factory_kwargs))
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\cuda\__init__.py", line 221, in _lazy_init
    raise AssertionError("Torch not compiled with CUDA enabled")
AssertionError: Torch not compiled with CUDA enabled
model
RNN(
  (rnn): RNN(2, 50, num_layers=2, batch_first=True)
  (fc): Linear(in_features=50, out_features=1, bias=True)
)
model=nn.Linear(2, hidden_size, num_layers, output_size)
Traceback (most recent call last):
  File "<pyshell#64>", line 1, in <module>
    model=nn.Linear(2, hidden_size, num_layers, output_size)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\linear.py", line 96, in __init__
    self.weight = Parameter(torch.empty((out_features, in_features), **factory_kwargs))
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\cuda\__init__.py", line 221, in _lazy_init
    raise AssertionError("Torch not compiled with CUDA enabled")
AssertionError: Torch not compiled with CUDA enabled
nn.RNN(20, 20)
RNN(20, 20)
nn.RNN(20, 50)
RNN(20, 50)

=============== RESTART: C:\Users\KDCA\Desktop\IL\base\network.py ==============
Network System stabilized
Successful Network Application, Test start
Epoch 10

Test Error: 
 Accuracy: 84.0%, Avg loss: 0.424352 

0.1866411417722702
Epoch 20

Test Error: 
 Accuracy: 85.3%, Avg loss: 0.377197 

0.15964370965957642
Epoch 30

Test Error: 
 Accuracy: 85.7%, Avg loss: 0.358206 

0.13667628169059753
Epoch 40

Test Error: 
 Accuracy: 85.9%, Avg loss: 0.348086 

0.1211749017238617
Epoch 50

Test Error: 
 Accuracy: 86.4%, Avg loss: 0.341697 

0.1108778566122055
Epoch 60

Test Error: 
 Accuracy: 86.7%, Avg loss: 0.339301 

0.10075513273477554
Epoch 70

Test Error: 
 Accuracy: 86.8%, Avg loss: 0.338749 

0.09170271456241608
Epoch 80

Test Error: 
 Accuracy: 86.8%, Avg loss: 0.338912 

0.08286281675100327
Epoch 90

Test Error: 
 Accuracy: 86.9%, Avg loss: 0.339757 

0.07534725219011307
Epoch 100

Test Error: 
 Accuracy: 87.1%, Avg loss: 0.340002 

0.06913146376609802
Epoch 110

Test Error: 
 Accuracy: 87.0%, Avg loss: 0.339797 

0.06400388479232788
Epoch 120

Test Error: 
 Accuracy: 87.1%, Avg loss: 0.338801 

0.05990832298994064
Traceback (most recent call last):
  File "C:\Users\KDCA\Desktop\IL\base\network.py", line 357, in <module>
    model_fin.roll(150, 10)
  File "C:\Users\KDCA\Desktop\IL\base\network.py", line 165, in roll
    reinforce(epoch, alert, self, DataLoader(self.trd.dataset[first:last+1], batch_size=(last-first)//100), self.ted, self.optim, self.sched)
  File "C:\Users\KDCA\Desktop\IL\base\network.py", line 221, in reinforce
    losses = train_loop(trd, mod, loss_fn, optim)
  File "C:\Users\KDCA\Desktop\IL\base\network.py", line 177, in train_loop
    pred = model.forward(X)
  File "C:\Users\KDCA\Desktop\IL\base\network.py", line 108, in forward
    rnn_out, hidden = self.stack[i](toinput.unsqueeze(1))
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\rnn.py", line 476, in forward
    result = _VF.rnn_tanh(input, hx, self._flat_weights, self.bias, self.num_layers,
KeyboardInterrupt
with open(paths+'\\\\'+'mobs_data.json') as f:
            t = json.load(f)

                          
t[0][0]
                          
[50, 50]
t[0]
                          
[[50, 50]]
t[30]
                          
[[2, 41], [50, 50]]
t[20]
                          
[[50, 50]]
nn.RNN(2, 20, 2, 1)(torch.tensor(t[20]))
                          
Traceback (most recent call last):
  File "<pyshell#73>", line 1, in <module>
    nn.RNN(2, 20, 2, 1)(torch.tensor(t[20]))
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\rnn.py", line 476, in forward
    result = _VF.rnn_tanh(input, hx, self._flat_weights, self.bias, self.num_layers,
TypeError: rnn_tanh() received an invalid combination of arguments - got (Tensor, Tensor, list, int, int, float, bool, bool, bool), but expected one of:
 * (Tensor data, Tensor batch_sizes, Tensor hx, tuple of Tensors params, bool has_biases, int num_layers, float dropout, bool train, bool bidirectional)
      didn't match because some of the arguments have invalid types: ([32;1mTensor[0m, [32;1mTensor[0m, [31;1mlist[0m, [31;1mint[0m, [31;1mint[0m, [31;1mfloat[0m, [31;1mbool[0m, [32;1mbool[0m, [32;1mbool[0m)
 * (Tensor input, Tensor hx, tuple of Tensors params, bool has_biases, int num_layers, float dropout, bool train, bool bidirectional, bool batch_first)
      didn't match because some of the arguments have invalid types: ([32;1mTensor[0m, [32;1mTensor[0m, [31;1mlist[0m, [31;1mint[0m, [32;1mint[0m, [32;1mfloat[0m, [32;1mbool[0m, [32;1mbool[0m, [32;1mbool[0m)

nn.RNN(2, 20, 2, 1)(torch.tensor(t[20]))
                          
Traceback (most recent call last):
  File "<pyshell#74>", line 1, in <module>
    nn.RNN(2, 20, 2, 1)(torch.tensor(t[20]))
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\rnn.py", line 476, in forward
    result = _VF.rnn_tanh(input, hx, self._flat_weights, self.bias, self.num_layers,
TypeError: rnn_tanh() received an invalid combination of arguments - got (Tensor, Tensor, list, int, int, float, bool, bool, bool), but expected one of:
 * (Tensor data, Tensor batch_sizes, Tensor hx, tuple of Tensors params, bool has_biases, int num_layers, float dropout, bool train, bool bidirectional)
      didn't match because some of the arguments have invalid types: ([32;1mTensor[0m, [32;1mTensor[0m, [31;1mlist[0m, [31;1mint[0m, [31;1mint[0m, [31;1mfloat[0m, [31;1mbool[0m, [32;1mbool[0m, [32;1mbool[0m)
 * (Tensor input, Tensor hx, tuple of Tensors params, bool has_biases, int num_layers, float dropout, bool train, bool bidirectional, bool batch_first)
      didn't match because some of the arguments have invalid types: ([32;1mTensor[0m, [32;1mTensor[0m, [31;1mlist[0m, [31;1mint[0m, [32;1mint[0m, [32;1mfloat[0m, [32;1mbool[0m, [32;1mbool[0m, [32;1mbool[0m)

nn.RNN(2, 20, 2, 1)(torch.tensor(t[20]))
                          
Traceback (most recent call last):
  File "<pyshell#75>", line 1, in <module>
    nn.RNN(2, 20, 2, 1)(torch.tensor(t[20]))
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\rnn.py", line 476, in forward
    result = _VF.rnn_tanh(input, hx, self._flat_weights, self.bias, self.num_layers,
TypeError: rnn_tanh() received an invalid combination of arguments - got (Tensor, Tensor, list, int, int, float, bool, bool, bool), but expected one of:
 * (Tensor data, Tensor batch_sizes, Tensor hx, tuple of Tensors params, bool has_biases, int num_layers, float dropout, bool train, bool bidirectional)
      didn't match because some of the arguments have invalid types: ([32;1mTensor[0m, [32;1mTensor[0m, [31;1mlist[0m, [31;1mint[0m, [31;1mint[0m, [31;1mfloat[0m, [31;1mbool[0m, [32;1mbool[0m, [32;1mbool[0m)
 * (Tensor input, Tensor hx, tuple of Tensors params, bool has_biases, int num_layers, float dropout, bool train, bool bidirectional, bool batch_first)
      didn't match because some of the arguments have invalid types: ([32;1mTensor[0m, [32;1mTensor[0m, [31;1mlist[0m, [31;1mint[0m, [32;1mint[0m, [32;1mfloat[0m, [32;1mbool[0m, [32;1mbool[0m, [32;1mbool[0m)

nn.RNN(2, 20, 2, 1)
                          
RNN(2, 20, num_layers=2, bias=1)
nn.RNN(2, 20, )
                          
RNN(2, 20)
nn.RNN(2, 20, 2, 1)
                          
RNN(2, 20, num_layers=2, bias=1)
nn.RNN(2, 20, 2, 1)
                          
RNN(2, 20, num_layers=2, bias=1)
nn.RNN(2, 20, 2, 1)
                          
RNN(2, 20, num_layers=2, bias=1)
nn.RNN(2, 20, 2, 1)
                          
RNN(2, 20, num_layers=2, bias=1)
nn.RNN(2, 20, 2, 1)
                          
RNN(2, 20, num_layers=2, bias=1)
nn.RNN(2, 20, 2, 1)
                          
RNN(2, 20, num_layers=2, bias=1)
nn.RNN(2, 20, 2, 1)
                          
RNN(2, 20, num_layers=2, bias=1)
nn.RNN(2, 20, 2, 1)(5)
                          
Traceback (most recent call last):
  File "<pyshell#85>", line 1, in <module>
    nn.RNN(2, 20, 2, 1)(5)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\rnn.py", line 444, in forward
    is_batched = input.dim() == 3
AttributeError: 'int' object has no attribute 'dim'
nn.RNN(2, 20, 2, 1)(torch.tensor(t[20]))
Traceback (most recent call last):
  File "<pyshell#86>", line 1, in <module>
    nn.RNN(2, 20, 2, 1)(torch.tensor(t[20]))
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\rnn.py", line 476, in forward
    result = _VF.rnn_tanh(input, hx, self._flat_weights, self.bias, self.num_layers,
TypeError: rnn_tanh() received an invalid combination of arguments - got (Tensor, Tensor, list, int, int, float, bool, bool, bool), but expected one of:
 * (Tensor data, Tensor batch_sizes, Tensor hx, tuple of Tensors params, bool has_biases, int num_layers, float dropout, bool train, bool bidirectional)
      didn't match because some of the arguments have invalid types: ([32;1mTensor[0m, [32;1mTensor[0m, [31;1mlist[0m, [31;1mint[0m, [31;1mint[0m, [31;1mfloat[0m, [31;1mbool[0m, [32;1mbool[0m, [32;1mbool[0m)
 * (Tensor input, Tensor hx, tuple of Tensors params, bool has_biases, int num_layers, float dropout, bool train, bool bidirectional, bool batch_first)
      didn't match because some of the arguments have invalid types: ([32;1mTensor[0m, [32;1mTensor[0m, [31;1mlist[0m, [31;1mint[0m, [32;1mint[0m, [32;1mfloat[0m, [32;1mbool[0m, [32;1mbool[0m, [32;1mbool[0m)

nn.RNN(2, 20, 2, 1)(torch.randn(2, 2, 20))
                          
Traceback (most recent call last):
  File "<pyshell#87>", line 1, in <module>
    nn.RNN(2, 20, 2, 1)(torch.randn(2, 2, 20))
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\rnn.py", line 472, in forward
    self.check_forward_args(input, hx, batch_sizes)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\rnn.py", line 234, in check_forward_args
    self.check_input(input, batch_sizes)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\rnn.py", line 210, in check_input
    raise RuntimeError(
RuntimeError: input.size(-1) must be equal to input_size. Expected 2, got 20
nn.RNN(2, 20, 2, 1)(torch.randn(2, 20, 2))
Traceback (most recent call last):
  File "<pyshell#88>", line 1, in <module>
    nn.RNN(2, 20, 2, 1)(torch.randn(2, 20, 2))
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\rnn.py", line 476, in forward
    result = _VF.rnn_tanh(input, hx, self._flat_weights, self.bias, self.num_layers,
TypeError: rnn_tanh() received an invalid combination of arguments - got (Tensor, Tensor, list, int, int, float, bool, bool, bool), but expected one of:
 * (Tensor data, Tensor batch_sizes, Tensor hx, tuple of Tensors params, bool has_biases, int num_layers, float dropout, bool train, bool bidirectional)
      didn't match because some of the arguments have invalid types: ([32;1mTensor[0m, [32;1mTensor[0m, [31;1mlist[0m, [31;1mint[0m, [31;1mint[0m, [31;1mfloat[0m, [31;1mbool[0m, [32;1mbool[0m, [32;1mbool[0m)
 * (Tensor input, Tensor hx, tuple of Tensors params, bool has_biases, int num_layers, float dropout, bool train, bool bidirectional, bool batch_first)
      didn't match because some of the arguments have invalid types: ([32;1mTensor[0m, [32;1mTensor[0m, [31;1mlist[0m, [31;1mint[0m, [32;1mint[0m, [32;1mfloat[0m, [32;1mbool[0m, [32;1mbool[0m, [32;1mbool[0m)

nn.RNN(2, 20, 2)
                          
RNN(2, 20, num_layers=2)
model=nn.RNN(2, 20, 2)
                          
model(torch.randn(2, 20, 2))
                          


=============== RESTART: C:\Users\KDCA\Desktop\IL\base\network.py ==============
Network System stabilized
Successful Network Application, Test start
Traceback (most recent call last):
  File "C:\Users\KDCA\Desktop\IL\base\network.py", line 370, in <module>
    model_fin.roll(150, 10)
  File "C:\Users\KDCA\Desktop\IL\base\network.py", line 178, in roll
    reinforce(epoch, alert, self, DataLoader(self.trd.dataset[first:last+1], batch_size=(last-first)//100), self.ted, self.optim, self.sched)
  File "C:\Users\KDCA\Desktop\IL\base\network.py", line 234, in reinforce
    losses = train_loop(trd, mod, loss_fn, optim)
  File "C:\Users\KDCA\Desktop\IL\base\network.py", line 190, in train_loop
    pred = model.forward(X)
  File "C:\Users\KDCA\Desktop\IL\base\network.py", line 121, in forward
    rnn_out, hidden = self.stack[i](toinput.unsqueeze(1))
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\rnn.py", line 476, in forward
    result = _VF.rnn_tanh(input, hx, self._flat_weights, self.bias, self.num_layers,
KeyboardInterrupt
return
SyntaxError: 'return' outside function
torch
<module 'torch' from 'C:\\Users\\KDCA\\AppData\\Local\\Programs\\Python\\Python310\\lib\\site-packages\\torch\\__init__.py'>
seqRNN(2, 20, 2, 1)
Traceback (most recent call last):
  File "<pyshell#94>", line 1, in <module>
    seqRNN(2, 20, 2, 1)
  File "C:\Users\KDCA\Desktop\IL\base\network.py", line 23, in __init__
    super(RNN, self).__init__()
NameError: name 'RNN' is not defined

=============== RESTART: C:\Users\KDCA\Desktop\IL\base\network.py ==============
Network System stabilized
Successful Network Application, Test start
Epoch 10

Traceback (most recent call last):
  File "C:\Users\KDCA\Desktop\IL\base\network.py", line 370, in <module>
    model_fin.roll(150, 10)
  File "C:\Users\KDCA\Desktop\IL\base\network.py", line 178, in roll
    reinforce(epoch, alert, self, DataLoader(self.trd.dataset[first:last+1], batch_size=(last-first)//100), self.ted, self.optim, self.sched)
  File "C:\Users\KDCA\Desktop\IL\base\network.py", line 234, in reinforce
    losses = train_loop(trd, mod, loss_fn, optim)
  File "C:\Users\KDCA\Desktop\IL\base\network.py", line 190, in train_loop
    pred = model.forward(X)
  File "C:\Users\KDCA\Desktop\IL\base\network.py", line 121, in forward
    rnn_out, hidden = self.stack[i](toinput.unsqueeze(1))
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\rnn.py", line 476, in forward
    result = _VF.rnn_tanh(input, hx, self._flat_weights, self.bias, self.num_layers,
KeyboardInterrupt
seqRNN
                          
<class '__main__.seqRNN'>
seqRNN(2, 20, 2, 1)
                          
Traceback (most recent call last):
  File "<pyshell#96>", line 1, in <module>
    seqRNN(2, 20, 2, 1)
  File "C:\Users\KDCA\Desktop\IL\base\network.py", line 23, in __init__
    super(nn.RNN, self).__init__()
TypeError: super(type, obj): obj must be an instance or subtype of type
class seqRNN(nn.Module):
    def __init__(self, input_size, hidden_size, num_layers, output_size):
        super(seqRNN, self).__init__()
        self.hidden_size = hidden_size
        self.num_layers = num_layers
        self.rnn = nn.RNN(input_size, hidden_size, num_layers, batch_first=True)
        self.fc = nn.Linear(hidden_size, output_size)
    def forward(self, x):
        hO = torch.zeros(self.num_layers, x.size(0), self.hidden_size).to(x.device)
        out, _ = self.rnn(x, hO)
        out = self.fc(out[:, -1, :])
        return out

    
seqRNN(2, 20, 2, 1)
seqRNN(
  (rnn): RNN(2, 20, num_layers=2, batch_first=True)
  (fc): Linear(in_features=20, out_features=1, bias=True)
)
seqRNN(2, 20, 2, 1) = 5
SyntaxError: cannot assign to function call here. Maybe you meant '==' instead of '='?
with open(paths+'\\\\'+'mobs_data.json') as f:
            t = json.load(f)

            
seqRNN(2, 20, 2, 1)(torch.randn(2, 20, 2))
tensor([[0.1732],
        [0.2443]], grad_fn=<AddmmBackward0>)
seqRNN(2, 20, 2, 1)(torch.randn(2, 20, 1))
Traceback (most recent call last):
  File "<pyshell#104>", line 1, in <module>
    seqRNN(2, 20, 2, 1)(torch.randn(2, 20, 1))
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "<pyshell#98>", line 10, in forward
    out, _ = self.rnn(x, hO)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\rnn.py", line 472, in forward
    self.check_forward_args(input, hx, batch_sizes)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\rnn.py", line 234, in check_forward_args
    self.check_input(input, batch_sizes)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\rnn.py", line 210, in check_input
    raise RuntimeError(
RuntimeError: input.size(-1) must be equal to input_size. Expected 2, got 1
seqRNN(2, 20, 2, 1)(torch.randn(2, 20, 2))
tensor([[0.2169],
        [0.1897]], grad_fn=<AddmmBackward0>)
seqRNN(2, 20, 2, 3)(torch.randn(2, 20, 2))
tensor([[-0.3464, -0.1823, -0.0106],
        [-0.4589, -0.2567, -0.0329]], grad_fn=<AddmmBackward0>)
torch.tensor(t[20])
tensor([[50, 50]])
torch.tensor(t[25])
tensor([[50, 50]])
torch.tensor(t[590])
tensor([[62, 51],
        [28, 16],
        [50, 50]])
seqRNN(2, 20, 2, 3)(torch.tensor(t[590]))
Traceback (most recent call last):
  File "<pyshell#110>", line 1, in <module>
    seqRNN(2, 20, 2, 3)(torch.tensor(t[590]))
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "<pyshell#98>", line 10, in forward
    out, _ = self.rnn(x, hO)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\rnn.py", line 450, in forward
    raise RuntimeError(
RuntimeError: For unbatched 2-D input, hx should also be 2-D but got 3-D tensor
torch.tensor(t[590]).T
tensor([[62, 28, 50],
        [51, 16, 50]])
torch.randn(1, 3, 2)
tensor([[[ 0.5005,  0.5610],
         [ 1.0950,  0.3782],
         [-1.0101, -0.2499]]])
seqRNN(2, 20, 2, 3)(torch.randn(1, 3, 2))
tensor([[ 0.1709, -0.1954, -0.3717]], grad_fn=<AddmmBackward0>)
seqRNN(2, 20, 2, 1)(torch.randn(1, 3, 2))
tensor([[-0.1091]], grad_fn=<AddmmBackward0>)
torch.tensor(t[590], type=torch.float32)
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    torch.tensor(t[590], type=torch.float32)
TypeError: tensor() got an unexpected keyword argument 'type'
torch.tensor(t[590], dtype=torch.float32)
tensor([[62., 51.],
        [28., 16.],
        [50., 50.]])
torch.tensor(t[590], dtype=torch.float32)
tensor([[62., 51.],
        [28., 16.],
        [50., 50.]])
seqRNN(2, 20, 2, 1)(torch.tensor(t[590], dtype=torch.float32))
Traceback (most recent call last):
  File "<pyshell#118>", line 1, in <module>
    seqRNN(2, 20, 2, 1)(torch.tensor(t[590], dtype=torch.float32))
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "<pyshell#98>", line 10, in forward
    out, _ = self.rnn(x, hO)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\module.py", line 1194, in _call_impl
    return forward_call(*input, **kwargs)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\nn\modules\rnn.py", line 450, in forward
    raise RuntimeError(
RuntimeError: For unbatched 2-D input, hx should also be 2-D but got 3-D tensor
torch.tensor(t[590], dtype=torch.float32).shape
torch.Size([3, 2])
torch.randn(1, 3, 2).shape
torch.Size([1, 3, 2])
torch.tensor(t[590], dtype=torch.float32).unsqueeze()
Traceback (most recent call last):
  File "<pyshell#121>", line 1, in <module>
    torch.tensor(t[590], dtype=torch.float32).unsqueeze()
TypeError: unsqueeze() missing 1 required positional arguments: "dim"
torch.tensor(t[590], dtype=torch.float32).unsqueeze(dim=-1)
tensor([[[62.],
         [51.]],

        [[28.],
         [16.]],

        [[50.],
         [50.]]])
torch.tensor(t[590], dtype=torch.float32).unsqueeze(dim=-1).size
<built-in method size of Tensor object at 0x000002D0864427A0>
torch.tensor(t[590], dtype=torch.float32).unsqueeze(dim=-1).size()
torch.Size([3, 2, 1])
torch.tensor(t[590], dtype=torch.float32).unsqueeze(dim=1).size
<built-in method size of Tensor object at 0x000002D0864427A0>
torch.tensor(t[590], dtype=torch.float32).unsqueeze(dim=1).size()
torch.Size([3, 1, 2])
torch.tensor(t[590], dtype=torch.float32).unsqueeze(dim=2).size()
torch.Size([3, 2, 1])
torch.tensor(t[590], dtype=torch.float32).unsqueeze(dim=0).size()
torch.Size([1, 3, 2])
torch.tensor(t[590], dtype=torch.float32).unsqueeze(0)
tensor([[[62., 51.],
         [28., 16.],
         [50., 50.]]])
seqRNN(2, 20, 2, 1)(torch.tensor(t[590], dtype=torch.float32).unsqueeze(0))
tensor([[0.1198]], grad_fn=<AddmmBackward0>)
seqRNN(2, 20, 2, 1)(torch.tensor(t[590], dtype=torch.float32).unsqueeze(0))
tensor([[0.0684]], grad_fn=<AddmmBackward0>)
seqRNN(2, 20, 2, 1)(torch.tensor(t[590], dtype=torch.float32).unsqueeze(0))
tensor([[0.5647]], grad_fn=<AddmmBackward0>)
seqRNN(2, 20, 2, 1)(torch.tensor(t[590], dtype=torch.float32).unsqueeze(0))
tensor([[-0.3157]], grad_fn=<AddmmBackward0>)
seqRNN(2, 20, 2, 1)(torch.tensor(t[590], dtype=torch.float32).unsqueeze(0))
tensor([[-0.4881]], grad_fn=<AddmmBackward0>)
seqRNN(2, 20, 2, 1)(torch.tensor(t[590], dtype=torch.float32).unsqueeze(0))
tensor([[0.3528]], grad_fn=<AddmmBackward0>)
seqRNN(2, 20, 2, 1)(torch.tensor(t[590], dtype=torch.float32).unsqueeze(0))
tensor([[0.0516]], grad_fn=<AddmmBackward0>)
seqRNN(2, 20, 2, 1)(torch.tensor(t[590], dtype=torch.float32).unsqueeze(0))
tensor([[-0.0857]], grad_fn=<AddmmBackward0>)
model=seqRNN(2, 20, 2, 1)
model(torch.tensor(t[590], dtype=torch.float32).unsqueeze(0))
tensor([[-0.0693]], grad_fn=<AddmmBackward0>)
model(torch.tensor(t[590], dtype=torch.float32).unsqueeze(0))
tensor([[-0.0693]], grad_fn=<AddmmBackward0>)
model(torch.tensor(t[590], dtype=torch.float32).unsqueeze(0))
tensor([[-0.0693]], grad_fn=<AddmmBackward0>)
seqRNN(2, 20, 2, 6)
seqRNN(
  (rnn): RNN(2, 20, num_layers=2, batch_first=True)
  (fc): Linear(in_features=20, out_features=6, bias=True)
)
model = seqRNN(2, 20, 2, 6)
model(torch.tensor(t[590], dtype=torch.float32).unsqueeze(0))
tensor([[-0.0763,  0.1023,  0.2869,  0.0073,  0.6275, -0.1460]],
       grad_fn=<AddmmBackward0>)
model(torch.tensor(t[590], dtype=torch.float32).unsqueeze(0))
tensor([[-0.0763,  0.1023,  0.2869,  0.0073,  0.6275, -0.1460]],
       grad_fn=<AddmmBackward0>)
model(torch.tensor(t[591], dtype=torch.float32).unsqueeze(0))
tensor([[-0.0746,  0.1015,  0.2754,  0.0181,  0.6200, -0.1544]],
       grad_fn=<AddmmBackward0>)
model(torch.tensor(t[598], dtype=torch.float32).unsqueeze(0))
tensor([[ 0.1460,  0.0945,  0.2702, -0.1582,  0.4287, -0.1839]],
       grad_fn=<AddmmBackward0>)
model = NeuralNetwork(2, sequence=True)
model
NeuralNetwork(
  (flatten): Flatten(start_dim=1, end_dim=-1)
  (start): seqRNN(
    (rnn): RNN(2, 20, num_layers=2, batch_first=True)
    (fc): Linear(in_features=20, out_features=30, bias=True)
  )
  (stack): ModuleList(
    (0): Linear(in_features=12, out_features=6, bias=True)
    (1): Linear(in_features=18, out_features=6, bias=True)
    (2): RNN(18, 6)
  )
  (last): Linear(in_features=12, out_features=6, bias=True)
)
model.base_set(t, call=False)
model.roll(10)
Traceback (most recent call last):
  File "<pyshell#151>", line 1, in <module>
    model.roll(10)
  File "C:\Users\KDCA\Desktop\IL\base\network.py", line 178, in roll
    reinforce(epoch, alert, self, DataLoader(self.trd.dataset[first:last+1], batch_size=(last-first)//100), self.ted, self.optim, self.sched)
  File "C:\Users\KDCA\Desktop\IL\base\network.py", line 234, in reinforce
    losses = train_loop(trd, mod, loss_fn, optim)
  File "C:\Users\KDCA\Desktop\IL\base\network.py", line 188, in train_loop
    for batch, (X, y) in enumerate(dataloader):
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\utils\data\dataloader.py", line 628, in __next__
    data = self._next_data()
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\utils\data\dataloader.py", line 671, in _next_data
    data = self._dataset_fetcher.fetch(index)  # may raise StopIteration
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\utils\data\_utils\fetch.py", line 61, in fetch
    return self.collate_fn(data)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\utils\data\_utils\collate.py", line 265, in default_collate
    return collate(batch, collate_fn_map=default_collate_fn_map)
  File "C:\Users\KDCA\AppData\Local\Programs\Python\Python310\lib\site-packages\torch\utils\data\_utils\collate.py", line 139, in collate
    raise RuntimeError('each element in list of batch should be of equal size')
RuntimeError: each element in list of batch should be of equal size
>>> model[0]
Traceback (most recent call last):
  File "<pyshell#152>", line 1, in <module>
    model[0]
TypeError: 'NeuralNetwork' object is not subscriptable
>>> model
NeuralNetwork(
  (flatten): Flatten(start_dim=1, end_dim=-1)
  (start): seqRNN(
    (rnn): RNN(2, 20, num_layers=2, batch_first=True)
    (fc): Linear(in_features=20, out_features=30, bias=True)
  )
  (stack): ModuleList(
    (0): Linear(in_features=12, out_features=6, bias=True)
    (1): Linear(in_features=18, out_features=6, bias=True)
    (2): RNN(18, 6)
  )
  (last): Linear(in_features=12, out_features=6, bias=True)
)
>>> model.start
seqRNN(
  (rnn): RNN(2, 20, num_layers=2, batch_first=True)
  (fc): Linear(in_features=20, out_features=30, bias=True)
)
>>> model.feature_label[0]
[[50, 50]]
>>> model.feature_label[0:20]
[[[50, 50]], [[50, 50]], [[50, 50]], [[50, 50]], [[50, 50]], [[50, 50]], [[50, 50]], [[50, 50]], [[50, 50]], [[50, 50]], [[50, 50]], [[50, 50]], [[50, 50]], [[50, 50]], [[50, 50]], [[50, 50]], [[50, 50]], [[50, 50]], [[50, 50]], [[50, 50]]]
