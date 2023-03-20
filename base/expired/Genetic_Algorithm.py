import os
import sys

sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname('neural_network'))))

from neural_network_test import *
import tensorflow as tf
import numpy as np
import random

class Gene:
    def __init__(self, curve, code, lenlim, mutation_rate=0.2, sight=11, params = [], output_length = 6, const = [], mrec= []):
        self.curve = curve
        self.code = code
        self.mutation_rate = mutation_rate
        self.lenlim = lenlim
        self.sight = sight
        self.params = params
        self.output_length = output_length
        self.const = const
        self.mutation_record = mrec

    def m_curve(self):
        draw_curve = random.randint(0, len(self.curve)-1)
        self.curve[draw_curve] += [-1, 1][random.randint(0, 1)]

    def m_code(self):
        draw_code1 = random.randint(0, len(self.code)-1)
        draw_code2 = random.randint(0, 2)
        draw_code3 = random.randint(2, 6)

        if draw_code2 == 0:
            self.code[draw_code1] = [random.randint(0, 6) for i in range(draw_code3)]
        if draw_code2 == 1:
            draw_code4 = random.randint(1, 3)
            for i in range(draw_code4+1):
                if len(self.code[draw_code1])-draw_code4+i < 6:
                    self.code[draw_code1].append(random.randint(0, 6))
        if draw_code2 == 2:
            draw_code4 = random.randint(1, 3)
            for i in range(draw_code4+1):
                if len(self.code[draw_code1])-draw_code4+i > 2:
                    self.code[draw_code1][random.randint(0, len(self.code[draw_code1])-1)]
                    
    def m_lenlim(self):
        self.lenlim += [1, -1][random.randint(0, 1)]
        if self.lenlim > 20:
            self.lenlim = 20
        elif self.lenlim < 3:
            self.lenlim = 3
            
    def m_params(self):
        draw_params1 = random.randint(0, 20)
        draw_params2 = random.randint(0, len(self.params)-1)
        for i in range(draw_params1):
            e = self.params[draw_params2]
            f = np.array(self.params[draw_params2])
            f[random.randint(0, e.shape[0]-1)][random.randint(0, e.shape[1]-1)] = np.random.uniform(-1, 1)
            self.params[draw_params2] = f

    def mutation_roulette(self, percentage=10):
        mutation_number = 0
        while random.random() < self.mutation_rate:
            mutation_number += 1
            self.mutation_rate *= random.uniform(0.8, 1.2)
            if self.mutation_rate > 0.6:
                self.mutation_rate = 0.6
        while mutation_number > 0:
            draw = random.randint(3, percentage)
            if draw == 0:
                self.m_curve()
                self.mutation_record.append('curve')
                mutation_number -= 1
            elif draw == 1:
                self.m_code()
                self.mutation_record.append('code')
                mutation_number -= 1
            elif draw == 2:
                self.m_lenlim()
                self.mutation_record.append('lenlim')
                mutation_number -= 1
            elif draw > 2:
                self.m_params()
                self.mutation_record.append('params')
                mutation_number -= 1
            
    def genetest(self, rep, output=6):
        #print(self.mutation_record)
        #print([])
        mselist = dist_analyze(layer_create(self.sight, self.curve, length=self.lenlim, output=output), rep, self.code, self.sight, output_length = self.output_length, const = self.const)
        mse = 0
        diff = rep/len(mselist)
        for i in mselist:
            mse += (diff-i)**2
        return mse

    def length_adjust(self):
        if self.lenlim > len(self.curve):
            for i in range(self.lenlim-len(self.curve)):
                self.curve.append(random.randint(0, 5))
        elif self.lenlim < len(self.curve):
            for i in range(self.lenlim-len(self.curve)):
                del self.curve[-1]

        if self.lenlim > len(self.code):
            for i in range(self.lenlim-len(self.code)):
                self.code.append([np.random.randint(0, 7) for j in range(sum([len(self.code[k]) for k in range(len(self.code))])//len(self.code))])
        elif self.lenlim < len(self.code):
            for i in range(len(self.code)-self.lenlim):
                del self.code[-1]

        layers = layer_create(self.sight, self.curve, length=self.lenlim)
        parameter = param_renew(layers)[1]
        
        if len(layers)-1 > len(self.const):
            for i in range(len(layers)-1-len(self.const)):
                try :
                    cons = param_renew(layers)
                    self.const.append(cons[1][-(len(layers)-len(self.const)+i)])
                except Exception as e:
                    print(e, len(layers)-len(self.const), len(self.const), len(cons[1]))
        elif len(layers)-1 < len(self.const):
            for i in range(len(self.const)-len(layers)+1):
                del self.const[-1]

        for i in range(len(layers)-1):
            compare = parameter[i]
            self.const[i] = compare
            '''if len(self.const[i]) != 1:
                self.const[i] = np.transpose(self.const[i])
                transposed = True
            if len(parameter[i]) != 1:
                compare = np.transpose(compare)
            if len(compare) > len(self.const[i][0]):
                for j in range(layers[i]-len(self.const[i][0])):
                        self.const[i] = [np.append(self.const[i][0], np.random.uniform(-1, 1))]

            elif len(compare) < len(self.const[i][0]):
                for j in range(len(self.const[i][0])-layers[i]):
                        self.const[i] = [np.delete(self.const[i][0], -1)]
            if transposed == True:
                self.const[i] = np.transpose(self.const[i])'''
