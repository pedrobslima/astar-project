from dicts import *
from classes import *

# Para pegar a linha específica da estação seguinte:
#(é usado para saber se vai precisar trocar de linha ou não)
def StationByIdx(nodeA: Node, indexB: int, t: Tree):
    global lines
    nameA = nodeA.name
    nameB = 'E' + str(indexB + 1)
    color = 'blank'

    for c in lines.keys():
        if(nameA in lines[c] and nameB in lines[c]):
            color = c
    
    return t.getStation(nameB, color)

# Coisas de quicksort para a ordenação da fronteira:
#----------------------------------------------------
def partition(A: list, l: int, r: int):
    tam = r - l
    if(tam > 0):
        pivo = A[l].f
        i = l
        j = r+1

        cond = True
        while(cond):
            condi = True
            condj = True
            while(condi):
                i += 1
                condi = (A[i].f < pivo) and (i < r)
            while(condj):
                j -= 1
                condj = (A[j].f > pivo) and (j > l)

            A[i], A[j] = A[j], A[i]

            cond = j > i

        A[i], A[j] = A[j], A[i]

        A[l], A[j] = A[j], A[l]
        
        return j, A

def quicksort(A: list, l: int, r: int):
    if(l < r):
        # s = split position
        s, A = partition(A, l, r)
        A = quicksort(A, l, s-1) 
        A = quicksort(A, s+1, r)
    return A

#----------------------------------------------------

# Usado antes para converter matrizes:
'''
# Conversão de distância para tempo,
# não sei se uso ou não:

# 30km/h => 0,5km/min

def dist_to_time(dist: float):
    if(dist > 0):
        return dist * 0.5
    return dist

direta = []
real = []

for i in range(14):
    d = []
    r = []
    for j in range(14):
        d.append(dist_to_time(dist_direct[i][j]))
        r.append(dist_to_time(dist_real[i][j]))
    direta.append(tuple(d))
    real.append(tuple(r))

print(tuple(direta))
print(tuple(real))
'''