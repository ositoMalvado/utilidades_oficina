import flet as ft
from Tabs import *
import random

def main(page: ft.Page):

    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER


    def change_color():
        random_color = "#%02x%02x%02x" % (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        page.theme = ft.Theme(
            color_scheme_seed=random_color
        )
        page.update()
    change_color()

    page.add(
        ft.Tabs(
            [
                ft.Tab(
                    text="Federación Patronal",
                    content=ft.Tabs(
                        [
                            TabFederacionFranquicias()
                        ],
                        tab_alignment=ft.TabAlignment.CENTER,
                        expand=True,
                        scrollable=True
                    )
                ),
                ft.Tab(
                    text="Río Uruguay",
                    content=ft.Tabs(
                        [
                            TabRioUruguayPremio()
                        ],
                        tab_alignment=ft.TabAlignment.CENTER,
                        expand=True,
                        scrollable=True
                    )
                ),
                ft.Tab(
                    text="General",
                    content=ft.Tabs(
                        [
                            TabGeneralPatentes()
                        ],
                        tab_alignment=ft.TabAlignment.CENTER,
                        expand=True,
                        scrollable=True
                    )
                )
            ],
            tab_alignment=ft.TabAlignment.CENTER,
            expand=True
        )
    )



ft.app(main, assets_dir="assets")
