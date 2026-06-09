import os
import random

from manim import *
from manim_slides import Slide


def black(func):
    """Sets default color to black"""

    def wrapper(*args, color=BLACK, **kwargs):
        return func(*args, color=color, **kwargs)

    return wrapper


Tex = black(Tex)
Text = black(Text)
MathTex = black(MathTex)
Line = black(Line)
Dot = black(Dot)
Brace = black(Brace)
Arrow = black(Arrow)
Angle = black(Angle)
config.background_color = WHITE # fundo branco

class Item:
    def __init__(self, initial=1):
        self.value = initial

    def __repr__(self):
        s = repr(self.value)
        self.value += 1
        return s


def paragraph(*strs, alignment=LEFT, direction=DOWN, **kwargs):
    texts = VGroup(*[Text(s, **kwargs) for s in strs]).arrange(direction)

    if len(strs) > 1:
        for text in texts[1:]:
            text.align_to(texts[0], direction=alignment)

    return texts


class VideoAnimation(Animation):
    def __init__(self, video_mobject, **kwargs):
        self.video_mobject = video_mobject
        self.index = 0
        self.dt = 1.0 / len(video_mobject)
        super().__init__(video_mobject, **kwargs)

    def interpolate_mobject(self, dt):
        index = int(dt / self.dt) % len(self.video_mobject)

        if index != self.index:
            self.index = index
            self.video_mobject.pixel_array = self.video_mobject[index].pixel_array

        return self


class VideoMobject(ImageMobject):
    def __init__(self, image_files, **kwargs):
        assert len(image_files) > 0, "Cannot create empty video"
        self.image_files = image_files
        self.kwargs = kwargs
        super().__init__(image_files[0], **kwargs)

    def __len__(self):
        return len(self.image_files)

    def __getitem__(self, index):
        return ImageMobject(self.image_files[index], **self.kwargs)

    def play(self, **kwargs):
        return VideoAnimation(self, **kwargs)


class Main(Slide):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        random.seed(1234)

        # Colors
        self.BS_COLOR = BLUE_D
        self.UE_COLOR = MAROON_D
        self.SIGNAL_COLOR = BLUE_B
        self.WALL_COLOR = LIGHT_BROWN
        self.INVALID_COLOR = RED
        self.VALID_COLOR = "#28C137"
        self.IMAGE_COLOR = "#636463"
        self.X_COLOR = DARK_BROWN

        # Coordinates

        self.UL = Dot().to_corner(UL).get_center()
        self.UR = Dot().to_corner(UR).get_center()
        self.DL = Dot().to_corner(DL).get_center()
        self.DR = Dot().to_corner(DR).get_center()

        # Font sizes
        self.TITLE_FONT_SIZE = 48
        self.CONTENT_FONT_SIZE = 0.6 * self.TITLE_FONT_SIZE
        self.SOURCE_FONT_SIZE = 0.2 * self.TITLE_FONT_SIZE

        # Mutable variables

        self.slide_number = Integer(1).set_color(BLACK).to_corner(DR)
        self.slide_title = Text(
            "Sumário", color=BLACK, font_size=self.TITLE_FONT_SIZE
        ).to_corner(UL)
        self.add_to_canvas(slide_number=self.slide_number, slide_title=self.slide_title)

        self.tex_template = TexTemplate()
        self.tex_template.add_to_preamble(
            r"""
        \usepackage{siunitx}
        \usepackage{amsmath}
        \newcommand{\ts}{\textstyle}
        """
        )


    def next_slide_number_animation(self):
        return self.slide_number.animate(run_time=0.5).set_value(
            self.slide_number.get_value() + 1
        )

    def next_slide_title_animation(self, title):
        return Transform(
            self.slide_title,
            Text(title, color=BLACK, font_size=self.TITLE_FONT_SIZE)
            .move_to(self.slide_title)
            .align_to(self.slide_title, LEFT),
        )

    def new_clean_slide(self, title, contents=None):
        if self.mobjects_without_canvas:
            self.play(
                self.next_slide_number_animation(),
                self.next_slide_title_animation(title),
                self.wipe(
                    self.mobjects_without_canvas,
                    contents if contents else [],
                    return_animation=True,
                ),
            )
        else:
            self.play(
                self.next_slide_number_animation(),
                self.next_slide_title_animation(title),
            )

#############################################################################################
    def construct_intro(self):
        # Title

        titulo = Paragraph(
            "Comparação entre Modelos de Redes Neurais",
            "U-Net e U-Net Fuzzy para Mensurar ",
            "Regiões de Imagens de Ultrassonografia Bovina",
            alignment="center", color=BLACK).scale(0.8)
        author = (
            Text("Autor: Victor Patrick Sena Barbosa", color=BLACK)
            .scale(0.3)
            .next_to(titulo, DOWN)
        )
        Orientadora = (
            Text("Orientadora: Rosana Sueli da Motta Jafelice ", color=BLACK)
            .scale(0.3)
            .next_to(author, DOWN)
        )
        Coorientadora = (
            Text("Coorientador: Caio August Rodrigues dos Santos ", color=BLACK)
            .scale(0.3)
            .next_to(Orientadora, DOWN)
        )

        self.next_slide(notes="Início da apresentação")

        self.play(FadeIn(titulo))
        self.play(FadeIn(author, shift=DOWN))
        self.play(FadeIn(Orientadora, shift=DOWN))
        self.play(FadeIn(Coorientadora, shift=DOWN))

       
        self.next_slide(
            notes="""
        # Breve introdução.
        """
        )
        self.play(FadeOut(author, shift=DOWN))
        self.play(FadeOut(Orientadora, shift=DOWN))
        self.play(FadeOut(Coorientadora, shift=DOWN))

        self.play(titulo.animate.scale(0.6).to_edge(UL))


        img1 = ImageMobject("imagens/intro/ultrassom.jpg").to_edge(ORIGIN)

        self.play(FadeIn(img1))
        self.next_slide(
            notes="""
        # Imagem.
        """
        )

        self.new_clean_slide("Breve introdução")
        self.play(FadeIn(titulo))
        

        # self.next_slide(
        #     loop=True,
        #     notes="""
        # Let the speaker emit audio waves towards the audience.
        # """,
        # )
  
        self.wipe(
            [],
            Text(
                "We just did Ray Tracing (RT)!",
                color=BLACK,
                font_size=self.CONTENT_FONT_SIZE,
            ).shift(3 * DOWN),
        )

        # Contents

        i = Item()

        contents = paragraph(
            f"{i}. Ray Tracing and EM Fundamentals;",
            f"{i}. Motivations for Differentiable Ray Tracing;",
            f"{i}. How to trace paths;",
            f"{i}. Differentiable Ray Tracing;",
            f"{i}. Status of Work;",
            f"{i}. and Conclusion.",
            color=BLACK,
            font_size=self.CONTENT_FONT_SIZE,
        ).align_to(self.slide_title, LEFT)

        self.next_slide(notes="Table of contents")
        self.wipe(self.mobjects_without_canvas, [*self.canvas_mobjects, contents])

    

    def construct(self):
        self.wait_time_between_slides = 0.10

        self.construct_intro()
