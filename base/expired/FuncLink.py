from default_functions import *
from calculation import *

class FunctionLink:
    def __init__(self, genes, moblist, me_loc):
        self.genes = genes
        
    def linker(self, code):
            if code[1] == 0:
                dirs = []
                for i in moblist:
                    location = [moblist[i][0]-me_loc[0], moblist[i][1]-me_loc[1]]
                    dirs.append(dir_cal_4(location))
                    return(dir4_response(dirs, method = self.genes[code[0]]))
