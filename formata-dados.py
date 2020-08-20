import json

linhas = open("dados.json")
arquivo = open("dados-visualizacao.json", "w")

dict_paises = {}
contador_paises = 0

#montando dicionario para selecoes
for linha in linhas:
    dado = json.loads(linha)
    if dado["team"] not in dict_paises:
        dict_paises[dado["team"]] = contador_paises
        contador_paises = contador_paises+1



for linha in linhas:


print(dict_paises)

# {"rank": "1", "shirt-number": "12", "name": "Bruno Lima", "team": "ARG", "spikes": "177", "faults": "50", "shots": "98", "total-attempts": "325", "success-rate": "54.46\n"}
# FORMATO OBJETIVO
# {
#     "name": "BR",
#     "children": [
#         {
#             "name": "cluster",
#             "children": [
#                 {
#                     "name": "AgglomerativeCluster",
#                     "value": 3938
#                 }
#             ]
#         },
#         {
#             "name": "graph",
#             "children": [
#                 {
#                     "name": "BetweennessCentrality",
#                     "value": 3534
#                 }
#             ]
#         },
#         {
#             "name": "optimization",
#             "children": [
#                 {
#                     "name": "AspectRatioBanker",
#                     "value": 7074
#                 }
#             ]
#         }
#     ]
# }
