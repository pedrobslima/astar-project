# Node representam <nome da estação> + <linha>
class Node: # E4az ou E4vd
    def __init__(self, name: str, color: str):
        self.name = name # E4
        self.line = color # azul ou verde
        self.idx = int(self.name[1:]) - 1 # 3
            # ^ Para pegar o índice nas matrizes 
            #   mais facilmente

# Estado: [<Estação>, <g(n)>, <h(n)>, <lista de est. anteriores>]
class State:
    def __init__(self, station: Node, g: float, h: float, previous: list):
        self.station = station # E4az
        self.g = g # 200
        self.h = h # 100
        self.f = g + h # 300
        self.path = previous 
        # ^ lista de estações anteriores (apenas os nomes)

    def arrowPath(self):
        return ' -> '.join(self.path + [self.station.name])

# Tree representa a árvore completa
class Tree:
    def __init__(self, conections: tuple):
        self.stations = [] # lista de Nodes
        self.conect = conections # dist_direct
        self.frontier = [] # fronteira atual
        self.frontGen = 1 # geração atual da fronteira
        self.ndNames = [] # lista com os nomes das estações
        self.current_gen = [] # lista com os novos estados (só é usado no print)
    
    # Para adicionar nós à árvore:
    def addNode(self, station_name: str, station_line: str):
        EXbl = Node(station_name, station_line) # EX_blank é só um nome place holder
        self.stations.append(EXbl)              # para o próximo nó a ser adicionado
        if(station_name not in self.ndNames):
            self.ndNames.append(station_name)
    
    # Para pegar o objeto nó com esses atributos:
    def getStation(self, name: str, line: str):
        for e in self.stations:
            if(e.name == name and e.line == line):
                return e

    def updateFrontier(self, generation: list):
        self.current_gen = generation
        self.frontier = generation + self.frontier[1:]
        self.frontGen += 1
        
    def printFrontier(self):
        print(f'--------------------[F{self.frontGen}]--------------------')
        for state in self.frontier:
            print(f'[{state.station.name}-{state.station.line}] ', end='')
            print(f'\tf(n)={state.f:.2f} | h(n)={state.h:.2f} | g(n)={state.g:.2f}', end='')
            print(f' ||  Path: {state.arrowPath()}', end='')
            if(state in self.current_gen): print('\t [new!]', end='')
            print('')