# Este código realiza uma regressão linear simples utilizando o Python. 
# 1 a criação de um vetor de 1000 elementos. 
# 2 variável 'yaux' usando uma função linear f(x) = a * x + b. 
# 3 adicionado um ruído aleatório à variável 'yaux', criando a variável 'y'.
# 
# 4 para encontrar a reta de melhor ajuste entre 'x' e 'y',
# utilizando o modelo LinearRegression da biblioteca 'scikit-learn'.
# o gráfico de dispersão é gerado para visualizar os dados originais, 
# e a reta de ajuste é plotada sobre os dados para comparar o modelo com os valores reais.
# 
# 5 problema prático: estimar o preço de imóveis com base na área construída.
# conjunto de dados fictícios representando áreas e preços de imóveis, ajustando uma reta e calculando a qualidade do modelo.

# Murilo Rmalho da Mata
# Camila Gomes da Silva Casa

# --- instalar as bibliotecas necessárias
import subprocess
import sys
def install_packages():
    subprocess.check_call([sys.executable, "-m", "pip", "install", "numpy", "matplotlib", "scikit-learn"])
install_packages()

# --- projeto
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.metrics import r2_score

x = np.linspace(0, 20, 1000)
a, b = 1.2, -3.5
yaux = a * x + b

random_noise = np.random.uniform(-2, 2, size=x.shape)
y = yaux + random_noise

x_reshape = x.reshape(-1, 1)

model = LinearRegression()
model.fit(x_reshape, y)

beta1 = model.coef_[0]
beta2 = model.intercept_

y_pred = model.predict(x_reshape)
r2 = r2_score(y, y_pred)

print(f"Função de ajuste: φ(x) = {beta1:.4f} * x + {beta2:.4f}")
print(f"Coeficiente de Determinação (R²): {r2:.4f}")

plt.figure(figsize=(10, 6))
plt.scatter(x, y, color="blue", alpha=0.5, label="Dados com ruído")
plt.plot(x, y_pred, color="red", label=f"Reta de ajuste: φ(x) = {beta1:.4f}x + {beta2:.4f}")
plt.title("Regressão Linear Simples")
plt.xlabel("x")
plt.ylabel("y")
plt.legend()
plt.grid()
plt.show()

area = np.array([50, 60, 70, 80, 90, 100, 110, 120, 130, 140,
                 150, 160, 170, 180, 190, 200, 210, 220, 230, 240])
price = np.array([150, 180, 210, 240, 270, 300, 330, 360, 390, 420,
                  450, 480, 510, 540, 570, 600, 630, 660, 690, 720])

plt.figure(figsize=(10, 6))
plt.scatter(area, price, color="blue", label="Dados observados")
plt.title("Dados Observados - Área vs. Preço")
plt.xlabel("Área (m²)")
plt.ylabel("Preço (milhares de reais)")
plt.grid()
plt.legend()
plt.show()

area_reshape = area.reshape(-1, 1)
model = LinearRegression()
model.fit(area_reshape, price)

beta1 = model.coef_[0]
beta2 = model.intercept_

price_pred = model.predict(area_reshape)
r2 = r2_score(price, price_pred)

print(f"Função de ajuste: φ(x) = {beta1:.4f} * x + {beta2:.4f}")
print(f"Coeficiente de Determinação (R²): {r2:.4f}")

plt.figure(figsize=(10, 6))
plt.scatter(area, price, color="blue", label="Dados observados")
plt.plot(area, price_pred, color="red", label=f"Reta de ajuste: φ(x) = {beta1:.4f}x + {beta2:.4f}")
plt.title("Regressão Linear - Área vs. Preço")
plt.xlabel("Área (m²)")
plt.ylabel("Preço (milhares de reais)")
plt.legend()
plt.grid()
plt.show()
