import json

linhas = open("csv/Best Attackers.csv")
arquivo = open("dados.json", "w")

for linha in linhas:
    dados = linha.split(",")
    dado ={
        "rank": dados[0],
        "shirt-number": dados[1],
        "name": dados[2],
        "team": dados[3],
        "spikes": dados[4],
        "faults": dados[5],
        "shots":dados[6],
        "total-attempts":dados[7],
        "success-rate":dados[8]
    }
    dado_json = json.dumps(dado)
    arquivo.write(dado_json+"\n")
    print(dado_json)
