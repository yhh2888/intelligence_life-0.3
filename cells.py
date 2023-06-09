import random

sender_typelist = ['energy', 'energy_gradient',
                   'c_fooddistance', 'c_otherdistance', 'c_foodangle', 'c_otherangle',
                   'c_borderdistance', 'c_iscompetitorin', 'c_isfoodin', 'randompoint']
                   
class sender_neuron:
    def __init__(self, type_):
        if type_ in sender_typelist:
            ntype = sender_typelist.index(type_)

        if ntype == int:
            if ntype == 1:
                self.energy = 0
            elif ntype == 2:
                self.energy_g = 0
            elif ntype == 3:
                self.tofood = 0
            elif ntype == 4:
                self.toother = 0
            elif ntype == 5:
                self.foodangle = 0
            elif ntype == 6:
                self.otherangle = 0
            elif ntype == 7:
                self.toborder = 0
            elif ntype == 8:
                self.sawcompetitor = 0
            elif ntype == 9:
                self.sawfood = 0
            elif ntpye == 10:
                self.random_point = 0

    
