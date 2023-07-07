from functions import *

metro = Tree(dist_direct)

# Estações-linha pertencentes à árvore
metro.addNode('E1', 'azul') # E1az
metro.addNode('E2', 'azul') # E2az
metro.addNode('E2', 'amarelo') # E2am
metro.addNode('E3', 'azul') # E3az
metro.addNode('E3', 'vermelho') # E3vm
metro.addNode('E4', 'azul') # E4az
metro.addNode('E4', 'verde') # E4vd
metro.addNode('E5', 'azul') # E5az
metro.addNode('E5', 'amarelo') # E5am
metro.addNode('E6', 'azul') # E6az
metro.addNode('E7', 'amarelo') # E7am
metro.addNode('E8', 'amarelo') # E8am
metro.addNode('E8', 'verde') # E8vd
metro.addNode('E9', 'amarelo') # E9am
metro.addNode('E9', 'vermelho') # E9vm
metro.addNode('E10', 'amarelo') # E10am
metro.addNode('E11', 'vermelho') # E11vm
metro.addNode('E12', 'verde') # E12vd
metro.addNode('E13', 'vermelho') # E13vm
metro.addNode('E13', 'verde') # E13vd
metro.addNode('E14', 'verde') # E14vd

origin = ''
dest = ''

# Para garantir que escolham uma estação dentro do conjunto formado:
while(not(origin in metro.ndNames and dest in metro.ndNames)):
    origin = input("Estação de origem: ")
    dest = input("Estação de destino: ")
    print('\n')

idx_dest = int(dest[1:])-1 # o índice da estação de destino na tabela
h_og = metro.conect[int(origin[1:])-1][idx_dest] # h(n) da estação de origem

#   [ usar metro.getStation(origin, 'blank') 
# v [ ao invés de só declarar o novo node direto?
s0 = State(Node(origin, 'blank'), 0, h_og, []) # estado inicial

metro.frontier.append(s0) # adicionando à fronteira
metro.printFrontier()

while(metro.frontier[0].station.name != dest):
    # NOVA GERAÇÃO:
    new_gen = [] # lista de estados
    sum_weight = 0 # soma dos pesos total, conhecido como g(n)
    best = metro.frontier[0] # a opção escolhida sempre será a 1a da fronteira

    for j in range(14): # a ideia é que ele vai verificar todas as conexões da matriz dist_direct
        g_temp = dist_real[best.station.idx][j] # 1) Pega a dist real entre essa e a próxima estação
        if(g_temp > 0): # 1.5) Se for igual a -1, é pq não existe conexão, se for 0 é pq é a mesma estação
            sum_weight = best.g + g_temp # 2) Soma o peso do caminho atual + a nova conexão
            new_station = StationByIdx(best.station, j, metro) # 3) Pega a nova estação apenas pela
                                                               # estação atual e o índice da próxima
            if(new_station.line != best.station.line): # 4) Adiciona +4min se as
                sum_weight += 4                        # linhas forem diferentes
            history = best.path + [best.station.name] # 5) Cria o histórico de estações do novo estado
            # v 6) Cria o novo estado:
            new_state = State(new_station, sum_weight, metro.conect[new_station.idx][idx_dest], history)
            '''print(new_state)''' # para testes [tirar na versão final]
            new_gen.append(new_state) # 7) Adiciona o novo estado na lista da nova geração
    
    # ATUALIZAÇÃO FRONTEIRA:
    # 1) Adiciona a nova geração à fronteira:
    metro.updateFrontier(new_gen)
    # 2) Ordena a fronteira de menor para maior, baseado na função f(n) de cada estado:
    metro.frontier = quicksort(metro.frontier, 0, len(metro.frontier)-1)
    # 2.5) Printar fronteira atual
    metro.printFrontier()

# PRINTAR CAMINHO:
print(f'''\nCAMINHO:\n{'-'*30}
{metro.frontier[0].arrowPath()}
{'-'*30}
Tempo total: {metro.frontier[0].g:.2f}min
{'-'*30}''')
