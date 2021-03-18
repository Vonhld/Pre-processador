from os import system

arq = "entrada.c"
def tratamento(arq):
    arquivo = open(arq,'r')
    if (arquivo == None):
        print("Erro ao ler arquivo")
    
    # Separa o código do arquivo entrada por linhas.
    lista = []
    for line in arquivo:
        linha = line.strip('\n')
        lista.append(linha)
    arquivo.close()

    # Remove os comentários //
    for linha in lista:
        if '//' in linha:
            aux = linha.index('/')
            aux2 = lista.index(linha)
            lista[aux2] = linha[0:aux]

    # Separa as "listas de string" em "lista de listas de strings".
    listaEspaco = []
    for esq in lista:
        varA = esq.split()
        listaEspaco.append(varA)
    
    # Armazenando os includes
    listainclude = []
    for db in listaEspaco:
        if ("#include" in db):
            listainclude.append(db[1][1:-1])
            del(listaEspaco[listaEspaco.index(db)])

    # Coloca as linhas da biblioteca na frente
    if len(listainclude) != 0:
        for w in listainclude:
            aux = tratamento(w)
            listaEspaco = aux + listaEspaco 
    return listaEspaco

listaEspaco = tratamento(arq)

# Muda os '#define' pelos seus determinados valores.
def tratardefine(nomedef, valordef, listaEspaco):
    for linhas in listaEspaco:
        for palavras in linhas:
            if nomedef in palavras:
                indexLinha = listaEspaco.index(linhas)
                indexPalavra = listaEspaco[indexLinha].index(palavras)
                listaEspaco[indexLinha][indexPalavra] = listaEspaco[indexLinha][indexPalavra].replace(nomedef, valordef)
    return listaEspaco

# Armazenando os defines em listas e deletando a linha dos '#define'.
listaNomeDef = []
listaValorDef = []

for db in listaEspaco:
    if '#define' in db:
        listaEspaco = tratardefine(db[1], db[2], listaEspaco)
        listaEspaco[listaEspaco.index(db)] = ''


# Remove os comentários do tipo '/*' '*/' do código.
for string in listaEspaco:
    index = listaEspaco.index(string)
    listaEspaco[index] = ''.join(listaEspaco[index])

listaEspaco = ''.join(listaEspaco)
listaEspaco = listaEspaco.replace('/*','*/')
listaEspaco = listaEspaco.split('*/')

for y in range (1,len(listaEspaco),2):
    listaEspaco[y] = ""
listaEspaco = ''.join(listaEspaco)

# tratamento para execução
funcoes_em_c = ['void','int','if','char']
printf = 'print f'
for s in funcoes_em_c:
    if s in listaEspaco:
        j = s + ' '
        listaEspaco = listaEspaco.replace(s,j)
if printf in listaEspaco:
    listaEspaco = listaEspaco.replace(printf,'printf')




system('cls')
print('Pronto!')
print('\n\n\n')
system('pause')

with open('ProgramaPreProcessado.c', 'w') as output:
    output.write(listaEspaco)
    output.close()
