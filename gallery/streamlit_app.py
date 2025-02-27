import pkgutil
from importlib import import_module
import qrcode
from PIL import Image
import io

import streamlit as st
import streamlit_extras
from streamlit_extras.add_vertical_space import add_vertical_space
from streamlit_extras.row import row

st.set_page_config(layout="centered", page_icon=":knot:", page_title="streamlit-extras")

""" # :knot: streamlit-extras """


@st.cache_resource
def show_extras():
    extra_names = [
        extra.name
        for extra in pkgutil.iter_modules(streamlit_extras.__path__)
        if extra.ispkg
    ]

    icon_row = row(10)

    for extra_name in extra_names:
        mod = import_module(f"streamlit_extras.{extra_name}")
        icon = mod.__icon__
        icon_row.link_button(
            icon,
            f"https://arnaudmiribel.github.io/streamlit-extras/extras/{extra_name}/",
            help=mod.__title__,
            use_container_width=True,
        )

    icon_row.markdown("### ...")


st.markdown(
    "streamlit-extras is a Python library putting together useful Streamlit bits of code. It"
    " includes > 40 (count emojis below!) functional or visual additions to Streamlit that will"
    " make your life easier or your apps nicer. We call them *extras* and anyone's welcome to add"
    " their owns!"
)

add_vertical_space(1)

show_extras()

add_vertical_space(1)
st.markdown(
    """
#### Get started
```
pip install streamlit-extras
```
"""
)

def generate_qr_code(link):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    img = qr.make_image(fill="black", back_color="white")
    img_bytes = io.BytesIO()
    img.save(img_bytes, format="PNG")
    return img_bytes

buttons = {
    "Google": "https://www.google.com",
    "GitHub": "https://github.com",
    "Streamlit": "https://streamlit.io"
}

for button_name, url in buttons.items():
    if st.button(button_name):
        qr_code = generate_qr_code(url)
        st.image(qr_code, caption=f"Scan to visit {button_name}")

add_vertical_space(1)
st.markdown("#### Learn more")
links_row = row(2, vertical_align="center")
links_row.link_button(
    "📖  Visit our documentation",
    "https://arnaudmiribel.github.io/streamlit-extras/",
    use_container_width=True,
)
links_row.link_button(
    "🐙  Visit our repository",
    "https://github.com/arnaudmiribel/streamlit-extras",
    use_container_width=True,
)
