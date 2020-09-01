from string import Template

arquivoFonte = "./attackers/BestAttackers.csv"
arq = open("./attackers/Best-CSV.csv","w")
arq.write("RANK,SHIRTNUMBER,NAME,TEAM,SPIKES,FAULTS,SHOTS,TOTAL ATTEMPTS,SUCCESS %\n")

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
    attacks = []
    blocks = []
    serves = []
    total = []
    for dado in list_paises[i]["dados"]:
        attacks.append(int(dado.split(",")[4]))
        blocks.append(int(dado.split(",")[5]))
        serves.append(int(dado.split(",")[6]))
        total.append(int(dado.split(",")[7]))
    tot = sum(total)
    att = sum(attacks)/tot
    blo = sum(blocks)/tot
    ser = sum(serves)/tot
    string_aux = Template('''$pais,
    {axis:"Attacks",value:$att},
    {axis:"Blocks",value:$blo},
    {axis:"Serves",value:$ser}
    ''')
    string = string_aux.substitute(pais=pais,att=att,blo=blo,ser=ser)
    arq.write(string + "\n")
