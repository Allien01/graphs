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
        file.write(line +"\n")
    file.close()
    print("\nGrafo gerado! Arquivo salvo como '{}' ".format(arquivo))

# adicionando prevenção contra input invalido
try:
    option = int(input('''Por favor, escolha o método de entrada:\n
                  1- Carregar o grafo de um arquivo\n
                  2- Criar um grafo\n
                  3- Busca em largura\n
                  Opção: '''))
except:
    print("Opção inválida! Encerrando programa...")
    quit()

if option == 1:
    arquivo = input("Digite o nome do arquivo que deseja carregar('arquivo.txt'): ")
    fhandle = open(arquivo)
    for i in fhandle:
        print(i.rstrip())
    quit()
elif option == 2:
    graph_name = input("Insira o nome do arquivo para salvar seu grafo: ")
    n = int(input("Insira o número de Vertices: "))  # inserir um try/except aqui
    m = int(input("Insira o número de Arestas: "))  # inserir um try/except aqui
    print("Insira as entradas da Diagonal Superior da Matriz de Adjacências")
    matriz = cria_matriz(n)   # cria a Matriz MxM
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
elif option == 3:
     option = input("""Por favor, Insira o nome do arquivo:\n
                  1- 'Grafoteste.txt'\n
                  2- 'Grafobipartido.txt'\n
                  3- 'Grafo.txt'
                  Opção:""" )

# Inicio da parte 2 do programa
fhandle = open(option)
n = 0
m = 0
matrix = []
for line in fhandle:
    linha = []
    line = line.strip()
    print(line)
    n += 1  # conta o numero de vertices
    for j in line:
        linha.append(int(j))
        if int(j) == 1:
            m += 1  # conta o numero de arestas
    matrix.append(linha)  # recria a matriz NxN
m = m // 2

"""
# SEPARANDO O PROGRAMA 2
"""

# criando os vertices de letra da matriz
vertices = []
Alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

i = 0
while i != n:
    vertices.append(Alphabet[i])
    i += 1


column = []
for j in range(n):
    lista = []
    for i in range(n):
        lista.append(matrix[i][j])
    column.append(lista)

dic = {}
for i in range(n):
    key = vertices[i]
    adj_list = []
    for j in range(n):
        if column[i][j] == 1:
            adj_list.append(vertices[j])
    dic[key] = adj_list
    print(key, dic[key])

"""
Criando os nós da lista encadeada
"""

class Node:
    data = None
    adjacent_nodes = []
    color = None

    def __init__(self, data):
        self.data = data    
