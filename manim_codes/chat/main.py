from manim import *
from manim_slides import Slide


from introducao import add_slides as add_intro_slides
from capitulo1 import add_slides as add_capitulo1_slides
from capitulo2 import add_slides as add_capitulo2_slides
from capitulo3 import add_slides as add_capitulo3_slides
from capitulo4 import add_slides as add_capitulo4_slides
from conclusao import add_slides as add_conclusao_slides
from utils import PresentationBase

config.background_color = WHITE

class Main(PresentationBase):
    def construct(self):
        self.setup_presentation()
        add_intro_slides(self)
        add_capitulo1_slides(self)
        # add_capitulo2_slides(self)
        # add_capitulo3_slides(self)
        # add_capitulo4_slides(self)
        # add_conclusao_slides(self)