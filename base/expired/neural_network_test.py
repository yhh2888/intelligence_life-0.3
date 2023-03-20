import tensorflow as tf
import numpy as np
import time, random
tester = None
if __name__ == '__main__':
        tester = []
def Network(param, space, code, output_length, const):
        length = len(param)
        width = length**2
        params = {}
        params[0] = space
        z = params[0]
        matrs=[]
        for i in range(length):
                params[i+1] = param[i]
        for i in range(0, length-1):
                try:
                        z = Activation(z, params[i+1], const[i], code[i]).single_interprete()
                except Exception as e:
                        #print(e, 2)
                        try :
                                z = Activation(z, params[i+1], np.transpose(const[i]), code[i]).single_interprete()
                        except Exception as e:
                                print(e, 2, len(params)-i)
		#print(params[i+1].shape, len(const[i]))
                matrs.append(z)
        if tester != None:
                tester.append(matrs)
                
        try:
                z = tf.matmul(param[-1], z) + const[-1]
                
        except Exception as e:
                print(e, 'f')
        freq = [0 for i in range(output_length)]
        z = np.transpose(z)
        try:
                for i in z:
                        freq[np.argmax(i)] += 1
        except Exception as e:
                print(e, z.shape)
        return freq

def create(length):
	er = []
	for i in range(length**2):
		if np.random.randint(0, (length**2)//3) == 0:
			er.append(1)
		else:
			er.append(0)
	return np.float64(np.reshape(er, (length, length)))

def matrix_create(length):
        return np.random.uniform(-1, 1, size=(length, length))

def _1D_create(length):
        created = []
        num = [random.randint(-1, 1) for i in range(length)]
        for i in num:
                created.append([i for j in range(length)])
        return np.array(created)

def param_renew(layer, sight=11, final_num=20):
        paramlist = []
        const = []
        layer_ = layer
        true_val = [layer_[0], layer_[0]]
        for i in range(0, len(layer_)-3):
                paramlist.append(np.random.uniform(-1, 1, size=(true_val[1], layer_[i+1])))
                const.append(np.random.uniform(-1, 1, size=(true_val[0], 1)))
                true_val = [true_val[0], layer_[i+1]]
        paramlist.append(np.random.uniform(-1, 1, size=(true_val[1], final_num)))
        const.append(np.random.uniform(-1, 1, size=(true_val[0], 1)))
        true_val = [true_val[0], 20]
        paramlist.append(np.random.uniform(-1, 1, size=(layer_[-1], true_val[0])))
        const.append(np.random.uniform(-1, 1, size=(1, final_num)))
        return paramlist, const


def dist_analyze(layer, rep, code, sight, params = [], output_length = 6, const=[]):
        tem = time.time()
        t = [0 for i in range(output_length)]
        if params != []:
                so = params
        else :
                so = param_renew(layer, sight= sight)
                if const == []:
                        const = so[1]
                so = so[0]
        '''for i in range(len(so)-1):
                try:
                       print(so[i].shape, const[i].shape)
                except Exception as e:
                        print(e, so[i].shape, const[i])'''
        
        try :
                for i in range(rep):
                        t[np.argmax(Network(so, matrix_create(sight), code, output_length = output_length, const = const))] += 1
        except Exception as e:
                print(e)
        #print(time.time() - tem)
        return t

def layer_create(begin, gen, stop=3, length=20, output=6):
	neu_st = []
	val = begin + gen[0]
	neu_st.append(begin)
	for i in range(1, len(gen)):
		val = val + gen[i]
		if val <= stop or len(neu_st) >= length-1:
			break
		neu_st.append(val)
	neu_st.append(output)
	return neu_st

class Activation:
        def __init__(self, a, b, c, code):
                self.result = np.dot(a, b) + c
                self.code = code
        def sigmoid(self):
                self.result = tf.nn.sigmoid(self.result)
        def relu(self):
                self.result = tf.nn.relu(self.result)
        def softmax(self):
                self.result = tf.nn.softmax(self.result)
        def leakyrelu(self, alpha=0.2):
                self.result = tf.nn.leaky_relu(self.result, alpha)
        def elu(self):
                self.result = tf.nn.elu(self.result)
        def tanh(self):
                self.result = tf.nn.tanh(self.result)
        def code_interprete(self):
                for i in self.code:
                        if i == 1:
                                self.sigmoid()
                        elif i == 2:
                                self.relu()
                        elif i == 3:
                                self.softmax()
                        elif i == 4:
                                self.leakyrelu()
                        elif i == 5:
                                self.elu()
                        elif i == 6:
                                self.tanh()
                        else:
                                pass
                return self.result
        def single_interprete(self):
                self.leakyrelu()
                return self.result

def activation_code_create(length, _max=5, _min=0, lenlim=12):
	code_list = []
	for i in range(lenlim):
		code_list.append([np.random.randint(_min, _max) for i in range(length)])
	return code_list

layer = layer_create(11, [np.random.randint(-5, 5) for i in range(10)])
se = activation_code_create(4)
layervalue=[np.random.randint(-1, 3) for i in range(2)]+[np.random.randint(-3, 3) for i in range(6)]+[np.random.randint(-3, 1) for i in range(2)]
genetics = [layervalue, activation_code_create(4, lenlim=11), 11]
a = param_renew(layer_create(genetics[2], genetics[0]))


'''
Network(a[0], create(11), genetics[1], output_length = 6, const = a[1])
'''
