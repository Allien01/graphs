def cria_matriz(vertices):
    matriz = []
    for i in range(vertices):
        linha = []
        for j in range(vertices):
            linha.append(" ")
        matriz.append(linha)
    return matriz

def cria_arquivo(graph_name, matriz):
    arquivo = graph_name + '.txt'
    file = open(arquivo, 'w')
    for i in matriz:
        line = ''
        for j in i:
            line += str(j)
        file.write(line + "\n")
    file.close()
    print("\nGrafo gerado! Arquivo salvo como '{}' ".format(arquivo))

def cria_arquivo2(graph_name):
    arquivo = graph_name + '.txt'
    file = open(arquivo, 'w')
    for i in M_micielsky:
        line = ''
        for j in i:
            line += str(j)
        file.write(line + "\n")
    file.close()
    print("\nGrafo gerado! Arquivo salvo como '{}' ".format(arquivo))

def print_matrix(g):
    for line in g:
        print(line)

def matriz_de_classe(option):
    fhandle = open(option)
    n = 0
    m = 0
    matrix = []
    for line in fhandle:
        linha = []
        line = line.strip()
        n += 1  # conta o numero de vertices
        for j in line:
            linha.append(int(j))
            if int(j) == 1:
                m += 1  # Conta o numero de arestas
        matrix.append(linha)  # Recria a matriz nxn
    vertices = []  # Criando os vertices de letra da matriz
    Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
                "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    g = Graph()  # Adicionando os vertices do grafo
    i = 0
    while i != n:
        vertices.append(Alphabet[i])
        node = Vertex(Alphabet[i])
        g.add_vertex(node)
        i += 1
    column = []  # Criando as arestas
    for j in range(n):
        lista = []
        for i in range(n):
            lista.append(matrix[i][j])
        column.append(lista)
    dic = {}  # Criando a lista de adjacencias
    for i in range(n):
        key = vertices[i]
        adj_list = []
        for j in range(n):
            if column[i][j] == 1:
                adj_list.append(vertices[j])
        dic[key] = adj_list
    edges = []
    for k, v in dic.items():
        for word in v:
            if ord(word) > ord(k):
                edges.append(k + word)
    for edge in edges:
        g.add_edge(edge[:1], edge[1:])
    return g

# Declaração das Classes e Métodos
class Vertex:
    def __init__(self, n):
        self.name = n
        self.neighbors = list()
        self.degree = 0

        self.distance = 1000
        self.color = 'white'

    def __repr__(self):
        return self.name

    def add_neighbor(self, v):
        if v not in self.neighbors:
            self.neighbors.append(v)
            self.neighbors.sort()


class Graph:
    vertices = {}
    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex.name not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
            return True
        else:
            return False

    def print_graph(self):
        print("---------------------------------------------------------------")
        print("\nImprimindo o Grafo:\n")
        for key in sorted(list(self.vertices.keys())):
            if self.vertices[key].distance == 1000:
                print("{ " + key + " : " + str(self.vertices[key].neighbors) +
                      "}")
            else:
                print("{ " + key + " : " + str(self.vertices[key].neighbors) +
                      "}")
        print("---------------------------------------------------------------")

    def connected_components(self):
        connected_components = list()
        for v in self.vertices:
            self.vertices.get(v).color = 'white'
        for v in self.vertices:
            if self.vertices.get(v).color == 'white':
                component = self.bfs(self.vertices.get(v))
                connected_components.append(component)
        return connected_components

    def avg_components(self, components):
        sum = 0
        for cc in components:
            sum = sum + len(cc)
        avg = sum / len(components)
        print("Media de vertices de cada Componente Conexa:", round(avg))
        return round(avg)

    def avg_size(self, num, components):
        total = 0
        for cc in components:
            if len(cc) == num:
                total += 1
        print("Componentes Conexas igual a media de vertices:", total)
        return total

    def unique_size(self, components):
        counter = 0
        for cc in components:
            if len(cc) == 1:
                counter += 1
        print("Componentes Conexas com 1 vertice:", counter)

    def bfs(self, vert):
        q = list()
        list_bfs = list()
        list_bfs.append(vert.name)
        vert.distance = 0
        vert.color = 'gray'
        for v in vert.neighbors:
            self.vertices[v].distance = vert.distance + 1
            q.append(v)
        while len(q) > 0:
            u = q.pop(0)
            list_bfs.append(u)
            node_u = self.vertices[u]
            node_u.color = 'gray'
            for v in node_u.neighbors:
                node_v = self.vertices[v]
                if node_v.color == 'white' and node_v.name not in q:
                    q.append(v)
                    if node_v.distance > node_u.distance + 1:
                        node_v.distance = node_u.distance + 1
        return sorted(list_bfs)

    def greedy_coloring(self):
        vertices_list = sorted(list(self.vertices), key = lambda x: len(self.vertices[x].neighbors), reverse = True)
        color_map = {}
        for node in vertices_list:
            available_colors = [True] * len(vertices_list)  # cores disponíveis: delta + 1
            for neighbor in self.vertices[node].neighbors:
                if neighbor in color_map:  # verifica o vertice no mapa de cores
                    color = color_map[neighbor]
                    available_colors[color] = False
            for color, available in enumerate(available_colors):
                if available:
                    color_map[node] = color
                    break
        return color_map


    def even_degree(self):
        vertices = self.vertices.keys()
        for v in vertices:
            grau = len(self.vertices[v].neighbors)
            if grau % 2 != 0:
                return False
        return True


class Micielsky:
    def adjacency_micielsky(self, w, x):
        if (w == x):
            matrix_kn = cria_matriz(w)
            for i in range(w):
                for j in range(w):
                    if (i == j):
                        matrix_kn[i][j] = 0
                    else:
                        matrix_kn[i][j] = 1
            return matrix_kn
        else:
            pass  # consertar resolucao do grafo de Micieslky
    return matrix_micielsky



# Fim da declaração de Classes e Métodos

# Início da execução do programa
try:
    option = int(input('''Por favor, escolha o método de entrada:\n
                  1- Carregar o grafo de um arquivo\n
                  2- Criar um grafo\n
                  3- Busca em largura\n
                  4- Criar grafo de Micielski\n
                  5- Coloração Gulosa\n
                  6- Verificar se é Euleriano\n
                  Opção: '''))
except:
    print("Opção inválida! Encerrando programa...")
    quit()

if option == 1:
    arquivo = input("\nDigite o nome do arquivo que deseja carregar('nomearquivo.txt'): ")
    print("---------------------------------------------------------------")
    print("Imprimindo Matriz na tela...")
    fhandle = open(arquivo)
    for i in fhandle:
        print(i.rstrip())
    quit()
elif option == 2:
    graph_name = input("\nInsira o nome do arquivo para salvar seu grafo: ")
    n = int(input("Insira o numero de Vertices do grafo: "))
    m = int(input("Insira o numero de Arestas do grafo: "))
    print("Insira as entradas da Diagonal Superior da Matriz de Adjacências")
    matriz = cria_matriz(n)   # cria a Matriz nxn
    for i in range(n):
        matriz[i][i] = '0'
        count = i + 1
        while count < n:
            j = count
            elemento = input("Digite um valor para [{}, {}]: ".format(i, j))
            matriz[i][j] = elemento
            matriz[j][i] = elemento
            count += 1
    print("\n")
    for linha in matriz:
        print(linha)
    cria_arquivo(graph_name, matriz)
    quit()
elif option == 3:
    option = input("""\nPor favor, insira o nome do arquivo como no exemplo abaixo:\n
                  'NomedoGrafo.txt'\n
                  Arquivo:  """)
    g = matriz_de_classe(option)
    g.bfs(g.vertices.get('A'))
    components_list = g.connected_components()
    print("\nComponentes Conexos:", components_list)
    print("Numero de Componentes Conexas:", len(components_list))
    components_avg = g.avg_components(components_list)
    components_size = g.avg_size(components_avg, components_list)
    g.unique_size(components_list)
elif option == 4:
    w = int(input("\nInforme o valor do número de Clique do grafo de Micieslky: "))
    x = int(input("Informe o valor do número Cromático do grafo de Micieslky: "))
    # graph_name = input("Insira o nome do arquivo para ser salvo: ")
    if (w>=2) and (x>=w):
        M = Micielsky()
        print("---------------------------------")
        print("Imprimindo Grafo de Micielsky")
        print(M.adjacency_micielsky(w, x))
        # M_micielsky = M.adjacency_micielsky(w, x)
        # cria_arquivo(graph_name, M_micielsky)
        quit()
    else:
        print("\nERROR!! Certifique-se que o número de Clique(w) é >= 2 e o número Cromático(X) >= nº de Clique(w)")
elif option == 5:
    option = input("""\nPor favor, insira o nome do arquivo como no exemplo abaixo:\n
                      'NomedoGrafo.txt'\n
                      Arquivo:  """)
    g = matriz_de_classe(option)
    g.bfs(g.vertices.get('A'))
    g.print_graph()
    x = g.greedy_coloring()
    print("Imprindo Coloração Gulosa: ")
    print(x)
elif option == 6:
    option = input("""\nPor favor, insira o nome do arquivo como no exemplo abaixo:\n
                      'NomedoGrafo.txt'\n
                      Arquivo:  """)
    g = matriz_de_classe(option)
    g.bfs(g.vertices.get('A'))
    components_list = g.connected_components()
    grau = g.even_degree()
    if (len(components_list) == 1) and (grau):
        print("O Grafo é Euleriano!")
    else:
        print("Não é Euleriano!")