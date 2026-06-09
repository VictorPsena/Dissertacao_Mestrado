from manim import *

from configuracoes import *


def add_slides(scene):
    contributions = scene.make_bullets(
        [
            "Comparação sistemática entre U-Net multitarefa e U-Net Fuzzy para AOL, EGL e EGG.",
            "Ampliação do escopo da literatura bovina além da AOL, incluindo EGL e EGG.",
            "Entrega de um aplicativo em Tkinter para segmentação, mensuração e exportação de resultados.",
            "Evidência de que a vantagem fuzzy depende da estrutura anatômica e do modo de cálculo do indicador.",
        ],
        font_size=23,
        width=54,
        bullet_color=PRIMARY_COLOR,
    )
    summary = scene.make_highlight_box(
        "Síntese final: a U-Net Fuzzy foi claramente superior na AOL, teve desempenho equilibrado na EGL e não superou a U-Net multitarefa na medida final da EGG."
    )
    scene.show_slide("Conclusões e Contribuições", VGroup(contributions, summary).arrange(DOWN, buff=0.35))

    future = scene.make_bullets(
        [
            "Explorar mecanismos de atenção combinados à U-Net.",
            "Aplicar transferência de aprendizado e fine tuning para bases pequenas.",
            "Reduzir dependência de características específicas do aparelho de ultrassom.",
            "Ampliar a base e padronizar ainda mais o protocolo de aquisição das imagens.",
            "Investigar adaptação do aplicativo para dispositivos móveis.",
        ],
        font_size=23,
        width=56,
        bullet_color=SECONDARY_COLOR,
    )
    scene.show_slide("Trabalhos Futuros", future)

    closing = VGroup(
        Text("Obrigado!", font_size=46, color=PRIMARY_COLOR),
        Text("Perguntas?", font_size=34, color=SECONDARY_COLOR),
        Text("Resumo preparado a partir de resumo_dissertacao.mk", font_size=SMALL_FONT_SIZE, color=MUTED_COLOR),
    ).arrange(DOWN, buff=0.25)
    scene.show_cover(closing)
