def inverterString(string):
    return string[::-1]

entrytexto = str(input("Digite seu texto: ")).upper()
print(f"Você digitou: {entrytexto}")
print(f"Texto convertido:{inverterString(entrytexto)}")
