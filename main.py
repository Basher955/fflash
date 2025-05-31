from flet import *
from flet_flashlight import *
from flet_permission_handler import *
def main(page:Page):
    #page.window.width=370
    #page.window.height=740
    #page.window.top=10
    #page.window.left=1040
    page.theme_mode=ThemeMode.LIGHT
    flashlight = Flashlight()
    permission_handler = PermissionHandler()
    page.overlay.append(permission_handler)
    def open_ap(e):
        permission_handler.open_app_settings()
    page.overlay.append(flashlight)
    page.add(
        AppBar(
            bgcolor="#e31113",
            title=Text("Flash light[BM]",color=Colors.WHITE, size=16,weight=FontWeight.BOLD),
            center_title=True,
            actions=[
                IconButton(Icons.SETTINGS,icon_color=Colors.WHITE,on_click=open_ap)
            ]
        ),
        Row([
            Text("\n\n\n\nFLASH LIGHT APP",size=31),
        ],alignment=MainAxisAlignment.CENTER),
        Row([
            Image(src="im.png",width=180,)
        ],alignment=MainAxisAlignment.CENTER),
        Text("\n"),
        Row([
            ElevatedButton(
                "ON",
                width=90,
                icon=Icons.PLAY_ARROW,
                style=ButtonStyle(
                    bgcolor="#e31113",
                    padding=15,
                    color=Colors.WHITE,
                    shape=ContinuousRectangleBorder(radius=100)
                ),
                on_click=lambda _:flashlight.turn_on()

            ),
             ElevatedButton(
                "OFF",
                width=90,
                icon=Icons.PLAY_DISABLED_SHARP,
                style=ButtonStyle(
                    bgcolor="#e31113",
                    padding=15,
                    color=Colors.WHITE,
                    shape=ContinuousRectangleBorder(radius=100)
                ),
                on_click=lambda _:flashlight.turn_off()

            ),

        ],alignment=MainAxisAlignment.CENTER),
         Row([
            Text("\n\n\n\n\nBasher mgbool python apss 2025",size=14),
        ],alignment=MainAxisAlignment.CENTER),
    )
    page.update()
app(target=main,assets_dir='assets/')
