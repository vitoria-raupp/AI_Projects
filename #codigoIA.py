#codigoIA

ponto1 = int(input("Qual a primeira distância? "))
ponto2_1 = int(input("Qual a segunda distância? "))
ponto2_2 = int(input("Qual a segunda distância? "))
ponto3_1 = int(input("Qual a terceira distância? "))
ponto3_2 = int(input("Qual a terceira distância? "))
ponto3_3 = int(input("Qual a terceira distância? "))
ponto3_4 = int(input("Qual a terceira distância? "))

ponto2 = min(ponto2_1, ponto2_2)
ponto3 = min(ponto3_1, ponto3_2, ponto3_3, ponto3_4)

soma = ponto1 + ponto2 + ponto3

print('O valor do menor caminho resulta em: ' soma)
