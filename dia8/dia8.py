def c_p_f(celsius):
  fahrenheit = (celsius * 9/5) + 32 
  return fahrenheit

entrada = float(input("Digite a temperatura em Celcius: "))

print(f"A temperatura em Fahrenheit é: {c_p_f(entrada)}")