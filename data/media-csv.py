arquivoFonte = "./data/attackers/BestAttackers.csv"
arq = open("./data/attackers/Total-CSV.csv","w")
arq.write("TEAM,SPIKES,FAULTS,SHOTS,TOTAL_ATTEMPTS\n")

linhas = open(arquivoFonte)
# 1,12,Bruno Lima,ARG,177,50,98,325,54.46

dict_paises = {}
list_paises = []
contador_paises = 0

#montando dicionario de selecoes para saber a posicao de cada pais na lista
#iniciando a lista de paises com os paises disponiveis
for linha in linhas:
    dados = linha.split(",")
    if len(dados[3]) == 3 and dados[3] not in dict_paises:
        dict_paises[dados[3]] = contador_paises
        contador_paises = contador_paises + 1
        list_paises.append({"name":dados[3],"dados":[]})

#reabrindo arquivo para resetar posicao do cursor
linhas = open(arquivoFonte)

#pegando cada linha e colocando no seu pais correspondente na lista
for linha in linhas:
    dado = linha.split(",")
    if len(dado[3]) == 3:
        list_paises[dict_paises[dado[3]]]["dados"].append(linha)

#fazendo as operacoes nos jogadores separados por pais na lista
for i in range(0,16):
    pais =  list_paises[i]["name"] #pegando o nome do pais
    
    spikes = []
    faults = []
    shots = []
    total = []
    success = []
    
    for dado in list_paises[i]["dados"]:
        spikes.append(int(dado.split(",")[4]))
        faults.append(int(dado.split(",")[5]))
        shots.append(int(dado.split(",")[6]))
        total.append(int(dado.split(",")[7]))

    tot = sum(total)
    spks = sum(spikes)
    flts = sum(faults)
    shts = sum(shots)
    
    arq.write("%s, %f, %f, %f, %f \n" % (pais, spks, flts, shts, tot))
