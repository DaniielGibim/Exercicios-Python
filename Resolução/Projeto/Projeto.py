import csv

def criarMenu():
    print('1. carregar dados do arquivo')
    print('2. listar todos os dados')
    print('3. Qual o percentual de vitórias dos times mandantes')
    print('4. Crie uma nova coluna para informar se o jogo ocorreu durante a manhã, o dia ou a noite.')
    print('5. Considerando que a vitória dá 3 pontos ao time vencedor e um ponto a cada empate, '
          'calcule a pontuação global de cada time desde 2003 e informe o primeiro e o segundo colocados.')
    print('6. Qual a arena que teve mais jogos?')
    print('7. Qual o ano com a maior média de gols?')
    print('8. Peça ao usuário o nome de um time. Depois informe qual o ano que ele teve a melhor campanha '
          '(considerando que vitória é 3 pontos e empate 1 ponto)')
    print('9. Qual o estado recebeu mais jogos?')
    print('10. Qual time tem o pior saldo de gols em cada ano?')
    print('11. Qual a média de gols dos times de São Paulo no ano de 2003')
    print('12. Gere um novo arquivo informando o ano e time campeão dos dados disponíveis.')
    print('13. Crie uma nova consulta a seu critério.')

    op = int(input('Digite a opcao desejada: '))
    return op

def salvarNaMatriz(mat, lista):
    mat.append(lista)

def carregarArquivo(mat, nomeArq):

    arquivo = open(nomeArq, 'r', encoding='utf-8')
    arquivo.readline()
    leitor_csv = csv.reader(arquivo)

    for linha in leitor_csv:
        salvarNaMatriz(mat, linha)
    arquivo.close()


def listar(mat):
    for i in range(len(mat)):
        print(mat[i])

def porcentagemVitorias(mat):
    vitorias = 0
    for i in range(len(mat)):          #Posso usar para pegar a % de vitoria dos visitante e até msm % de empates
        if mat[i][13] > mat[i][14]:
            vitorias = vitorias + 1

    return vitorias /100

def horaDosJogosSplitada(horas):
    horasSplitada = horas.split(':')
    hora = horasSplitada[0]
    horaFormatda = int(hora)

    return horaFormatda

def criarColuna(mat):

    for linha in range(len(mat)):
        hora = mat[linha][3]
        horaFormatada = horaDosJogosSplitada(hora)

        if horaFormatada >= 12 and horaFormatada < 18:
            mat[linha].append('Tarde')

        elif horaFormatada >= 18 and horaFormatada <= 24:
            mat[linha].append('Noite')

        else:
            mat[linha].append('Manhã')

def pontuacaoGlobal(mat):
    dicionarioTimes = {}

    for i in range(len(mat)):
        timeMandante = mat[i][5]
        timeVisitante = mat[i][6]
        pontos = 0

        if timeMandante not in dicionarioTimes:
            dicionarioTimes[timeMandante] = 0
        if timeVisitante not in dicionarioTimes:
            dicionarioTimes[timeVisitante] = 0

    for i in range(len(mat)):
        colunaTimeGanhador = mat[i][11]

        if colunaTimeGanhador == '-':
            timeMandante = mat[i][5]
            timeVisitante = mat[i][6]
            dicionarioTimes[timeMandante] = dicionarioTimes[timeMandante] + 1
            dicionarioTimes[timeVisitante] = dicionarioTimes[timeVisitante] + 1

        else:
            dicionarioTimes[colunaTimeGanhador] = dicionarioTimes[colunaTimeGanhador] + 3

    primeiroLugar = ''
    segundoLugar = ''

    for timeCorrente in dicionarioTimes:
        if primeiroLugar == '':
            primeiroLugar = timeCorrente

        elif segundoLugar == '':
            segundoLugar = timeCorrente

        if dicionarioTimes[timeCorrente] > dicionarioTimes[primeiroLugar]:
            primeiroLugar = timeCorrente

        elif segundoLugar != '' and dicionarioTimes[timeCorrente] > dicionarioTimes[segundoLugar]:
            segundoLugar = timeCorrente

    print(dicionarioTimes)
    print(primeiroLugar, segundoLugar)

def estadoMaisJogos(mat, colunaEstado): #função que utiliza Dicionário

    dicionarioEstado = {}
    for i in range(len(mat)):
        estado = mat[i][colunaEstado]
        if estado in dicionarioEstado:
            dicionarioEstado[estado] = dicionarioEstado[estado] + 1
        else:
            dicionarioEstado[estado] = 0

    estadoJogos = ''
    qtdeVezesQueJogaram = 0
    for estado in dicionarioEstado:
        if dicionarioEstado[estado] > qtdeVezesQueJogaram:
            qtdeVezesQueJogaram = dicionarioEstado[estado]
            estadoJogos = estado

    return estadoJogos, qtdeVezesQueJogaram

def estadioMaisJogos(mat, colunaEstadio): #função que utiliza Dicionário

    dicionarioEstadio = {}
    for i in range(len(mat)):
        estado = mat[i][colunaEstadio]
        if estado in dicionarioEstadio:
            dicionarioEstadio[estado] = dicionarioEstadio[estado] + 1
        else:
            dicionarioEstadio[estado] = 1

def recuperarAno(data):
    dataSplitada = data.split('/')
    ano = dataSplitada[2]
    anoFormatado = int(ano)
    return anoFormatado

def golsNoAno(mat):
    dicionarioAno = {}
    dicionarioQuantidadeDeJogos = {}
    maiorQtdeDeGols = 0
    anoComMaiorMediaGols = ''
    maiorMediaDeGols = 0
    for i in range(len(mat)):
        dataCompleta = mat[i][2]
        golsfeitos = int(mat[i][13]) + int(mat[i][14])
        ano = recuperarAno(dataCompleta)

        if ano not in dicionarioAno:
            dicionarioAno[ano] = golsfeitos
            dicionarioQuantidadeDeJogos[ano] = 1

        else:
            dicionarioAno[ano] = dicionarioAno[ano] + golsfeitos
            dicionarioQuantidadeDeJogos[ano] = dicionarioQuantidadeDeJogos[ano] + 1



    for ano in dicionarioAno:
        if dicionarioAno[ano] > maiorQtdeDeGols:
            maiorQtdeDeGols = dicionarioAno[ano]
            anoComMaiorMediaGols = ano
            maiorMediaDeGols = dicionarioAno[ano] / dicionarioQuantidadeDeJogos[ano]
            # dicionarioAno[ano] > maiorMediaDeGols
            # maiorMediaDeGols = dicionarioAno[ano]

    print(f'O ano que teve a maior média de gols foi {anoComMaiorMediaGols} tendo {maiorMediaDeGols} gols por partida.')
    print(f'O ano {anoComMaiorMediaGols} foi o que teve maior quantidade de gols sendo:{maiorQtdeDeGols} ')
    print(dicionarioAno, dicionarioQuantidadeDeJogos)

def campanhaDeCadaTime(mat):
    # Peça ao usuário o nome de um time. Depois informe qual o ano que ele teve a melhor campanha
    #  considerando que vitória é 3 pontos e empate 1 ponto)')
    dicionarioTimes = {}

    timeEscolhido = input('Dgite o time esolhido')
    for i in range(len(mat)):
        if timeEscolhido.upper() == mat[i][5].upper():
            dicionarioTimes[timeEscolhido] = 0
            if timeEscolhido == mat[i][11]:
                dicionarioTimes[timeEscolhido] = dicionarioTimes[timeEscolhido] + 3
            else:
                dicionarioTimes[timeEscolhido] = dicionarioTimes[timeEscolhido] + 1

    print(dicionarioTimes)

opcao = -1
matriz = []
nomeArquivo = 'campeonato-brasileiro-gols.csv'

while opcao != 0:
    opcao = criarMenu()

    if opcao == 1:
        carregarArquivo(matriz, nomeArquivo)

    elif opcao == 2:
        listar(matriz)

    elif opcao == 3:
        print('A porcentagem de vitoria dos mandantes é: ' + str(porcentagemVitorias(matriz)) + '%')

    elif opcao == 4:
        criarColuna(matriz)

    elif opcao == 5:
        pontosGlobal = pontuacaoGlobal(matriz)
        #print(pontosGlobal)
        # for i in pontosGlobal.items():
        #     print(i)

    elif opcao == 6:
        colunaestaido = 12
        print('O estadio que recebeu a maior quantidade de jogos foi: ' + str(estadoMaisJogos(matriz, 12)))

    elif opcao == 7:
        golsNoAno(matriz)

    elif opcao == 8:
        campanhaDeCadaTime(matriz)

    elif opcao == 9:
        print('O estado que recebeu a maior quantidade de jogos foi: ' + str(estadoMaisJogos(matriz, 15)))