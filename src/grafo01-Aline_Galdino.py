def cria_matriz(vertices):
    matriz = []
    for i in range(vertices):
        linha = []
        for j in range(vertices):
            linha.append(" ")
        matriz.append(linha)
    return matriz



# adicionando prevenção contra input invalido
try:
    option = int(input('''Por favor, escolha o método de entrada:\n
                  1- Carregar o grafo de um arquivo\n
                  2- Criar um grafo\n
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

# cria o grafo
elif option == 2:
    graph_name = input("Insira o nome do arquivo para salvar seu grafo: ")
    m = int(input("Insira o número de Vertices: ")) # inserir um try/except aqui
    n = int(input("Insira o número de Arestas: ")) # inserir um try/except aqui
    print("Insira as entradas da Diagonal Superior da Matriz de Adjacências")
    matriz = cria_matriz(m)  #cria a matriz MxM
    for i in range(m):
        matriz[i][i] = '0'
        count = i + 1
        while count < m:
            j = count
            elemento = input("Digite um valor para [{}, {}]: ".format(i, j))
            matriz[i][j] = elemento
            matriz[j][i] = elemento
            count += 1
    for i in matriz:
            print(i)
    print("\nGrafo gerado! Arquivo salvo como '{}.txt' ".format(graph_name))        
else:
    print("Opção inexistente! Encerrando o programa...")

# cria o arquivo
arquivo = graph_name + '.txt'
file = open(arquivo, 'w')
for i in matriz:
    line = ''
    for j in i:
        line += j
    file.write(line +"\n")
file.close()
