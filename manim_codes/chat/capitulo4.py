from manim import *

from configuracoes import *


def add_slides(scene):
    overview_cards = VGroup(
        scene.make_card(
            "AOL",
            [
                "Melhor segmentação: U-Net Fuzzy.",
                "Melhor medida numérica: U-Net Fuzzy.",
                "Ganho claro com a inferência fuzzy.",
            ],
            width=3.8,
            min_height=2.7,
            title_color=SECONDARY_COLOR,
            body_font_size=18,
        ),
        scene.make_card(
            "EGL",
            [
                "Dice e acurácia levemente melhores na U-Net multitarefa.",
                "MAE e R² ligeiramente melhores na U-Net Fuzzy.",
                "Sem vencedor absoluto.",
            ],
            width=3.8,
            min_height=2.7,
            title_color=HIGHLIGHT_COLOR,
            body_font_size=18,
        ),
        scene.make_card(
            "EGG",
            [
                "Leve vantagem em Dice para a U-Net Fuzzy.",
                "Melhor medida final na U-Net multitarefa.",
                "Erro acumulado de duas segmentações pesa no resultado.",
            ],
            width=3.8,
            min_height=2.7,
            title_color=PRIMARY_COLOR,
            body_font_size=18,
        ),
    ).arrange(RIGHT, buff=0.28, aligned_edge=UP)
    highlight = scene.make_highlight_box(
        "Leitura geral: a integração fuzzy foi mais efetiva quando a estrutura segmentada tinha contorno mais amplo e mais estável, como na AOL."
    )
    content = VGroup(overview_cards, highlight).arrange(DOWN, buff=0.35)
    scene.show_slide("Resultados Gerais", content)

    aol_left = scene.make_card(
        "U-Net multitarefa",
        [
            "Dice: 92,73%",
            "Acurácia: 94,75%",
            "R²: 0,5578",
            "MAE: 2,988 cm²",
            "Épocas: 80",
        ],
        width=5.7,
        min_height=3.0,
        title_color=HIGHLIGHT_COLOR,
    )
    aol_right = scene.make_card(
        "U-Net Fuzzy",
        [
            "Dice: 93,29%",
            "Acurácia: 95,15%",
            "R²: 0,7423",
            "MAE: 2,312 cm²",
            "Épocas: 89",
        ],
        width=5.7,
        min_height=3.0,
        title_color=SECONDARY_COLOR,
    )
    aol_note = scene.make_highlight_box(
        "Para AOL, a U-Net Fuzzy superou o modelo multitarefa nas principais métricas de segmentação e nas medidas numéricas, apesar de maior oscilação no treinamento."
    )
    scene.show_slide(
        "Resultados - AOL",
        VGroup(VGroup(aol_left, aol_right).arrange(RIGHT, buff=0.35), aol_note).arrange(
            DOWN, buff=0.35
        ),
    )

    egl_left = scene.make_card(
        "U-Net multitarefa",
        [
            "Dice: 70,25%",
            "Acurácia: 99,85%",
            "R²: 0,6899",
            "MAE: 0,018 mm",
            "Melhor segmentação consolidada.",
        ],
        width=5.7,
        min_height=3.05,
        title_color=HIGHLIGHT_COLOR,
    )
    egl_right = scene.make_card(
        "U-Net Fuzzy",
        [
            "Dice: 69,39%",
            "Acurácia: 99,50%",
            "R²: 0,7031",
            "MAE: 0,015 mm",
            "Leve vantagem nas medidas numéricas.",
        ],
        width=5.7,
        min_height=3.05,
        title_color=SECONDARY_COLOR,
    )
    egl_note = scene.make_highlight_box(
        "A EGL é uma tarefa fortemente desbalanceada: a região de interesse ocupa poucos pixels, o que torna a acurácia menos informativa e o Dice mais sensível."
    )
    scene.show_slide(
        "Resultados - EGL",
        VGroup(VGroup(egl_left, egl_right).arrange(RIGHT, buff=0.35), egl_note).arrange(
            DOWN, buff=0.35
        ),
    )

    egg_left = scene.make_card(
        "U-Net multitarefa",
        [
            "Dice: 82,74% (Biceps) e 79,84% (gordura)",
            "R²: 0,4287",
            "MAE: 0,7 mm",
            "Melhor medida final da EGG.",
        ],
        width=5.7,
        min_height=3.05,
        title_color=HIGHLIGHT_COLOR,
        body_font_size=19,
    )
    egg_right = scene.make_card(
        "U-Net Fuzzy",
        [
            "Dice: 84,60% (Biceps) e 79,99% (gordura)",
            "R²: 0,3178",
            "MAE: 0,8 mm",
            "Leve ganho em Dice, mas não na medida final.",
        ],
        width=5.7,
        min_height=3.05,
        title_color=SECONDARY_COLOR,
        body_font_size=19,
    )
    egg_note = scene.make_highlight_box(
        "A EGG depende de duas segmentações. Pequenos erros na localização do início do Biceps Femoris se propagam e afetam a medida final mais do que as métricas de máscara isolada sugerem."
    )
    scene.show_slide(
        "Resultados - EGG",
        VGroup(VGroup(egg_left, egg_right).arrange(RIGHT, buff=0.35), egg_note).arrange(
            DOWN, buff=0.35
        ),
    )

    strengths = scene.make_card(
        "Pontos fortes",
        [
            "Integração entre aprendizado profundo e lógica fuzzy.",
            "Uso explícito da raça do animal como contexto.",
            "Aplicativo funcional para apoio à avaliação ultrassonográfica.",
        ],
        width=5.8,
        min_height=2.7,
        title_color=PRIMARY_COLOR,
    )
    limits = scene.make_card(
        "Limitações",
        [
            "Qualidade heterogênea das imagens e base reduzida para deep learning.",
            "Dependência do aparelho de ultrassom usado na aquisição.",
            "Literatura ainda escassa para U-Net Fuzzy neste domínio.",
        ],
        width=5.8,
        min_height=2.7,
        title_color=SECONDARY_COLOR,
    )
    scene.show_slide(
        "Discussão dos Resultados",
        VGroup(strengths, limits).arrange(RIGHT, buff=0.35, aligned_edge=UP),
    )
