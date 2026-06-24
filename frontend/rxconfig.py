import reflex as rx

config = rx.Config(
    app_name="sociedade_front",
    frontend_port=3000,
    backend_port=8005,
    plugins=[
        rx.plugins.SitemapPlugin(),
        rx.plugins.TailwindV4Plugin(),
        rx.plugins.RadixThemesPlugin(
            theme=rx.theme(
                appearance="light",
                has_background=True,
                radius="medium",
                accent_color="blue",
                gray_color="slate",
            ),
        ),
    ]
)