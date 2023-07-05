from functions import *

# Estações possíveis
E1az = Node('E1', 'azul')
E2az = Node('E2', 'azul')
E2am = Node('E2', 'amarelo')
E3az = Node('E3', 'azul')
E3vm = Node('E3', 'vermelho')
E4az = Node('E4', 'azul')
E4vd = Node('E4', 'verde')
E5az = Node('E5', 'azul')
E5am = Node('E5', 'amarelo')
E6az = Node('E6', 'azul')
E7am = Node('E7', 'amarelo')
E8am = Node('E8', 'amarelo')
E8vd = Node('E8', 'verde')
E9am = Node('E9', 'amarelo')
E9vm = Node('E9', 'vermelho')
E10am = Node('E10', 'amarelo')
E11vm = Node('E11', 'vermelho')
E12vd = Node('E12', 'verde')
E13vm = Node('E13', 'vermelho')
E13vd = Node('E13', 'verde')
E14vd = Node('E14', 'verde')

metro = Tree()

metro.conect = dist_direct
metro.stations = [E1az, E2az, E2am, E3az, E3vm, E4az, E4vd, 
                  E5az, E5am, E6az, E7am, E8am, E8vd, E9am, E9vm, 
                  E10am, E11vm, E12vd, E13vm, E13vd, E14vd]

origin = ''
dest = ''

while(not(origin in metro.getNames() and dest in metro.getNames())):
    origin = input("Estação de origem: ")
    dest = input("Estação de destino: ")
    print('\n')

EXbl = Node(origin, 'blank')
idx_dest = int(dest[1:])-1
x = dist_direct[int(origin[1:])-1][idx_dest] # mudar nome

s0 = State(EXbl, 0, x, [])

metro.frontier.append(s0)

count = 1
while(True):
    count = printFrontier(metro, count)
    # nova geração:
    new_gen = []
    sum_weight = 0
    best = metro.frontier[0]

    if(best.station.name == dest or count > 9): break
    # tá dando erro por aqui ó vvv
    for j in range(14):
        g_temp = dist_real[best.station.idx()][j]
        if(g_temp > 0):
            sum_weight = best.g + g_temp
            new_station = getThing(best.station, j, metro)
            if(new_station.line != best.station.line):
                sum_weight += 4
            history = best.previous + [best.station.name]
            new_state = State(new_station, sum_weight, dist_direct[best.station.idx()][idx_dest], history)
            print(new_state)
            new_gen.append(new_state)
    
    # atualização fronteira:
    metro.frontier = new_gen + metro.frontier[1:]
    metro.frontier = quicksort(metro.frontier, 0, len(metro.frontier)-1)

# printar caminho
print('CAMINHO:')
for i in range(len(best.previous)):
    print(best.previous[i], ' -> ', end='')
print(f'''{best.station.name}

Tempo total: {best.f}''')