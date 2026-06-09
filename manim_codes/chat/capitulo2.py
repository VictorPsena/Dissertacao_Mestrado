from manim import *

from configuracoes import *


def add_slides(scene):
    cnn_card = scene.make_card(
        "Base em redes neurais",
        [
            "Revisão de perceptron, backpropagation, regularização, overfitting e otimização com Adam.",
            "Redes convolucionais com convolução, pooling, padding, stride e convolução transposta.",
        ],
        width=5.9,
        min_height=3.0,
    )
    unet_card = scene.make_card(
        "Arquitetura U-Net",
        [
            "Encoder-decoder com skip connections para segmentação pixel a pixel.",
            "Adequada para bases menores e segmentação de imagens biomédicas.",
            "No trabalho, a arquitetura base foi adaptada para multitarefa e para integração fuzzy.",
        ],
        width=5.9,
        min_height=3.0,
        title_color=SECONDARY_COLOR,
    )
    scene.show_slide(
        "Fundamentação Teórica I",
        VGroup(cnn_card, unet_card).arrange(RIGHT, buff=0.35, aligned_edge=UP),
    )

    fuzzy_card = scene.make_card(
        "Lógica fuzzy e ANFIS",
        [
            "Conjuntos fuzzy tratam incerteza e imprecisão em bordas mal definidas.",
            "ANFIS combina aprendizado de redes neurais com regras fuzzy do tipo Takagi-Sugeno.",
            "Na U-Net Fuzzy, o módulo fuzzy refina o bottleneck antes do decoder.",
        ],
        width=5.8,
        min_height=3.0,
        title_color=PRIMARY_COLOR,
    )

    formulas = VGroup(
        MathTex(r"Dice = \frac{2|A \cap B|}{|A| + |B|}"),
        MathTex(r"MAE = \frac{1}{n}\sum_{i=1}^{n}|y_i - \hat{y}_i|"),
        MathTex(r"R^2 = 1 - \frac{\sum (y_i - \hat{y}_i)^2}{\sum (y_i - \bar{y})^2}"),
    ).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
    formula_card = scene.make_card(
        "Métricas de avaliação",
        [
            "Dice e acurácia avaliam a qualidade da segmentação.",
            "MAE e R² avaliam a precisão das medidas extraídas das máscaras.",
        ],
        width=5.8,
        min_height=2.2,
        title_color=HIGHLIGHT_COLOR,
    )
    right = VGroup(formulas, formula_card).arrange(DOWN, aligned_edge=LEFT, buff=0.28)
    scene.show_slide(
        "Fundamentação Teórica II",
        VGroup(fuzzy_card, right).arrange(RIGHT, buff=0.35, aligned_edge=UP),
        subtitle="Referências centrais: Ronneberger et al. (2015), Jang (1993), Melo et al. (2022) e Kirichev et al. (2021).",
    )
