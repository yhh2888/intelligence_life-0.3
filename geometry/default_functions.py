import random, time
import numpy as np
from collections import deque
from geometry.calculation import *

def dir4_response(directions, method = []):
    default_dir = ['up', 'down', 'left', 'right']
    if method == []:
        if len(directions) == 1:
            return directions[0]
        elif len(directions) == 2:
            for i in range(default_dir-1):
                for j in range(1+i, 4):
                    if (default_dir[i] not in directions) and (default_dir[j] not in directions):
                        return [default_dir[i], default_dir[j]][random.randint(0, 1)]
        elif len(directions) == 3:
            for i in default_dir:
                if i not in directions:
                    return i
        elif len(directions) == 4:
            return default_dir[random.randint(0, 3)]
                
def dir8_response(directions, method = []):
    default_dir = ['rightup', 'rightdown', 'downright', 'downleft', 'leftdown', 'leftup', 'upleft', 'upright']
    if method == []:
        dir_point = [0 for i in range(8)]
        for i in directions:
            dir_point[default_dir.index(i)] += 1
        dir_space_cal = []
        for i in range(8):
            for j in range(8):
                e = (i+j)%8
                if dir_point[e] != 0:
                    right = j
            for j in range(8):
                e = (i-j)%8
                if dir_point[e] != 0:
                    left = j
            dir_space_cal.append(right**0.5+left**0.5)
        return default_dir[np.argmax(dir_space_cal)]
    
def space_check_response(self, nums, mob_loc, method = []):
    pass

class distance_response:
    def __init__(self, distances, method = []):
        self.distances = distances
        self.method = method

    def nearest_response(self, moblist, num = 1):
        line_length = []
        for i in self.distances:
            line_length.append((i[0]**2+i[1]**2)**2)
        moblist_ = []
        lines_ = []
        nearests = []
        for i in range(len(line_length)):
            lines_.append(line_length[i])
            moblist_.append(moblist[i])
        if moblist_ != []:
            for i in range(num):
                nearests.append(moblist_[np.argmin(lines_)])
                del moblist_[np.argmin(lines_)]
                del lines_[np.argmin(lines_)]
        return nearests
    
    def average_loc_response(self):
        pass

    def pass_drawer(self):
        pass

class dist_dist:
    def __init__(self, distances):
        self.dist_value = 1
        for i in distances:
            self.dist_value *= i
        self.dist_value = self.dist_value**(0.125)
    def compare(self, crit):
        if crit> self.dist_value:
            return True
        else :
            return False
        
def location_create(direction, figure):
    loc_gen = deque([])
    default_dir = ['rightup', 'rightdown', 'downright', 'downleft',
                           'leftdown','leftup', 'upleft', 'upright']
    if direction == default_dir[0]:
        loc_gen.append(random.uniform(0, 3))
        loc_gen.append(random.uniform(loc_gen[0]*(-1), 0))
    elif direction == default_dir[1]:
        loc_gen.append(random.uniform(0, 3))
        loc_gen.append(random.uniform(0, loc_gen[0]))
    elif direction == default_dir[2]:
        loc_gen.append(random.uniform(0, 3))
        loc_gen.appendleft(random.uniform(0, loc_gen[0]))
    elif direction == default_dir[3]:
        loc_gen.append(random.uniform(0, 3))
        loc_gen.appendleft(random.uniform(loc_gen[0]*(-1), 0))
    elif direction == default_dir[4]:
        loc_gen.append(random.uniform(-3, 0))
        loc_gen.append(random.uniform(0, abs(loc_gen[0])))
    elif direction == default_dir[5]:
        loc_gen.append(random.uniform(-3, 0))
        loc_gen.append(random.uniform(loc_gen[0], 0))
    elif direction == default_dir[6]:
        loc_gen.append(random.uniform(-3, 0))
        loc_gen.appendleft(random.uniform(loc_gen[0], 0))
    elif direction == default_dir[7]:
        loc_gen.append(random.uniform(-3, 0))
        loc_gen.appendleft(random.uniform(0, abs(loc_gen[0])))
    return [int(loc_gen[0]*figure), int(loc_gen[1]*figure)]

def avoider(moblist, crit, figure, me_loc, directions = 8):
    #moblist: self.mobs.moblist, crit: 5~20 figure: 1.7~3, ~5, me_loc: [self.snake.x, self.snake.y]
    default_dir = ['rightup', 'rightdown', 'downright', 'downleft',
                           'leftdown','leftup', 'upleft', 'upright']
    
    mobparsed = [[] for i in range(directions)]
    
    distance_ = distance(moblist, me_loc)
    
    for i in range(len(moblist)):
        
        mobparsed[default_dir.index(dir_cal_8(distance_[i])[0])].append(distance_[i])
        
    distindir = []
    
    for i in range(len(mobparsed)):
        if mobparsed[i] != []:
            themob = distance_response(mobparsed[i]).nearest_response(mobparsed[i])[0]
            distindir.append((themob[0]**2+themob[1]**2)**0.5)
        else:
            distindir.append(50)
    if dist_dist(distindir).compare(crit) == True:
        avoid_loc = location_create(default_dir[distindir.index(min(distindir))], figure)
    else:
        avoid_loc = []
    return avoid_loc

#avoider(self.

class IF_Exception:
    def __init__(self, me_loc, figure, mode):
        self.figure = [figure[0]+me_loc[0], figure[1]+me_loc[1]]
        self.mode = mode
    def moder(self, me_loc):
        if self.mode == 'location':
            if self.figure[0] == me_loc[0] and self.figure[1] == me_loc[1]:
                return True
            else:
                return False

def pointoline(linepoint1, linepoint2, point):
    if linepoint2[0] != linepoint1[0]:
        c = [linepoint2[0]-linepoint1[0], linepoint2[1]-linepoint1[1]]
        dist = (c[0]**2+c[1]**2)**0.5
        incline = (linepoint2[1]-linepoint1[1])/(linepoint2[0]-linepoint1[0])
        addist = ((linepoint1[0]-point[0])**2+(linepoint1[1]-point[1])**2)**0.5
        bddist = ((linepoint2[0]-point[0])**2+(linepoint2[1]-point[1])**2)**0.5
        if ((-(point[0]-linepoint1[0]))*(linepoint2[0]-linepoint1[0])+(point[1]-linepoint1[1])*(linepoint2[1]-linepoint1[1]))/ \
           [(dist*(addist)) if (dist*(addist)) != 0 else 1][0] < 0:
            e = addist
        elif ((point[0]-linepoint1[0])*(linepoint2[0]-linepoint1[0])+(point[1]-linepoint1[1])*(linepoint2[1]-linepoint1[1]))/dist > dist:
            e = bddist
        else :
            e = abs(incline*point[0]+point[1]+linepoint2[0]-incline*linepoint1[0])/(incline**2+1)**0.5
        return e

def optimal_point(me_loc, pointlist, moblist, mapsize):
    rate = []
    for i in pointlist:
        mobtoway = []
        dist = ((me_loc[0]-i[0])**2+(me_loc[1]-i[1])**2)**0.5
        for j in moblist:
            if pointoline(me_loc, i, j) != None:
                mobtoway.append(pointoline(me_loc, i, j))
                
            else :
                mobtoway.append(0)
        if dist != 0 and (i[0] != mapsize/2 or i[1] != mapsize/2):
            rate.append(min(mobtoway)/dist)
            #((i[0]-mapsize/2)**2+(i[1]-mapsize/2)**2)**0.5)
        else :
            rate.append(0)
    if rate != []:
        return pointlist[np.argmax(rate)]
    else:
        pass

def opt_timetest(mobrate, range_, rep, me_loc, mapsize):
    moblist = [[random.randint(30, 70), random.randint(30, 70)] for i in range(mobrate)]
    pointlist = [[random.randint(0, 100), random.randint(0, 100)] for i in range(range_**2)]
    opt_points = []
    for i in range(rep):
        if i == 0:
            t = time.time()
        opt_points.append(optimal_point(me_loc, pointlist, moblist, mapsize))
        if i == rep-1:
            print(time.time()-t)
        return opt_points

def movepoint(me_loc, moblist, mapsize, range_=3):
    if len([i for i in distance(mobsurround(moblist, me_loc, 10, range_*2, mapsize), me_loc) if -range_*2<i[0]<range_*2 and -range_*2<i[1]<range_*2])>10:
        moveto = optimal_point(me_loc, mobsurround(moblist, me_loc, 10, range_, mapsize), moblist, mapsize)
        moveto[0] -= me_loc[0]
        moveto[1] -= me_loc[1]
        #특정 현상 때문에 moveto[a] = me_loc[a] - moveto[a]도 좋음
        return moveto
'''
for i in range(10):
	opt_timetest(10, 20, 1, me_loc=[random.randint(30, 70), random.randint(30, 70)], 100)

if len([i for i in distance(mobsurround(moblist, me_loc, 20, 5, mapsize), me_loc) if -6<i[0]<6 and -6<i[1]<6])>40:
    moveto = optimal_point(me_loc, mobsurround(moblist, me_loc, 20, 2, mapsize), moblist, mapsize)
'''
