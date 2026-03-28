import numpy as np
import matplotlib.pyplot as plt

def plot_graf(x, y, title='Graf', output_path='graf.png', pontosBanco=None, pontosTreino = None) -> str:
    plt.plot(x, y, label='Rede Neural', color='green')
    plt.xlabel(r'$z$', fontsize=16)
    plt.ylabel(r"$\sigma'(z)$", fontsize=16)
    plt.title(title, fontsize=18)
    plt.grid(False)
    if pontosBanco:
        for i, ponto in enumerate(pontosBanco):
            plt.scatter(*ponto, color='red', label='banco de treino' if i == 0 else "")
        # plt.legend()
    if pontosTreino:
        for i, ponto in enumerate(pontosTreino):
            plt.scatter(*ponto, color='blue', label='banco de teste' if i == 0 else "")
        plt.legend()

    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    return output_path


x = np.linspace(-10, 10, 100)
y = 1/(1 + np.exp(-x))
z = y*(1-y)

a = (0, 0.25)



figure = plot_graf(x, z, title='', pontosBanco=[a], output_path='sigmoid_derivative.png')
print(f'Figura salva em: {figure}')
