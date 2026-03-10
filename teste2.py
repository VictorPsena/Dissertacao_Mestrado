"""Animacao da convolucao de f(t)=exp(-t)u(t) e g(t)=u(t).

O script gera uma animacao com tres paineis:
1) f(tau) e g(t-tau)
2) integrando f(tau)g(t-tau) com area integrada
3) resultado da convolucao (f*g)(t) = (1-exp(-t))u(t)
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter


def u(x: np.ndarray) -> np.ndarray:
	"""Funcao degrau unitario."""
	return (x >= 0).astype(float)


def f(x: np.ndarray) -> np.ndarray:
	"""f(t) = exp(-t)u(t)."""
	return np.exp(-x) * u(x)


def g(x: np.ndarray) -> np.ndarray:
	"""g(t) = u(t)."""
	return u(x)


def conv_analitica(t: np.ndarray) -> np.ndarray:
	"""(f*g)(t) = (1 - exp(-t))u(t)."""
	return (1 - np.exp(-t)) * u(t)


# Eixo para o integrando (variavel tau) e parametro de animacao (variavel t)
tau_min, tau_max = -2.0, 8.0
tau = np.linspace(tau_min, tau_max, 1200)
t_values = np.linspace(-2.0, 8.0, 240)

fig, axes = plt.subplots(3, 1, figsize=(10, 11), sharex=False)
ax1, ax2, ax3 = axes

# Painel 1: f(tau) e g(t-tau)
line_f, = ax1.plot(tau, f(tau), lw=2.2, color="#1f77b4", label=r"$f(\tau)=e^{-\tau}u(\tau)$")
line_gshift, = ax1.plot(tau, g(0 - tau), lw=2.2, color="#ff7f0e", label=r"$g(t-\tau)=u(t-\tau)$")
t_text = ax1.text(0.02, 0.9, "", transform=ax1.transAxes, fontsize=12)
ax1.set_xlim(tau_min, tau_max)
ax1.set_ylim(-0.05, 1.2)
ax1.set_title("Funcoes na integral de convolucao")
ax1.set_ylabel("Amplitude")
ax1.grid(alpha=0.25)
ax1.legend(loc="upper right")

# Painel 2: produto e area integrada
line_prod, = ax2.plot(tau, np.zeros_like(tau), lw=2.2, color="#2ca02c", label=r"$f(\tau)g(t-\tau)$")
fill_poly = [None]
area_text = ax2.text(0.02, 0.9, "", transform=ax2.transAxes, fontsize=12)
ax2.set_xlim(tau_min, tau_max)
ax2.set_ylim(-0.05, 1.2)
ax2.set_title("Integrando e area acumulada")
ax2.set_ylabel("Amplitude")
ax2.grid(alpha=0.25)
ax2.legend(loc="upper right")

# Painel 3: resultado da convolucao
t_plot = np.linspace(-2.0, 8.0, 800)
conv_plot = conv_analitica(t_plot)
ax3.plot(t_plot, conv_plot, lw=2.2, color="#d62728", label=r"$(f*g)(t)=(1-e^{-t})u(t)$")
line_progress, = ax3.plot([], [], lw=3.0, color="#9467bd", label="valor ja percorrido")
point_now, = ax3.plot([], [], "o", color="#111111", ms=6)
ax3.set_xlim(-2.0, 8.0)
ax3.set_ylim(-0.05, 1.1)
ax3.set_title("Resultado da convolucao")
ax3.set_xlabel("t")
ax3.set_ylabel("(f*g)(t)")
ax3.grid(alpha=0.25)
ax3.legend(loc="lower right")


def init() -> tuple:
	line_gshift.set_ydata(g(0 - tau))
	line_prod.set_ydata(np.zeros_like(tau))
	line_progress.set_data([], [])
	point_now.set_data([], [])
	t_text.set_text("")
	area_text.set_text("")
	return line_f, line_gshift, line_prod, line_progress, point_now, t_text, area_text


def update(frame: int) -> tuple:
	t = t_values[frame]
	g_shift = g(t - tau)
	prod = f(tau) * g_shift

	line_gshift.set_ydata(g_shift)
	line_prod.set_ydata(prod)

	if fill_poly[0] is not None:
		fill_poly[0].remove()
	fill_poly[0] = ax2.fill_between(tau, 0, prod, color="#2ca02c", alpha=0.25)

	conv_now = conv_analitica(np.array([t]))[0]
	idx = np.searchsorted(t_plot, t, side="right")
	line_progress.set_data(t_plot[:idx], conv_plot[:idx])
	point_now.set_data([t], [conv_now])

	t_text.set_text(fr"t = {t:5.2f}")
	area_text.set_text(fr"$\int f(\tau)g(t-\tau)d\tau = {conv_now:5.3f}$")

	return line_f, line_gshift, line_prod, line_progress, point_now, t_text, area_text


ani = FuncAnimation(
	fig,
	update,
	frames=len(t_values),
	init_func=init,
	interval=40,
	blit=False,
)

plt.tight_layout()

# Salva como GIF para facilitar visualizacao em qualquer sistema.
output_file = "convolucao_exp_step.gif"
ani.save(output_file, writer=PillowWriter(fps=25))
print(f"Animacao salva em: {output_file}")

plt.show()

