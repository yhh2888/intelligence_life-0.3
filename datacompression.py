import random, itertools

def datatest(num, data):
    done, had = False, 0
    alter_data = [int(i, 16) for i in data]
    datan = [int(i, 16) for i in data]
    perms = itertools.permutations("0123456789abcdef")
        
    while True:
        alter_data = []
        tbp = 0
        for i in datan:
            nth_perm = next(itertools.islice(perms, tbp, None))
            alter_data.append(int(nth_perm[i], 16))
            datan = alter_data
            tbp += 1
                
        data_dic = {}
        
        for i in range(len(data)-1):
            fir, sec = data[i], data[i+1]
            if fir+sec in data_dic:
                data_dic[fir+sec] += 1
            else:
                data_dic[fir+sec] = 1
                
        for i in data_dic:
            if data_dic[i] >= num and len(set(data)) != 16:
                changed = [j for j in range(0, 16) if j not in set(data)][0]
                changer = i
                for j in range(len(data)-1):
                    if data[j]+data[j+1] == changer:
                        data = data[0:j]+str(changed)+data[j+2:]
                data = data + changer + changed + hex(had) + '0'
                return data
            
        had += 1

thenumb = ''.join([hex(random.randint(0, 15))[2:] for i in range(50)])
