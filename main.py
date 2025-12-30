from fasthtml.common import (
    fast_app, serve,
    A, Card, Container, Group, P, Titled,
    picolink,
)

app, rt = fast_app(hdrs=(picolink))


@rt("/")
def get():
    summary = P(
        "FastHTML is a new next-generation web framework for fast, scalable "
        "web applications with minimal, compact code. It builds on top of "
        "popular foundations like ASGI and HTMX. You can now deploy FastHTML "
        "with Vercel CLI or by pushing new changes to your git repository.",
    )
    ex_url = "https://vercel.com/templates/python/fasthtml-python-boilerplate"
    footer_content = P(
        A("Deploy your own", href=ex_url),
        " or ",
        A("learn more", href="https://docs.fastht.ml/"),
        " about FastHTML.",
    )
    return (
        Container(
            Card(
                Group(summary),
                header=(Titled("FastHTML + Vercel")),
                footer=(footer_content),
            ),
        ),
    )

serve()
