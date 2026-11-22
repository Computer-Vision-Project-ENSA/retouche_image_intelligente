
from io import BytesIO

import gradio as gr
import numpy as np
import requests
from PIL import Image

API_URL = "http://127.0.0.1:8000/api/process"


def process_image(image):
    if image is None:
        raise gr.Error("Veuillez importer une image.")

    buffer = BytesIO()
    Image.fromarray(image).convert("RGB").save(
        buffer, format="PNG"
    )

    buffer.seek(0)

    try:
        response = requests.post(
            API_URL,
            files={"file": ("image.png", buffer, "image/png")},
            timeout=60,
        )
        response.raise_for_status()
    except requests.RequestException as error:
        raise gr.Error(
            f"Erreur de communication avec le Backend : {error}"
        ) from error

    result = Image.open(BytesIO(response.content))
    return np.array(result.convert("RGB"))


with gr.Blocks(title="Suppression intelligente d'objets") as demo:
    gr.Markdown("# Suppression intelligente d'objets")
    gr.Markdown("Segmentation SAM + Inpainting LaMa")

    with gr.Row():
        input_image = gr.Image(label="Image originale", type="numpy")
        output_image = gr.Image(label="Résultat", type="numpy")

    button = gr.Button("Traiter l'image")

    button.click(
        fn=process_image,
        inputs=input_image,
        outputs=output_image,
    )


if __name__ == "__main__":
    demo.launch()
