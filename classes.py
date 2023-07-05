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
        self.previous = previous 
        # ^ lista de estações anteriores (apenas os nomes)

# Tree representa a árvore completa
class Tree:
    def __init__(self):
        self.stations = [] # lista de Nodes
        self.conect: tuple # dist_direct (tirar dps?)
        self.frontier = [] # fronteira atual
    
    # Para adicionar nós à árvore:
    def addNode(self, station_name: str, station_line: str):
        EXbl = Node(station_name, station_line) # EX_blank é só um nome place holder
        self.stations.append(EXbl)              # para o próximo nó a ser adicionado
    
    # Para pegar uma lista com apenas os nomes das estações:
    def getNames(self):
        temp = []
        for stt in self.stations:
            if(stt.name not in temp):
                temp.append(stt.name)
        return temp
    
    # Para pegar o objeto nó com esses atributos:
    def getStation(self, name: str, line: str):
        for e in self.stations:
            if(e.name == name and e.line == line):
                return e
        #return Node(name, line)