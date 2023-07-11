# astar-project
projeto da disciplina de sistemas inteligentes sobre o algoritmo A*

astar.py é o arquivo principal, nele possui a função A* e será usado na apresentação

functions.py é um arquivo que possui funções úteis que serão usadas no A*:
  - StationByIdx: função para pegar a linha específica da estação seguinte
  - Quicksort:
    - partition()
    - quicksort()

classes.py é um arquivo que possui as seguintes classes:
  - Node: classe que vai representar um nó da estação
    - name: atributo _str_ que diz o nome da estação
    - line: atributo _str_ que diz a cor da estação
    - idx: atributo _int_ que diz o índice do nó nas matrizes de conexões
  - State: classe que vai representar os estados na fronteira do algoritmo
    - station: atributo _Node_ que diz a estação do estado atual
    - g: atributo _float_ que diz o peso do tempo gasto no caminho atual
    - h: atributo _float_ que diz o tempo, em min, até a estação de destino, em linha reta
    - f: atributo _float_ que representa função g+h
    - path: atributo _list_ que armazena o nome das estações que indicam o caminho tomado até o estado atual
  - Tree: classe que representa o grafo que contém os nós (_Node_)
    - stations: atributo _list_ que representa a lista de todos os nós do grafo
    - real_conect: atributo _tuple_ que representará a matriz contendo as distâncias (em min) reais entre estações
    - conect: atributo _tuple_ que representará a matriz contendo as distâncias (em min) diretas entre estações
    - frontier: atributo _list_ que representa a fronteira atual de estados
    - frontGen: atributo _int_ com o número da geração atual da fronteira
    - ndNames: atributo _list_ com a lista dos nomes em _str_ das estações
    - current_gen: atributo _list_ com a lista de novos estados (só é usado no print)

dicts.py é um arquivo que possui:
  - dist_direct: matriz com as distâncias diretas (em min) entre estações
  - dist_real: matriz com as distâncias reais (em min) entre estações
  - lines: _dict_ que conecta as estações e suas linhas

teste.py é um arquivo que é essencialmente a mesma coisa que astar.py, mas serve para fazer os testes de forma mais rápida

mapa.png é uma imagem do mapa recebido para o exercício
