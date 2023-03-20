import numpy as np

def dir_cal_4(location):
    #location = [moblist[i][0]-me_loc[0], moblist[i][1]-me_loc[1]]
    if abs(location[0])>=abs(location[1]):
        if location[0]>=0:
            return 'right'
        elif location<0:
            return 'left'
    elif abs(location[0])<abs(location[1]):
        if location[1]>0:
            return 'up'
        elif location[1]<0:
            return 'down'

def dir_cal_8(location):
    if abs(location[0])>=abs(location[1]):
        if location[0]>=0 and location[1]>=0:
            return 'rightup', (location[0]**2+location[1]**2)**0.5
        elif location[0]>=0 and location[1]<0:
            return 'rightdown', (location[0]**2+location[1]**2)**0.5
        elif location[0]<0 and location[1]>=0:
            return 'leftup', (location[0]**2+location[1]**2)**0.5
        elif location[0]<0 and location[1]<0:
            return 'leftdown', (location[0]**2+location[1]**2)**0.5
    elif abs(location[0])<abs(location[1]):
        if location[1]>0 and location[0]>=0:
            return 'upright', (location[0]**2+location[1]**2)**0.5
        elif location[1]>0 and location[0]<0:
            return 'upleft', (location[0]**2+location[1]**2)**0.5
        elif location[1]<0 and location[0]>=0:
            return 'downright', (location[0]**2+location[1]**2)**0.5
        elif location[1]<0 and location[0]<0:
            return 'downleft', (location[0]**2+location[1]**2)**0.5
        
def distance(moblist, me_location):
    return [(i[0]-me_location[0], i[1]-me_location[1]) for i in moblist]

def space_check(location, moblist):
    #location example = [(5, 6), (8, 12)]
    nums = 0
    mob_loc = []
    xs = [location[0][0], location[1][0]]
    ys = [location[0][1], location[1][1]]
    for i in moblist:
        if min(xs)<=i[0]<=max(xs) and min(ys)<=i[1]<=max(ys):
            nums += 1
            mob_loc.append(i[0:2])
    return nums, mob_loc

def mobsurround(moblist, me_loc, sight, range_, mapsize):
    xs = [me_loc[0]-sight, me_loc[0]+sight]
    ys = [me_loc[1]-sight, me_loc[1]+sight]
    dist_list = []
    for i in moblist:
        if min(xs)<=i[0]<=max(xs) and min(ys)<=i[1]<=max(ys):
            dist_list = dist_list + \
                        [[-range_+x+i[0], -range_+y+i[1]] for y in range(range_*2+1) for x in range(range_*2+1)\
                        if 0<=-range_+x+i[0]<=mapsize and 0<=-range_+y+i[1]<=mapsize]
    return dist_list

def mobsum(moblist):
    sum_ = [0, 0]
    for i in moblist:
        sum_[0] =+ i[0]
        sum_[1] =+ i[1]
    sum_[0] = sum_[0]/len(moblist)
    sum_[1] = sum_[1]/len(moblist)
    return sum_
