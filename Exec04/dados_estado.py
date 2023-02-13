def calculaPercentualRepresentacao(valorSP, valorRJ, valorMG, valorES, valorOutros):
  # Calcula o valor total da distribuidora
  valorTotal = valorSP + valorRJ + valorMG + valorES + valorOutros

  # Calcula o percentual de representação de cada estado
  percentualRepresentacaoSP = (valorSP / valorTotal) * 100
  percentualRepresentacaoRJ = (valorRJ / valorTotal) * 100
  percentualRepresentacaoMG = (valorMG / valorTotal) * 100
  percentualRepresentacaoES = (valorES / valorTotal) * 100
  percentualRepresentacaoOutros = (valorOutros / valorTotal) * 100

  # Imprime os resultados
  print("Percentual de representação de SP: %.2f%%" % percentualRepresentacaoSP)
  print("Percentual de representação de RJ: %.2f%%" % percentualRepresentacaoRJ)
  print("Percentual de representação de MG: %.2f%%" % percentualRepresentacaoMG)
  print("Percentual de representação de ES: %.2f%%" % percentualRepresentacaoES)
  print("Percentual de representação de Outros: %.2f%%" % percentualRepresentacaoOutros)

# Valores de faturamento mensal
valorFaturamentoSP = 67836.43
valorFaturamentoRJ = 36678.66
valorFaturamentoMG = 29229.88
valorFaturamentoES = 27165.48
valorFaturamentoOutros = 19849.53

# Executa a função
calculaPercentualRepresentacao(valorFaturamentoSP, valorFaturamentoRJ, valorFaturamentoMG, valorFaturamentoES, valorFaturamentoOutros)
