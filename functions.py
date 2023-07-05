from dicts import *
from classes import *

def getThing(nodeA: Node, indexB: int, t: Tree): # mudar nome
    global lines
    nameA = nodeA.name
    nameB = 'E' + str(indexB + 1)
    color = 'blank'

    for c in lines.keys():
        if(nameA in lines[c] and nameB in lines[c]):
            color = c
    
    return t.getStation(nameB, color)

def partition(A: list, l: int, r: int):
    tam = r - l
    if(tam > 0):
        pivo = A[l].f
        i = l+1
        j = r

        while(j > i):
            while((A[i].f < pivo) and (i < r)):
                i += 1
            while((A[j].f > pivo) and (j > l)):
                j -= 1

            temp = A[i]
            A[i] = A[j]
            A[j] = temp

        temp = A[i]
        A[i] = A[j]
        A[j] = temp

        A[l] = A[j]
        A[j] = pivo
        return j, A

def quicksort(A: list, l: int, r: int):
    if(l < r):
        # s = split position
        s, A = partition(A, l, r)
        return quicksort(A, l, s-1) + A[s:s+1] + quicksort(A, s+1, r)
    return A

def printFrontier(t: Tree, gen: int):
    print(f'{gen}a:', end='')
    '''for state in t.frontier:
        print(state)
        print(f' [{state.station.name}, {state.station.line}, {state.g}+{state.h}={state.f}]')
    '''
    print(t.frontier)
    print('_'*20)
    return gen+1

# 30km/h => 0,5km/min

'''def dist_to_time(current: int, next_station: int, current_line: str):
    dist = dist_real[current][next_station]
    time = 0
    if(dist > 0):
        if(name_st(next_station) not in lines[current_line]):
            time += 4
        time += dist * 0.5
    return time'''


