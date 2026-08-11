import os
os.system("cls")


print("digite os nomes do candidato:")
cand1 = input("1: ")
while cand1 == "":
    cand1 = input("Nome em branco, digite algo!\n1: ")

cand2 = input("2: ")
while cand2 == "":
    cand2 = input("Nome em branco, digite algo!\n2: ")

cand3 = input("3: ")
while cand3 == "":
    cand3 = input("Nome em branco, digite algo!\n3: ")

print(f"""
CANDIDATOS

1 - {cand1}
2 - {cand2} 
3 - {cand3}
0 - FIM DA VOTAÇÃO
""")
voto_cand1 = voto_cand2 = voto_cand3 = voto_nulo = total_votos = 0

while True:
    voto = input("VOTO: ")
    match voto:
        case '0':
            break
        case '1':
            voto_cand1 = voto_cand1 + 1    
        case '2':
            voto_cand2 += 1
        case '3':
            voto_cand3 += 1

    total_votos += 1

if total_votos != 0:
    perc_cand1 = voto_cand1 / total_votos * 100
    perc_cand2 = voto_cand2 / total_votos * 100     
    perc_cand3 = voto_cand3 / total_votos * 100     
    perc_nulo = voto_nulo / total_votos * 100           
   
    print(f"""
    CANDIDATOS
    TOTAL DE VOTOS: {total_votos}
    1 - {cand1:12s} -> {voto_cand1:3d} -> {perc_cand1:5.1f}%           
    2 - {cand2:12s} -> {voto_cand2:3d} -> {perc_cand2:5.1f}%        
    3 - {cand3:12s} -> {voto_cand3:3d} -> {perc_cand3:5.1f}%
    {"NULOS":12s} -> {voto_nulo:3d} votos -> {perc_nulo:5.1f}%
    """)
else:
    print("Não houveram votos")   