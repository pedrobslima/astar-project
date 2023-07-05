class Node: # E4az ou E4vd
    def __init__(self, name: str, color: str):
        self.name = name # E4
        self.line = color # azul ou verde
    def idx(self):
        return int(self.name[1:]) - 1 # 3

# Estado: [<Estação>, <g(n)>, <h(n)>, <lista de est. anteriores>]
class State:
    def __init__(self, station: Node, g: float, h: float, previous: list):
        self.station = station
        self.g = g
        self.h = h
        self.f = g + h
        self.previous = previous


class Tree:
    def __init__(self):
        self.stations: list
        self.conect: tuple
        self.frontier = []
    def getNames(self):
        temp = []
        for stt in self.stations:
            if(stt.name not in temp):
                temp.append(stt.name)
        return temp
    def getStation(self, name: str, line: str):
        for e in self.stations:
            if(e.name == name and e.line == line):
                return e
        return Node(name, line)