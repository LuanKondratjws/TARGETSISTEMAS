import json

#vermelho = \033[31m
#verde    = \033[32m
#azul     = \033[34m

def faturamentoMensal(arquivo):
    # Abrir o arquivo json
    with open(arquivo, "r") as file:
        dados = json.load(file)
    
    # Inicializa as variáveis de menor e maior valor
    menorValor = float("inf")
    maiorValor = float("-inf")
    
    soma = 0
    
    diasComFaturamento = 0
    
    # Loop por cada dia no arquivo
    for dia in dados:
        # Verifica se o valor de faturamento é maior que zero, se for, considera no cálculo
        if dia["valor"] > 0:
            diasComFaturamento += 1
            soma += dia["valor"]
            
            if dia["valor"] < menorValor:
                menorValor = dia["valor"]
            
            if dia["valor"] > maiorValor:
                maiorValor = dia["valor"]
    
    media = soma / diasComFaturamento
    
    diasAcimaDaMedia = 0
    
    for dia in dados:
        # Verifica se o valor de faturamento é maior que zero e acima da média, se for, incrementa a variável
        if dia["valor"] > 0 and dia["valor"] > media:
            diasAcimaDaMedia += 1
    
    # Retorna o menor valor, o maior valor, e o número de dias acima da média
    print(f"\033[31mMenor\033[m valor de faturamento diário: \033[31m{menorValor}\033[m")
    print(f"\033[32mMaior\033[m valor de faturamento diário: \033[32m{maiorValor}\033[m")
    print(f"Dias com \033[34mfaturamento acima da média\033[m mensal: \033[34m{diasAcimaDaMedia}\033[m")

faturamentoMensal("dados.json")

