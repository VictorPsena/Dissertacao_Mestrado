import numpy as np
import matplotlib.pyplot as plt

# Criando uma matriz 28x28 com valores de 0 a 255
matriz = np.random.randint(0, 256, (10, 10))
fig, ax = plt.subplots()

# Exibe a matriz como imagem em escala de cinza
im = ax.imshow(matriz, cmap='gray', vmin=0, vmax=255)

# Adiciona os valores dentro de cada célula
for i in range(matriz.shape[0]):
    for j in range(matriz.shape[1]):
        ax.text(j, i, matriz[i, j],
                ha='center', va='center',
                color='red')

plt.colorbar(im)
# plt.title(f"Matriz em Escala de Cinza ({matriz.shape[0]}x{matriz.shape[1]})")

backend = plt.get_backend().lower()
if "agg" in backend:
    output_file = "matriz_escala_cinza.png"
    plt.savefig(output_file, dpi=300, bbox_inches="tight")
    print(f"Backend não interativo detectado ({backend}). Figura salva em: {output_file}")
else:
    plt.show()