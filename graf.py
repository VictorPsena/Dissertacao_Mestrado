import numpy as np
import matplotlib.pyplot as plt


def plot_graf(x, y, title='Graf', output_path='graf.png') -> str:
    plt.plot(x, y)
    plt.xlabel('x')
    plt.ylabel('y')
    plt.title(title)
    plt.grid(False)
    plt.savefig(output_path, dpi=300, bbox_inches='tight')
    plt.close()
    return output_path


x = np.linspace(-10, 10, 100)
y = x**2

figure = plot_graf(x, y, title=r'')
print(f'Figura salva em: {figure}')
