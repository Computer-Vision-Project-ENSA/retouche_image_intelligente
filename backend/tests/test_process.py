
from io import BytesIO

from fastapi.testclient import TestClient
from PIL import Image

from backend.app.main import app


client = TestClient(app)


def create_test_image(image_format="PNG"):
    image = Image.new("RGB", (100, 100), color="red")

    buffer = BytesIO()
    image.save(buffer, format=image_format)

    return buffer.getvalue()


def test_process_valid_png():
    image_bytes = create_test_image("PNG")

    response = client.post(
        "/api/process",
        files={
            "file": ("test.png", image_bytes, "image/png")
        }
    )

    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"

    result = Image.open(BytesIO(response.content))
    assert result.size == (100, 100)


def test_process_valid_jpeg():
    image_bytes = create_test_image("JPEG")

    response = client.post(
        "/api/process",
        files={
            "file": ("test.jpg", image_bytes, "image/jpeg")
        }
    )

    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"


def test_process_unsupported_format():
    response = client.post(
        "/api/process",
        files={
            "file": ("test.txt", b"Hello World", "text/plain")
        }
    )

    assert response.status_code == 415


def test_process_corrupted_image():
    response = client.post(
        "/api/process",
        files={
            "file": ("test.png", b"not a real image", "image/png")
        }
    )

    assert response.status_code == 400


def test_process_missing_file():
    response = client.post("/api/process")

    assert response.status_code == 422
