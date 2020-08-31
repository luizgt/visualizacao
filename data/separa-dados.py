linhas = open("./setters/BestSetters.csv")
# 1,12,Bruno Lima,ARG,177,50,98,325,54.46

dict_paises = {}
list_paises = []
contador_paises = 0

#montando dicionario para selecoes
for linha in linhas:
    dados = linha.split(";")
    if len(dados[3]) == 3 and dados[3] not in dict_paises:
        dict_paises[dados[3]] = contador_paises
        contador_paises = contador_paises + 1
        list_paises.append({"name":dados[3],"dados":[]})

# reabrindo arquivo para resetar posicao do cursor
linhas = open("./setters/BestSetters.csv")

for linha in linhas:
    dado = linha.split(";");
    if len(dado[3]) == 3:
        list_paises[dict_paises[dado[3]]]["dados"].append(linha)

for i in range(0,16):
    pais = list_paises[i]["name"]
    nomeArq = "setters/Setters-%s.csv" %pais
    arq = open(nomeArq,"w")
    arq.write("RANK,SHIRTNUMBER,NAME,TEAM,SPIKES,FAULTS,SHOTS,TOTAL ATTEMPTS,SUCCESS %\n")
    for dado in list_paises[i]["dados"]:
        arq.write(dado)


print(len(list_paises));
# print(list_paises[1]);
