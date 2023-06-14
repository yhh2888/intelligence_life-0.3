import random, math

sender_typelist = ['energy', 'energy_g',
                   'c_fooddistance', 'c_otherdistance', 'c_foodangle', 'c_otherangle',
                   'c_borderdistance', 'c_iscompetitorin', 'c_isfoodin', 'randompoint']
                   
class Sender_neuron:
    def __init__(self, ntype)
        
        if type(ntype) == int:
            if ntype == 1:
                self.energy = 0
            elif ntype == 2:
                self.energy_g = 0
            elif ntype == 3:
                self.c_fooddistance = 0
            elif ntype == 4:
                self.c_otherdistance = 0
            elif ntype == 5:
                self.c_foodangle = 0
            elif ntype == 6:
                self.c_otherangle = 0
            elif ntype == 7:
                self.c_borderdistance = 0
            elif ntype == 8:
                self.c_iscompetitorin = 0
            elif ntype == 9:
                self.c_isfoodin = 0
            elif ntype == 10:
                self.randompoint = 0

    def execute(self):
        pass

    
class Variate_neuron:
    def __init__(self, proto, variate_pattern, scope):
        self.proto = proto
        self.value = proto
        self.variate_pattern = variate_pattern
        self.min = scope[0]
        self.max = scope[1]

    def variate(self, num, type_):
        if self.variate_pattern[type_] == 0:
            self.value += num
        elif self.variate_pattern[type_] == 1:
            self.value -= num
        elif self.variate_pattern[type_] == 2:
            self.value *= num
        elif self.variate_pattern[type_] == 3:
            self.value /= num

    def scope_adjust(self):
        if not self.min <= self.value <= self.max:
            self.value = self.min+self.value%(self.max-self.min)

    def reset(self):
        self.value = self.proto

    def execute(self, value, type_=0):
        self.variate(value, type_)

class Convert_neuron:
    def __init__(self, type_, coeff, degree, const=0):

        self.coeff = coeff
        self.degree = degree
        self.const = const

        if type_==0:
            self.func = self.sin
        elif type_==1:
            self.func = self.cos
        elif type_==2:
            self.func = self.arctan
        elif type_==3:
            self.func = self.root
        elif type_==4:
            self.func = self.scoper

    def sin(self, value):
        return self.coeff*math.sin(value*self.degree)+self.const

    def cos(self, value):
        return self.coeff*math.cos(value*self.degree)+self.const

    def arctan(self, value):
        return self.coeff*math.atan(value*self.degree)/math.pi+self.const

    def root(self, value):
        return self.coeff*(value**(1/self.degree))+self.const

    def scoper(self, value):
        return self.coeff*((value*self.degree)%2-1)+self.const

    def execute(self, value, type_=None):
        self.func(value)

class Reinf_decide:
    def __init__(self, crit=1):
        self.crit = crit
        self.value = 0
        self.strength = 0
        self.reinforce = False
        
    def isreinf(self):
        if self.value >= self.crit:
            self.reinforce = True

class Movecell:
    def __init__(self):
        self.right = 0
        self.down = 0
        self.left = 0
        self.up = 0
        
    
