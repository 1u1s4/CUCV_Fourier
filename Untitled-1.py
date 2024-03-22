
from math import pi, cos, sin


def a(n):
    return 2000/(pi - n**2 * pi)

def b(n):
    return 2000/(n * pi)

a0 = 1000/pi - 1000/2


def P(t):
    h = 0.01
    N = int(t/h)

    valores_an = []
    for n in range(0, N + 1):
        if n%2 == 0:
            valores_an.append(a(n) * cos(n * 2 * pi * t))
    
    valores_bn = []
    for n in range(0, N + 1):
        if n%2 == 1:
            valores_bn.append(b(n) * sin(n * 2 * pi * t))
    
    return a0 + sum(valores_an) + sum(valores_bn)
    


valores_Pt = []
h = 0.00001
N_max = int(1/h)
for n in range(0, N_max + 1):
    t = h * n
    valores_Pt.append((t, P(t)))


import matplotlib.pyplot as plt

# Separa los puntos en dos listas: una para X y otra para Y
x = [punto[0] for punto in valores_Pt]
y = [punto[1] for punto in valores_Pt]

# Crea el gráfico
plt.figure(figsize=(10, 6))  # Ajusta el tamaño del gráfico
plt.plot(x, y, marker='o', linestyle='-', color='b')  # Puedes cambiar el estilo, el color y el marcador
plt.title('Gráfico de Puntos')  # Título del gráfico
plt.xlabel('Eje X')  # Etiqueta del eje X
plt.ylabel('Eje Y')  # Etiqueta del eje Y
plt.grid(True)  # Muestra una cuadrícula para facilitar la lectura

# Muestra el gráfico
plt.show()





