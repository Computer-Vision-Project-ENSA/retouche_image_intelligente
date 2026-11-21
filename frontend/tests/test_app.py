
from io import BytesIO
from unittest.mock import Mock, patch

import numpy as np
import pytest
import requests
from PIL import Image

from frontend.app import process_image


def create_test_image():
    return np.full((100, 100, 3), 255, dtype=np.uint8)


def test_frontend_sends_image():
    image = create_test_image()

    buffer = BytesIO()
    Image.fromarray(image).save(buffer, format="PNG")

    mock_response = Mock()
    mock_response.content = buffer.getvalue()
    mock_response.raise_for_status.return_value = None

    with patch("frontend.app.requests.post", return_value=mock_response) as mock_post:
        result = process_image(image)

    assert isinstance(result, np.ndarray)
    assert result.shape == (100, 100, 3)

    mock_post.assert_called_once()

    args, kwargs = mock_post.call_args

    assert args[0] == "http://127.0.0.1:8000/api/process"
    assert "file" in kwargs["files"]


def test_frontend_rejects_missing_image():
    with pytest.raises(Exception):
        process_image(None)


def test_frontend_handles_api_error():
    image = create_test_image()

    with patch(
        "frontend.app.requests.post",
        side_effect=requests.ConnectionError("Backend unavailable")
    ):
        with pytest.raises(Exception):
            process_image(image)
