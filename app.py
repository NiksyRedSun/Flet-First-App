import flet as ft
import asyncio



async def main(page: ft.Page):
    page.title = "Diamond Clicker"
    page.theme_mode = ft.ThemeMode.DARK
    page.bgcolor = "#ffffff"
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER
    page.fonts = {"FulboArgenta": "fonts/FulboArgenta.ttf"}
    page.theme = ft.Theme(font_family="FulboArgenta")

    message_iter = iter(
        ["Всем поднюханным кликерам посвящается", "Добро пожаловать в webbbb", "Сюда можно будет впихнуть что угодно"])


    async def score_up(event: ft.ContainerTapEvent) -> None:
        score.data += 1
        score.value = int(score.data)


        image.scale = 0.95

        score_counter.opacity = 100
        score_counter.value = "+1"
        score_counter.right = 0
        score_counter.bottom = 0

        progres_bar.value += (1/20)

        if score.data % 20 == 0:
            page.snack_bar = ft.SnackBar(
                content=ft.Text(
                value=next(message_iter),
                size=20,
                color="#5353ec",
                text_align=ft.TextAlign.CENTER
                ),
                bgcolor="#800080"
            )
            page.snack_bar.open = True
            progres_bar.value = 0

        await page.update_async()

        await asyncio.sleep(0.1)
        image.scale = 1

        score_counter.opacity = 0

        await page.update_async()

    score = ft.Text(value="0",
                    size=100,
                    data=0,
                    color="#5353ec")

    score_counter = ft.Text(size=100,
                            animate_opacity=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE),
                            color="#5353ec")

    image = ft.Image(src="diamond.png",
                     fit=ft.ImageFit.CONTAIN,
                     animate_scale=ft.Animation(duration=600, curve=ft.AnimationCurve.EASE))

    progres_bar = ft.ProgressBar(
        value=0,
        width=page.width - 100,
        bar_height=20,
        color="#0014a8",
        bgcolor="#5353ec"
    )

    await page.add_async(
        score,
        ft.Container(
            content=ft.Stack(controls=[image, score_counter]),
            on_click=score_up,
            margin=ft.Margin(0, 0, 0, 30)
        ),
        ft.Container(
            content=progres_bar,
            border_radius=ft.BorderRadius(10, 10, 10, 10)
        )
    )

if __name__ == "__main__":
    ft.app(target=main, view=None, port=8000)