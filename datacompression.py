import random, itertools

def datatest(num, data):
    done, had = False, 0
    alter_data = [int(i, 16) for i in data]
    datan = [i for i in data]
    perms = itertools.permutations("0123456789abcdef")
    print(data)
    
    while True:
        alter_data = []
        for j in range(len(datan)):
            nth_perm = next(itertools.islice(perms, j, None))
            alter_data.append(int(nth_perm[int(str(datan[j]), 16)], 16))

        datan = [hex(i)[2:] for i in alter_data]
        data_dic = {}
        
        for i in range(len(datan)-1):
            fir, sec = datan[i], datan[i+1]
            if datan[i-1] == fir:
                continue
            if fir+sec in data_dic:
                data_dic[fir+sec] += 1
            else:
                data_dic[fir+sec] = 1
                
        for i in data_dic:
            if data_dic[i] >= num and 0 not in set(datan):
                changer = i
                datan = ''.join(datan)
                print(datan)
                k = 0
                for j in range(len(datan)-1):
                    if datan[j-k]+datan[j+1-k] == i:
                        datan = datan[0:j-k]+str(0)+datan[j-k+2:]
                        k += 1
                print(datan, changer, str(hex(had)[2:]))
                datan = datan + changer + str(hex(had)[2:])
                return datan
            
        had += 1

thenumb = ''.join([hex(random.randint(0, 15))[2:] for i in range(32)])
