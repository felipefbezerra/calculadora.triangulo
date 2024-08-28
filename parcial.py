# Função para calcular a área do triângulo
def calcular_area(base, altura):
    area = (base * altura) / 2
    return area

# Programa principal
print("Calculadora de Área de Triângulo")

# Solicita a base e a altura do triângulo ao usuário
base = float(input("Digite a base do triângulo: "))
altura = float(input("Digite a altura do triângulo: "))

# Calcula a área do triângulo
area = calcular_area(base, altura)

# Mostra os resultados
print("Base do triângulo:", base)
print("Altura do triângulo:", altura)
print("Área do triângulo:", area)