from pathlib import Path

from manim import *


ROOT_DIR = Path(__file__).resolve().parent.parent
ULTRASOUND_IMAGE = ROOT_DIR / "imagens" / "intro" / "ultrassom.jpg"

BACKGROUND_COLOR = "#FFFFFF"
TEXT_COLOR = "#14213D"
PRIMARY_COLOR = "#0F766E"
SECONDARY_COLOR = "#C2410C"
HIGHLIGHT_COLOR = "#1D4ED8"
MUTED_COLOR = "#475569"
CARD_FILL_COLOR = "#FFFDF8"
CARD_STROKE_COLOR = "#D6D3D1"
SOFT_HIGHLIGHT = "#FEF3C7"

TITLE_FONT_SIZE = 34
SUBTITLE_FONT_SIZE = 24
BODY_FONT_SIZE = 22
SMALL_FONT_SIZE = 18
FORMULA_FONT_SIZE = 30

PRESENTATION_TITLE = (
    "Comparação entre Modelos de Redes Neurais\n"
    "U-Net e U-Net Fuzzy para Mensurar Regiões\n"
    "de Imagens de Ultrassonografia Bovina"
)
PRESENTATION_SUBTITLE = "Dissertação de Mestrado - Universidade Federal de Uberlândia"
AUTHOR = "Victor Patrick Sena Barbosa Lima"
ADVISOR = "Orientadora: Profa. Dra. Rosana Sueli da Motta Jafelice"
CO_ADVISOR = "Coorientador: Prof. Dr. Caio Augusto Rodrigues dos Santos"

AGENDA = [
    "Contexto, motivação e objetivos do trabalho",
    "Fundamentação teórica: U-Net, lógica fuzzy e ANFIS",
    "Metodologia experimental e organização da base de dados",
    "Resultados para AOL, EGL e EGG",
    "Conclusões, contribuições e trabalhos futuros",
]


def apply_theme():
    config.background_color = BACKGROUND_COLOR
    Text.set_default(color=TEXT_COLOR, font_size=BODY_FONT_SIZE)
    Tex.set_default(color=TEXT_COLOR, font_size=FORMULA_FONT_SIZE)
    MathTex.set_default(color=TEXT_COLOR, font_size=FORMULA_FONT_SIZE)
