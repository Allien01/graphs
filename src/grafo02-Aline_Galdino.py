"""
    Início do Programa 1
"""

def cria_matriz(vertices):
    matriz = []
    for i in range(vertices):
        linha = []
        for j in range(vertices):
            linha.append(" ")
        matriz.append(linha)
    return matriz


def cria_arquivo(graph_name):
    arquivo = graph_name + '.txt'
    file = open(arquivo, 'w')
    for i in matriz:
        line = ''
        for j in i:
            line += j
        file.write(line + "\n")
    file.close()
    print("\nGrafo gerado! Arquivo salvo como '{}' ".format(arquivo))


# Adicionando prevenção contra input inválido
try:
    option = int(input('''Por favor, escolha o método de entrada:\n
                  1- Carregar o grafo de um arquivo\n
                  2- Criar um grafo\n
                  3- Busca em largura\n
                  Opção: \n\n'''))
except:
    print("Opção inválida! Encerrando programa...")
    quit()

if option == 1:
    arquivo = input("Digite o nome do arquivo que deseja carregar('nomearquivo.txt'):\n")
    print("---------------------------------------------------------------")
    print("Imprimindo Matriz na tela...")
    fhandle = open(arquivo)
    for i in fhandle:
        print(i.rstrip())
    quit()
elif option == 2:
    graph_name = input("Insira o nome do arquivo para salvar seu grafo: ")
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
    cria_arquivo(graph_name)
    quit()
elif option == 3:
    option = input("""Por favor, insira o nome do arquivo como no exemplo abaixo:\n
                  'NomedoGrafo.txt'\n
                  Arquivo:\n\n""")

"""
    Fim do Programa 1
"""

"""
    Início do Programa 2
"""

# Declaração das Classes e Métodos
class Vertex:

    def __init__(self, n):
        self.name = n
        self.neighbors = list()

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
                print("Vertice: " + key + " | Vertices adjacentes: " + str(self.vertices[key].neighbors) +
                      "  | Distancia: Infinita")
            else:
                print("Vertice: " + key + " | Vertices adjacentes: " + str(self.vertices[key].neighbors) +
                  "  | Distancia: " + str(self.vertices[key].distance))
        print("Fim do Grafo")
        print("---------------------------------------------------------------")

    def connected_components(self):
        connected_components = list()
        for v in self.vertices:
            self.vertices.get(v).color = 'white'

        for v in self.vertices:
            if self.vertices.get(v).color == 'white':
                component = self.bfs(self.vertices.get(v))
                connected_components.append(component)

        print("\nComponentes Conexos:",connected_components)
        print("Numero de Componentes Conexas:", len(connected_components))
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

# Fim da declaração de Classes e Métodos

fhandle = open(option)
n = 0
m = 0
matrix = []
print("---------------------------------------------------------------")
print("Imprindo a Matriz de Adjacências...")
for line in fhandle:
    linha = []
    line = line.strip()
    print(line)
    n += 1  # conta o numero de vertices
    for j in line:
        linha.append(int(j))
        if int(j) == 1:
            m += 1  # Conta o numero de arestas
    matrix.append(linha)  # Recria a matriz nxn
m = m // 2  # Divide o numero total de arestas por 2

# Criando os vertices de letra da matriz
vertices = []
Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L",
            "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

# Adicionando os vertices do grafo
g = Graph()
i = 0

while i != n:
    vertices.append(Alphabet[i])
    node = Vertex(Alphabet[i])
    g.add_vertex(node)
    i += 1


# Criando as arestas
column = []
for j in range(n):
    lista = []
    for i in range(n):
        lista.append(matrix[i][j])
    column.append(lista)

# Criando a lista de adjacencias
dic = {}
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
            edges.append(k+word)

for edge in edges:
    g.add_edge(edge[:1], edge[1:])

g.bfs(g.vertices.get('A'))
components_list = g.connected_components()
components_avg = g.avg_components(components_list)
components_size = g.avg_size(components_avg, components_list)
g.unique_size(components_list)
