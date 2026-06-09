from manim import *
from manim_slides import Slide

# Configurações iniciais
config.background_color = WHITE # fundo branco
MathTex.set_default(color=BLACK, font_size=40)
Tex.set_default(color=BLACK, font_size=40)
Text.set_default(color=BLACK, font_size=40)

# Tamanhos fontes
titulo_font_size = 40
subtitulo_font_size = 30
texto_font_size = 20

# Posições para os elementos
borda_superior = UP
borda_inferior = DOWN
canto_superior_esquerda = UL
canto_superior_direita = UR
canto_inferior_esquerda = DL
canto_inferior_direita = DR
# Cores
cor_fundo = WHITE
cor_texto = BLACK
cor_titulo = BLACK

# Nomes
Nomes_Introducao = {

    "autor": Text("Autor: Victor Sena", font_size=texto_font_size),
    "orientadora": Text("Orientadora: Rosana Sueli da Motta Jafelice ", font_size=texto_font_size),
    "coorientadora": Text("Coorientador: Caio August Rodrigues dos Santos ", font_size=texto_font_size)
}

# Nomes_capitulos
Nomes_Capitulos = {
    "capitulo1": "Capítulo 1: Introdução",
    "capitulo2": "Capítulo 2: Revisão Bibliográfica",
    "capitulo3": "Capítulo 3: Metodologia",
    "capitulo4": "Capítulo 4: Resultados e Discussão",
    "capitulo5": "Capítulo 5: Conclusão"
}


class Introducao(Slide):
    def construct(self):
        titulo = Paragraph(
            "Comparação entre Modelos de Redes Neurais",
            "U-Net e U-Net Fuzzy para Mensurar ",
            "Regiões de Imagens de Ultrassonografia Bovina",
            alignment="center",
            font_size=titulo_font_size,)
        titulo.to_edge(ORIGIN)  
        autor = Nomes_Introducao["autor"].next_to(titulo, DOWN, buff=0.5)
        orientadora = Nomes_Introducao["orientadora"].next_to(autor, DOWN)
        coorientadora = Nomes_Introducao["coorientadora"].next_to(orientadora, DOWN)
        self.play(Write(titulo))

        self.add(autor)
        self.add(orientadora)
        self.add(coorientadora)
        self.next_slide()
        