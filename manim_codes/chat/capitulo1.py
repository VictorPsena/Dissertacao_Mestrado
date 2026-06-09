from manim import *
from manim_slides import *

from configuracoes import *


def add_slides(self, scene):
    info_card = scene.make_paragraph(
        "O problema de pesquisa deste trabalho é a comparação entre os modelos de redes neurais U-Net e U-Net Fuzzy para mensurar regiões de imagens de ultrassonografia bovina, visando avaliar qual modelo apresenta melhor desempenho na tarefa de segmentação dessas imagens."
    ).set_width(5.5)
    problem_card = scene.make_paragraph(
        "A aplicação é voltada à ultrassonografia de carcaça de bovinos Nelore e Caracu, com o objetivo de mensurar áreas de olho de lombo (AOL), gordura localizada (EGL) e espessura de gordura (EGG)."
    ).set_width(5.5)

    scene.show_slide(
        "Problema de Pesquisa",
        VGroup(info_card, problem_card).arrange(RIGHT, buff=0.35, aligned_edge=UP),
        subtitle="A aplicação é voltada à ultrassonografia de carcaça de bovinos Nelore e Caracu.",
    )

    self.next_slide()
    

