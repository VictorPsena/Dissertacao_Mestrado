from manim import *

from configuracoes import *


def add_slides(scene):
    data_card = scene.make_card(
        "Base de dados",
        [
            "Imagens do Centro Avançado de Pesquisa e Desenvolvimento de Bovinos de Corte, em Sertãozinho-SP.",
            "Animais machos das raças Nelore e Caracu, avaliados por ultrassom Aloka SSD-500 com sonda linear de 3,5 MHz.",
            "A dissertação registra uma divergência pontual entre 134 e 135 imagens; o resumo privilegia 135 imagens.",
        ],
        width=6.0,
        min_height=3.5,
    )
    prep_card = scene.make_card(
        "Pré-processamento",
        [
            "Recorte das imagens, normalização para [0, 1] e redimensionamento para 256 x 256.",
            "Aumento de dados com rotações em [-15°, 15°] e variações de brilho.",
            "Ground truths criados com Label Studio; para EGG foram usadas duas máscaras: gordura e Biceps Femoris.",
        ],
        width=6.0,
        min_height=3.5,
        title_color=SECONDARY_COLOR,
    )
    scene.show_slide(
        "Metodologia Experimental I",
        VGroup(data_card, prep_card).arrange(RIGHT, buff=0.35, aligned_edge=UP),
    )

    multitask = scene.make_card(
        "U-Net multitarefa",
        [
            "Recebe imagem e codificação one-hot da raça do animal.",
            "Modula o bottleneck com uma camada densa seguida por multiplicação dos mapas de características.",
        ],
        width=5.7,
        min_height=2.8,
        title_color=HIGHLIGHT_COLOR,
    )
    fuzzy = scene.make_card(
        "U-Net Fuzzy",
        [
            "Mantém a camada multitarefa e acrescenta um módulo de inferência fuzzy inspirado no ANFIS.",
            "Usa 3 conjuntos fuzzy e 9 regras fuzzy para refinar o bottleneck.",
        ],
        width=5.7,
        min_height=2.8,
        title_color=SECONDARY_COLOR,
    )
    training = scene.make_bullets(
        [
            "Divisão dos dados: 70% treino, 20% validação e 10% teste.",
            "Treinamento com Adam, taxa 0,001, batch size 4, até 100 épocas.",
            "Binary Cross-Entropy, Dropout 0,2 e EarlyStopping com 15 épocas.",
            "Cada modelo foi treinado 4 vezes; os resultados apresentados são médias.",
        ],
        font_size=22,
        width=48,
        bullet_color=PRIMARY_COLOR,
    )
    content = VGroup(VGroup(multitask, fuzzy).arrange(RIGHT, buff=0.35), training).arrange(
        DOWN, buff=0.35
    )
    scene.show_slide("Metodologia Experimental II", content)

    steps = scene.make_bullets(
        [
            "Delimitação manual por especialista e obtenção das medidas de referência em ImageJ.",
            "Criação das máscaras de segmentação para AOL, EGL e EGG.",
            "Treinamento separado por indicador; para EGG foram usados dois modelos por arquitetura.",
            "Extração das medidas numéricas a partir das máscaras preditas e comparação com as medidas reais.",
            "Entrega final de um aplicativo em Tkinter para uso prático e exportação em Excel.",
        ],
        font_size=23,
        width=56,
        bullet_color=HIGHLIGHT_COLOR,
    )
    scene.show_slide(
        "Desenvolvimento da Pesquisa",
        steps,
        subtitle="Fluxo completo: aquisição, rotulação, treinamento, segmentação, mensuração e disponibilização prática.",
    )
