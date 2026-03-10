import numpy as np
import matplotlib.pyplot as plt

def plot_graf(x, y, title='Graf', output_path='graf.png', pontosBanco=None, pontosTreino = None) -> str:
    plt.plot(x, y, label='Rede Neural', color='green')
    plt.xlabel('x', fontsize=16)
    plt.ylabel('y', fontsize=16)
    plt.title(title, fontsize=18)
    plt.grid(False)
    if pontosBanco:
        for i, ponto in enumerate(pontosBanco):
            plt.scatter(*ponto, color='red', label='banco de treino' if i == 0 else "")
        plt.legend()
    if pontosTreino:
        for i, ponto in enumerate(pontosTreino):
            plt.scatter(*ponto, color='blue', label='banco de teste' if i == 0 else "")
        plt.legend()

    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    return output_path


x = np.linspace(0, 2, 100)
y = np.cos(x)**2

# Pontos
a1 = (0.25, 1.7)
a2 = (0.75, 0.7)
a3 = (1.7, 1.5)
x1 = (1, np.cos(1)**2)
x2 = (2, np.cos(2)**2)
x3 = (0, np.cos(0)**2)


figure = plot_graf(x, y, title='', output_path='cos2_graf.png', pontosBanco=[x1, x2, x3], pontosTreino=[a1, a2, a3])
print(f'Figura salva em: {figure}')
