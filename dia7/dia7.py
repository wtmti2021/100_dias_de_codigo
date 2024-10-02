def gerar_tabuada(numero):
  print(f"Tabuada do {numero}")
  for i in range(1, 11):
    resultado = numero * i
    print(f"{numero} * {i} = {resultado}")

# Solicita ao usuário que insira um número
numero = int(input("Digite um número para gerar a tabuada: "))

# Chama a funçao para gerar a tabuada
gerar_tabuada(numero)