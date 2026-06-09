import textwrap

from manim import *
from manim_slides import Slide

from configuracoes import *


def wrap_text(text, width=46):
    return "\n".join(
        textwrap.wrap(text, width=width, break_long_words=False, break_on_hyphens=False)
    )


class PresentationBase(Slide):
    def setup_presentation(self):
        apply_theme()
        self.page_number = 1
        self.wait_time_between_slides = 0.1

    def make_title_block(self, title, subtitle=None):
        title_mob = Text(title, font_size=TITLE_FONT_SIZE, color=PRIMARY_COLOR)
        title_mob.to_corner(UL).shift(0.25 * DOWN)

        divider = Line(ORIGIN, RIGHT * 10.8, color=CARD_STROKE_COLOR, stroke_width=2)
        divider.next_to(title_mob, DOWN, buff=0.18)
        divider.align_to(title_mob, LEFT)

        if subtitle is None:
            return VGroup(title_mob, divider)

        subtitle_mob = Paragraph(
            *wrap_text(subtitle, 70).split("\n"),
            alignment="left",
            font_size=SMALL_FONT_SIZE,
            color=MUTED_COLOR,
            line_spacing=0.8,
        )
        subtitle_mob.next_to(divider, DOWN, buff=0.14)
        subtitle_mob.align_to(title_mob, LEFT)
        return VGroup(title_mob, divider, subtitle_mob)

    def make_page_number(self):
        return Text(
            f"{self.page_number:02d}",
            font_size=SMALL_FONT_SIZE,
            color=MUTED_COLOR,
        ).to_corner(DR)

    def make_paragraph(self, text, font_size=BODY_FONT_SIZE, width=72, color=TEXT_COLOR):
        paragraph = Paragraph(
            *wrap_text(text, width).split("\n"),
            alignment="left",
            font_size=font_size,
            color=color,
            line_spacing=0.8,
        )
        return paragraph

    def make_bullets(self, items, font_size=BODY_FONT_SIZE, width=50, bullet_color=SECONDARY_COLOR):
        rows = []
        for item in items:
            dot = Dot(radius=0.055, color=bullet_color)
            text = Paragraph(
                *wrap_text(item, width).split("\n"),
                alignment="left",
                font_size=font_size,
                color=TEXT_COLOR,
                line_spacing=0.8,
            )
            row = VGroup(dot, text).arrange(RIGHT, aligned_edge=UP, buff=0.22)
            rows.append(row)
        group = VGroup(*rows).arrange(DOWN, aligned_edge=LEFT, buff=0.26)
        return group

    def make_card(
        self,
        title,
        lines,
        width=5.8,
        min_height=2.6,
        title_color=PRIMARY_COLOR,
        stroke_color=CARD_STROKE_COLOR,
        fill_color=CARD_FILL_COLOR,
        body_font_size=20,
    ):
        title_mob = Text(title, font_size=SUBTITLE_FONT_SIZE, color=title_color)
        body_items = [
            self.make_paragraph(line, font_size=body_font_size, width=32) for line in lines
        ]
        body = VGroup(*body_items).arrange(DOWN, aligned_edge=LEFT, buff=0.16)
        content = VGroup(title_mob, body).arrange(DOWN, aligned_edge=LEFT, buff=0.22)

        box = RoundedRectangle(
            corner_radius=0.16,
            width=max(width, content.width + 0.55),
            height=max(min_height, content.height + 0.55),
            stroke_color=stroke_color,
            fill_color=fill_color,
            fill_opacity=0.96,
            stroke_width=2,
        )
        content.move_to(box.get_center())
        content.align_to(box.get_left() + RIGHT * 0.28, LEFT)
        return VGroup(box, content)

    def make_highlight_box(self, text, width=11.5):
        paragraph = self.make_paragraph(text, font_size=SMALL_FONT_SIZE + 1, width=78)
        box = RoundedRectangle(
            corner_radius=0.14,
            width=max(width, paragraph.width + 0.5),
            height=paragraph.height + 0.42,
            stroke_color=SECONDARY_COLOR,
            fill_color=SOFT_HIGHLIGHT,
            fill_opacity=0.92,
            stroke_width=2,
        )
        paragraph.move_to(box.get_center())
        return VGroup(box, paragraph)

    def fit_to_content_area(self, mob, max_width=12.3, max_height=5.9):
        if mob.width > max_width:
            mob.scale_to_fit_width(max_width)
        if mob.height > max_height:
            mob.scale_to_fit_height(max_height)
        mob.move_to(DOWN * 0.35)
        return mob

    def show_slide(self, title, content, subtitle=None):
        title_block = self.make_title_block(title, subtitle)
        page = self.make_page_number()
        content = self.fit_to_content_area(content) # content é o VGroup que contém os elementos do slide
        group = VGroup(title_block, content, page)
        self.play(FadeIn(title_block, shift=0.2 * DOWN), FadeIn(page), FadeIn(content, shift=0.15 * UP))
        self.next_slide()
        self.play(FadeOut(group))
        self.page_number += 1

    def show_cover(self, content):
        content = self.fit_to_content_area(content, max_width=12.8, max_height=6.6)
        self.play(FadeIn(content, shift=0.2 * UP))
        self.next_slide()
        self.play(FadeOut(content))
        self.page_number += 1
