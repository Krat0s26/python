import reflex as rx


class State(rx.State):
    pass


def index() -> rx.Component:
    return rx.container(
        rx.vstack(
            rx.heading("Jhonny Portillo", size="9"),
            rx.text(
                "Data Center Technician • Fiber Optics • Linux",
                size="5",
            ),

            rx.divider(),

            rx.heading("About Me", size="6"),
            rx.text(
                "Technician with experience in data centers, "
                "fiber optic installation, structured cabling, "
                "Linux and networking."
            ),

            rx.divider(),

            rx.heading("Skills", size="6"),
            rx.hstack(
                rx.badge("Linux"),
                rx.badge("Python"),
                rx.badge("Networking"),
                rx.badge("Fiber Optics"),
                rx.badge("Git"),
                spacing="3",
            ),

            rx.divider(),

            rx.heading("Certifications", size="6"),
            rx.text("OSHA 10"),
            rx.text("OSHA 30"),

            spacing="6",
            align="center",
            width="100%",
        ),
        max_width="900px",
        padding="2em",
    )

app = rx.App()
app.add_page(index)