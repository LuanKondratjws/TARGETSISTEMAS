
# Atividade 2): Dado a sequência de Fibonacci, onde se inicia por 0 e 1 e o próximo valor sempre será a soma dos 2 valores anteriores
#(exemplo: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34...), escreva um programa na linguagem que desejar onde, informado um número,
# ele calcule a sequência de Fibonacci e retorne uma mensagem avisando se o número informado pertence ou não a sequência.

# Define a função lambda de cálculo de Fibonacci na onde n é o parâmetro da função.
fibonacci = lambda n: 0 if n == 0 else 1 if n == 1 else fibonacci(n-1) + fibonacci(n-2)

num = int(input("Informe um número: "))

# Cria a lista dos 20 primeiros números da sequência de Fibonacci
fibSequence = [fibonacci(i) for i in range(20)]

# Verifica se o número informado pertence à lista
if num in fibSequence:
    print(f"O número {num} pertence à sequência de Fibonacci.")
else:
    print(f"O número {num} não pertence à sequência de Fibonacci.")
    
# Para imprimir a lista dos 20 primeiros números da sequência, basta descomentar o # do print abaixo.   
#print(fibSequence)
