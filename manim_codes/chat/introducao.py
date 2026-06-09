from manim import *

from configuracoes import *


def add_slides(scene):
    title = Paragraph(
        *PRESENTATION_TITLE.split("\n"),
        alignment="left",
        font_size=38,
        color=TEXT_COLOR,
        line_spacing=0.8,
    )
    subtitle = Text(PRESENTATION_SUBTITLE, font_size=SUBTITLE_FONT_SIZE, color=PRIMARY_COLOR)
    author = Text(f"Autor: {AUTHOR}", font_size=BODY_FONT_SIZE)
    advisor = Text(ADVISOR, font_size=BODY_FONT_SIZE - 1)
    co_advisor = Text(CO_ADVISOR, font_size=BODY_FONT_SIZE - 1)

    left = VGroup(title, subtitle, author, advisor, co_advisor).arrange(
        DOWN, aligned_edge=LEFT, buff=0.22
    )

    accent = Line(ORIGIN, DOWN * 5.4, color=SECONDARY_COLOR, stroke_width=4)

    right_items = []
    if ULTRASOUND_IMAGE.exists():
        image = ImageMobject(str(ULTRASOUND_IMAGE)).scale_to_fit_width(4.6)
        image_frame = SurroundingRectangle(
            image,
            color=CARD_STROKE_COLOR,
            buff=0.12,
            corner_radius=0.12,
        )
        image_group = Group(image_frame, image)
        right_items.append(image_group)

    badge = scene.make_card(
        "Escopo",
        [
            "Comparação entre U-Net multitarefa e U-Net Fuzzy.",
            "Mensuração automática de AOL, EGL e EGG.",
            "Aplicação em ultrassonografia bovina.",
        ],
        width=4.9,
        min_height=2.4,
        title_color=SECONDARY_COLOR,
        body_font_size=18,
    )
    right_items.append(badge)
    right = Group(*right_items).arrange(DOWN, buff=0.32)

    cover = Group(left, accent, right).arrange(RIGHT, buff=0.48, aligned_edge=UP)
    scene.show_cover(cover)

    agenda = scene.make_bullets(AGENDA, font_size=26, width=55, bullet_color=PRIMARY_COLOR)
    scene.show_slide(
        "Roteiro da Apresentação",
        agenda,
        subtitle="Estrutura preparada a partir do resumo analítico da dissertação.",
    )
