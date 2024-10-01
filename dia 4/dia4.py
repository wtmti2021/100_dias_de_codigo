def Adicao(x,y):
  return x+y

def subtracao(x,y):
  return x-y

def multiplicacao(x,y):
  return x*y

def divisao(x,y):
  return x/y

def calculadora():
  print("Selecione a operação. ")
  print("1.Adicao")
  print("2.Subtração")
  print("3.Multiplicacao")
  print("4.Divisao")


  while True:
    escolha = input("Escolha(1/2/3/4): ")
    if escolha in ('1', '2', '3', '4'):
      x = int(input("Digite o primeiro numero: "))
      y = int(input("Digite o segundo numero: "))
      if escolha == '1':
        print("Resultado: ", Adicao(x,y))
      if escolha == '2':
        print("Resultado: ", subtracao(x,y))
      if escolha == '3':
        print("Resultato: ", multiplicacao(x,y))
      if escolha == '4':
        if y != 0:
          print ("Resultado: ", divisao(x,y))
        else:
          print("Não é permitida a divisão por zero.")
    else:
      print("Escolha inválida.")

    continuar = input("Deseja fazer outra operação? (s/n)")
    if continuar == "n":
      print("Calculadora encerrada.")
      break;

calculadora()    
  
  
