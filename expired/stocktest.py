import math

def stock(middle=0.002, probability=0.6, diversify=6, freq=5):
    return ((1.01+middle)**(10*probability)*0.99**(10*(1-probability))*0.99835**10)**((1/diversify)*(freq/2)*48)

prots=13
for i in range(10):
    prots = prots*stock(middle=0.0012+i*0.00035, probability=0.55+i*0.015, freq=5+i)+10
    print(25+i, prots)
