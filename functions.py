from dicts import *
from classes import *
from math import floor

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
