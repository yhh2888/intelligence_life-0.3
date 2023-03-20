import numpy as np
import math

def rotate(i : int, j : int, rotation : float):
    theta = math.pi*rotation
    return math.sin(theta)*i-math.cos(theta)*j, math.cos(theta)*i+math.sin(theta)*j

def roundoff(num):
    return [int(num) if num%1<0.5 else int(num)+1][0]
    
def O_matrix(size : float,
                    width : float,
                    length : float,
                    
                    point : float = 0.5,
                    emptyvalue : float = 0,
                    rotation : float = 0,
                    rev : bool = False):
    
    optinum1 = size*2-1
    optinum2 = size-1
    
    matrix = np.zeros(shape=(optinum1, optinum1))
      
    for i in range(-optinum2, size):
        for j in range(-optinum2, size):
            a, b = rotate(i, j, rotation)
            if emptyvalue <= a**2/width**2+b**2/length**2 <= 1.01:
                matrix[i+optinum2][j+optinum2] += 1
    if rev==True:
        matrix = np.multiply(np.full((optinum1, optinum1), 1)-matrix, np.full((optinum1, optinum1), point))
    elif rev==False:
        matrix = np.multiply(matrix, np.full((optinum1, optinum1), point))
    return matrix

def edge3_matrix(width : float,
                  length : float,
                  matsize : float,

                  point : float = 0.5,
                  emptyvalue : float = 0,
                  rotation : float = 0,
                  rev : bool = False):

    matrix = np.zeros(shape=(matsize*2-1, matsize*2-1))
    def fill(a, b, i, j):
        right = (((2*length)/width)*(a)+(1/2)*length)
        left = ((-(2*length)/width)*(a)+(1/2)*length)
        bottom = -(1/2)*length
        empty = (((2/3)-emptyvalue)*length)

        if (b<=right) and (b <= left) and (b >= bottom):
            if emptyvalue != 0:
                if (right-empty<=b<=right or left-empty<=b<=left or bottom<=b<=bottom+(1/2)*empty):
                    if 0<=i+matsize-1<matsize*2 and 0<=j+matsize-1<matsize*2:
                        matrix[i+matsize-1, j+matsize-1] += 1
            else:
                if 0<=i+matsize-1<matsize*2 and 0<=j+matsize-1<matsize*2:
                        matrix[i+matsize-1, j+matsize-1] += 1
			
    for i in range(-matsize+1, matsize):
        for j in range(-matsize+1, matsize):
            a, b = rotate(i, j, rotation)
            fill(a, b, i, j)
    if rev==True:
        matrix = np.multiply(np.full((matsize*2-1, matsize*2-1), 1)-matrix, np.full((matsize*2-1, matsize*2-1), point))
    elif rev==False:
        matrix = np.multiply(matrix, np.full((matsize*2-1, matsize*2-1), point))
    return np.flip(matrix)

def edge4_matrix(width : float,
                  length : float,
                  matsize : float,
                  
                  point : float = 0.5,
                  emptyvalue : float = 0,
                  rotation : float = 0,
                  rev : bool = False):
    
    matrix = np.zeros(shape=(matsize*2-1, matsize*2-1))
    def fill(a, b, i, j):
        if abs(a) <= width-1 and emptyvalue*length<=abs(b)<length:
            matrix[i+matsize-1, j+matsize-1] += 1
        elif abs(b) <= length-1 and emptyvalue*width<=abs(a)<width:
            matrix[i+matsize-1, j+matsize-1] += 1
    for i in range(-matsize+1, matsize):
        for j in range(-matsize+1, matsize):
            a, b = rotate(i, j, rotation)
            fill(a, b, i, j)
    if rev==True:
        matrix = np.multiply(np.full((matsize*2-1, matsize*2-1), 1)-matrix, np.full((matsize*2-1, matsize*2-1), point))
    elif rev==False:
        matrix = np.multiply(matrix, np.full((matsize*2-1, matsize*2-1), point))
    return matrix


'''def square_matrix(size, matsize, point=0.5, emptyvalue=0, rotation=0):
    matrix = np.zeros(shape=(matsize*2-1, matsize*2-1))
    def fill(a, b, i, j):
        if emptyvalue <= abs(a) <= size-1 and matsize-size<abs(b)<matsize+size:
            matrix[i+matsize-1, j+matsize-1] += point
        elif emptyvalue <= abs(b) <= size-1 and matsize-size<abs(a)<matsize+size:
                matrix[i+matsize-1, j+matsize-1] += point
    for i in range(-matsize+1, matsize):
        for j in range(-matsize+1, matsize):
            a = math.sin(math.pi*rotation)*i-math.cos(math.pi*rotation)*j
            b = math.cos(math.pi*rotation)*i+math.sin(math.pi*rotation)*j
            fill(a, b, i, j)
    return matrix'''

def curve_matrix(size :float,

                     grad : float = 1,
                     bias : int = 2,
                     point : float = 0.5,
                     rotation : float = 0,
                     rev : bool = False):
    
    matrix = np.zeros(shape=(size*2-1, size*2-1))
    for i in range(-size+1+bias, size+bias):
        for j in range(-size+1, size):
            a, b = rotate(i, j, rotation)
            if rev==False and b*4*grad >= a**2:
                matrix[-j+size-1, i+size-1-bias] += point
            elif rev==True and b*4*grad <= a**2:
                matrix[-j+size-1, i+size-1-bias] += point
    return matrix

def reflect_matrix(size : float,
                   
                   grad : float = 1,
                   bias : float = 2,
                   point : float = 0.5,
                   rotation : float = 0,
                   thickness : float = 1.5,
                   angle : float = 90,
                   rev : bool = False):
    
    matrix = np.zeros(shape=(size*2-1, size*2-1))

    if angle == 90:
        anglevalue1, anglevalue2 = 0, 0
    elif angle%180 == 0:
        anglevalue1, anglevalue2 = 1, 2
    elif angle == 270:
        anglevalue1, anglevalue2 = 2, 0
    else:
        anglevalue1, anglevalue2 = -(math.tan((0.25*(angle)*math.pi)/90)-1), 0
    
    for i in range(-size+1+bias, size+bias):
        for j in range(-size+1, size):
            a, b = rotate(i, j, rotation)
            if b+size-1 <= -abs(a)+size+bias+anglevalue1*b+anglevalue2*a <= b+size-1+thickness and 0<=i+size<size*2-1 and 0<=-j+size-1<size*2-1:
                matrix[-j+size-1, -i+size] += 1
    if rev==True:
        matrix = np.multiply(np.full((size*2-1, size*2-1), 1)-matrix, np.full((size*2-1, size*2-1), point))
    elif rev==False:
        matrix = np.multiply(matrix, np.full((size*2-1, size*2-1), point))
    return matrix


#----------------------------distance functions--------------------------#

def conjunct_matrix(loc, trait, map_):
    loc[1] += 1 #y+1 deflection fix
    try : traitsize = trait.shape
    except Exception as e: traitsize = (len(trait), len(trait[0]))
    try : mapsize = map_.shape
    except Exception as e: mapsize = (len(map_), len(map_[0]))

    traitrad = int((trait.shape[0]+1)/2)

    north, south, east, west = None, None, None, None

    try : north = np.zeros(shape=(loc[1]-int((traitsize[1]+1)/2+1)+1, mapsize[0]))
    except Exception as e: trait = trait[-(traitsize[1]+(loc[1]-int((traitsize[1]+1)/2+1)+1)):, :]
        
    try : south = np.zeros(shape=(mapsize[1]-loc[1]-int((traitsize[1]+1)/2)+1, mapsize[0]))
    except Exception as e: trait = trait[:traitsize[1]+(mapsize[1]-loc[1]-int((traitsize[1]+1)/2)+1)-
                                         [traitsize[0]-loc[1]+100+traitrad+1 if loc[1]>=100+traitrad else 0][0], :]

    try :west = np.zeros(shape=(traitsize[1], loc[0]-int((traitsize[0]+1)/2)+1))
    except Exception as e: trait = trait[:, -(traitsize[0]+(loc[0]-int((traitsize[0]+1)/2)+1)):]

    try :east = np.zeros(shape=(traitsize[1], mapsize[0]-loc[0]-int((traitsize[0]+1)/2+1)+1))
    except Exception as e: trait = trait[:, :traitsize[0]+(mapsize[0]-loc[0]-int((traitsize[0]+1)/2+1)+1)]

    if type(west) != type(None) :
        trait = np.concatenate((west[:trait.shape[0], :min(100, west.shape[1])-
                                            [trait.shape[1] if 100+traitrad<=loc[0] else 0][0]] , trait), axis=1)
    if type(east) != type(None) :
        trait = np.concatenate((trait, east[:trait.shape[0], :min(100, east.shape[1])-
                                            [trait.shape[1] if -traitrad*3+2<=loc[0]<=-traitrad else 0][0]]), axis=1)
    if type(north) != type(None) :
        trait = np.concatenate((north[:min(100, loc[1]-traitrad), :trait.shape[1]], trait), axis=0)
    if type(south) != type(None) :
        trait = np.concatenate((trait, south[:min(100, south.shape[1])-
                                             [trait.shape[0] if -traitrad*3+2<=loc[1]<=-traitrad+1 else 0][0], :trait.shape[1]]), axis=0)
        
    '''for i in range(len(trait)):
        print(trait[i])'''
    
    return trait+map_ #error occurs when map_ is rectangle

def conjunct2(loc, matrix, mapsize):
    empty = np.zeros(shape=(mapsize, mapsize))
    pillar = np.zeros(shape=(mapsize, matrix.shape[0]))
    for i in range(matrix.shape[0]):
        pillar[i+loc[0]][i] += 1
    pillar = np.dot(pillar, matrix)
    empty[:, loc[1]:loc[1]+matrix.shape[0]] += pillar
    return empty
        
def face_angle(subj, obj):
    return (math.atan((subj[1]-obj[1])/(subj[0]-obj[0]))/math.pi)*180

def apart_loc(obj : list,
          dist : int,
          angle : float):
    a, b = rotate(0, -dist, -angle/180)
    # direction by value → : 0, 360 ↗ : 45, ↑ : 90,
    # ↖ : 135, ← : 180, ↙ : 225, ↓ : 270, ↘ : 315
    return [obj[0]+roundoff(a), obj[1]+roundoff(a)]
    
def between_loc(subj : list,
                obj : list,
                
                strength : float = 1,
                resist : float = 0):
    
    increv = -(subj[0]-obj[0])/(subj[1]-obj[1])
    edge_x = ([1 if resist >= 0 else -1][0]*(resist/(increv**2+1)))**.5
    edge_y = increv*edge_x

    real_loc = [(strength*subj[0]+obj[0])/(strength+1)+edge_x, (strength*subj[1]+obj[1])/(strength+1)+edge_y]
    #print(real_loc)
    
    loc = [roundoff(real_loc[0]), roundoff(real_loc[1])]

    return loc
