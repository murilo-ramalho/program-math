import numpy as np
from scipy.stats import norm
from scipy.integrate import quad

# Murilo Ramalho da Mata
# Camila Gomes da Silva Casa

def normal_pdf(x, mu, sigma):
    """Função densidade de probabilidade para a distribuição normal."""
    return (1 / (sigma * np.sqrt(2 * np.pi))) * np.exp(-0.5 * ((x - mu) / sigma) ** 2)

def calcular_probabilidade(a, b, mu, sigma):
    """Calcula P(a ≤ x ≤ b) para uma normal com média mu e desvio padrão sigma."""
    prob, _ = quad(normal_pdf, a, b, args=(mu, sigma))
    return prob

def main():
    print("Escolha uma opção:")
    print("1 - Digitar o desvio padrão")
    print("2 - Digitar a variância")
    
    escolha = input("Digite sua escolha (1 ou 2): ").strip()
    
    if escolha == '1':
        sigma = float(input("Digite o valor do desvio padrão: "))
    elif escolha == '2':
        variancia = float(input("Digite o valor da variância σ²: "))
        sigma = np.sqrt(variancia)
    else:
        print("Escolha inválida!")
        return
    
    mu = float(input("Digite o valor da média: "))
    a = float(input("Digite o valor de a: "))
    b = float(input("Digite o valor de b: "))
    
    probabilidade = calcular_probabilidade(a, b, mu, sigma)
    
    print(f"A probabilidade P({a} ≤ x ≤ {b}) é {probabilidade:.4f}")

if __name__ == "__main__":
    main()
