import reflex as rx


def breadcrumbs(items: list[tuple[str, str | None]]) -> rx.Component:
    links = []
    for label, href in items:
        if href is None:
            links.append(rx.text(label, size="2", color_scheme="gray"))
        else:
            links.append(
                rx.link(label, href=href, size="2", color_scheme="blue",
                        underline="hover")
            )
        if href is not None:
            links.append(rx.text("/", size="2", color_scheme="gray"))
    return rx.hstack(*links, spacing="2", padding="0.75rem 0", wrap="wrap")
